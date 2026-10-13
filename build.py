# /// script
# requires-python = ">=3.11"
# dependencies = ["pyyaml", "markdown-it-py", "pagefind[extended]"]
# ///
"""Build the book: index.md + chapters/<dir>/*.md → site/ (static HTML, GitHub Pages).

uv run build.py              # build everything, check everything, index for search
uv run build.py --no-search  # skip the search index (faster while writing)

Order of chapters and pages comes from book.yaml. Markdown conventions are in README.md:
- `## 問題 {#q-id}`: heading with an explicit id; every h2/h3 that other pages link to needs one.
- `[[key]]` / `[[key1,key2]]`: footnote from refs/**/*.yaml; numbered per page, list at the end.
- A paragraph made only of images becomes figures: `![圖說[[key]]](img/x.png)`;
  two images in one paragraph sit side by side, three or more in a row of three.
  Add `{.s}` or `{.xs}` right after an image for a smaller figure.
- Links to other pages: `[文字](lasers.md#q-id)`, `[文字](../ccl/index.md)`; checked at build time.
- Raw HTML (svg diagrams, wide tables) is allowed.
"""
import html
import posixpath
import re
import shutil
import subprocess
import sys
from pathlib import Path
from urllib.parse import unquote

import yaml
from markdown_it import MarkdownIt

HERE = Path(__file__).parent
SITE = HERE / "site"
TOKEN = re.compile(r"\[\[([a-z0-9][a-z0-9,\-_ ]*)\]\]")
HEAD_ID = re.compile(r"<h([1-4])>((?:(?!</h[1-4]>).)*?)\s*\{#([\w-]+)\}</h\1>", re.S)
IMG = re.compile(r'<img src="([^"]*)" alt="([^"]*)"\s*/?>(\{\.(s|xs)\})?')
LINK = re.compile(r'href="(?![a-z]+:)([\w./-]*?)([\w-]+)\.(?:md|html)(#[\w-]+)?"')

md = MarkdownIt("commonmark", {"html": True}).enable("table").enable("strikethrough")


def figures(body: str) -> str:
    def para(m: re.Match) -> str:
        inner = m.group(1)
        imgs = IMG.findall(inner)
        if not imgs or IMG.sub("", inner).strip():
            return m.group(0)
        figs = []
        for src, alt, _, size in imgs:
            cap = html.unescape(alt)
            plain = html.escape(TOKEN.sub("", cap).strip(), quote=True)
            cls = f' class="{size}"' if size else ""
            figs.append(f'<figure{cls}><img src="{src}" alt="{plain}" loading="lazy">'
                        f"<figcaption>{cap}</figcaption></figure>")
        if len(figs) == 1:
            return figs[0]
        grid = "pair" if len(figs) == 2 else "trio"
        return f'<div class="{grid}">' + "".join(figs) + "</div>"

    return re.sub(r"<p>((?:\s*<img [^>]*>(?:\{\.(?:s|xs)\})?\s*)+)</p>", para, body)


def footnotes(body: str, refs: dict, name: str, errors: list) -> str:
    order: list[str] = []

    def cite(m: re.Match) -> str:
        nums = []
        for k in (k.strip() for k in m.group(1).split(",") if k.strip()):
            if k not in refs:
                errors.append(f"{name}: unknown ref key {k}")
            if k not in order:
                order.append(k)
            nums.append(order.index(k) + 1)
        links = ",".join(f'<a href="#ref-{n}">{n}</a>' for n in sorted(set(nums)))
        return f'<sup class="fn">{links}</sup>'

    body = TOKEN.sub(cite, body)
    if not order:
        return body
    items = []
    for n, k in enumerate(order, 1):
        r = refs.get(k, {})
        who, title = html.escape(str(r.get("who", k))), html.escape(str(r.get("title", "")))
        date, level = html.escape(str(r.get("date", ""))), html.escape(str(r.get("level", "")))
        url = r.get("url") or ""
        head = f"{who}，〈{title}〉" if title else who
        link = f' <a href="{html.escape(url)}">連結</a>' if url else ""
        items.append(f'<li id="ref-{n}">{head}，{date}。<span class="lv">{level}</span>{link}</li>')
    return (body + '\n<section data-pagefind-ignore><h2 id="refs">參考資料</h2>\n<p class="src">可信度：一手＝原始文件、財報、專利、規格書、論文；'
            "公司說＝公司在法說、訪談、問答裡講的；媒體報；第三方＝研究機構、分析、券商；KOL＝社群、未具名紀要。"
            "圖的出處寫在圖說的編號裡。</p>\n"
            '<ol class="refs">\n' + "\n".join(items) + "\n</ol></section>")


def render(key: str, path: Path, refs: dict, errors: list) -> dict:
    """key: 'index' for the home page, '<dir>/<page>' for chapter pages."""
    body = md.render(path.read_text())
    body = HEAD_ID.sub(lambda m: f'<h{m.group(1)} id="{m.group(3)}">{m.group(2).strip()}</h{m.group(1)}>', body)
    body = figures(body)
    here = posixpath.dirname(key)
    links = []

    def link(m: re.Match) -> str:
        prefix, page, anchor = m.group(1), m.group(2), m.group(3) or ""
        target = posixpath.normpath(posixpath.join(here, prefix, page))
        links.append((target, anchor[1:]))
        return f'href="{prefix}{page}.html{anchor}"'

    body = LINK.sub(link, body)
    ids = re.findall(r'\sid="([\w-]+)"', body)
    dup = {i for i in ids if ids.count(i) > 1}
    if dup:
        errors.append(f"{key}: duplicate ids {sorted(dup)}")
    m = re.search(r"<h1>(.*?)</h1>", body, re.S)
    title = re.sub(r"<[^>]+>", "", m.group(1)) if m else key
    h2s = re.findall(r'<h2 id="([\w-]+)">(.*?)</h2>', body, re.S)
    if len(h2s) > 2 and m:
        toc = '<nav class="toc"><ol>' + "".join(f'<li><a href="#{i}">{t}</a></li>' for i, t in h2s) + "</ol></nav>"
        body = body.replace(m.group(0), m.group(0) + "\n" + toc, 1)
    body = footnotes(body, refs, key, errors)
    for src in re.findall(r'<img[^>]+src="([^"]+)"', body):
        if not src.startswith(("http:", "https:")) and not (path.parent / unquote(src)).exists():
            errors.append(f"{key}: missing image {src}")
    return {"title": title, "body": body, "ids": set(ids), "links": links}


def sidebar(book: dict, key: str, built: dict, root: str) -> str:
    out = [f'<a class="home" href="{root}index.html">{html.escape(book["title"])}</a>',
           '<div id="search"></div>']
    for ch in book["chapters"]:
        cur_ch = key.startswith(ch["dir"] + "/")
        items = []
        for p in ch["pages"]:
            k = f'{ch["dir"]}/{p}'
            label = "總覽" if p == "index" else built[k]["title"]
            cls = ' class="cur"' if k == key else ""
            items.append(f'<li{cls}><a href="{root}{k}.html">{html.escape(label)}</a></li>')
        out.append(f'<details{" open" if cur_ch else ""}><summary>{html.escape(ch["title"])}</summary>'
                   f'<ol>{"".join(items)}</ol></details>')
    return "\n".join(out)


def page(book: dict, key: str, built: dict, order: list[str]) -> str:
    root = "../" * key.count("/")
    b = built[key]
    i = order.index(key)
    pager = []
    if i > 0:
        pager.append(f'<a class="prev" href="{root}{order[i-1]}.html">← {html.escape(built[order[i-1]]["title"])}</a>')
    if i < len(order) - 1:
        pager.append(f'<a class="next" href="{root}{order[i+1]}.html">{html.escape(built[order[i+1]]["title"])} →</a>')
    head_title = b["title"] if key == "index" else f'{b["title"]}｜{book["title"]}'
    return (
        '<!doctype html>\n<html lang="zh-TW">\n<head>\n<meta charset="utf-8">\n'
        '<meta name="viewport" content="width=device-width,initial-scale=1">\n'
        f"<title>{html.escape(head_title)}</title>\n"
        f'<link rel="stylesheet" href="{root}style.css">\n'
        f'<link rel="stylesheet" href="{root}pagefind/pagefind-ui.css">\n</head>\n<body>\n'
        f'<details class="menu" open><summary>目錄</summary><aside class="side">\n{sidebar(book, key, built, root)}\n</aside></details>\n'
        f'<main data-pagefind-body>\n{b["body"]}\n<nav class="pager">{"".join(pager)}</nav>\n</main>\n'
        f'<script src="{root}pagefind/pagefind-ui.js"></script>\n'
        "<script>\n"
        "if (window.PagefindUI) new PagefindUI({element: '#search', showSubResults: true, showImages: false});\n"
        "if (matchMedia('(max-width: 900px)').matches) document.querySelector('details.menu').removeAttribute('open');\n"
        "</script>\n</body></html>\n"
    )


def load_refs(errors: list) -> dict:
    refs: dict = {}
    for f in sorted((HERE / "refs").rglob("*.yaml")):
        for k, v in (yaml.safe_load(f.read_text()) or {}).items():
            if k in refs and refs[k] != v:
                errors.append(f"{f.relative_to(HERE)}: key {k} differs from an existing definition")
            refs.setdefault(k, v)
    return refs


def main(args: list[str]) -> None:
    book = yaml.safe_load((HERE / "book.yaml").read_text())
    errors: list[str] = []
    refs = load_refs(errors)
    sources = {"index": HERE / "index.md"}
    for ch in book["chapters"]:
        listed = set(ch["pages"])
        on_disk = {p.stem for p in (HERE / "chapters" / ch["dir"]).glob("*.md")}
        for p in sorted(on_disk - listed):
            errors.append(f'chapters/{ch["dir"]}/{p}.md is not listed in book.yaml')
        for p in ch["pages"]:
            sources[f'{ch["dir"]}/{p}'] = HERE / "chapters" / ch["dir"] / f"{p}.md"
    for k, p in sources.items():
        if not p.exists():
            sys.exit(f"book.yaml lists {k}, but {p.relative_to(HERE)} does not exist")
    built = {k: render(k, p, refs, errors) for k, p in sources.items()}
    for key, b in built.items():
        for target, anchor in b["links"]:
            if target not in built:
                errors.append(f"{key}: link to missing page {target}.md")
            elif anchor and anchor not in built[target]["ids"]:
                errors.append(f"{key}: link to missing anchor {target}.md#{anchor}")
    if errors:
        sys.exit("\n".join(errors))

    if SITE.exists():
        shutil.rmtree(SITE)
    SITE.mkdir()
    shutil.copy(HERE / "style.css", SITE / "style.css")
    (SITE / ".nojekyll").write_text("")
    for ch in book["chapters"]:
        img = HERE / "chapters" / ch["dir"] / "img"
        if img.exists():
            shutil.copytree(img, SITE / ch["dir"] / "img")
    order = list(sources)
    for key, b in built.items():
        out = SITE / f"{key}.html"
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(page(book, key, built, order))
        n_img = b["body"].count("<img ")
        n_ref = b["body"].count('<li id="ref-')
        print(f"{key}.html: {n_img} images, {n_ref} refs")
    if "--no-search" not in args:
        subprocess.run([sys.executable, "-m", "pagefind", "--site", str(SITE)], check=True)


if __name__ == "__main__":
    main(sys.argv[1:])
