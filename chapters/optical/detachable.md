# 可拆式接頭、玻璃橋：FAU 會變成什麼

<p class="src">2026-10-12。CPO 主題筆記之一。FAU（光纖陣列單元，把一排光纖對準光晶片的小零件）本身是什麼、怎麼做，見 <a href="fau.html#q11">FAU 本身</a>；這一份講它在 2026 年的兩個變化：拆成「黏在晶片上的接座」和「可以拔的插頭」兩半，以及 Corning 用一塊玻璃取代 V 形槽的玻璃橋。句尾小數字是參考資料，文末標了可信度。</p>

## 為什麼要可拆？ {#det-why}

先看今天的麻煩。插拔式光模組壞了，從交換器前面板拔出來換一支就好；CPO（共同封裝光學，把光引擎和交換器晶片裝在同一片基板上）的光引擎卻是焊在基板上的。要拆下來，得在晶片旁邊加熱到 220 到 260°C，而光引擎裡次微米等級的光纖對位撐不過第二次加熱，所以焊上之後幾乎沒有重工的路[[tomshardware-npo-20260813]]。業界報導也寫，「對位失準即報廢」已是共識[[technews-gmt-20260320]]。至於常被轉述的「整批報廢」，沒有找到原文。

光纖如果一開始就永久黏在光引擎上，還會卡住另一件事：回焊（把整顆封裝放進爐子裡讓錫球融化焊上去）時光纖和膠要一起過爐，光引擎也沒辦法在接上光纖之前先單獨測好。2026 年各家的方向是**先測好、再接上**：光纖做成可以拔插的接頭，晶粒和光引擎先篩過，最後一步才接光纖，避開「最後才永久貼光纖」的良率風險[[marvell-ectc2026]]。Marvell 的論文甚至把可拆式接頭稱為 I/O 小晶片「事實上的必要條件」[[marvell-ectc2026]]。

NVIDIA 已經這樣做。NVIDIA 說 Spectrum-X 交換器用的是「光從晶片表面垂直出來」的可拆式光纖接頭：光引擎能過回焊，接上交換器晶片之前先全部篩選，光纖在最後階段由精密機台全自動接上[[nvidia-blog-20260106]]。每個 Spectrum-X 封裝有 32 顆光引擎，每顆 16 收 16 發、3.2 Tbps，直接回焊到模組基板上，再用可拆式光學接頭做自動化量產[[nvidia-blog-20250826]]。NVIDIA 在 Hot Chips 2025 的簡報把一道光的路排成一串，光纖接頭是其中獨立的一格，「可拆式光纖接頭」也被列為它的特點之一[[hotchips2025-nvidia-cpo-slides]]。

![NVIDIA 簡報上的一道光：由左到右是光的晶片（Photonic IC）、電的晶片（Electronic IC）、兩者疊在一起的剖面、台積電 COUPE 的微透鏡加表面耦合、光纖接頭（Fiber Connector，一排光纖接在透明的接頭上）、光學子模組（Optical Sub-Assembly，金屬外殼拉出光纖）。光纖接頭在這條路上是單獨的一站。廠商簡報圖[[hotchips2025-nvidia-cpo-slides]]](img/vendor/nvidia-hotchips2025-cpo-chain-pic-to-fiber-connector-p14-20250826.png)

![NVIDIA 專利裡的一整顆 CPO 封裝：中間方形是晶片區，旁邊每一個小方塊（600）是一個光纖接頭，8 個一組（800），扣在光引擎上，後面拉出光纖排線。專利寫一顆封裝可以有 4 組、每組 8 個。示意圖，專利線稿[[us20260276925a1]]](img/patents/US20260276925A1-FIG1A.png){.s}

NVIDIA 的兩台交換器接法不一樣（見 [FAU 的固定式和可拆式](fau.md#fau-types)），Quantum-X 的光引擎還裝在可拆的光學子模組上[[semianalysis-cpo-book]]。

**「可拆」能帶來的維修好處有上限。** 一家研究機構說，Quantum-X 的 FAU 做成可拆，是為了光纖斷了能換；但機殼裡的光纖要穿過光纖匣，換一顆 FAU 得打開機殼、拆掉壞的、重新穿線，比在前面板換一支插拔式模組麻煩得多[[semianalysis-cpo-book]]。產品規格也看得出它不是為了天天拔插：Lightmatter 的可拆 FAU 標的是 50 次以上[[lightmatter-vclick-product]]；Senko 和 PHIX 合作時說，可拆是「通往未來現場可維修」的路[[senko-phix-ecoc2026-20260917]]。照目前公開的說法，可拆的主要用處在生產線上「先測好、再接上」，不是讓機房常常換。

現場故障資料也還沒指向 FAU。Meta 公開的 CPO 可靠度數據裡，第一階段主要的失效來源是外部雷射模組驅動電路上一顆元件劣化；「髒的光纖和接頭」是插拔式和 CPO 共同的問題；沒有把 FAU 單獨列成一項。這份數據目前只看到社群的整理，沒找到論文原文[[simpletechtrend-meta-cpo-2026]]。可靠度的整理見 [可靠度數據](equipment-test.md#eq-reliability)。

## 拆成哪兩半？哪一半最精密？ {#det-structure}

各家的結構都一樣是兩半：**一半永久固定在光晶片（PIC）上，另一半帶著光纖、可以拔插。**下面這張圖由上到下是：可拆的光纖接頭、蓋板、永久黏在晶片上的接座、PIC。接座一次黏好，光纖接頭可以拔插。

![可拆式的結構：由上到下是可拆的光纖接頭、蓋板、永久固定在晶片上的接座（SEAT）、PIC。接座一次黏好，光纖接頭可以拔插。廠商示意圖[[senko-wiwynn-computex2026]]](img/vendor/senko-wiwynn-computex2026-seat-detachable-pic-202606-03.png){.s}

<div class="scroll">
<svg viewBox="0 0 900 360" width="100%" role="img" aria-label="可拆式接頭的兩半和三個對位步驟">
<defs><marker id="detarrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" style="fill:var(--fg)"/></marker></defs>
<text class="head" x="30" y="40">永久固定在晶片上</text>
<text class="head" x="410" y="40">可以拔的插頭</text>
<rect class="box" x="30" y="205" width="320" height="55"/>
<text class="item" x="190" y="238" text-anchor="middle">PIC（光的晶片）</text>
<rect class="hl" x="220" y="120" width="120" height="85"/>
<text class="item" x="280" y="158" text-anchor="middle">接座</text>
<text class="note" x="280" y="180" text-anchor="middle">（多半含透鏡）</text>
<line class="dash" x1="375" y1="75" x2="375" y2="270"/>
<rect class="box" x="400" y="100" width="240" height="120"/>
<text class="note" x="410" y="122">插頭外殼</text>
<rect class="hl" x="415" y="135" width="175" height="55"/>
<text class="item" x="502" y="168" text-anchor="middle">FAU（V 槽＋光纖）</text>
<line class="light" x1="590" y1="152" x2="860" y2="152"/>
<line class="light" x1="590" y1="162" x2="860" y2="162"/>
<line class="light" x1="590" y1="172" x2="860" y2="172"/>
<text class="note" x="650" y="140">光纖排線（接到機內整線、前面板）</text>
<path class="solid" d="M300,205 L300,162 L413,162" marker-end="url(#detarrow)"/>
<text class="item" x="228" y="112">①</text>
<text class="item" x="424" y="130">②</text>
<text class="item" x="381" y="72">③</text>
<text class="note" x="30" y="295">① 最精密的一步：接座對準 PIC 再黏死。有的用測試光纖通光、找最亮的位置（主動對位），有的靠擋塊和記號（被動對位）。</text>
<text class="note" x="30" y="318">② FAU 對準插頭再黏死，在插頭這一側做；可拔的那一半裡面多半還是一顆 FAU。</text>
<text class="note" x="30" y="341">③ 插上、拔下：靠插銷或定位座落回同一個位置。NVIDIA 專利寫重複拆裝的誤差在次微米以內。</text>
</svg>
</div>
<p class="tag">示意圖，非實際比例。依各家專利和新聞稿整理[[us20260276917a1,senko-gf-detachable-20250924,us20260267080a1,us20260147160a1]]</p>

### 各家哪一半黏死、哪一半能拔

| 公司 | 永久固定在晶片上的那一半 | 可以拔的那一半 |
|---|---|---|
| NVIDIA（一件專利） | 固定座，黏在 PIC 上，上面有幾個定位點[[us20260276917a1]] | 插頭，裡面黏著一顆 FAU[[us20260276917a1]] |
| NVIDIA（另一件專利） | 插座，裡面有斜面鏡和微透鏡[[nvidia-mellanox-us20260063849a1]] | V 槽基板的 FAU，從側面滑進插座[[nvidia-mellanox-us20260063849a1]] |
| Senko＋GlobalFoundries | 先用主動對位把微透鏡嵌進 PIC 上蝕刻出的溝槽，量過光，再把 SEAT 接座直接黏在晶粒表面[[senko-gf-detachable-20250924]] | Senko 的金屬 PIC 耦合器（MPC），被動對位插上接座[[senko-gf-detachable-20250924]] |
| Lightmatter vClick | 晶片端的垂直擴束光學做在晶圓製程裡，撐得過封膠再研磨的製程[[lightmatter-vclick-20260311,lightmatter-vclick-product]] | 可拆 FAU，用 Senko 的 SEAT 和 MPC[[lightmatter-vclick-20260311]] |
| Marvell（併入的 Celestial AI 技術） | 封膠前用折射率匹配膠把透鏡光學塊黏在 PIC 頂面，研磨後露出來，再黏 FAU 接座[[marvell-ectc2026]] | FAU[[marvell-ectc2026]] |
| Teramount（已被 Molex 收購） | 「光學凸塊」，在矽光子晶圓製程裡做出來[[gazettabyte-teramount-20240326,gazettabyte-teramount-20260129]] | 「光學插頭」，抓著光纖[[gazettabyte-teramount-20240326]] |
| Corning（翻轉式插座專利） | 底座永久黏在 PIC 上[[us20260276918a1]] | 會翻的載具接 FAU，壓下去落到對位位置[[us20260276918a1]] |
| Corning（擴束式專利） | PIC 端微透鏡陣列加插座[[us20260267074a1]] | 帶 V 槽的 FAU 加 FAU 端微透鏡陣列[[us20260267074a1]] |
| Corning＋GlobalFoundries 玻璃橋 | 晶片上的機械擋塊（管高度）和微影記號（管平面位置）[[corning-gf-ectc2026]] | 可拆的玻璃波導接頭（見 [玻璃橋](#q29)） |
| 波若威 | 插座外殼加 PIC 端透鏡陣列，用膠固定[[us20260147160a1]] | 插頭外殼加準直器陣列（光纖陣列加準直透鏡），靠插銷對位[[us20260147160a1]] |
| Ayar Labs | 黏在晶片上的插座[[us20260267080a1]] | 裝著 FAU 的插頭，兩根插銷加扣具[[us20260267080a1]] |
| HTK（日本本多通信工業） | 透鏡陣列和接座用樹脂一體成型[[htk-cpo-connector-202601]] | 標準 MT 插芯；主機板裝進機殼之後才接光纖，光纖不用過回焊[[htk-cpo-connector-202601]] |
| 合聖（AuthenX） | 晶片上放超穎透鏡（用奈米結構做的平面透鏡）[[technews-authenx-20260622]] | 另一端接 FAU[[technews-authenx-20260622]] |

下面幾張是專利裡的樣子，各代表一種「兩半怎麼對上」的做法。

![擴束式：晶片這邊（101）在波導出口放一排透鏡（110），把光放大成一段較粗的平行光（115）；光纖那邊（103）也有一排透鏡（114），把粗光束再聚回光纖。兩邊在虛線（112）分開，中間光束粗，接回去時差一點點位置，光也不太會漏。示意圖，專利線稿[[us20260267074a1]]](img/patents/US20260267074A1-FIG1.png) ![插銷式：左邊是黏在晶片上的插座（260），右邊是光纖的插頭（160）。插頭上的插銷（180）插進插座的孔（280），兩邊的透鏡（240、140）就對準，光從晶片的波導經過兩顆透鏡進到光纖（124）。示意圖，專利線稿[[us20260147160a1]]](img/patents/US20260147160A1-FIG3.png)

![定位座式：一個從晶片上拔起來的光纖接頭（600）。下面小方塊是光的晶片（6318），上面黏著固定座（322）；接頭壓回去時，靠固定座上的幾個定位點落回同一個位置，重複拆裝的誤差在 1 微米以內。示意圖，專利線稿[[us20260276917a1]]](img/patents/US20260276917A1-FIG1A.png) ![同一件專利的組裝順序，由上到下：固定座平放對準 PIC → 用一根或多根測試光纖把固定座的光學窗口對準 PIC → 把固定座黏死 → FAU 對準插頭 → 把 FAU 黏死在插頭裡。前三步做的是接座，後兩步才是 FAU。專利線稿[[us20260276917a1]]](img/patents/US20260276917A1-FIG7A.png)

![插座加扣具：晶片（603）上黏著插座（609），光纖排線（616）末端的 FAU（615）裝在插頭（621）裡。插頭的兩根插銷（623、625）插進插座，扣具（627）壓住，兩邊的透鏡（605、617）就對準。圖上的 A–F 是剖面線，可以忽略。示意圖，專利線稿[[us20260267080a1]]](img/patents/US20260267080A1-FIG6A.png) ![翻轉式：插座（150）繞著轉軸（170）掀起來，把 FAU（20）放進去，再壓下來被後面的卡榫（138a、138b）扣住，FAU 就落到對準的位置。示意圖，專利線稿[[us20260276918a1]]](img/patents/US20260276918A1-FIG1.png)

![做成產品的樣子：一顆封裝的金屬框下緣扣著一條可拆的接頭，接頭拉出三束黃色光纖，每束末端是一顆 FAU。廠商產品照[[lightmatter-vclick-product]]](img/vendor/lightmatter-vclick-detachable-fau-product-20261010-01.webp){.xs}

### 可以拔的那一半，裡面還是 FAU 嗎？

是。NVIDIA 專利的插頭裡黏的是一顆 FAU[[us20260276917a1]]；Corning 擴束式專利的權利要求直接寫接頭包含一顆有 V 槽的 FAU 和黏在上面的微透鏡陣列[[us20260267074a1]]；Ayar Labs 專利的插頭裡也是 FAU[[us20260267080a1]]。廠商自己的產品名也這樣叫：Coherent 把 FlexConnect 叫「可拆式 FAU 接頭」，強調拔插重複性、互換性、光路不用膠、撐得住高功率雷射[[coherent-ecoc2026-20260920]]；Lightmatter 把 vClick 叫「可拆式 FAU（dFAU）」[[lightmatter-vclick-product]]。緯穎在 COMPUTEX 2026 的展板標題是「Optical Engine Detachable Solution｜Fiber Array Unit (FAU)」[[trendforce-computex2026-cpo-20260611]]。大立光 2026 年第三季法說說，客戶希望它從 FA 延伸到 FAU、甚至 FAU＋Carrier，理由是整合出貨能減少良率責任的爭議，「目前聚焦 detachable FAU」；這段目前只看到法說筆記[[stockfeel-largan-q3-20261008]]。

所以可拆式沒有拿掉 FAU，而是把它拆成兩件：**接座＋帶 FAU 的插頭**，兩件可能由不同公司做。

### 黏在晶片上的那一半，還要多精密？

這一題各家分成兩邊。

**還在做主動對位或次微米對位的。**主動對位是邊通光邊量、把零件推到光最亮的位置再固定（見 [FAU 怎麼對準](fau.md#q14)）。

- NVIDIA 的專利：先用測試光纖把固定座對準 PIC 再黏死，測試光纖量到的光回饋給下一步的移動；之後 FAU 對準插頭再黏死；拔插後光纖對 PIC 的對位在「預定的次微米公差」內[[us20260276917a1]]。另一件把整顆封裝的接頭組拆成三步對位：接頭彼此之間先對好、每個接頭對各自的 PIC、再對定位介面[[us20260276925a1]]。
- Senko＋GlobalFoundries：微透鏡用主動對位嵌進溝槽，量過光才黏接座[[senko-gf-detachable-20250924]]。Senko 和 PHIX 的方案組合了微稜鏡陣列、SEAT 接座、對位母件和「精密六軸對位製程」[[senko-phix-ecoc2026-20260917]]。Senko 在 SEMICON Taiwan 2026 的演講摘要把次微米對位精度、能過回焊、拔插的重複性和互換性列為主要難題[[senko-semicontaiwan-202609]]。
- Marvell：FAU 接座的組裝要做到次微米對位，並嚴格控制膠層厚度；通道越多，光學塊越高越窄，越難[[marvell-ectc2026]]。
- 波若威的專利：PIC 和 PIC 端透鏡陣列用主動對位；插座和插頭接好後，還要再做一次準直器陣列對 PIC 的主動對位[[us20260147160a1]]。
- Corning 擴束式專利的背景段：擴束接頭方案「常有四個主動對位步驟」，但多數步驟的公差容易達成[[us20260267074a1]]。

**說可以被動對位的。**被動對位是靠機構、記號把零件放到位，不用通光量測。

- Lightmatter vClick：生產或接光纖時都不需要主動對位，規格表寫晶圓級被動對位[[lightmatter-vclick-product]]。
- Teramount：擴束讓組裝公差放寬到 ±30 微米，在這 60 微米範圍內只損失 0.5 dB；代價是晶圓製程比較複雜[[gazettabyte-teramount-20240326]]。Molex 收購時說它的被動對位容得下大的組裝誤差，適合晶圓級製程[[molex-teramount-close-20260507]]。它的專利寫，玻璃晶粒貼到 PIC 用取放機台加對位記號，精度「次微米到數十微米」，接座放好、微調後再灌膠固定[[us20260299225a1]]。
- Corning＋GlobalFoundries：晶片上的機械擋塊控制高度，PIC 和玻璃上的微影記號控制平面位置[[corning-gf-ectc2026]]。
- Intel：用被動對位把剛性玻璃耦合器貼進 PIC 的 V 槽，論文說它比傳統 FAU 的光斑匹配更好、損耗更低，也能做成帶透鏡和反射鏡的可插拔接頭[[intel-ectc2026]]。
- imec＋ASMPT：76 微米的擴束光纖陣列耦合，側向容差 ±12 微米[[imec-asmpt-expanded-beam-202604]]。
- 合聖新聞稿說，傳統永久接合需要「接近零」的對位公差，它用超穎透鏡放大容差[[authenx-detachable-2dfau-20260528]]。

**這裡改寫了原本的看法。**原本把精度難度放在「FAU 廠把 FAU 做好、再對上光引擎」這一步。可拆式之後，一部分難度落在接座對 PIC 這一步，做這一步的可能是 Senko 這類接頭廠、晶圓代工廠（Teramount 的凸塊、Lightmatter 的晶片端光學都在晶圓製程裡做）、或封測廠（vClick 示範的是日月光的封裝流程[[lightmatter-vclick-20260311]]），不一定是 FAU 廠。至於「主動對位、人工佔成本大頭」那套數字（見 [FAU 為什麼難做](fau.md#q12)），講的是永久黏貼的 FAU；說能被動對位的幾家都沒有公開成本或良率，兩邊還不能直接比。

### 損耗多少？能拔幾次？

| 誰 | 公開的數字 |
|---|---|
| Lightmatter vClick | 插入和重插損耗 < 1.5 dB；50 次以上；頻寬 80 奈米以上[[lightmatter-vclick-product]] |
| Corning＋GlobalFoundries 玻璃橋 | 每個介面 < 1.5 dB，偏振相關損耗 < 0.5 dB，撐到 280 mW 光功率[[corning-gf-ectc2026]] |
| Senko 可拆 FAU | 重複性 < 0.15 dB（3σ），互換性 < 0.5 dB（3σ）[[senko-semicontaiwan-202609]] |
| Teramount | ±30 微米範圍內對位損失 0.5 dB；總插入損耗沒公開[[gazettabyte-teramount-20240326]] |
| 古河電工 12 芯接頭 | 連接損耗 < 0.5 dB，重複性 ±0.05 dB[[furukawa-cpo-connector-20250327]] |
| imec＋ASMPT 擴束 | 側向容差 ±12 微米[[imec-asmpt-expanded-beam-202604]] |
| NVIDIA | 沒公開 dB；專利只寫重複拆裝在次微米公差內[[us20260276917a1]] |
| Coherent FlexConnect、合聖、HTK、Corning 的 OFC 2026 接頭 | 沒公開數字，只寫「低損耗」[[coherent-ecoc2026-20260920,authenx-detachable-2dfau-20260528,htk-ofc2026-20260216,corning-ir-ofc2026-20260316]] |

拿什麼比：dB 是損耗的對數單位，每多 3 dB 光就少一半。前面板常用的接頭，擴束接頭聯盟公開的隨機插拔測試是平均 0.32 dB[[ebo-msa-ecoc2026-20260923]]；晶片端的可拆接頭公開的多在 0.5 到 1.5 dB 之間。

OCP 的開放矽光子白皮書說，標準應該規定 FAU 每個介面的插入損耗（典型和最大）、通道間一致性、回波損耗、偏振相關損耗、熱循環和老化下的損耗漂移；可再插的接頭要標拔插次數，並符合 IEC 61753。具體數字留給之後的基礎規格[[ocp-opensiph-whitepaper-202607]]。

## 誰在做？ {#det-who}

| 公司 | 東西 | 做到哪（各自怎麼說） |
|---|---|---|
| NVIDIA | Spectrum-X、Quantum-X 的可拆接頭 | 隨交換器出貨[[nvidia-blog-20260106]]；Spectrum-X 量產進度見 [量產到哪一步](timing.md#q27) |
| Senko（日） | 36 芯可拆式 MPC 接頭 | 2025-04 說整合進 Marvell 以 6.4T 光引擎為基礎的客製 XPU 架構；沒寫是否出貨[[senko-marvell-36ch-20250404]] |
| Senko＋GlobalFoundries | 晶圓級可拆接頭加 SEAT 接座 | 2025-09 發表；GlobalFoundries 說能在紐約廠量產；沒寫出貨[[senko-gf-detachable-20250924]] |
| Senko＋PHIX | 歐洲的可拆光纖組裝 | 2026-09 宣布合作框架[[senko-phix-ecoc2026-20260917]] |
| Lightmatter（和 Senko） | vClick | 產品頁寫「Production-validated」；示範在日月光的封裝流程[[lightmatter-vclick-product,lightmatter-vclick-20260311]] |
| Teramount（Molex） | TeraVERSE | 送樣中；多家代工廠已把凸塊做進晶圓、大型封測廠組裝；目標 2027 年中達到年產數百萬顆的能力[[gazettabyte-teramount-20260129]]；Molex 2026-05-07 完成收購[[molex-teramount-close-20260507]] |
| Astera Labs（美） | 高密度、可拆、能過回焊的光纖貼合連接器（用它收購的 XScale 的核心技術） | 2026 年 5 月法說會（轉錄稿）：說預計 2027 年起量產出貨，致詞另說這款超高精度光纖耦合器正在一家大型 AI 平台業者做認證。8 月法說會（轉錄稿）把它列為光學策略的第一步：最長 50 公尺、超低延遲的高密度光纖貼合方案，第一個一線客戶預計 2027 年量產[[fool-astera-2026q1-20260505,fool-astera-2026q2-20260811]] |
| Corning | 玻璃橋、以 FAU 為基礎的可拆接頭 | 論文和展示階段，沒寫出貨[[corning-gf-ectc2026,corning-ir-ofc2026-20260316]] |
| Coherent | FlexConnect 可拆 FAU 接頭 | 2026-09 展示[[coherent-ecoc2026-20260920]]；自己的時程寫 2027 年第一季「production ready」[[coherent-photonlink-deck-20260921]] |
| 古河電工、Lightera（日） | Snap-Beam：擴束、磁吸、能過回焊的 PIC 接頭 | 2025-03 發表 12 芯款[[furukawa-cpo-connector-20250327]]；2026-09 得 ECOC 獎，發表 8×40＝320 通道一次接上的接頭[[furukawa-snapbeam-ecoc-20260922]] |
| HTK（日） | 樹脂一體成型的 CPO 接頭 | OFC 2026 展示「開發中的原型」[[htk-ofc2026-20260216]] |
| Intel | 玻璃耦合器加擴束的邊緣耦合可拆接頭 | ECTC 2026 論文，有損耗和可靠度測試資料[[intel-glass-ebconnector-202605]]；一家研究機構說 Intel 2025 年第二代 CPO 已改用插在封裝側邊的玻璃光橋接頭[[semianalysis-cpo-book]] |
| Marvell | Photonic Fabric 的可拆接頭組裝 | ECTC 2026 論文，「初步」光學和可靠度量測[[marvell-ectc2026]] |
| 合聖（光聖子公司，興櫃 7928） | Detachable 2D FAU（40 透鏡）、超穎透鏡 | COMPUTEX 2026 首次展示[[authenx-detachable-2dfau-20260528]]；媒體引法人說送樣美系大廠，「預計」2026 下半年少量試產、2027 有機會量產[[technews-authenx-20260622]] |
| 大立光 | detachable FAU、FAU＋Carrier | 法說筆記：FAU 客戶認證通過，明年年中量產[[stockfeel-largan-q3-20261008]]（見 [大立光、上詮各走到哪](fau-makers.md#q25)） |
| 波若威 | 可拆式光學組件專利；多款 FAU | 專利 2026-05 公開[[us20260147160a1]]；出貨時程見 [誰在做 FAU](fau-makers.md#q22) |
| 上詮 | 緯穎展板上的「FAU to mini-MT」；2026 年 9 月簡報專頁「Detachable 80CH/40CH/36CH FAU for MCM/OOI」 | 2025 法說筆記說它的 FAU 是固定封裝在光引擎內，可對插的是後段接頭[[fugle-foci-20250523]]；9 月簡報的交貨欄寫 2026／Q3 微量「(DFAU、FAU)」，沒寫出貨或客戶[[mops-foci-slides-20260902]]（並排見下文） |
| 포스텍（韓） | FAU 加微透鏡陣列的可拆式產品 | 只有媒體報導：和 AI 晶片公司談規格、評估樣品[[financescope-postech-20260910]] |
| Mixx（新創） | SxC 接頭，同一個外型支援單模和保偏光纖 | 只有媒體報導[[sdxcentral-mixx-20260901]] |

![緯穎 COMPUTEX 2026 的 CPO 供應鏈展板。右上「Optical Engine Detachable Solution｜Fiber Array Unit (FAU)」一格：Corning（展品是拖著光纖的 FAU 線束，標 FlexConnect）、上詮（FOCI，FAU to mini-MT）、Senko（MPC）、波若威（80、64、72 通道 FAU 和 40 通道擴束 FAU）。中排是機內光纖，下排是外部雷射模組的電連接器、籠子和光接頭。展場照片，含廠商產品[[trendforce-computex2026-cpo-20260611]]](img/vendor/trendforce-computex2026-wiwynn-cpo-supply-chain-board-20260611.jpg)

### NVIDIA 交換器上的接頭是誰做的？

**只有 Senko 自己說。**Senko 2025 年 3 月說，它為 Spectrum-X Photonics 和 Quantum-X Photonics 交換器供應光學連接方案，它的矽光子 PIC 接頭提供低損耗、可拆的晶片連接[[senko-nvidia-ecosystem-20250318]]。NVIDIA 的部落格、手冊、簡報都沒有寫接頭是哪家做的。NVIDIA 2025 年 3 月列的光纖接頭和光纖組件夥伴是波若威、Corning、Senko、天孚、Coherent，上詮、大立光不在名單上[[nvidia-blog-20250327]]；名單是合作開發的夥伴，不是完整的供應商名單。NVIDIA 自己的可拆式專利都是用子公司 Mellanox 的名義申請[[us20260276917a1,us20260276925a1,nvidia-mellanox-us20260063849a1]]。

另外兩份說法只有社群和紀要等級：一篇社群文章說 Quantum 3400 的 FAU 幾乎由天孚獨佔，Spectrum 改成可插拔接頭之後才把 Corning、Senko 放進第二供應商，沒附出處[[stt-fau-15-vendors-20260706]]；一份未具名的公司調研紀要說，可拆 FAU 的供應商有「公司」、天孚、Senko，上詮、波若威、Corning 計畫加入，但 Corning 和上詮的樣品還沒推出[[eastmoney-dfau-survey-20260531]]。

誰在 NVIDIA 交換器上把接座黏到 PIC、誰做那一步對位，查不到。誰實際在供 NVIDIA 的整張表見 [誰實際在供 NVIDIA](players.md#pl-nv)。

### 接座和插頭各是誰做？

- Senko 兩半都做：SEAT 是接座，MPC 是插上去的那一半[[senko-gf-detachable-20250924]]。Lightmatter vClick 用的也是 Senko 的 SEAT 和 MPC[[lightmatter-vclick-20260311]]。
- Teramount 的凸塊做在代工廠的晶圓上，插頭由 Teramount（現屬 Molex）提供[[gazettabyte-teramount-20260129]]。
- 玻璃橋：GlobalFoundries 的平台，Corning 的接頭[[convergedigest-gf-corning-202509]]。
- OCP 白皮書的分法：FAU 有兩端，PIC 那一端屬於光引擎本身，「通常是光引擎廠商的責任」；光纖那一端才是生態系的分界[[ocp-opensiph-whitepaper-202607]]。

### 台廠在哪一格？

緯穎名單上的可拆 FAU 供應商有波若威、上詮（另兩家是 Corning、Senko）[[trendforce-computex2026-cpo-20260611]]；大立光說聚焦 detachable FAU[[stockfeel-largan-q3-20261008]]；合聖做 Detachable 2D FAU[[authenx-detachable-2dfau-20260528]]；連訊被一篇報導列為有一維、二維高密度 FAU 和可插拔方案[[taiwanhot-fau-top10-20260908]]。上詮有一件已核准的「可插拔光學封裝結構」專利（US12411295B2），用插座加連接器加光纖陣列連接器；一篇社群文章說這是上詮「可重工光纖陣列連接」（RelFACon）的底層，專利原文這次沒抓[[stt-foci-patents-20260721]]。

上詮的位置有兩種說法要並排看：

| 說法 | 出處等級 |
|---|---|
| 緯穎展板把上詮放在「可拆式 FAU」一格，展品是「FAU to mini-MT」 | 展場照片[[trendforce-computex2026-cpo-20260611]] |
| 上詮 2025 年法說：它的 FAU 是固定封裝在光引擎內，可對插的是後段的接頭 | 法說筆記[[fugle-foci-20250523]] |
| 上詮 2026 年 9 月簡報：有一頁專寫「Detachable 80CH/40CH/36CH FAU for MCM/OOI」，交貨欄把 DFAU 和 FAU 並列、2026／Q3 微量；沒說已出貨、誰是客戶 | 公司簡報[[mops-foci-slides-20260902]] |
| 一份調研紀要（2026-05-31）：上詮計畫加入可拆 FAU，樣品尚未推出 | 調研紀要[[eastmoney-dfau-survey-20260531]] |

這也表示台廠不只走台積電 COUPE 供 FAU 這一條；不經過 COUPE 的幾條路整理在 [不經過 COUPE 的路](fau-makers.md#fau-routes)。

### 名稱撞在一起：FlexConnect

緯穎展板在 Corning 下面標「FlexConnect™」，Coherent 2026 年 9 月也把它的可拆 FAU 接頭叫 FlexConnect，兩個名字看起來是同一件東西，其實不是：

- Corning 的 CPO FlexConnect 是一種**光纖**：抗彎單模光纖，O 波段，模場直徑 9.2 微米，2025 年推出[[corning-oem139-flexconnect-202604]]；ECOC 2026 的獎項名單也寫「Corning CPO FlexConnect Fiber」[[convergedigest-ecoc2026-awards-20260922]]。Corning 的光纖管理型錄寫「預裝卡匣整合 CPO FlexConnect 和 PANDA 保偏光纖」[[corning-oem166-oms-202605]]。
- Coherent 的 FlexConnect 是一種**可拆式 FAU 接頭**[[coherent-ecoc2026-20260920]]。
- 所以緯穎展板 Corning 那一格的展品，是用 FlexConnect 光纖做的 FAU 線束（看圖判讀）；Lightmatter 的近封裝光引擎 L20 規格寫「Corning CPO Flexconnect」，指的也是光纖種類，不是 FAU[[lightmatter-l20-20261012]]。

Corning 自己的 FAU 線束生意見 [誰在做 FAU](fau-makers.md#q22)。

## 有沒有標準？ {#det-standards}

**晶片和光纖之間的可拆介面，目前沒有任何標準。**下表是 2026 年和這段介面最接近的幾個組織；各規格整體的比較見 [各種規格](alternatives.md#alt-specs)。

| 組織 | 管哪一段 | 有沒有管到晶片端的可拆接頭 |
|---|---|---|
| OIF（光互連論壇） | 已發布的 CPO 文件只有框架文件、3.2T CPO 模組、外部雷射模組 ELSFP 和它的管理介面[[oif-ia-list-20261012]]；2026 年第二季新開 12.8T／6.4T 近封裝光學模組專案，預計包含雷射配置和「光學接頭的考量」；同場的高密度接頭框架講的是**電**連接器[[oif-q2-2026-npo-20260604]] | 沒有 |
| OCP（開放運算計畫） | 開放矽光子工作流 2026-07 發了 294 頁的架構白皮書，把 FAU 的寬度、對位公差等級、損耗、拔插次數列為要「宣告」的參數，數值留給之後的基礎規格[[ocp-opensiph-whitepaper-202607,sdxcentral-open-cpo-20260814]] | 列了要管的參數，還沒有數值 |
| EBO MSA（擴束光學接頭） | 擴束接頭，把 9 微米光斑放大到 80 微米跨空氣隙；路線圖是 128 芯規格進行中、16 芯 MPO 討論中、16 芯小型接頭和外部雷射接頭計畫中；規格 1.0 還沒發布[[ebo-msa-ecoc2026-20260923,ebo-msa-site-20261012]] | 沒有，管的是面板、跳線、雷射模組那一段 |
| Open CPX MSA | 插在插座上的 CPO／近封裝光引擎模組；規格 1.0 已公開，光纖束直接從模組拖出，接頭型式留給應用自定，全文沒有 FAU 字樣[[opencpx-spec-v1-20260916]] | 沒有，晶片端的光纖貼合在模組內部完成 |
| OCI MSA | 只定光學實體層；外部光源用 ELSFP、光要耦合進保偏光纖再接到晶片[[oci-msa-spec-v1-20260311]] | 沒有，不管接頭和光纖 |
| ODCC 的 UPO（騰訊主導） | 只有一篇第三方整理說框架裡有「可插拔 FAU（D-FAU）」，讓光纖組件和光引擎分開處理[[fibermall-upo-npo-20260918]] | 有提到，規格查不到 |
| COBO、IEEE | 查不到它們發布過晶片對光纖可拆介面的規格 | 沒有 |

EBO 的成員很大：Oracle 主席，3M 共同主席，Amphenol、住友、Senko 是編輯；成員 60 家，包括 NVIDIA、Microsoft、Meta、Molex、TE、天孚、昂納、立訊、嘉澤、鴻海[[ebo-msa-ecoc2026-20260923,ebo-msa-site-20261012]]。它的第一份規格管的是擴束接頭，不是晶片端的 FAU[[3m-ebo-msa-20260512,ebo-msa-ecoc2026-20260923]]。

成立時間有兩種說法：一篇報導說 2026 年 3 月一共簽了六個光互連 MSA，包括 OCI、Open CPX、XPO、LPO、EBO 和四芯光纖的 SDM4[[hpcwire-oci-msa-20260824]]；EBO 自己的成立新聞稿是 2026 年 5 月[[3m-ebo-msa-20260512]]。

跟原本看法要對一下的地方：原本把 FAU 當成一種可以多家供應的零件。現在晶片端的接座各家結構都不一樣（[上面的表](#det-structure)），公開資料裡沒有任何一份規定接座長什麼樣，OCP 白皮書還明說 PIC 端是光引擎廠的責任。Open CPX 這類模組化的光引擎，則把光纖接到光引擎這一步放進模組廠，分工比較像今天的插拔式光模組。

## 保偏光纖會不會被拿掉？ {#det-pm}

保偏光纖是在纖芯兩側多兩塊應力區、讓光的偏振方向不亂跑的光纖（樣子見 [光纖本身](fau.md#q16)）。在 CPO 裡，它把外部雷射的光送進光引擎：光引擎裡的調變器對偏振方向很挑，雷射放在機殼外面（原因見 [雷射為什麼在外面](inside.md#q10)），一路上偏振不能亂。保偏光纖要一根根轉到同一個方向才能放進 FAU，是 FAU 裡最難做的一種（見 [FAU 一步一步怎麼做](fau.md#q13)）。

**2025 年 NVIDIA 提過拿掉它。**NVIDIA 在 ECTC 2025 的論文提出：外部雷射到發射端改用一般單模光纖，晶片上加主動偏振追蹤電路，自己把偏振轉回來；封裝成本約降 2.7 倍，代價是多約 0.74 dB 損耗[[nvidia-ectc2025-allsmf,laserfocusworld-nvidia-smf-202505]]。如果成真，雷射那一側的 FAU 規格會變。

**2026 年 NVIDIA 自己的下文：查不到。**查了 ECTC 2026 的論文收錄、OFC 2026、NVIDIA Research 的出版頁，只有 2025 年那篇。反方向的 2026 年事實倒有一串：

- NVIDIA 2026 年 9 月公開的可拆接頭專利，FAU 裡「只有一部分光纖是保偏光纖」，其餘是一般單模，接頭裡加一片只蓋住保偏光纖那一段的偏振片[[us20260276917a1]]。
- NVIDIA 同月公開的光纖整線盒專利，整線盒同時容納接運算的單模光纖和接外部雷射的保偏光纖[[us20260276934a1]]。
- 外部雷射模組的標準 ELSFP 定義了每個 MT-12 插芯放 4 根或 8 根保偏光纖，並以插芯兩個導孔的連線為基準規定偏振消光比[[oif-elsfp-02-202501]]；OCI 規格要求外部光源的光耦合進保偏光纖[[oci-msa-spec-v1-20260311]]。
- OCP 白皮書估：一個 102.4T 交換器托盤要 1,000 根以上單模訊號光纖，加約 128 根給雷射用的保偏光纖[[ocp-opensiph-whitepaper-202607]]。
- 賣的人在加碼：Coherent 說它在 CPO 裡供應雷射、外部雷射模組、隔離器、保偏光纖、光纖貼合組件和矽光子[[futurum-coherent-q4fy26-20261009]]；長飛總裁說保偏光纖市場「非常火爆」，未來一兩年需求 10 到 20 倍成長，正在擴產[[10jqka-yofc-pmf-20260719]]，並說 NVIDIA、Marvell 等在外部雷射到光引擎之間用長飛的方案，這句 NVIDIA、Marvell 沒有證實[[thepaper-yofc-pmf-20260718]]；長飛 2026-09 發布 CPO／近封裝光學專用特種光纖[[c114-yofc-copackalign-20260917]]；古河集團的 Lightera 推出 CPO 用 80/125 微米的保偏和單模光纖[[lightera-cpo-fiber-20260316]]；新創 Mixx 的接頭在同一個外型裡同時支援單模和保偏[[sdxcentral-mixx-20260901]]。

![NVIDIA 可拆接頭專利裡的光纖排。8E 是從端面看：一排光纖躺在 V 形槽裡，中間四根（611）各有兩個小圓，是保偏光纖的應力區；兩邊（612）是一般單模光纖。8D、8F：接頭裡加一片偏振片（840），上面只有中間一條（842）蓋住保偏光纖那一段。專利線稿[[us20260276917a1]]](img/patents/US20260276917A1-FIG8D-8F.png){.s}

**供應商端第一個回應：上詮。** 2025 年 11 月的法說會上，有人問「聽說有大廠在開發偏振追蹤器，未來可能不需要保偏光纖，公司有沒有參與」，回答是：業界確實希望拿掉保偏光纖，這需要更多設計與開發；若能成功，對 FAU 和光纜的生產效率會是最大化，所以正積極參與、配合客戶做相關改善。這是第三方（富果）整理的問答，不是逐字稿，引用前要核對影音；它沒有說做到哪一步，也沒說是哪個客戶[[fugle-foci-20251124]]。

**拿掉保偏光纖的另外兩條路。**

- 晶片上自己補償偏振：一篇 OFC 2026 的學界論文做了矽光子偏振補償元件，能補償 1 公里外外部雷射送來的任意偏振態，插入損耗 1.9 dB、偏振相關損耗 0.77 dB[[mcgill-ofc2026-polcomp-202603]]。
- 把雷射放回封裝裡：OCP 白皮書說，光源整合到晶片上可以省掉保偏光纖和它接頭的消光比預算，代價是封裝熱環境變差、壞了要換整個封裝[[ocp-opensiph-whitepaper-202607]]。華為的近封裝光引擎用內置光源，不需要保偏光纖[[eeo-huawei-npo-20260918]]；阿里、華為在一場研討會上也主張整合雷射，Coherent 偏向外部雷射（社群整理）[[simpletechtrend-ipec-npo-20260508]]。中國的路線見 [華為、阿里、騰訊的 NPO](china.md#cn-npo)。

**所以 v4 那一條要改寫。**v4 寫「保偏光纖可能被拿掉」，只有 NVIDIA 2025 年一篇論文；到 2026 年 10 月，NVIDIA 自己的新專利、ELSFP、OCI、OCP 和賣保偏光纖的廠商都還在用或在推保偏光纖。會不會被拿掉，比較像是看架構：外部雷射架構（NVIDIA、OCI、Open CPX 的外部雷射版）還要它，內置光源的架構（華為、Open CPX 的內建雷射版）不要它。

### 外部雷射那一端的接頭：ELSFP

保偏光纖的另一端插在外部雷射模組上，這一段有標準。最新版是 OIF-ELSFP-02.0（2025-01），文件寫「目前正式進入維護」[[oif-elsfp-02-202501]]。

- 光功率分六級，每根光纖每個波長從 11 dBm 到 26 dBm（±1.5 dB）[[oif-elsfp-02-202501]]。拿比較：26 dBm 約 400 mW，是 11 dBm（約 12.6 mW）的 30 倍左右（計算：10^(26/10) ÷ 10^(11/10) ＝ 10^1.5 ≈ 31.6）。
- 接頭是模組背面的盲插接頭，12、24 或 36 芯 MT 插芯，可以實體接觸或留空氣間隙；目的是雷射壞了能在現場安全更換，並把系統維持在雷射危害等級 1[[oif-elsfp-02-202501]]。
- 功率高是擴束接頭的理由之一：2024 年有論文寫，多數 CPO 做法用保偏光纖送外部雷射的光，功率會到 250 mW 以上，擴束接頭可以降低外露表面的光強度[[usconec-eb-highpower-202401]]。
- 緯穎展板的雷射模組一欄：Molex 和 TE 供電連接器和籠子，Senko 供光接頭和轉接器[[trendforce-computex2026-cpo-20260611]]。

雷射本身的供應鏈見 [從銦到外部光源模組的幾層](lasers.md#las-layers)。

## 康寧的玻璃橋會取代 FAU 嗎？ {#q29}

玻璃橋（GlassBridge）是 Corning 的另一種接法：不用 FAU 的 V 形槽一根根擺光纖，而是在一片玻璃晶圓上用離子交換（IOX，把玻璃裡的離子換掉，讓那一條的折射率變高、能導光）做出一排波導，切成小塊。一端貼著 PIC 的側邊，一端是標準的 TMT 插芯（MPO、MMC 這類多芯接頭用的插芯），光纖接頭插上去就對準[[corning-glassbridge-brochure,itiger-glassbridge]]。它靠晶片上的擋塊和對位記號**被動對準**，可以拆；論文標題寫每個接面損耗低於 1.5 dB[[corning-gf-ectc2026]]。

![玻璃橋裝在 CPO 上的樣子：中間紅色大塊是交換器晶片，四周 8 塊是 PIC，每塊 PIC 的邊上插 2 個玻璃接頭（綠色），光纖帶往四面拉出去。右下放大：玻璃裡一排發亮的光通道直接貼著 PIC 側邊，後面接插芯和兩根導針。廠商型錄示意圖[[corning-glassbridge-brochure]]](img/vendor/corning-glassbridge-cpo-layout-brochure-202603-02.png) ![玻璃橋本體：一小塊玻璃裡做出一排平行的光通道，兩根金屬導針讓光纖接頭插上就對準。不用 V 形槽，也不用一根根擺光纖。廠商渲染圖[[corning-glassbridge-page]]](img/vendor/corning-glassbridge-connector-render-20261011-01.jpg)

型錄和報導寫的規格[[corning-glassbridge-brochure,thelec-glassbridge-20260630]]：

| 項目 | 寫的是什麼 |
|---|---|
| 一個接頭幾芯 | 24 芯；一片 PIC 可以放好幾個（例如 2 × 24） |
| 玻璃本體寬 | 6.4 毫米 |
| 損耗 | O 波段光纖到 PIC 耦合 1.5 dB（型錄）；Corning 對媒體說目標是低於 2 dB |
| PIC 那一側的間距 | 可選 40、80、127、165 微米；首款產品支援 30 微米以上 |
| 對位方式 | 被動對位 |
| 可不可以拆 | 可以 |
| 能不能過回焊 | 可以 |
| 光纖那一側的介面 | 標準 TMT 插芯（125 微米孔）、實體接觸 |
| 製法 | 晶圓級做出離子交換波導 |

<div class="scroll">
<svg viewBox="0 0 900 260" width="100%" role="img" aria-label="FAU 和玻璃橋的組裝步驟對照">
<defs><marker id="gbarrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" style="fill:var(--fg)"/></marker></defs>
<text class="head" x="20" y="28">把一排光纖接到 PIC 側邊：兩種做法的步驟</text>
<text class="item" x="20" y="80">FAU</text>
<rect class="box" x="110" y="55" width="170" height="44"/><text class="item" x="195" y="82" text-anchor="middle">光纖一根根擺進 V 槽</text>
<rect class="box" x="320" y="55" width="170" height="44"/><text class="item" x="405" y="82" text-anchor="middle">通光、量光、移動找最亮</text>
<rect class="box" x="530" y="55" width="170" height="44"/><text class="item" x="615" y="82" text-anchor="middle">上膠、照光固化</text>
<line class="solid" x1="280" y1="77" x2="318" y2="77" marker-end="url(#gbarrow)"/>
<line class="solid" x1="490" y1="77" x2="528" y2="77" marker-end="url(#gbarrow)"/>
<text class="note" x="110" y="122">對位在組裝現場一顆一顆做（主動對位）</text>
<text class="item" x="20" y="180">玻璃橋</text>
<rect class="box" x="110" y="155" width="170" height="44"/><text class="item" x="195" y="182" text-anchor="middle">晶圓上做好一排波導</text>
<rect class="hl" x="320" y="155" width="170" height="44"/><text class="item" x="405" y="182" text-anchor="middle">靠擋塊、記號放上去</text>
<rect class="box" x="530" y="155" width="170" height="44"/><text class="item" x="615" y="182" text-anchor="middle">TMT 插芯接頭插上</text>
<line class="solid" x1="280" y1="177" x2="318" y2="177" marker-end="url(#gbarrow)"/>
<line class="solid" x1="490" y1="177" x2="528" y2="177" marker-end="url(#gbarrow)"/>
<text class="note" x="110" y="222">波導位置在玻璃製程裡就定好，組裝時被動對準</text>
<text class="note" x="720" y="80">（細節見 FAU 筆記）</text>
</svg>
</div>
<p class="tag">示意圖，非實際比例。細節見 <a href="fau.html#q13">FAU 一步一步怎麼做</a>、<a href="fau.html#q14">怎麼對準</a>。[[ctee-glassbridge-20260812,corning-glassbridge-brochure]]</p>

![Corning 2023 年的玻璃 CPO 構想剖面：左邊光纖接進接頭（Connector），進到做在玻璃表面的離子交換波導（IOX glass waveguides），再交給 PIC 的波導；PIC 和交換器晶片都放在玻璃封裝基板上，TGV 是穿過玻璃的導電孔。用的是同一套離子交換波導技術，但這不是玻璃橋產品本身。論文轉載圖[[mdpi-mi15-01211]]](img/papers/mdpi-mi15-01211-corning-glass-cpo-iox-waveguide-fig10.png){.s}

![2026 年 6 月 24 日首爾一場研討會上用的圖：玻璃塊裡的細線就是波導，兩根導針讓接頭直接放上去對準；右下寫「pick and place」，意思是用一般的取放機台就能裝。廠商簡報圖[[thelec-glassbridge-20260630]]](img/media/THEELEC-Corning-GlassBridge-20260630-01.png){.xs}

### 數字和耐熱

- 損耗的數字有兩種寫法要並排：論文標題和摘要寫每面低於 1.5 dB、偏振相關損耗低於 0.5 dB、撐到 280 mW[[corning-gf-ectc2026]]；一篇社群解讀引論文的圖說，實測 TE 偏振每面 1.44 dB、TM 偏振 1.75 dB（含 PIC 內波導損耗），偏振相關損耗約 0.3 dB[[stt-gf-corning-ectc2026-20260625]]。
- 耐熱：同一場會議 Corning 還有一篇玻璃配方的論文，社群解讀說 CPO 晶片旁的玻璃約 110°C，一般離子交換玻璃裡的銀離子會擴散、第一個月就失效；Corning 篩了 200 多種玻璃，做出五年折射率變化小於 1.5% 的配方[[stt-corning-glass-ectc2026-20260624]]。這篇的論文原文沒找到。

### 它會不會取代 FAU？

說法分兩邊，可以整理成下表。關鍵在一件事：玻璃橋接的是**晶片側邊**（邊緣耦合，EC），而今天 NVIDIA 交換器用的是光從晶片**表面垂直出來**的接法（光柵耦合，GC）[[nvidia-blog-20260106]]，兩種接法的晶片內部設計不同（見 [PIC 怎麼電光互換](inside.md#q7)）。

| 說會並存、不會很快取代 | 說長期有取代壓力 |
|---|---|
| Corning 的說法是玻璃橋是 FAU 的「補充」：傳統 FAU 在現在的應用裡仍然有效，只是光纖數極高時組裝和擴充變難；這句是媒體轉述產品頁 FAQ[[itiger-glassbridge]]。Corning 自己也在供 CPO 用的 FAU：它設計、製造帶 FAU 的光纖線束，交給光引擎廠裝上[[thelec-glassbridge-20260630]]，OFC 2026 同時展示以 FAU 為基礎的可拆接頭和 CPO 用光纖[[corning-ir-ofc2026-20260316]]。 | 券商的說法：FAU 廠在 CPO 的發展路上面臨長期顛覆壓力；CPO 和近封裝光學在 2028 到 2030 年逐步商業化時，玻璃橋會在新的部署專案裡和 FAU 競爭[[wallstreetcn-glassbridge-20260624]]。 |
| 大立光執行長說玻璃橋本質是為邊緣耦合設計的，「就算它（EC）成功，還是會有 GC 的市場；現在 GC 市場（規模）還是明顯大於 EC」；而且邊緣耦合也還是需要 FA 把光導出去[[wealth-largan-q2-20260709]]。媒體整理多家研究機構的看法，光柵耦合仍會是未來三到五年的主流[[ctee-glassbridge-20260812]]。 | 券商的說法：傳統 FAU 在光纖數大增時組裝複雜度急升、難擴充；玻璃橋用晶圓級的被動對位，密度更高、更好擴充[[wallstreetcn-glassbridge-20260624]]。 |
| 現有的 CPO 方案（Quantum、Spectrum 系列）已經定型，預計不受影響；2027 下半年 Rubin Ultra Kyber 用的 CPO 方案 2026 下半年完成設計確認，也不太可能被換掉。這兩點也是券商的說法[[wallstreetcn-glassbridge-20260624]]。 | 媒體評論：玻璃橋真正造成衝擊要兩件事同時成立，Corning 完成量產驗證，以及至少一家大客戶在新一輪 PIC 設計裡選擇邊緣耦合[[ctee-glassbridge-20260812]]。 |
| **Corning 財務長 2026-09 的時程**：到 2030 年，「CPO 的成長會由傳統產品帶動，也就是保偏光纖、FAU 這類已經存在、但還沒規模化的光學零件」；玻璃橋這類用玻璃的新產品「比較是 2030 年以後的機會」[[investing-corning-cfo-citi-20260909]]。 | 玻璃也不只 Corning 在做：Intel 的論文說剛性玻璃耦合器是傳統 FAU 的替代，損耗更低[[intel-ectc2026]]，另一篇做成了玻璃耦合器加擴束的可拆接頭[[intel-glass-ebconnector-202605]]。 |

台積電的 COUPE 兩種接法都有（COUPE-GC 和 COUPE-EC），代工廠沒有替客戶決定用哪一種[[ctee-glassbridge-20260812]]。媒體報導的標題也大多落在「不是取代」這一邊[[digitimes-glassbridge-20260706,ctee-glassbridge-20260812]]。

**這裡改寫了 v4 的看法。**v4 把 Corning 放在「拿玻璃橋替代 FAU」的那一格。照 Corning 財務長自己的說法，2030 年前它的 CPO 營收主力是 FAU 和保偏光纖，也就是說，在 2030 年前 Corning 是 **FAU 線束的直接競爭者**，玻璃橋是更後面的事；它的 FAU 生意整理在 [誰在做 FAU](fau-makers.md#q22) 和 [一台交換器裡 FAU 值多少錢](fau-makers.md#fau-value)。

### 設備商和中國廠怎麼說玻璃橋

- **羅博特科（ficonTEC 的母公司，賣對位設備）**，2026 年 7 月的投資者關係活動記錄表：玻璃橋「並非全新技術，近期隨著行業需求變化重新受到關注」，ficonTEC 在更早的時間就和部分國際合作夥伴參與過玻璃橋的技術合作，量產化「會有一個過程」；玻璃橋和傳統 FAU 是互補關係，玻璃橋的優勢是能支持多波段光傳輸，傳統 FAU 的優勢是能集成多組光纖；不管走玻璃橋還是 FAU，ficonTEC 都能提供相關設備[[cninfo-robotechnik-irm-20260721]]。設備商兩條路都賣，所以這段話不替任何一邊下注。
- **華工科技**，2026 年 7 月的集體接待日：玻璃橋技術成熟後，能給光模組或光引擎帶來設計簡化等優勢，有利於產品開發；公司在 CPO、2.5D 封裝、3D 封裝都有布局和研究，玻璃基板是重要的技術路徑之一[[qgw-hgtech-20260709]]。
- **天孚通信**有兩次說法，角度不同：2026 年 7 月 9 日的記錄表說，任何一種技術從出現到規模產業化都需要一個時間週期，還要上下游供應鏈協同、客戶時間窗口等因素；公司有預研團隊，研究未來各種長期的新一代技術，「抓住每一代產品的機會」[[cninfo-tfc-irm-20260709]]。8 月 21 日的投資人問答回覆是「預計不會對公司的 FAU 產品產生重大影響」[[cninfo-irm-china-fau-20261012]]。前者談時間要多久，後者談有沒有影響，並排放，不下結論。

中國廠對玻璃橋的看法整理，見 [中國的 FAU 和零件廠](china.md#cn-fau)。

### 誰在用、什麼時候量產

- **合作對象**：公開的只有 GlobalFoundries。GlobalFoundries 說，玻璃橋是「配合 GF 平台 V 槽的玻璃波導邊緣耦合器」，雙方另在開發「垂直耦合的可拆光纖對 PIC 方案」；Corning 帶的是特殊玻璃配方、玻璃晶圓、離子交換、雷射加工和 FAU[[gf-corning-glassbridge-20250929]]。Corning 說正和多家夥伴共同開發，沒有點名[[thelec-glassbridge-20260630]]。
- **怎麼發表的**：v4 寫「2026 年 3 月出型錄、6 月正式發表」，要改正。2025 年 OFC 先預覽了玻璃波導接晶片的概念驗證[[corning-blog-cpo-fau-harness-2025]]；2026 年 3 月出型錄[[corning-glassbridge-brochure]]；5 月 ECTC 發表論文[[corning-gf-ectc2026]]；6 月 24 日是在首爾一場光通訊研討會上，由 Corning 韓國的 CPO 技術經理演講介紹[[thelec-glassbridge-20260630]]。Corning 沒有為這次發新聞稿，只有產品頁和型錄[[corning-glassbridge-page]]；9 月 ECOC 的新聞稿列了可拆光纖對晶片接頭、CPO 抗彎光纖、預組光纖托盤，沒有提玻璃橋[[corning-pr-ecoc2026-20260917]]。
- **量產時程**：Corning 沒有公開量產時程；財務長說是 2030 年以後的機會[[investing-corning-cfo-citi-20260909]]。中國廠宇瞳在投資人問答引「市場信息」說，玻璃橋在送樣、工程驗證和可靠度測試，量產「最快不低於一年」[[cninfo-irm-china-fau-20261012]]。

## 還不知道的 {#det-open}

日期從 [日曆](calendar.md#cal-events) 抄。

- **NVIDIA 交換器上的接座是誰黏、誰對位**：查日月光、矽品的法說和 2026 年專利；日月光營運長 7/30 說 CPO 服務內容要再等兩季，從 7 月底起算是 Q4 結果的法說（約 2027 年 2 月）；去年同期 10/30 開線上法說，今年的 Q3 法說還沒申報，可能提前講。
- **NVIDIA 方面說的接頭供應商**：目前只有 Senko 自己說；等 NVIDIA 下一次公布夥伴名單（GTC Washington, D.C. 11/30–12/3、GTC 2027 3/14–18）。
- **NVIDIA 接頭的插入損耗**：部落格、Hot Chips 簡報、手冊都沒有 dB 數字。
- **上詮 9 月簡報「Detachable 80CH/40CH/36CH FAU」到底出貨了沒、客戶是誰**：簡報只寫 2026／Q3 微量；看上詮 Q3 財報（11/14 前）和 11 月簡報有沒有改寫。
- **上詮「FAU to mini-MT」是什麼、和 RelFACon、US12411295B2 的關係**：抓 USPTO 全文；上詮去年同期 11/17、11/24 有法說，今年還沒申報。
- **大立光 FAU＋Carrier 是什麼、客戶是誰**：10/08 法說已開，目前只有筆記；要對照公司公布的簡報和逐字稿。
- **合聖的產能**：竹南 FAU 線年產 20 萬套、第三季架設第四季試產是社群和媒體的說法，要對公司公告或興櫃公開說明書。
- **Marvell 和 Senko 的 36 芯接頭有沒有量產**：等 Marvell FY27Q3 財報（12 月初，還沒公告）。
- **Astera Labs 可拆回焊光纖連接器的客戶和量產進度**：兩場法說都只說一家大型（tier 1）AI 平台業者在認證或導入、2027 年量產；看 Astera Q3 法說（2026 年 11 月初，日期未公告）有沒有點名或給數量。
- **Coherent FlexConnect 的量產和客戶**：自己的時程是 2027 年第一季；等 Coherent FY27Q1 法說（11 月初，還沒公告）和 FY27Q2 法說（2027 年 2 月初）。
- **古河 Snap-Beam 的量產時程和客戶、320 通道接頭的論文全文**：新聞稿沒寫；從古河說明會資料和 ECOC 2026 論文集查。
- **Teramount 的總插入損耗**：只查到對位容差；從 Molex 的 OFC 2027（3/7–11）資料或 Teramount 論文查。
- **Ayar Labs 2026 年用哪一家的可拆接頭**：只查到 2024 年的報導（Intel Foundry、Teramount 兩種）；從 Ayar Labs 技術文件查。
- **可拆式 FAU 的單價、價值量**：中英文搜尋只找到付費報告目錄和券商文章開頭。
- **EBO 第一份接頭規格**：規格 1.0 還沒發布，看 ebomsa.org。
- **OIF 12.8T 近封裝光學模組專案的「光學接頭考量」**：等 OIF 下一次季會新聞稿（日期沒查）。
- **OCP 基礎規格的時程**：白皮書說數值寫在之後的基礎規格；看 OCP Global Summit（10/12–15）的工作流進度。
- **UPO 的可插拔 FAU（D-FAU）規格**：ODCC 官網下載區還沒有 UPO 文件；從 ODCC 秋季峰會報導、騰訊網絡平台公眾號查。
- **COBO、IEEE 的晶片對光纖可拆介面**：查不到，只有 COBO 2020 年成立 CPO 工作組的舊新聞。
- **台積電 COUPE 自己有沒有可拆接頭**：查不到台積電談可拆光纖接頭的資料；10/15 台積電法說看有沒有被問到。
- **Broadcom 的光纖接法是不是可拆**：Broadcom 只談雷射模組可現場更換，沒寫光纖接頭。
- **NVIDIA 有沒有把偏振追蹤做進產品**：查 NVIDIA 2026 年專利（偏振追蹤、偏振控制）和 ECTC 2027（6/1–4）、OFC 2027 的論文。
- **長飛說 NVIDIA、Marvell 用它的保偏光纖**：只有長飛總裁說；長飛三季報 10/31（不會寫客戶），要看年報的客戶集中度。
- **ELSFP 2026 年有沒有新專案**：OIF 在 OFC、ECOC 2026 的互通展示新聞稿這次沒抓到。
- **玻璃橋的客戶和量產時程**：等 Corning 第三季法說（10/27）看有沒有提。
- **Corning 玻璃配方那篇論文的原文**：目前只有社群解讀；從 IEEE Xplore 用作者名查。
- **FlexConnect 的商標登記**：沒查 USPTO 商標資料庫。
- **Senko、HTK 這些日本接頭廠營收裡 CPO 佔多少**：Senko 的財務查不到，從日本媒體查。
- **Mixx 的接頭和它在台灣的合作廠**：從它的新聞稿查。
- **imec＋ASMPT 擴束耦合的全文**：ASMPT 是封裝設備商，±12 微米的方案如果量產，會影響主動對位機台的需求；從 IEEE 全文查。
