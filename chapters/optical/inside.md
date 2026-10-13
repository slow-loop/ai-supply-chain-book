# 拆開來：一道光在 CPO 裡怎麼走

2026-10-12。把一台 CPO（共同封裝光學）交換器拆開，照光走的順序一塊一塊講：光引擎、PIC、透鏡和反射鏡、外部雷射、散熱，最後看台積電的光引擎平台 COUPE 接下來往哪裡長。為什麼需要光、CPO 和插拔式差在哪，見[CPO 怎麼解決](basics.md#q3)；光怎麼從晶片出去到光纖，見[FAU 是什麼](fau.md#q11)。自己算的數字標「計算」並寫算式。

## 一台 CPO 交換器拆開，有哪幾塊？ {#q5}

先看實物。下面這張是 NVIDIA 第一台 CPO 交換器 Quantum-X 拆開的樣子：左上從晶片開始，電的晶片和光的晶片疊成一顆光引擎；光引擎表面做了微透鏡，光從晶片表面進出；光引擎接上光纖接頭，三顆一組裝進金屬殼，叫光學次組件；右邊是插在機器上的外部雷射光源模組。

![一台 CPO 交換器拆開來。上排由左到右：電的晶片（Electronic IC）和光的晶片（Photonic IC）疊在一起（3D Stacked）；光引擎表面的微透鏡（COUPE uLens），光從表面進出；光纖接頭（Fiber Connector）；三顆光引擎裝成一個光學次組件（Optical Sub-Assembly）。右邊：外部雷射光源模組（External Laser Source Module）、模組裡的雷射封裝（Laser Source Package）。各框上方的公司標誌是製圖者標的分工，不是每一家都經過公司證實；中間灰框是原文加的標題，擋住一塊畫面。[[technews-sipho-20260317]]](img/media/TechNews-矽光子商轉元年-20260317-07.jpg)

再看機器裡面。NVIDIA 在發表會上秀過 Quantum-X 機殼內部：中間是一顆交換器晶片，周圍 6 個金屬殼就是光學次組件，白色、綠色、褐色的光纖在機殼的溝槽裡繞好，再拉到前面板。畫面上寫，這一顆晶片共有 324 條光連線，其中 36 條送雷射光進來、288 條傳資料[[semianalysis-cpo-book]]。

![CPO 交換器內部俯視。中間是交換器晶片，上下左右 6 個金屬殼是光學次組件，每個裝 3 顆光引擎；光纖沿機殼溝槽繞到前面板（Built-in Fiber Management）。圖上寫一顆晶片 324 條光連線：36 條雷射輸入（Laser Inputs）、288 條資料（Data Links）。右側圓形是轉載者的浮水印。[[semianalysis-cpo-book]]](img/semianalysis/img054.jpeg)

這三個數字對得起來。每個光學次組件有 3 顆光引擎，6 個就是 18 顆；每顆光引擎接 8 條發送、8 條接收、2 條雷射光纖[[nvidia-blog-20250826]]。18 × 16 ＝ 288 條資料光纖，18 × 2 ＝ 36 條雷射光纖，加起來 324 條（計算）。

乙太網路那一系列的 Spectrum-X 用同一套零件，只是數量不同。前面板接頭：Quantum-X800 Q3450-LD 是 144 個 MPO-12[[nvidia-qx800-datasheet-20260911]]；Spectrum-X 的 SN6810-LD（1 顆交換器晶片）是 128 個 MMC-16，SN6800-LD（4 顆）是 512 個 MMC-16；外部雷射模組分別是 16 個和 64 個[[nvidia-sn6000-manual-20260916,nvidia-blog-20250826]]。NVIDIA 2026 年 1 月的規格書把同兩台的接頭寫成 MMC-12，9 月的硬體手冊改成 MMC-16[[nvidia-sn6000-datasheet-20260119,nvidia-sn6000-manual-20260916]]；接頭的事見[前面板接頭](passive.md#pas-mmc)。

把一道光從頭到尾走一遍，就是下面這張圖：

<div class="scroll"><figure><svg viewBox="0 0 1000 380" width="100%" role="img" aria-label="CPO 交換器裡的光路示意">
<defs>
<marker id="p2a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="10" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1,1 L9,5 L1,9" class="solid"/></marker>
<marker id="p2c" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="10" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1,1 L9,5 L1,9" class="cu"/></marker>
</defs>
<text x="10" y="22" class="note">發送：電 → 光</text>
<rect x="10" y="50" width="130" height="70" rx="6" class="box"/><text x="75" y="80" text-anchor="middle" class="head">外部雷射</text><text x="75" y="104" text-anchor="middle" class="item">ELS 模組</text>
<rect x="185" y="50" width="95" height="70" rx="6" class="box"/><text x="232" y="80" text-anchor="middle" class="head">FAU</text><text x="232" y="104" text-anchor="middle" class="item">光纖→晶片</text>
<rect x="325" y="50" width="180" height="70" rx="6" class="box"/><rect x="325" y="50" width="180" height="70" rx="6" class="hl"/><text x="415" y="74" text-anchor="middle" class="head">光引擎</text><text x="415" y="95" text-anchor="middle" class="item">PIC 把資料印上光</text><text x="415" y="113" text-anchor="middle" class="item">EIC 推動調變器</text>
<rect x="550" y="50" width="95" height="70" rx="6" class="box"/><text x="597" y="80" text-anchor="middle" class="head">FAU</text><text x="597" y="104" text-anchor="middle" class="item">晶片→光纖</text>
<rect x="690" y="50" width="130" height="70" rx="6" class="box"/><text x="755" y="80" text-anchor="middle" class="head">機內整線</text><text x="755" y="104" text-anchor="middle" class="item">光纖重新排</text>
<rect x="865" y="50" width="120" height="70" rx="6" class="box"/><text x="925" y="80" text-anchor="middle" class="head">前面板</text><text x="925" y="104" text-anchor="middle" class="item">MPO／MMC</text>
<line x1="140" y1="85" x2="183" y2="85" class="light" marker-end="url(#p2a)"/><text x="162" y="40" text-anchor="middle" class="note">保偏光纖</text>
<line x1="280" y1="85" x2="323" y2="85" class="light" marker-end="url(#p2a)"/>
<line x1="505" y1="85" x2="548" y2="85" class="light" marker-end="url(#p2a)"/>
<line x1="645" y1="85" x2="688" y2="85" class="light" marker-end="url(#p2a)"/><text x="667" y="40" text-anchor="middle" class="note">光纖</text>
<line x1="820" y1="85" x2="863" y2="85" class="light" marker-end="url(#p2a)"/>
<rect x="325" y="170" width="180" height="56" rx="6" class="box"/><text x="415" y="194" text-anchor="middle" class="head">交換器晶片</text><text x="415" y="216" text-anchor="middle" class="item">送出、收回電訊號</text>
<line x1="380" y1="170" x2="380" y2="123" class="cu" marker-end="url(#p2c)"/>
<line x1="450" y1="277" x2="450" y2="229" class="cu" marker-end="url(#p2c)"/>
<text x="540" y="203" class="note">橘色＝電，藍色＝光</text>
<text x="10" y="262" class="note">接收：光 → 電（不用雷射）</text>
<rect x="325" y="280" width="180" height="76" rx="6" class="box"/><rect x="325" y="280" width="180" height="76" rx="6" class="hl"/><text x="415" y="304" text-anchor="middle" class="head">光引擎</text><text x="415" y="326" text-anchor="middle" class="item">PIC 偵測器：光→電</text><text x="415" y="345" text-anchor="middle" class="item">EIC 放大（TIA）</text>
<rect x="550" y="283" width="95" height="70" rx="6" class="box"/><text x="597" y="313" text-anchor="middle" class="head">FAU</text><text x="597" y="337" text-anchor="middle" class="item">光纖→晶片</text>
<rect x="690" y="283" width="130" height="70" rx="6" class="box"/><text x="755" y="313" text-anchor="middle" class="head">機內整線</text><text x="755" y="337" text-anchor="middle" class="item">光纖重新排</text>
<rect x="865" y="283" width="120" height="70" rx="6" class="box"/><text x="925" y="313" text-anchor="middle" class="head">前面板</text><text x="925" y="337" text-anchor="middle" class="item">光從外面來</text>
<line x1="865" y1="318" x2="822" y2="318" class="light" marker-end="url(#p2a)"/>
<line x1="690" y1="318" x2="647" y2="318" class="light" marker-end="url(#p2a)"/>
<line x1="550" y1="318" x2="507" y2="318" class="light" marker-end="url(#p2a)"/>
</svg><figcaption>一道光在 CPO 交換器裡走的路。上排是發送：雷射在機器外面的模組裡產生沒有資料的光，經保偏光纖、FAU 進到光引擎；光引擎把交換器晶片送來的資料印到光上，再經 FAU、機內整線、前面板送出去。下排是接收：光從前面板進來，經整線、FAU 進光引擎，偵測器把光變回電、放大後交給交換器晶片。示意圖，非實際比例。</figcaption></figure></div>

用文字再講一次：

1. **雷射**在機器外面產生一道穩定、沒有資料的光，經過**保偏光纖**（讓光的振動方向保持不變的光纖，見[光纖本身](fau.md#q16)）送進來。
2. 光經過 **FAU**（Fiber Array Unit，光纖陣列單元，把一排光纖對準晶片的零件），從光纖進到**光引擎**。
3. 光引擎裡的 **PIC**（光的晶片）在 **EIC**（電的晶片）的驅動下，把交換器晶片送來的資料「印」到這道光上。
4. 帶著資料的光再經過 FAU 回到光纖，經過機器內的**光纖整線**和**接頭**，從前面板送出去。
5. 收資料的時候反過來：光從前面板進來，經 FAU 進 PIC，PIC 把光變回電，交給 EIC 放大，再交給交換器晶片。

NVIDIA 的專利畫出了另一個角度：一整顆 CPO 封裝，中間方形是晶片區，四周一排排可以拆下來的光纖接頭，每個接頭扣在一顆光引擎上[[us20260276925a1]]。

![一整顆 CPO 封裝：中間方形是晶片區（6300），旁邊每個小方塊（600）是一個光纖接頭，8 個一組（800），扣在光引擎上，後面拉出光纖排線。圖上畫了兩組；一顆封裝可以有四組、32 個。[[us20260276925a1]]](img/patents/US20260276925A1-FIG1A.png){.s}

Broadcom 的 CPO 交換器拆開，零件的種類一樣，排法不同。它的 Bailly（51.2 Tb/s）是 8 顆光引擎圍在交換器晶片四周，每顆拉出一束黃色光纖；光纖接到光引擎的地方是 Broadcom 自己命名的接頭 BFC（Broadcom Fiber Connector），可以拆、被動對準，光從晶片側邊進出（邊緣耦合，見[PIC 怎麼電光互換](#q7)）；雷射也做成插在前面板、可以更換的模組[[broadcom-ecoc2025-202509]]。NVIDIA 用的是光從晶片表面進出的光柵耦合，兩家在光引擎和光纖的接法上走不同的路。Broadcom 說 Bailly 從 2025 年第一季到第四季出貨量成長 7 倍，沒有給絕對數字[[broadcom-ecoc2025-202509]]。

![Broadcom 的 CPO 交換器 Bailly（廠商投影片）。左上：機殼打開，中間是交換器封裝，黃色光纖拉到前面板。右上：交換器晶片（中間深色方塊）四周一圈光引擎，每邊兩顆、共 8 顆，各自接出黃色光纖。下：機器正面插滿光纖。右邊柱狀圖：2024 年第三季到 2025 年第四季的 CPO 出貨量，2025 年內成長 7 倍，沒有刻度。[[broadcom-ecoc2025-202509]]](img/media/broadcom-ecoc2025-bailly-cpo-ramp-202509.png)

所以一台 CPO 交換器的主要零件是：交換器晶片、光引擎（EIC＋PIC）、外部雷射光源、FAU、光纖和接頭、機內整線、封裝基板、散熱，加上把這些組起來的封裝測試和整機組裝。接下來照這條路一塊一塊講。

這裡順便更正一個常見的說法：光引擎的兩片晶片是 **EIC** 和 **PIC**（不是 AIC）；兩片疊在一起，收發都做，不是一片管輸入、一片管輸出。另外雷射不是接在 FAU 後面，而是雷射的光先經光纖、FAU 送**進** PIC，資料光再經 FAU 送**出**去。

完整的零件清單（名字是素材裡出現過的；寫「查不到」的是查過、沒有公開資料）：

| 零件 | 做什麼 | 誰 |
|---|---|---|
| 交換器晶片 | 處理資料，輸出電訊號 | NVIDIA、Broadcom 設計；台積電製造 |
| EIC | 驅動、放大、控溫 | 晶片公司設計；台積電，製程有 N7、N6、5 奈米幾種說法（見[光引擎](#q6)） |
| PIC | 電轉光、光轉電 | 晶片公司設計；台積電 SOI N65（COUPE）；Tower、格芯、聯電、意法也做 PIC |
| SOI 晶圓 | 做 PIC 的起點（見[PIC 怎麼做](#q8)） | Soitec、環球晶在量產或小量生產；上海合晶在成立 SOI 合資公司；台積電向誰買，查不到[[soitec-fy27q1-20260722,technews-globalwafers-20260804,10jqka-hejing-soi-20260614]] |
| 矽透鏡、反射鏡 | 光進出晶片時聚焦、反射 | 台積電（晶圓階段） |
| 封裝基板（載板） | 承載交換器晶片和光引擎 | 欣興、AT&S 有談 CPO（見[載板](passive.md#pas-substrate)） |
| 封裝測試 | 把電和光的元件組在一起 | 矽品（見[封測廠](equipment-test.md#eq-osat)） |
| InP 基板、磊晶 | 雷射的原料（InP 是磷化銦） | 基板：JX 金屬、住友電工、AXT[[jx-inp-20260616,technews-sumitomo-inp-20260703,sec-axt-8k-20260730]]；磊晶：聯亞、全新、IET-KY（見[InP 基板和銦](lasers.md#las-inp)） |
| 雷射晶片 | 產生光 | Lumentum、Coherent、住友電工、三菱電機、古河電工、聯亞、源杰…（見[各國廠商](lasers.md#q21)） |
| 外部光源模組 | 可插拔的雷射模組 | 天孚、聯鈞、華星光、立碁…；Lumentum 有自己的 ELSFP 雷射[[lumentum-elsfp-wp-202606]]；Broadcom 用自己的模組[[broadcom-ecoc2025-202509]] |
| 保偏光纖 | 雷射送光 | 長飛、Fujikura（見[保偏光纖會不會被拿掉](detachable.md#det-pm)） |
| FAU 和零件 | 光纖對準 PIC | 見[誰在做 FAU](fau-makers.md#q22) |
| V 型槽用的玻璃 | FAU 基板的材料 | 炬光說它的 V 槽可用 Borofloat 33、熔融石英、S-TIH53、S-BSL7 等玻璃和矽；向誰買沒說[[focuslight-infostone-20260116]] |
| 光纖 | 傳光 | Corning、藤倉、住友、古河、長飛…（見[光纖、預製棒](passive.md#pas-fiber)） |
| 光纖預製棒 | 拉成光纖的玻璃棒 | 一般資料中心光纖的預製棒吃緊、價格上漲；CPO 專用光纖的說法查不到[[cru-preform-20260226]] |
| 機內光纖整線（shuffle） | 把光引擎的光纖重新分配到前面板接頭 | 波若威（媒體報導）、Corning（預組光纖托盤）、Coherent（被動光纖套件）；NVIDIA 用哪一家，查不到（見[光纖怎麼接到前面板](passive.md#q16b)、[機內整線](passive.md#pas-shuffle)） |
| 前面板接頭 | 對外接光纖；Quantum-X800 用 MPO，Spectrum-X 用 MMC-16（NVIDIA 1 月的規格寫 MMC-12） | MMC 由 US Conec 設計，Corning、Fujikura、Sumitomo 取得授權生產，白山、Sanwa 擴大供應；NVIDIA 機器上的接頭是哪家做的，查不到[[usconec-prizm-20260311,sanwa-usconec-20260217]]（見[MPO、MMC 和授權](passive.md#pas-mmc)） |
| 散熱 | 液冷冷板、管路 | CPO 的兩台 Spectrum-X 沒有風扇、只有液冷；冷卻液是 Recochem；冷板、分歧管的供應商查不到；健策供交換器晶片端的機構件和補強板，只有媒體報導（見[散熱](#q10b)） |
| 整機組裝 | 組成交換器 | 鴻海、Fabrinet（NVIDIA）；Micas、Celestica（Broadcom） |
| 設備 | 對位、點膠、檢測、雷射加工 | 高明鐵、萬潤、東佑達、均英、ficonTEC、致茂、穎崴、大族激光…（見[對位設備](equipment-test.md#eq-align)、[測試](equipment-test.md#eq-test)） |

## 光引擎是什麼？EIC、PIC 各做什麼？ {#q6}

光引擎是負責「電和光互相轉換」的那顆東西，由兩片晶片疊在一起。先看 NVIDIA 公布的實物剖面：最上面是一層矽，下面依序是 EIC 和 PIC。NVIDIA 在照片上標註，一顆光引擎有 2.2 億個電晶體、1,000 個光子元件[[semianalysis-cpo-book]]。

![NVIDIA 光引擎的實物剖面：最上面是 COUPE 的矽層，下面依序是 EIC（電的晶片）和 PIC（光的晶片）。左上的字：2.2 億個電晶體、用台積電 N6 製程，1,000 個光子元件。[[semianalysis-cpo-book]]](img/semianalysis/img060.jpeg)

- **EIC**（Electronic IC，電的晶片）：驅動器負責推動調變器；放大器（TIA，把偵測器送來的微弱電流放大）；另外還有控制溫度的加熱電路[[semianalysis-cpo-book]]。它是一般的邏輯晶片，用哪一代製程有好幾種說法，見下面的表。
- **PIC**（Photonic IC，光的晶片）：裡面是光的電路，負責把資料放上光（調變器）、把光變回電（偵測器），以及讓光在晶片裡走的通道（波導）。台積電用 SOI N65 製程做[[semianalysis-cpo-book]]。

台積電自己的簡報把兩片晶片的分工列得很清楚：EIC 管高速驅動電路、放大器和加熱控制；PIC 管光的電路；另外兩個框是光的進出口（透鏡、光柵、反射鏡）和 3D 堆疊[[technews-sipho-20260317]]。

![台積電的光引擎（COUPE）。左上灰框是電的晶片（Electrical Die，N7）：推動光調變器的驅動電路、把光二極體電流放大的 TIA、加熱控制。左下是光的晶片（Photonic Die，SOI N65）：光的電路設計和模擬。中間剖面：EIC 面朝下、PIC 面朝上，用 SoIC 直接接在一起；最上面一層矽上做了微透鏡（uLens），光經透鏡、光柵耦合器（Grating Coupler）進出，底下有金屬反射鏡（Metal Reflector）。[[technews-sipho-20260317]]](img/media/TechNews-矽光子商轉元年-20260317-05.jpg)

| | EIC | PIC |
|---|---|---|
| 全名 | Electronic IC，電的晶片 | Photonic IC，光的晶片 |
| 裡面有什麼 | 驅動器、放大器（TIA）、加熱控制電路 | 調變器、偵測器、波導、耦合器、多工器 |
| 台積電製程 | N7、N6、5 奈米三種說法（見下表），一般邏輯製程 | SOI N65 |
| 用的晶圓 | 一般矽晶圓 | SOI 晶圓（見[PIC 怎麼做](#q8)） |
| 在光引擎裡的位置 | 面朝下，疊在上面 | 面朝上，在下面 |

表的出處：[[technews-sipho-20260317,semianalysis-cpo-book]]

**EIC 用哪一代製程，說法並排。**原本只看到 N7 和 N6 兩種，這一輪又多了兩種。幾份資料講的可能不是同一代產品，原文都沒寫清楚，這裡不挑：

| 寫了什麼 | 誰寫的 |
|---|---|
| N7 | 台積電 COUPE 簡報上的電的晶片[[technews-sipho-20260317]] |
| N6 | NVIDIA 公布的光引擎剖面照上的標註[[semianalysis-cpo-book]] |
| 5 奈米 | NVIDIA 在 OFC 2026 的演講，經一篇整理文章轉述：COUPE 把 5 奈米 EIC 和 PIC 接在一起[[stt-ofc2026-cpo-panel-2026]] |
| 7 奈米 | NVIDIA 在 ISSCC 2026 發表的光鏈路；Broadcom 的 EIC 也是 7 奈米[[semianalysis-isscc2026]] |
| 65 奈米 | 一篇媒體文章寫第一階段 COUPE 是「65 奈米 EIC」接 PIC；其他資料寫的 65 奈米都是 PIC 的製程[[tomshardware-cpo-foundry-20260803]] |

**兩片怎麼接在一起。**不是並排，而是 EIC 直接疊在 PIC 上。台積電用自家的 SoIC 技術把兩片面對面接合，中間沒有凸塊，線路最短。同樣功耗下，SoIC 做的光引擎頻寬密度是用凸塊接合的 23 倍以上[[semianalysis-cpo-book]]。EIC 和 PIC 接在一起的方式從簡單到緊密有好幾種，下圖由上往下排：

![EIC 和 PIC 接在一起的幾種方式，越往下越緊密：並排打線（2D）、放在同一片中介層上（2.5D）、疊起來用小凸塊接（3D）、加上穿過矽的垂直導線（TSV），到「混合鍵合」（Hybrid bonding，兩片晶片的銅墊直接面對面接合，中間沒有凸塊，台積電 SoIC 屬於這一類）。最下面右邊是把電和光做在同一片晶片上。[[technews-sipho-20260317]]](img/media/TechNews-矽光子商轉元年-20260317-02.jpg)

這一步也是目前良率的難處。一家券商的估計：SoIC 接合的良率約 50–60%，後段組裝良率只有 20–50%；它的模型裡 2027 年光引擎出貨 600–700 萬顆，市場一般預期是 2,000–3,000 萬顆[[udn-ms-cpo-yield-20260611]]。這只有券商一家的估計，出貨量的各種說法見[量產到哪一步](timing.md#q27)。

**收和發在同一片。**Broadcom 公布的 EIC 晶片照上，32 路接收和 32 路發送各兩組，都在同一片晶片上；這片 7 奈米 EIC 疊在 PIC 上組成 6.4 Tb/s 的光引擎，8 顆光引擎配一顆交換器晶片[[semianalysis-isscc2026]]。

![Broadcom 光引擎裡電的晶片（7 奈米）。左上紅框：32 路接收（RX）和 32 路發送（TX）各兩組，收和發在同一片上。左下：交換器晶片四周 8 顆光引擎的封裝。[[semianalysis-isscc2026]]](img/media/SemiAnalysis-ISSCC2026-CPO-20260415-03.jpeg)

**誰設計、誰製造。**EIC 和 PIC 都是晶片公司自己設計，台積電代工。NVIDIA 自己設計光引擎，用微環調變器，自稱是第一家把微環放進 CPO 系統的公司；Broadcom 也自己設計，第一代 EIC 用矽鍺製程，Bailly 改用 CMOS[[semianalysis-cpo-book]]。台積電提供設計工具（PDK、EDA）和光路模擬，客戶在 COUPE 平台上自己設計[[semianalysis-cpo-book]]。PDK（製程設計套件）裡的現成元件有波導、彎道、耦合器、調變器、光偵測器[[technews-tsmc-coupe-20260831]]。

## PIC 怎麼把電變成光、再把光變回電？ {#q7}

先看一顆真的 PIC 在顯微鏡下長什麼樣。一顆研究用的矽光子晶片：整顆約幾毫米長，上面看得到偵測器、微環調變器、另一種調變器，和像風車一樣的光柵[[arxiv-2608-11639]]。

![一顆矽光子晶片在顯微鏡下。上面一整條是整顆晶片（比例尺 500 微米）。下面放大：PD 是光偵測器，把光變回電；MRM 是微環調變器，兩個小圓環；MZI 是另一種用光的干涉來切換的調變器；最右邊像風車的是光柵，光從這裡進出晶片。[[arxiv-2608-11639]]](img/arxiv-2608.11639-terabit-sipho-engine-fig2a-pic-micrographs.png)

PIC 裡有兩條路。發送：資料在調變器上被寫進光裡，光沿波導走，幾種顏色的光在多工器合成一路，從耦合器出晶片進光纖。接收：光從耦合器進來，多工器把顏色分開，偵測器把光變回電[[wallstreetcn-wins-forum]]。

![PIC（光的晶片）裡的兩條路。上排發送：資料（ASIC Data）在調變器（Modulator）寫進光裡，光沿波導（Routing）走，在 WDM（分波多工，讓一根光纖同時跑好幾個顏色）合在一起，從耦合器（Coupler）出晶片。下排接收倒過來：耦合器進光、WDM 分開各個顏色，偵測器（Photodetector）把光變回電。注意：圖上把光源（Source）畫在晶片流程裡；CPO 的雷射實際放在機器外面，經光纖送進來（見下面「光從哪裡來」）。[[wallstreetcn-wins-forum]]](img/華爾街見聞-穎崴CPO論壇-2026日期不明-03-pic-blueprint.png)

**光怎麼在矽裡走。**矽對波長超過約 1.1 微米的紅外光是透明的，資料中心用的光就在這個範圍。矽的折射率約 3.5，外面包一層折射率約 1.44 的二氧化矽，光從高折射率碰到低折射率的交界會全反射，於是被關在矽條裡，順著它走。這條矽條就是**波導**，截面只有幾百奈米[[wikipedia-silicon-photonics]]。可以把它想成縮小幾十倍的光纖。

![矽波導的切面：一條寬 450 奈米、高 220 奈米的矽條（深灰，折射率 3.45），躺在二氧化矽（折射率 1.44）上。矽的折射率比周圍高，光就被關在矽條裡。[[commons-soi-waveguide]]](img/explain/commons-soi-waveguide-cross-section-450x220nm.png){.s}

**怎麼把資料放上光。**雷射送進來的是一道穩定的光，資料要靠**調變器**放上去。原理是：矽裡帶電的粒子（自由電子和電洞）多一點或少一點，矽的折射率就跟著變；在波導旁邊做一個 PN 接面（跟二極體一樣的結構），加電壓就能控制這些粒子[[wikipedia-silicon-photonics]]。NVIDIA 和台積電用的是**微環調變器**（MRM，micro-ring modulator）：在直的波導旁邊放一個直徑 5 到 15 微米的小圓環，圓環只會「吃掉」特定波長的光。用電壓微調圓環的折射率，它吃的波長就偏掉一點，經過的光就一下亮、一下暗，亮暗就是 0 和 1[[semianalysis-cpo-book]]。

![微環的原理：光的波長剛好對上圓環時，會被圓環「吸」過去，原本那條路上的光就變暗。[[commons-ring-resonator]]](img/explain/commons-ring-resonator-at-resonance.png){.xs} ![同一件事畫成曲線：直的波導旁放一個圓環，符合共振波長的光被吸進環裡，右圖藍線（直通那一路）在 1552、1564 奈米掉到底，紅線（被吸走那一路）在同一位置衝高。兩次共振之間的波長間距叫 FSR。[[semianalysis-cpo-book]]](img/semianalysis/img051.jpeg)

加電壓之後，那個「吃掉」的波長會移動。下面是實測：電壓從 0 伏調到 −4 伏，凹谷每伏特往右移約 30 皮米（pm，十億分之一毫米）。雷射的波長固定在凹谷邊上，電壓一變，通過的光就忽亮忽暗[[arxiv-2608-11639]]。

![微環調變器怎麼把資料放上光：每條線是加上不同電壓時，各個波長通過了多少光，凹得最深的地方就是微環「吃掉」的波長。電壓從 0 V 到 −4 V，凹谷往右移（30 pm/V）。[[arxiv-2608-11639]]](img/arxiv-2608.11639-terabit-sipho-engine-fig2e-ring-shift-with-voltage.png){.s}

微環的好處是很小、很省電，而且每個圓環可以處理不同顏色的光，一條波導上排好幾個，**一根光纖就能同時跑好幾路資料**，叫 WDM（分波多工）。NVIDIA 在 ISSCC 2026 發表的光鏈路就是這樣：每一路分到一個專屬波長，8 路資料加 1 路時脈，一根光纖 256 Gb/s，用的是 3D 堆疊的 7 奈米 EIC 和 65 奈米 PIC[[semianalysis-isscc2026]]。

![一根光纖跑 9 種顏色。左邊 9 條通道（lane），每條經過一個不同顏色的微環，各自把資料放到一個專屬的波長上，全部走同一條波導、同一根光纖；到了右邊，再由 9 個同色的微環把各自的波長挑出來。8 條是資料、1 條是時脈。DWDM 是波長排得更密的 WDM。[[semianalysis-isscc2026]]](img/media/SemiAnalysis-ISSCC2026-CPO-20260415-01.jpeg)

![WDM 最直觀的樣子：四顆雷射各發一種波長，1270、1290、1310、1330 奈米，四根尖峰各帶各的資料，合進同一根光纖。[[arxiv-2602-08284]]](img/arxiv-2602.08284-sion-interposer-cpo-io-fig4a-four-wavelengths.png){.s}

**微環最怕熱。**微環對溫度的敏感度比其他調變器高 10 到 100 倍，所以 EIC 裡要有加熱器把溫度控住[[semianalysis-cpo-book]]。具體的數字：溫度每升 1°C，微環吃掉的波長約移 70–90 pm；只要變 2°C 就移 0.14 nm，超過 0.1 nm 這個讓微環失效的範圍[[semianalysis-cpo-book]]。一篇 CPO 散熱論文引用的數字是每 1°C 約 0.1 nm[[pmc-cpo-liquid-cooling-20250514]]。拿上面量到的電壓效果來比：電壓每伏只移 30 pm，所以溫度變 1°C 造成的偏移，相當於 2.3 到 3 伏電壓的效果（計算：70 ÷ 30 ≈ 2.3，90 ÷ 30 ＝ 3）；整段 0 到 −4 伏能移的 120 pm，溫度變 1.3 到 1.7°C 就抵掉了（計算：120 ÷ 90 ≈ 1.3，120 ÷ 70 ≈ 1.7）。兩組數字來自不同的元件，只是比大小。這就是為什麼 CPO 交換器對散熱的要求不只是「夠冷」，還要「各處一樣冷」，見[散熱](#q10b)。

**怎麼把光變回電。**矽對這種光是透明的，所以吸收不了，也就產生不了電流。解法是在矽上長一小塊**鍺**，鍺吸收得到這種光，照到就產生電流，再交給 EIC 放大[[wikipedia-silicon-photonics]]。

![光變回電的地方：藍色是矽波導，上面那塊紫色是鍺。光走進鍺會被吸收、產生電流，兩旁的 P+、N+ 區和上面的金屬條把電流引出去。[[mdpi-nano10-01683]]](img/papers/mdpi-nano10-01683-ge-waveguide-photodetector-fig1b.png){.s}

**光從哪裡進出晶片。**PIC 上有「耦合器」，是光進出晶片的入口。有兩種：**光柵耦合**是在晶片表面刻一排細條紋，光纖斜斜地從上面打下來，條紋把光彎進波導；**邊緣耦合**是光從晶片側邊的切面進出。光柵耦合可以排好幾排光纖、對位要求較寬、能在晶圓上就測試，但損耗較高、對偏振敏感；邊緣耦合損耗低，但要對得極準、只能排一排。NVIDIA 和台積電都偏好光柵耦合[[semianalysis-cpo-book]]。台積電的論文另外指出，從上方垂直進光的做法對晶片翹曲的容忍度大，邊緣耦合則不行[[tsmc-ectc2025-boe]]。

![光柵耦合：光纖從上面斜斜打下來（角度 θ），晶片表面那排細條紋把光彎進旁邊漸窄的波導。[[mdpi-mi11-00666]]](img/papers/mdpi-mi11-00666-grating-coupler-schematic-fig1.png) ![邊緣耦合：光纖（Fiber Core）從晶片側邊直直對進去，晶片上那條漸細的矽條（Si Taper）負責把光收進來。[[mdpi-app10-01538]]](img/papers/mdpi-app10-01538-edge-coupler-schematic-fig1.png)

| | 光柵耦合 | 邊緣耦合 |
|---|---|---|
| 光從哪裡進出 | 晶片表面 | 晶片側邊的切面 |
| 光纖可以排幾排 | 好幾排（二維） | 沿晶片邊緣一排 |
| 對位要求 | 較寬 | 極準 |
| 損耗 | 較高 | 較低 |
| 晶圓上能不能先測 | 能 | 難；台積電說已能對邊緣耦合元件做晶圓級光學測試（見[PIC 怎麼做](#q8)） |
| 晶片翹曲 | 容忍度大 | 容忍度小 |
| 誰在用 | NVIDIA、台積電偏好 | 台積電也有這個版本；Broadcom 的 BFC 接頭用這一種 |

表的出處：[[semianalysis-cpo-book,tsmc-ectc2025-boe,broadcom-ecoc2025-202509,trendforce-tsmc-sipho-20260831]]

台積電同一個平台兩種都做：左邊光柵耦合版，光從上方穿過矽載板進出，光柵下面墊一片金屬反射鏡；右邊邊緣耦合版，光從 PIC 側邊進出，那裡的波導用氮化矽[[semianalysis-cpo-book]]。2026 年 8 月台積電在 SEMICON Taiwan 列出兩版的關鍵結構：光柵版有矽透鏡、金屬反射鏡、矽或氮化矽的光柵耦合器；邊緣版有側邊切面、氮化矽尖端[[technews-tsmc-coupe-20260831]]。

![台積電光引擎的兩個版本。左（COUPE-GC）是光柵耦合版：光從上方穿過矽載板（Si Carrier）進出，PIC 裡光柵下面墊一片金屬反射鏡（MR）。右（COUPE-EC）是邊緣耦合版：光從 PIC 側面的切面（EC Facet）進出，那裡的波導用氮化矽（SiN WG）。中間是實際切開的剖面照片。[[semianalysis-cpo-book]]](img/semianalysis/img042.jpeg)

![把以上元件放在同一張剖面裡：底下黃色是矽，BOX 是埋在中間的二氧化矽層；左邊 Modulator 是調變器，上面是加熱器；中間的小鋸齒是光柵耦合器，光纖從上面接下來；中間那塊灰色玻璃夾著一整排光纖，就是 FAU；右邊 Detector 是偵測器；最上面 DRV（驅動器）和 TIA（放大器）屬於 EIC。[[semianalysis-cpo-book]]](img/semianalysis/img082.png)

## PIC 是怎麼做出來的？SOI 是什麼？ {#q8}

PIC 跟一般晶片一樣在晶圓廠做，一片晶圓切出很多顆。下面左邊是一片 12 吋矽光子晶圓，右邊是意法半導體的矽光子晶圓特寫。

![一片 12 吋（300 毫米）矽光子晶圓，表面布滿一顆顆晶片，反光成彩虹色。[[commons-sipho-300mm-wafer]]](img/explain/commons-silicon-photonics-300mm-wafer.jpg) ![意法半導體 PIC100 矽光子晶圓的邊緣特寫，每一小格是一顆光的晶片。原圖很小。廠商產品照。[[st-pic100-20260309]]](img/vendor/st-pic100-wafer-20260309-01.jpg)

PIC 用的是一般晶圓廠的機台，跟做邏輯晶片同一套工具：曝光、蝕刻、離子佈植、長膜。差別在起點的晶圓和做出來的元件。台積電沒有公開製程細節，只知道用 SOI N65[[semianalysis-cpo-book]]。起點的 **SOI 晶圓**（Silicon-on-Insulator，絕緣層上覆矽）像三明治：

<div class="scroll"><figure><svg viewBox="0 0 760 300" width="100%" role="img" aria-label="SOI 晶圓剖面示意">
<rect x="20" y="30" width="400" height="55" class="box"/>
<rect x="60" y="68" width="40" height="17" class="bar"/><rect x="150" y="68" width="40" height="17" class="bar"/><rect x="240" y="68" width="16" height="17" class="bar"/><rect x="266" y="68" width="16" height="17" class="bar"/><rect x="292" y="68" width="16" height="17" class="bar"/><rect x="340" y="68" width="50" height="17" class="bar"/>
<rect x="20" y="85" width="400" height="80" class="box"/>
<rect x="20" y="165" width="400" height="105" class="bar2"/>
<line x1="425" y1="52" x2="455" y2="52" class="grid"/><text x="462" y="57" class="item">二氧化矽包覆層</text>
<line x1="425" y1="76" x2="455" y2="76" class="grid"/><text x="462" y="81" class="item">頂層矽 220 奈米：刻成波導、微環、光柵</text>
<line x1="425" y1="125" x2="455" y2="125" class="grid"/><text x="462" y="120" class="item">埋入氧化層（BOX）3 微米</text><text x="462" y="140" class="note">折射率低，把光關在上面那層矽裡</text>
<line x1="425" y1="218" x2="455" y2="218" class="grid"/><text x="462" y="223" class="item">矽基板：撐住整片</text>
<text x="20" y="292" class="note">藍色小方塊＝頂層矽刻出來的波導、光柵</text>
</svg><figcaption>SOI 晶圓的三明治：最上層 220 奈米的薄矽是走光的材料，中間 3 微米的二氧化矽把光關住，底下是厚的矽基板。做 PIC 就是在最上面那層薄矽上刻出光路，再蓋一層二氧化矽。厚度數字取自一家矽光子代工廠的公開製程。示意圖，非實際比例。[[cmc-amf-process]]</figcaption></figure></div>

![專利裡畫的起點：101 是底下的矽基板，103 是中間的絕緣層（二氧化矽），105 是最上層的材料（可以是矽）。[[us20260133387a1]]](img/patents/US20260133387A1-FIG1.png){.s}

以下用新加坡矽光子代工廠 AMF（2025 年被格芯買下）公開的製程說明，看一片 PIC 怎麼一步步做出來[[cmc-amf-process,gf-pr-amf-20251118]]：

1. **晶圓**：SOI 晶圓，最上層 220 奈米的薄矽、中間 3 微米的二氧化矽、底下是厚矽。
2. **曝光**：用 193 奈米深紫外光，最細畫到約 140 奈米，把所有光路畫上去。
3. **蝕刻**：同一層矽刻三種深度，淺的做光柵耦合器，部分刻的做波導，刻穿的做波導和微環。
4. **離子佈植**：在調變器的位置打入六種濃度的雜質，做出 PN 接面。
5. **長鍺**：在偵測器的位置長出鍺。
6. **金屬線**：兩層金屬，接到調變器、偵測器和加熱器。

![第 3 步做出來的光柵：頂層矽（Si）被刻成一格一格，上下各一層二氧化矽（SiO₂），最底下是矽基板。光纖從正上方把光打下來。[[arxiv-2604-23394]]](img/arxiv-2604.23394-vertical-grating-coupler-fig1a-soi-layers.png){.s}

台積電做 COUPE 時，PIC 做好之後還多做幾件事：把 EIC 用 SoIC 疊上去；在 PIC 上方接一片 770 微米厚的矽，上面做矽透鏡；在光柵耦合器正下方放一片金屬反射鏡[[semianalysis-cpo-book,tsmc-ectc2025-coupe]]。

**做完之後掉了多少光。**台積電論文公布的量測：光柵耦合的插入損耗（光經過一個接點少掉多少，單位 dB，3 dB 約等於少一半）在 COUPE 上穩定小於 1.2 dB，和還在 PIC 晶圓上時量到的一樣，也就是疊成 COUPE 之後幾乎沒有多掉光；1 dB 頻寬約 25 奈米，比 PIC 晶圓上寬約 5 奈米；整片 12 吋晶圓上的中心波長控制在 ±1.7 奈米以內；光束角度誤差在 ±0.1° 以內，12 片晶圓的接合電阻一致[[tsmc-ectc2025-coupe]]。

**能在晶圓上就先測。**疊好的光引擎還在晶圓上時就能同時測電和光，在昂貴的組裝之前把壞的挑掉。NVIDIA 在 OFC 2026 講過 COUPE 能做晶圓級的光電測試（經整理文章轉述）[[stt-ofc2026-cpo-panel-2026]]；一家研究機構轉述媒體，說台積電連邊緣耦合元件也已能做晶圓級光學測試[[trendforce-tsmc-sipho-20260831]]。測試分幾段、各段誰的機台，見[測試分幾段](equipment-test.md#eq-test)。

**做多少。**台積電沒有公布 PIC 產能，只有法人和券商的估計，兩份對不上：

| 估計 | PIC 晶圓月產能 | 誰估的 |
|---|---|---|
| 法人（媒體轉述） | 約 500 片 → 2026 年第二季 1 萬片 → 第四季 1.5 萬片 → 2028 年至少 2.5 萬片；每片 648 顆，1 萬片／月約年產 7,800 萬顆 PIC | [[trendforce-pic-capacity-20260708]] |
| 一家券商 | 2027 年第一季才擴到每月 1 萬片 | [[udn-ms-cpo-yield-20260611]] |

648 顆 × 1 萬片 × 12 個月 ＝ 7,776 萬顆（計算，和法人的 7,800 萬一致）。這是 PIC 的顆數，不是光引擎的顆數，中間還隔著上面講的 SoIC 和組裝良率。產線在台積電哪個廠區，查不到。

**SOI 晶圓誰在供應。**SOI 晶圓市場長期由法國的 Soitec 領先[[gvm-globalwafers-20260831]]。查到三家在談光子用的 SOI：

| 公司 | 查到的事實 |
|---|---|
| Soitec（法國） | 光子用 SOI（Photonics-SOI）在 FY26（到 2026 年 3 月）營收超過 1 億美元，全公司 FY26 營收 5.92 億歐元[[soitec-fy26-20260527]]。FY27 第一季光子 SOI 營收年增一倍；新加坡 12 吋廠已通過首批客戶的量產認證；和多家客戶簽了多年期產能保留協議，客戶付了現金訂金；公司預估 FY27 光子 SOI 營收是 FY26 的兩倍以上；說可用在插拔式、NPO、CPO 三種形式[[soitec-fy27q1-20260722]]。 |
| 環球晶（台灣） | 美國密蘇里州聖彼得斯廠的 RF-SOI 和矽光子產品已進入小量生產，客戶送樣驗證持續進行[[technews-globalwafers-20260804]]。矽光子方面以 12 吋 SOI 做光波導為主，矽晶圓和 SOI 都是自己做[[gvm-globalwafers-20260902,gvm-globalwafers-20260831]]。公司說明年營收成長主要來自先進 12 吋晶圓和用於矽光子的 12 吋 SOI[[taipeitimes-globalwafers-20260806]]。 |
| 上海合晶（中國） | 要成立 SOI 合資公司，列的應用包含 AI 算力光互連、矽光子晶片；只有媒體報導[[10jqka-hejing-soi-20260614]]。 |
| 信越、SUMCO（日本） | 查不到 2025–2026 年談矽光子、CPO 用 SOI 的公司說法。 |

台積電 COUPE 的 SOI 晶圓向誰買：查不到。台積電、Soitec、環球晶都沒有點名客戶。

Soitec 執行長在 2026 年 7 月的法說（法說會轉錄稿）對 CPO 的口風：scale-out 的 CPO「ramp up end of the year」（年底起量）；scale-up「that's mostly plugable」（多半還是插拔式），CPO 何時真正進 scale-up「there is a question mark」（是個問號），原因在 CPO 的挑戰「more on the assembly side and as well on the testing」，也就是組裝和測試要達到好良率[[investing-soitec-fy27q1-20260723]]。另一段回答說，FY27 的營收多半來自插拔式，「partly NPO」，CPO 在 scale-out 的交換器機櫃上年底起量；公司說光子 SOI 客戶超過 10 家[[investing-soitec-fy27q1-20260723]]。

**別的代工廠在做什麼。** 表上列的 Tower、格芯也在談自己的矽光子平台，下面是它們法說上的說法（都是轉錄稿）：

- Tower（2025 年 11 月，AI 轉寫稿）：矽光子「continues to increase market share over EML solutions given its significant cost advantage」（相對 EML 持續增加市占，因為成本優勢大），同樣功能的方案「SiPho typically requires half the number of lasers」；問答裡又說矽光有矽調變器，比 III-V 的調變器便宜，也沒有 III-V 調變器的產能限制（轉錄稿把 III-V 轉成「3.5」）[[allmind-tower-q3-20251110]]。雷射顆數少一半的算法見[用幾顆雷射](lasers.md#las-count)。
- 格芯（2026 年 5 月）：推出給 NPO 和 CPO 用的完整光模組方案 SCALE（矽光子共同封裝先進光引擎；轉錄稿寫成小寫的 scale），公司稱這是「the industry's first OCI MSA capable platform」，規格超過 OCI MSA 的要求；第一季有兩個 CPO 設計案的新設計下線（tape-out），支援 OCI 標準（轉錄稿的地名有誤，不引用）[[fool-globalfoundries-q1-20260505]]。同一場還提到和 Corning、EXFO 一起展示整套 CPO 生態：可拆光纖接頭加晶粒級自動測試，接上高量矽光子製造[[fool-globalfoundries-q1-20260505]]。誰在代工、誰主導，見 [players.md](players.md#q18)。

## 光引擎上的透鏡、反射鏡在做什麼？ {#q9}

光纖的纖芯有 9 微米左右，晶片上的波導不到 1 微米，兩邊的「光斑」大小差很多，直接接，光會漏掉大半。所以要用透鏡把光聚焦，讓光纖的光能進到晶片、晶片的光能進到光纖。

![兩邊光斑一樣大時（橫軸等於 1），光幾乎全部接得過去；光斑大小差越多，接過去的光越少，差 10 倍時幾乎接不到。[[lsa-review-202601]]](img/lsa-s41377-025-02048-w-waveguide-couplers-review-fig7b-mode-size-mismatch.png){.s}

一道光從光纖走進晶片，台積電的專利畫得最清楚：光從光纖出來，先經過 FAU 前端的透鏡，碰到 FAU 的 45° 斜面轉成往下，穿過光引擎上方那片矽上的透鏡再聚焦一次，最後打進晶片裡的光柵耦合器[[us20260133379a1]]。

![光從光纖走進晶片的路。光纖（1005）的光先經 FAU（1001）前端的透鏡，碰到 FAU 的斜面轉成往下，穿過光引擎上方那片矽（701）上的透鏡（703）再一次聚焦，最後打進晶片裡的光柵耦合器（203，梳子狀那排）。光往回走（晶片到光纖）也是同一條路。[[us20260133379a1]]](img/US20260133379A1-tsmc-fau-placement-FIG10A.png)

台積電的做法是把透鏡直接做在光引擎上。透鏡是**矽**做的：耦合透鏡由矽基板用光罩加蝕刻做出來，表面鍍抗反射層，約 22 顆排成一排、直徑約 100 微米、間距約 127 微米[[us20260133379a1]]。矽對這種紅外光透明，所以能當透鏡。台積電的論文把這幾樣列成 COUPE 光路上的三個設計：埋在裡面的微透鏡陣列、背面的金屬反射鏡、抗反射鍍層，目的都是不讓光在疊層裡多掉或波長偏移[[tsmc-ectc2025-coupe]]。光柵耦合器正下方的**金屬反射鏡**，把往下漏的光反射回來，模擬能讓損耗少 0.5 dB[[tsmc-ectc2025-coupe]]。台積電論文只寫「metal」，寫它是銅的只有一篇研究機構的文章[[tsmc-ectc2025-coupe,trendforce-fau-bottleneck]]。

![台積電 COUPE 剖面：綠色 EIC 用 SoIC 接在藍色 PIC 上。紫色虛線是光路：光從最上面 770 微米的矽載板穿下來，經過右上的矽透鏡（照片是一排圓頂透鏡），打到 PIC 上的光柵耦合器（GC），底下的金屬反射鏡（MR）把漏下去的光反射回來。[[semianalysis-cpo-book]]](img/semianalysis/img043.jpeg)

![同一件專利的光引擎剖面。最上面那片矽（701）上做了兩樣東西：一顆透鏡（703），讓光進出晶片時聚焦；一條溝槽（707），之後讓 FAU 卡進來對位。下面層層疊疊的是電的晶片和光的晶片。[[us20260133379a1]]](img/US20260133379A1-tsmc-support-substrate-lens-FIG9.png)

FAU 怎麼卡進那條溝槽、怎麼固定，見[怎麼對準、怎麼固定](fau.md#q14)。

光柵底下墊金屬鏡子，不是台積電獨有的想法。學界整理的幾種讓光柵少漏光的做法裡，就有一種是在光柵下方加一層金屬反射鏡[[mdpi-mi11-00666]]。

![四種讓光柵耦合器少漏光的做法。右上（b）在光柵下方加一層金屬反射鏡（金或鋁），往下漏掉的光被彈回來（橘色箭頭），送進波導的光就多一些。台積電的金屬反射鏡是同一個想法。[[mdpi-mi11-00666]]](img/papers/mdpi-mi11-00666-grating-coupler-reflectors-fig5.png)

**透鏡不一定做在晶片上。**另一種做法是買現成的微透鏡陣列（MLA，一排很小的透鏡），夾在光纖接頭和晶片之間。光從光纖或晶片出來會散開，透鏡把它變成平行的光，另一端才接得住[[agc-mla-fau]]。

![微透鏡陣列的位置：光纖接頭（綠）壓在光的晶片（PIC）上，中間那排紅色光柱經過透鏡陣列。圖上的英文：透鏡陣列把散開的光變成平行光。廠商示意圖。[[agc-mla-fau]]](img/parts/agc-mla-cpo-overview-20261011.png) ![透鏡陣列和稜鏡的實物。長條和小方塊上一排小圓頂就是一顆顆透鏡；三角柱是稜鏡，用斜面把光轉 90°。這些是 FAU 廠可以外購的零件。廠商產品照。[[agc-mla-fau]]](img/parts/agc-mla-intro-20261011.png)

這些外購零件怎麼組進 FAU，見[一步一步怎麼做](fau.md#q13)。

這些透鏡誰設計？COUPE 提供透鏡設計和光路模擬的工具，讓客戶自己設計[[semianalysis-cpo-book]]；NVIDIA 那顆實際是誰設計，沒有公開。

## 光從哪裡來？雷射為什麼放在外面？ {#q10}

矽本身幾乎不會發光[[tianxia-coupe-20260818]]，所以光要從外面的雷射送進來。雷射晶片本身很小，下圖一顆雷射晶片卡在縫衣針的針孔裡。資料中心用的雷射是磷化銦（InP）做的，原料和廠商見[從銦到外部光源模組](lasers.md#las-layers)。

![一顆雷射晶片有多小：比縫衣針的針孔還小。這顆是偵測氣體用的雷射，不是資料中心用的，這裡只拿來比大小。[[commons-laser-diode-chip]]](img/explain/commons-laser-diode-chip-in-needle-eye.jpg){.s}

理論上可以把會發光的材料（磷化銦）貼到矽上，把雷射做在晶片裡，但業界的共識是放在外面，原因有三個：雷射是整個系統裡最容易壞的零件，放進光引擎，一顆壞了整顆晶片報廢；雷射怕熱，而交換器晶片旁邊是全系統最熱的地方；晶片上的雷射功率也不夠[[semianalysis-cpo-book]]。NVIDIA 在規格裡也說，外部光源持續把光送進光引擎，可以降低封裝上的熱、提高可靠度[[nvidia-sn6000-datasheet-20260119]]。

所以雷射做成獨立的**外部光源模組**（ELS，External Laser Source；做成插拔式的規格叫 ELSFP），長得像光模組，插在交換器上，壞了直接拔掉換一個。模組拆開來，裡面是電路板上的雷射組件，一端是光纖接口，一端是拉環[[lightwave-eugenlight-elsfp-20260910]]。

![一支外部光源模組拆開來：上蓋、外殼，綠色電路板上兩塊銅色的是雷射組件，左邊是光纖接口，右邊是拉環。外型像光模組，可以直接拔插。原圖很小。廠商渲染圖。[[lightwave-eugenlight-elsfp-20260910]]](img/media/Lightwave-光創聯ELSFP結構-20260910-01.jpg){.s}

不只 NVIDIA 這樣做。Broadcom 2024 年的 Bailly 就設計成可以接多個遠端雷射模組、在現場更換[[broadcom-pr-bailly-20240314]]；它在 2025 年 9 月的簡報上寫，雷射已經拆出來，做成插在前面板、可以更換的模組[[broadcom-ecoc2025-202509]]；下一代 TH6-Davisson 的新聞稿也寫「可現場更換的 ELSFP 雷射模組」[[broadcom-pr-20251008]]。

**一台用幾個、幾顆。**每個 ELS 裡有 8 顆雷射，一個 ELS 能供 Quantum-X 交換器 576 條發送通道中的 32 條[[nvidia-blog-20250826]]。照這兩個數字算，一台 Quantum-X 要 576 ÷ 32 ＝ 18 個 ELS（計算），跟模組廠聯鈞說的「一個 CPO 約需要 18 個外部光源」一致；聯鈞也說「沒有外部光源，就沒有 CPO」[[nvidia-blog-20250826,udn-unitedopto-20260818,moneydj-unitedopto-20260819]]。Spectrum-X 單顆晶片的 SN6810-LD 用 16 個 ELS，4 顆晶片的 SN6800-LD 用 64 個[[nvidia-blog-20250826,nvidia-sn6000-manual-20260916]]。

| 項目 | 數字 |
|---|--:|
| 一個 ELS 裡的雷射 | 8 顆 |
| 一個 ELS 供應的發送通道（Quantum-X） | 32 條 |
| Quantum-X 整台的發送通道 | 576 條 |
| Quantum-X 整台的 ELS（計算） | 18 個 |
| Quantum-X 整台的雷射（計算：18 × 8） | 144 顆 |
| SN6810-LD 的 ELS | 16 個 |
| SN6800-LD 的 ELS | 64 個 |
| 每顆光引擎的雷射光纖（Quantum-X） | 2 條 |

表的出處：[[nvidia-blog-20250826,nvidia-sn6000-manual-20260916]]

**「雷射少四倍」是跟什麼比。**NVIDIA 說，把雷射集中在 ELS 裡、放在自己溫度受控的空間，資料中心裡雷射的總數比「舊設計」少四倍；舊設計是哪一種，它沒寫[[nvidia-blog-20250826]]。拿同頻寬的插拔式模組來算：Quantum-X 的 576 條 200G 通道，換成 1.6T 的插拔式模組要 72 支（計算：576 ÷ 8）。傳統做法每條通道一顆 EML 雷射，一支 8 顆；矽光子模組一支只要 2 顆連續光雷射[[naddod-1p6t-lasers-20250530]]。所以：

| 同樣 576 條 200G 通道 | 雷射顆數（計算） | 和 CPO 比 |
|---|--:|--:|
| CPO：18 個 ELS × 8 顆 | 144 | 1 倍 |
| 插拔式，每條一顆 EML：72 × 8 | 576 | 4 倍 |
| 插拔式，矽光子每支 2 顆：72 × 2 | 144 | 1 倍 |

「少四倍」只有拿每條一顆 EML 的模組當基準才成立；和矽光子模組比，顆數一樣。做矽光 PIC 的 Tower 在法說上也說矽光子方案的雷射顆數是 EML 的一半[[allmind-tower-q3-20251110]]。CPO 用的每一顆雷射功率比較大，所以雷射這一層的分量沒有因為 CPO 變小。一台用多少錢的雷射、各家的說法，見[一台用幾顆雷射、值多少](lasers.md#las-count)。

雷射模組插在交換器上的地方，需要一個專門的光纖接頭：模組端一個、機器端一個。Senko 的機器端接頭裝在 CPO 交換器的電路板上，一次盲插兩個 MT 插芯（多芯光纖接頭的核心零件，見[光纖怎麼接到前面板](passive.md#q16b)），支援保偏光纖[[senko-elsfp-host]]；它也推比 MPO 更小的 SN-MT 接頭，讓前面板放得下更多雷射模組[[senko-snmt-elsfp-20251203]]。

![外部雷射模組（ELSFP）插在交換器前面板。模組端（Module Connector）和機器端（Host Connector）各有一個光纖接頭，雷射的光經這裡進機器、再送到光引擎。廠商展示圖。[[senko-wiwynn-computex2026]]](img/vendor/senko-wiwynn-computex2026-elsfp-202606-02.png){.s}

NVIDIA 的專利裡，雷射插座和機內的光纖整線盒畫在一起：盒子前面一大片是對外的光纖接頭，上方一排是外部雷射的插座，雷射的光經光纖送進機器裡[[us20260276934a1]]。

![交換器機殼裡的光纖整線盒（shuffle box）。前面一大片格子（120、124）是對外的光纖接頭；盒子裡面把光纖重新排線，接到後面的光引擎。上方那一排（153）是外部雷射模組（ELSFP）的插座，雷射的光經過 155 這些光纖、156 走線盒送進機器裡。[[us20260276934a1]]](img/patents/US20260276934A1-FIG1.png)

一個外部雷射怎麼供很多通道？靠分光：一根送光的光纖接進來，波導像樹枝一樣一分二、二分四，把同一道光分給一長排光的晶片[[us12625335b2]]。

![一根送光的光纖（502）焊在一片中介層（200）上，中介層裡的波導一分再分（206），把同一道光平均分給右邊一排光的晶片（504）。[[us12625335b2]]](img/patents/US12625335B2-FIG6.png) ![電的晶片（EIC）疊在光的晶片（PIC）上；右下的 ELS 就是外部光源，雷射的光從外面經光學接頭送進來，不放在晶片上。[[lsa-review-202601]]](img/lsa-s41377-025-02048-w-waveguide-couplers-review-fig17e-i-els-into-pic.png)

**雷射壞了怎麼換。**NVIDIA 的 Spectrum-X CPO 交換器手冊有一整節講 ELS 抽換[[nvidia-sn6000-manual-20260916]]：

1. 按開檢修門，把專用的抽取治具裝到 ELS 模組上。
2. 把模組輕輕往內推，同時微微抬起治具鬆開卡榫，再把模組整個拉出來，套上防塵蓋。
3. 新模組拿掉防塵蓋，用專用的轉接頭和清潔器清潔模組的光纖接頭，也清潔機器上的插槽。
4. 對準插槽，把新模組推到底。

手冊特別寫：運轉中的系統，拔掉 ELS 不要超過 30 分鐘；工程樣品的 ELS 只能由 NVIDIA 的支援工程師現場更換[[nvidia-sn6000-manual-20260916]]。整個過程不用碰到光引擎和 FAU，這就是雷射放在外面的好處。

**實際測試裡壞的是哪裡。**公開的大規模 CPO 可靠度數據，都來自 Meta 測 Broadcom 的 CPO 交換器。一篇整理 OFC 2026 演講的文章寫，Meta 第一階段測試裡最主要的故障來源是外部雷射模組裡驅動電路的一個表面黏著元件，不是光引擎本身；扣掉這個可以改設計解決的問題，CPO 的平均故障間隔是插拔式的 10 倍以上[[stt-meta-reliability-2026]]。這類故障發生在可以拔換的模組裡。這些數字只有轉述，Meta 原始投影片沒找到，數字的出入見[可靠度數據](equipment-test.md#eq-reliability)。

**對雷射本身的要求。**業界標準組織 OIF 給 CPO 雷射光源定的可靠度目標是 50 FIT（每 10 億個裝置小時壞 50 次），比插拔式常見的約 300 FIT 嚴 5 倍以上；Lumentum 說自家 400 mW 的高功率雷射定在 20 FIT[[lumentum-elsfp-wp-202606]]。Lumentum 技術長在 2026 年 8 月的論壇上強調雷射本身很可靠，難的是組裝之後整套光學能不能長時間穩定：黏膠、元件隨時間移位、水氣，以及雷射和 PIC 之間能不能一直對準[[techorange-semicon-20260831]]。

**功率。**雷射晶片廠聯亞的看法是：CPO 用的雷射可能要 300mW 以上，但 70 到 100mW 仍是未來一兩年的主流[[moneydj-landmark-20260813]]。住友電工的技術論文說，外部光源要幾百 mW 的光輸出、20% 以上的電轉光效率；它做出的雷射在 45°C 下輸出超過 400 mW、效率 25%[[sei-tr205-cpo-laser-202407]]。

**為什麼用保偏光纖。**雷射的光是經過保偏光纖送進光引擎的。原因是矽光子元件對光的偏振方向很敏感，偏振歪了效率就掉[[nvidia-ectc2025-allsmf,cornell-cnf-2024]]。保偏光纖的代價是對位更難、成本更高。NVIDIA 在論文裡提出另一條路：改用一般單模光纖，在晶片上加偏振追蹤電路，封裝成本約降 2.7 倍，代價是多 0.74 dB 損耗[[nvidia-ectc2025-allsmf]]。

**「第二代拿掉外部光源」的說法和手冊對不上。**一份未具名的專家紀要說：第一代 Quantum 交換器用 ELSFP，裡面有保偏光纖，高功率下保偏光纖可能被燒毀或讓系統不穩；客戶交了一部分貨之後，在後續設計裡砍掉外部光源，第二代改回一般光纖[[cnyes-hao-expert-spectrum-20260930]]。但 NVIDIA 2026 年 9 月的手冊上，SN6800-LD 仍有 64 個 ELS，抽換程序也寫在手冊裡；1 月的規格書同樣列了 ELS[[nvidia-sn6000-manual-20260916,nvidia-sn6000-datasheet-20260119]]。紀要講的「第二代」是哪一台，原文沒寫。兩種說法並列；保偏光纖會不會被拿掉，見[保偏光纖](detachable.md#det-pm)。

### 雷射會一直放在外面嗎？ {#inside-laser-future}

台積電講過一個反方向的做法。2026 年 8 月 31 日 SEMICON Taiwan 的矽光子論壇上，台積電副處長陳明發說，COUPE 下一階段可望把調變器、SOA（半導體光放大器，把光再放大的元件）和光源整合到 COUPE 平台的背面；COUPE 也可以當「光學中介層」，最大到 3.3 倍光罩尺寸[[technews-tsmc-coupe-20260831]]。現在的做法是雷射在機器外面、經保偏光纖送進來；背面整合是把光源放回光引擎封裝上。

這句話要小心用：同一場演講，通訊社的報導只寫「異質整合是很重要的發展方向」「COUPE 可能成為連接運算晶片和光學元件的整合平台」，沒有提光源，也沒有提背面[[cna-tsmc-coupe-20260831]]。所有報導都沒有時程，一家外媒查過也寫「沒有量產日期」，並指出台積電同一天講的瓶頸（雷射、光纖、光纖連接器、測試）講的是現在正要量產的這一代[[scn-tsmc-cpo-bottleneck-20260904]]。要用什麼雷射、怎麼接上去，都沒有說。

## CPO 交換器怎麼散熱？ {#q10b}

答案是水冷。NVIDIA 目前三台 CPO 交換器都是液冷：InfiniBand 的 Quantum-X800 Q3450-LD，乙太網路的 Spectrum-X SN6810-LD、SN6800-LD[[nvidia-qx800-datasheet-20260911,nvidia-sn6000-manual-20260916]]。Q3450-LD 約 85% 的熱走液冷、15% 走氣冷[[nvidia-qx800-datasheet-20260911]]。

**同一顆晶片，插拔式還能氣冷，CPO 只剩液冷。**用同一顆 Spectrum-6（102.4 Tb/s）交換器晶片，NVIDIA 同時有四種機器：插拔式的 SN6600 是交流電、氣冷，有 5 個風扇；插拔式的 SN6600-LD 是全液冷；CPO 的 SN6810-LD、SN6800-LD 手冊的風扇欄寫 N/A，沒有風扇、只有液冷[[nvidia-sn6000-manual-20260916]]。液冷不是 CPO 才有，但這一代 CPO 沒有氣冷版。

先看 Q3450-LD 的水路。冷卻液從機器後方左右兩個入口進來，分成兩條並聯的迴路，先流過交換器晶片（QM3）上的銅冷板，再經中板的分歧管，去冷卻交換板上的其他元件，最後從出口匯流出去[[nvidia-q3450ld-cooling]]。這套冷卻同時要讓旁邊對溫度敏感的光學元件保持穩定[[semianalysis-cpo-book]]。

![Q3450-LD 的液冷管路。右上兩塊紅銅色的是壓在交換器晶片上的冷板（QM3 cold plate）；右下入口分歧管（Inlet manifold）把冷卻液分出去；左下出口匯流塊（Outlet block）收回來；左邊 UQD04 是接機櫃水路的快接頭。廠商文件圖。[[nvidia-q3450ld-cooling]]](img/vendor/nvidia-q3450ld-liquid-cooling-loops-20261011-01.png) ![同一套管路，把板子拿掉、看得到中板的水路（Midplate loops）：紅銅色管子在板子底下來回彎折，帶走交換板上其他元件的熱。廠商文件圖。[[nvidia-q3450ld-cooling]]](img/vendor/nvidia-q3450ld-liquid-cooling-loops-20261011-02.png)

Spectrum-X 的兩台，從機器背面就看得到水冷接頭：SN6800-LD 背面左右兩排各 5 個圓形快接頭，5 個進冷水、5 個出熱水[[nvidia-sn6000-manual-20260916]]。

![SN6800-LD 背面：左右兩排圓形的是液冷快接頭（UQD），共 5 進 5 出（手冊規格寫 5 Cold + 5 Hot）。中間四個方形接口，手冊這一頁沒有標註。[[nvidia-sn6000-manual-20260916]]](img/nvidia-sn6800ld-rear-manual-p13.png){.s}

| | Q3450-LD | SN6810-LD | SN6800-LD | SN6600-LD（插拔式，對照） | SN6600（插拔式，對照） |
|---|---|---|---|---|---|
| 交換器晶片 | Quantum-X800 | 1 顆 Spectrum-6 | 4 顆 Spectrum-6 | 1 顆 Spectrum-6 | 1 顆 Spectrum-6 |
| 怎麼冷卻 | 約 85% 液冷、15% 氣冷 | 全液冷，沒有風扇 | 全液冷，沒有風扇 | 全液冷 | 氣冷，5 個風扇 |
| 冷卻液 | Recochem OAT PG25 | Recochem PG-25% | Recochem PG-25% | Recochem PG-25% | — |
| 入水溫度 | 17–45°C（回水最高 55°C） | 17–45°C | 17–45°C | 17–45°C | — |
| 每台流量（公升／分鐘） | 4.3 | 3.5 | 13.5 | 5.7 | — |
| 快接頭 | UQD04 | UQD8 v2，2 進 2 出 | UQD8 v2，5 進 5 出 | UQD8 v2，1 進 1 出 | — |
| 機內液量 | 410 毫升 | — | — | — | — |

表的出處：[[nvidia-qx800-datasheet-20260911,nvidia-q3450ld-cooling,nvidia-sn6000-manual-20260916]]。冷卻液 PG25 是含 25% 丙二醇的水；「—」是手冊沒寫或不適用。

<div class="scroll"><figure><svg viewBox="0 0 760 250" width="100%" role="img" aria-label="各機型每台液冷流量">
<text x="10" y="22" class="note">每台交換器的液冷流量（公升／分鐘）</text>
<line x1="230" y1="35" x2="230" y2="225" class="grid"/>
<text x="220" y="62" text-anchor="end" class="item">SN6810-LD（CPO）</text><rect x="230" y="46" width="115" height="24" class="bar"/><text x="352" y="64" class="item">3.5</text>
<text x="220" y="107" text-anchor="end" class="item">Q3450-LD（CPO）</text><rect x="230" y="91" width="142" height="24" class="bar"/><text x="379" y="109" class="item">4.3</text>
<text x="220" y="152" text-anchor="end" class="item">SN6600-LD（插拔式）</text><rect x="230" y="136" width="188" height="24" class="bar2"/><text x="425" y="154" class="item">5.7</text>
<text x="220" y="197" text-anchor="end" class="item">SN6800-LD（CPO）</text><rect x="230" y="181" width="446" height="24" class="bar"/><text x="683" y="199" class="item">13.5</text>
<text x="230" y="243" class="note">SN6810-LD 和 SN6600-LD 用同一顆晶片；SN6800-LD 有 4 顆</text>
</svg><figcaption>四台交換器每台需要的冷卻液流量。深色是 CPO，淺色是同一顆 Spectrum-6 晶片的插拔式版本。同一顆晶片，CPO 版（3.5）比插拔式版（5.7）需要的流量少；SN6800-LD 有 4 顆晶片，流量最大。[[nvidia-q3450ld-cooling,nvidia-sn6000-manual-20260916]]</figcaption></figure></div>

**為什麼難：一個很燙，一個要很均勻。**一篇中國科學院微電子所的 51.2 Tb/s CPO 液冷論文把兩種熱分開講。交換器晶片 750 W，每平方毫米 1.79 W；旁邊 8 個光模組每個 64 W，每平方毫米只有約 0.2 W，熱密度差約 9 倍（計算：1.79 ÷ 0.2）。光的部分難在溫度要一致：調變器的工作波長會隨溫度飄，所以光晶片彼此的溫差要小於 4°C。論文的設計因此用兩套散熱器：交換器晶片用歧管微通道冷板，壓住高熱；光模組用並聯微通道冷板，讓每個光模組的入水溫度都一樣。模擬結果是每分鐘 4 公升的流量下，交換器晶片最高 97.3°C，光模組最高 31.3°C、彼此溫差在 1.2°C 以內[[pmc-cpo-liquid-cooling-20250514]]。同一篇論文也記了早期的做法：Intel 第一代 CPO 是交換器晶片用氣冷散熱片、光模組用熱管，2021 年才第一次在 CPO 上試液冷[[pmc-cpo-liquid-cooling-20250514]]。

<div class="scroll"><figure><svg viewBox="0 0 760 170" width="100%" role="img" aria-label="交換器晶片和光模組的熱密度比較">
<text x="10" y="22" class="note">每平方毫米發多少熱（W/mm²），51.2 Tb/s CPO 的模擬條件</text>
<line x1="200" y1="35" x2="200" y2="140" class="grid"/>
<text x="190" y="64" text-anchor="end" class="item">交換器晶片 750 W</text><rect x="200" y="46" width="448" height="26" class="bar"/><text x="656" y="65" class="item">1.79</text>
<text x="190" y="114" text-anchor="end" class="item">光模組 64 W ×8</text><rect x="200" y="96" width="50" height="26" class="bar2"/><text x="258" y="115" class="item">約 0.2　要求：彼此溫差小於 4°C</text>
<text x="200" y="160" class="note">交換器晶片要壓住高熱；光的部分熱不多，但要各處一樣冷</text>
</svg><figcaption>同一個 CPO 封裝裡兩種不同的散熱問題。交換器晶片的熱密度約是光模組的 9 倍；光模組熱得少，但調變器的波長會跟著溫度飄，所以要求的是溫度一致。數字取自一篇 51.2 Tb/s CPO 液冷論文的模擬條件，不是 NVIDIA 機器的量測。示意圖，非實際比例。[[pmc-cpo-liquid-cooling-20250514]]</figcaption></figure></div>

溫度一飄，微環就失準：前面[PIC 怎麼電光互換](#q7)算過，溫度變 2°C，微環的波長就移出可以工作的範圍。雷射放在機器外面，也是為了不把雷射的熱加到封裝上[[nvidia-sn6000-datasheet-20260119]]。

**晶片多熱會怎樣。**交換器晶片的溫度門檻：99°C 以下正常，100–109°C 警告，110°C 起由韌體關掉晶片，120°C 起由硬體直接關[[nvidia-sn6000-manual-20260916]]。

**散熱和光纖搶空間。**光引擎貼著全機最熱的交換器晶片，散熱片要罩住晶片，光纖又要從旁邊接進去。矽品的一件專利就是在散熱片側邊開一條縫，讓光纖接頭從縫裡伸進去[[us20260157229a1]]。光引擎本身怎麼散熱（例如上方有沒有獨立的冷板），NVIDIA 的手冊和規格書都沒寫，查不到。

![散熱片（22）從上面罩住晶片，側邊開一條縫（2220），讓光纖接頭（23）從縫裡伸進去，接到裡面的光子元件（213）。[[us20260157229a1]]](img/patents/US20260157229A1-FIG2.png)

**誰做這些散熱零件。**手冊唯一點名的外部廠商是冷卻液 Recochem[[nvidia-q3450ld-cooling]]。冷板組件、交換托盤、分歧管出廠時由「供應商」充氮保壓，手冊沒寫是哪一家[[nvidia-sn6000-manual-20260916]]。媒體報導健策供應 NVIDIA 兩款 CPO 交換器晶片端的零件：Quantum-X 是協助插拔、保護插座的機構件，Spectrum-X 是防止翹曲的補強板，都不是冷板；公司沒有證實[[wantrich-jentech-20260408]]。冷板、分歧管是誰做的，查不到：這一輪搜了奇鋐、雙鴻、健策、富世達、英維克、飛榮達、Boyd、CoolIT、Cooler Master、台達，沒有一家被點名和這幾台光子交換器的冷板連在一起，搜得到的都是 GPU 機櫃的水冷板。CPO 系統級測試要在液冷環境下驗證[[ebc-sipho-20260527]]。

## 台積電的 COUPE 接下來往哪裡長？ {#inside-coupe}

上面講的光引擎都是台積電 COUPE（Compact Universal Photonic Engine，緊湊型通用光子引擎）這一代。台積電把它的路線拆成兩條：一條是光引擎放的位置離運算晶片越來越近，一條是 PIC 本身的速度和密度越來越高。

**第一條：放的位置。**先看台積電 2024 年和 2026 年的兩張投影片。

![台積電 2024 年的投影片（廠商投影片）。三個階段由左到右：插拔式光模組（OSFP）裡的 1.6 Tb/s 光引擎，2025 年；和交換器晶片放在同一片基板上的 6.4 Tb/s 光引擎，2026 年；放在中介層上、貼著運算晶片（XPU）和記憶體（HBM）的 12.8 Tb/s 光引擎，標「Pathfinding」（還在探索）。最左邊的剖面裡，FAU 立在 EIC、PIC 旁邊。下方功耗 1X、<0.5X、<0.1X，延遲 1X、<0.1X、<0.05X，以插拔式為基準。[[tomshardware-cpo-foundry-20260803]]](img/media/TomsHardware-TSMC-COUPE路線圖-20260803-01.png)

![台積電 2026 年 5 月台灣技術論壇的演講現場（台積電提供的照片）。投影片改用銅線當基準，由左到右：銅線 1X；COUPE 在電路板上（on PCB），功耗效率 2X、延遲 1X；COUPE 在基板上（on Substrate），4X、<0.1X；COUPE 在中介層上（on Interposer），10X、<0.05X。後三張小圖都在封裝邊上標出 FAU。[[technews-coupe-forum-20260514]]](img/media/TechNews-台積電2026技術論壇COUPE三階段-20260514-01.jpg)

兩張投影片的基準不同，數字不能直接互相換算，並排如下：

| 階段 | 2024 投影片（以插拔式為 1） | 2026 年 4–5 月的說法 |
|---|---|---|
| 電路板上／插拔式 | 1.6 Tb/s 光引擎，2025 年；功耗 1X、延遲 1X | 以銅線為基準：功耗效率 2X、延遲 1X[[technews-coupe-forum-20260514]] |
| 基板上（和交換器晶片同一片封裝） | 6.4 Tb/s 光引擎，2026 年；功耗 <0.5X、延遲 <0.1X | 新聞稿：2026 年開始生產，比電路板上的插拔式省 2 倍功耗、延遲降 10 倍[[tsmc-pr-20260422]]；論壇：以銅線為基準 4X、<0.1X，「2026 年下半年」[[technews-coupe-forum-20260514]] |
| 中介層上（貼著 GPU 等運算晶片） | 12.8 Tb/s 光引擎，「還在探索」；功耗 <0.1X、延遲 <0.05X | 以銅線為基準 10X、<0.05X；「下一步」，沒有年份[[technews-coupe-forum-20260514]] |

表的出處：2024 投影片[[tomshardware-cpo-foundry-20260803]]。

中介層這一階段，台積電從 2024 到 2026 都沒有給年份，媒體寫台積電把它定位為探索性質、沒有揭露商品化時程[[tomshardware-cpo-foundry-20260803]]。基板上這一代什麼時候、量多大，見[量產到哪一步](timing.md#q27)；scale-up（機櫃內 GPU 互連）什麼時候用光，見[scale-up 什麼時候用光](timing.md#tm-scaleup)。2026 年 7 月有一則傳聞說 NVIDIA 把下一代專案移出 COUPE，見[「NVIDIA 暫離 COUPE」傳聞](players.md#pl-coupe)。

**第二條：一顆光引擎跑多快。**台積電在 2026 年 8 月的論壇上講了兩種加頻寬的方法[[technews-tsmc-coupe-20260831]]：

- **快而窄（Fast and Narrow）**：每條通道（lane）從 200 Gb/s 提高到 400 Gb/s 以上，同時增加通道數，總頻寬從 3.2 Tb/s 到 12.8 Tb/s 以上。
- **慢而寬（Slow and Wide）**：單條速度不追，改增加 WDM 的波長數，從 1 個到 4、8、16 個以上。

通道數的說法對不上：一家媒體寫 64 條擴到 128 條[[technews-tsmc-coupe-20260831]]，一家研究機構轉述另一家媒體寫 16 條擴到 128 條以上[[trendforce-tsmc-sipho-20260831]]。用通道速度乘回去：16 × 200 Gb/s ＝ 3.2 Tb/s，64 × 200 Gb/s ＝ 12.8 Tb/s，128 × 400 Gb/s ＝ 51.2 Tb/s（計算）。原始投影片沒有公開。

一顆光引擎的頻寬也有不同的說法：2024 年投影片寫 2026 年基板上是 6.4 Tb/s；一家研究機構的報告摘要寫，台積電在 SEMICON 說單顆 COUPE 的頻寬 2027 年從 3.2 Tb/s 倍增到 6.4 Tb/s，未來目標超過 51.2 Tb/s[[trendforce-coupe-fau-equip-20260916]]。Broadcom 自己的光引擎是 6.4 Tb/s[[semianalysis-isscc2026]]。

**微環的路線和 FAU 的排數。**台積電說全球第一個 200 Gb/s 的微環調變器 2026 年量產，位元錯誤率低於 10⁻⁸；之後往 400 Gb/s 調變器、多波長、「多列光纖陣列單元」發展，2030 年頻寬密度做到每毫米 4 Tb/s[[technews-coupe-forum-20260514]]。一家媒體把它整理成一張表，FAU 的排數也在裡面[[tomshardware-cpo-foundry-20260803]]：

| 年份 | 2026 | 2028 | 2029 | 2030 |
|---|---|---|---|---|
| 每條通道（微環） | 200 Gb/s | 200 Gb/s | 200 Gb/s | 400 Gb/s |
| 頻寬密度（每毫米晶片邊長） | 0.5 Tb/s | 1 Tb/s | 2 Tb/s | 4 Tb/s |
| 波長 | 單一 | 單一 | 多個 | 多個 |
| FAU | 單排 | 雙排 | 雙排 | 雙排 |

<div class="scroll"><figure><svg viewBox="0 0 760 290" width="100%" role="img" aria-label="COUPE 頻寬密度路線">
<text x="10" y="22" class="note">COUPE 頻寬密度（Tb/s／毫米）</text>
<line x1="60" y1="230" x2="720" y2="230" class="grid"/>
<rect x="100" y="205" width="90" height="25" class="bar2"/><text x="145" y="198" text-anchor="middle" class="item">0.5</text>
<rect x="260" y="180" width="90" height="50" class="bar"/><text x="305" y="173" text-anchor="middle" class="item">1</text>
<rect x="420" y="130" width="90" height="100" class="bar"/><text x="465" y="123" text-anchor="middle" class="item">2</text>
<rect x="580" y="30" width="90" height="200" class="bar"/><text x="625" y="48" text-anchor="middle" class="item">4</text>
<text x="145" y="250" text-anchor="middle" class="head">2026</text><text x="305" y="250" text-anchor="middle" class="head">2028</text><text x="465" y="250" text-anchor="middle" class="head">2029</text><text x="625" y="250" text-anchor="middle" class="head">2030</text>
<text x="145" y="270" text-anchor="middle" class="note">200G・單波長・單排</text><text x="305" y="270" text-anchor="middle" class="note">200G・單波長・雙排</text><text x="465" y="270" text-anchor="middle" class="note">200G・多波長・雙排</text><text x="625" y="270" text-anchor="middle" class="note">400G・多波長・雙排</text>
</svg><figcaption>台積電微環路線的頻寬密度，四年 8 倍。淺色是單排 FAU，深色是雙排。從 2026 到 2028 年頻寬密度翻倍，通道速度和波長都沒變，變的是 FAU 從單排變雙排；2029 年再翻倍靠多波長；2030 年靠 400G 的微環。這張表只見於媒體整理，原始投影片沒有公開。示意圖，非實際比例。[[tomshardware-cpo-foundry-20260803]]</figcaption></figure></div>

台積電自己的論文也寫了「多排光纖的 iFAU」（整合式 FAU）[[tsmc-ectc2025-boe]]。也就是說，2026–2027 年的 FAU 是單排，雙排在 2028 年；FAU 廠的雙排、多排送樣進度見[大立光、上詮各走到哪](fau-makers.md#q25)，單排、雙排在結構上差在哪，見[FAU 是什麼](fau.md#q11)。

**第三條：把更多東西放上 COUPE。**就是前面講的[背面整合光源](#inside-laser-future)和光學中介層，目前沒有時程。

## 還不知道的 {#inside-open}

- 光引擎上方有沒有自己的冷板：NVIDIA 手冊和規格書都沒寫，等 GTC Washington D.C.（11/30–12/3）、GTC 2027（2027-03-14～18）的開蓋實機照或拆解文。
- 冷板、分歧管是誰做的：手冊只寫「供應商」；可以看 OCP Global Summit（10/12–15）的液冷 CPO 交換器展示，以及廣達 QCT TB064-IXP 液冷 CPO 交換器的產品資料（官網目前擋爬蟲）。
- 台積電「把光源、調變器、SOA 整合到 COUPE 背面」的時程和用哪種雷射：只有一家媒體寫到，等台積電 2026Q3 法說（10/15）有沒有被問，或之後的論文。
- COUPE 產線在竹南還是嘉義、PIC 月產能多少：台積電沒有公開，等台積電法說（10/15）；目前只有法人和券商的估計，兩份對不上。
- COUPE 的通道數是 16 條還是 64 條起跳：陳明發在 SEMICON 2026 的原始投影片沒有公開。
- EIC 是 N7、N6 還是 5 奈米：可能是不同代的產品，等 NVIDIA 在 GTC 2027（2027-03-14～18）、OFC 2027（2027-03-07～11）的公開資料。
- 「2028 年雙排 FAU」的台積電原始投影片：只有媒體的文字表；看台積電下一屆技術論壇（2026 年是 4 月北美、5 月台灣）。
- 台積電 COUPE 的 SOI 晶圓向誰買：台積電、Soitec、環球晶都沒點名；看 Soitec、環球晶下一次法說有沒有講客戶（Soitec FY27 上半年財報約 11/18，只有第三方列表，官網沒查到日期）。
- 格芯 SCALE 的兩個 CPO 設計案是誰的、什麼時候出貨：轉錄稿沒講客戶；格芯下一場法說（日期沒查到）。
- Soitec 說 scale-up 的 CPO 何時開始是「問號」，問題在組裝和測試良率：這一句和台積電、NVIDIA 的說法怎麼對，要看 Soitec 下一場法說，以及台積電第三季法說（10/15）對「量產」的定義。
- NVIDIA 第二代 CPO 交換器有沒有拿掉外部光源：只有一份未具名紀要說有，NVIDIA 9 月手冊仍有 ELS；等 GTC Washington D.C.（11/30–12/3）、GTC 2027 的新機規格，和 NVIDIA 硬體手冊的改版紀錄。
- NVIDIA（COUPE）交換器的任何可靠度數據：目前公開的都是 Meta 測 Broadcom 的機器，而且 Meta 原始投影片沒找到；等 OFC 2027（2027-03-07～11）。
- 外部雷射模組裡的散熱（熱電致冷器）由誰做、佔模組耗電多少：沒有存到可以引用的資料。
