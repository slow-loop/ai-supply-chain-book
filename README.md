# AI 供應鏈

AI 資料中心硬體的問答式筆記，一個題目一章。網站：https://slow-loop.github.io/ai-supply-chain-book/

研究（原始素材、調查紀錄、題庫）在 hello-video 的 `channels/market-decoded/` 做，寫好的章節放這裡。

## 建網站

```bash
uv run build.py
```

產生 `site/`（不進 git）。build 會檢查出處 key、圖片路徑、頁面之間的連結和錨點，有錯就不產生。寫的時候加 `--no-search` 比較快。push 到 `main` 之後 GitHub Actions 會自己建站、發佈。

本機看：

```bash
python3 -m http.server -d site 8000
```

## 結構

| 路徑 | 內容 |
|---|---|
| `book.yaml` | 章、每章的頁面和順序。新頁面要寫進來，沒寫進來的 build 會報錯 |
| `index.md` | 網站首頁 |
| `chapters/<章>/` | 一章一個資料夾，`index.md` 是這章的總覽，其他一個主題一份 |
| `chapters/<章>/img/` | 這章用到的圖 |
| `refs/` | 出處，全書共用；一章一份 `refs/<章>.yaml`，或拆成 `refs/<章>/<頁>.yaml` |
| `style.css` | 全站樣式，也是自己畫的 SVG 用的 class |

## 寫法

- **開頭寫日期**：每頁第一段寫資料截至哪一天。
- **標題帶 id**：`## 問題寫在這裡 {#q22}`。別的頁要連過來的 h2、h3 都要有 id。
- **出處用註腳**：句尾 `[[key]]` 或 `[[key1,key2]]`。key 寫在 `refs/` 的 yaml（who、title、date、level、url、clip）。內文不寫「某某說」「（某報 日期）」；公司講自己的事，公司可以當主詞。
- **別人的圖要標出處**：圖說最後放 `[[key]]`。`![圖說寫在這裡[[key]]](img/xxx.png)`。自成一段的圖會變成有圖說的 figure；同一段兩張並排、三張以上一排三張；圖後面接 `{.s}`、`{.xs}` 變小。
- **連到別的頁**：同一章 `[文字](lasers.md#las-shortage)`，別章 `[文字](../ccl/index.md#q1)`。
- **自己畫的圖**：直接寫 `<svg>`，用 `style.css` 的 class（box、hl、head、item、note、solid、cu、light、dash、bar、bar2、grid），不寫死顏色；圖說標「示意圖，非實際比例」。
- **表格**：一般 Markdown 表格。

## 加一章

1. 開 `chapters/<章>/`，放 `index.md` 和各頁，圖放 `img/`。
2. 出處寫進 `refs/<章>.yaml`。
3. 在 `book.yaml` 加這章，在首頁 `index.md` 的表格加一列。
