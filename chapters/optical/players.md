# 誰主導、代工廠、新創、供應鏈全圖、專利

這份筆記講 CPO 這門生意裡「誰是誰」：誰設計、誰製造、誰組整機、新創做到哪、整條供應鏈從原料到客戶怎麼接，以及從專利看誰握有技術。光和晶片之間怎麼連的基本概念，見 [CPO 是什麼](basics.md#q1)；FAU 本身見 [FAU 是什麼](fau.md#q11)；FAU 廠各自的進度和營收見 [誰在做 FAU](fau-makers.md#q22)。

和 2026-10-11 的單篇版本比，這份補了幾件事，會改變原本的理解：

- **NVIDIA 公開的供應商名單，不是固定的一份，也不是完整的供應商名單。** 2025 年 3 月的名單有 Fabrinet、Lumentum、住友電工、Coherent、Senko、Corning、波若威；2026 年 6 月 Spectrum-X 量產那篇只列台積電、矽品、「TFC」、鴻海。那篇只寫台灣生態系的段落，不能從這裡推誰退出（[誰實際在供 NVIDIA](#pl-nv)）。
- **2026 年 6 月名單裡的「TFC」，公開資料對得上的是蘇州的天孚，不是台灣公司。** 天孚的名字、產品、量產說法都對得上，只有「台灣」這一項對不上；沒有任何一方寫明這個 TFC 是誰（[「TFC」是誰](#pl-tfc)）。
- **天孚 2025 年營收的 63.31% 來自 Fabrinet，這是天孚年報具名的。** Fabrinet 在法說上說有三家客戶的 CPO 專案、營收很小（5 月財務長答「三家都在出貨」，同一場執行長說營收「大部分還在前面」，8 月又說「還沒到全量」）；但一手文件沒有任何一份把「天孚賣給 Fabrinet 的東西」和「NVIDIA 的 CPO」連在一起（[Fabrinet 做什麼](#pl-fabrinet)）。
- **唯一講到 NVIDIA 交換器 FAU 供應商分配的資料，是一份未具名的調研紀要，它把主位給了兩家非台廠。** 紀要說不可拆 FAU 主要是「公司」和天孚，可拆式是「公司」、天孚、Senko，上詮「也有相關業務」；紀要裡的「公司」，公開資料裡 Coherent 有多項對得上，但沒有任何一方寫出名字（[紀要](#pl-memo)）。
- **「NVIDIA 暫離 COUPE、改走 Tower 做 NPO」的傳聞，要拆成四句來看。** 「現在出貨的 Spectrum-X 用台積電 COUPE」有 NVIDIA 兩次公開說法；「下一代有 NPO」有好幾個非原作者的來源；只有「原因是台積電的光柵耦合器做壞、氮化矽設計套件延誤」這一句，除了原作者沒有任何來源（[傳聞](#pl-coupe)）。
- **Broadcom 那條線，光引擎端的 FAU 和線束，公開寫出來的供應商是 Corning，不是台廠。** 這條路也不經過 COUPE 的 FAU 廠（[誰在主導](#q17)）。
- **「把 FAU 貼上光引擎」這一步，日月光自己的年報、部落格、專利都說它做；但日月光、矽品、台積電、NVIDIA 四方都沒有說「NVIDIA 光引擎上的 FAU 在誰的廠貼」。** 細節和設備見 [封測廠做不做 FAU 對位](equipment-test.md#eq-osat)；專利見[專利](#q26b)。
- **OCP 這一週大部分 CPO、NPO 的光纖端，講的是接頭和插座，不是 FAU；台廠出現在系統廠、連接器廠的場次，議程 621 場的講者公司欄裡沒有大立光、上詮、波若威、光聖、台積電。** 會前只有新聞稿和議程摘要，現場內容 10/12–15 才會有（[OCP 會前](#pl-ocp)）。

## 誰在主導 CPO？ {#q17}

主導者有三種，各管不同的事：NVIDIA 賣整台交換器，Broadcom 賣交換器晶片，台積電替兩家製造光引擎。下面這張圖把兩種做生意的方式並排。

<div class="scroll">
<svg viewBox="0 0 1000 250" width="100%" style="min-width:760px" role="img" aria-label="NVIDIA 與 Broadcom 的 CPO 分工">
<defs><marker id="p3a1" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0,0 L10,5 L0,10 z" class="bar"/></marker></defs>
<text class="head" x="10" y="72">NVIDIA</text>
<rect class="box" x="110" y="30" width="160" height="72" rx="4"/><text class="item" x="120" y="58">設計晶片、光引擎</text><text class="note" x="120" y="82">NVIDIA</text>
<rect class="box" x="290" y="30" width="160" height="72" rx="4"/><text class="item" x="300" y="58">製造 PIC、EIC</text><text class="note" x="300" y="82">台積電（COUPE）</text>
<rect class="box" x="470" y="30" width="160" height="72" rx="4"/><text class="item" x="480" y="58">封裝測試</text><text class="note" x="480" y="82">矽品</text>
<rect class="box" x="650" y="30" width="160" height="72" rx="4"/><text class="item" x="660" y="58">組整台交換器</text><text class="note" x="660" y="82">鴻海；Fabrinet（2025）</text>
<rect class="box" x="830" y="30" width="160" height="72" rx="4"/><rect class="hl" x="830" y="30" width="160" height="72" rx="4"/><text class="item" x="840" y="58">賣整台交換器</text><text class="note" x="840" y="82">NVIDIA（先自家驗證）</text>
<path class="solid" d="M270,66 L290,66" marker-end="url(#p3a1)"/><path class="solid" d="M450,66 L470,66" marker-end="url(#p3a1)"/><path class="solid" d="M630,66 L650,66" marker-end="url(#p3a1)"/><path class="solid" d="M810,66 L830,66" marker-end="url(#p3a1)"/>
<text class="head" x="10" y="192">Broadcom</text>
<rect class="box" x="110" y="150" width="160" height="72" rx="4"/><text class="item" x="120" y="178">設計晶片、光引擎</text><text class="note" x="120" y="202">Broadcom</text>
<rect class="box" x="290" y="150" width="160" height="72" rx="4"/><text class="item" x="300" y="178">製造光引擎</text><text class="note" x="300" y="202">台積電（Davisson 起）</text>
<rect class="box" x="470" y="150" width="160" height="72" rx="4"/><rect class="hl" x="470" y="150" width="160" height="72" rx="4"/><text class="item" x="480" y="178">賣交換器晶片</text><text class="note" x="480" y="202">Broadcom</text>
<rect class="box" x="650" y="150" width="160" height="72" rx="4"/><text class="item" x="660" y="178">組機、賣給客戶</text><text class="note" x="660" y="202">Micas、Celestica 等</text>
<path class="solid" d="M270,186 L290,186" marker-end="url(#p3a1)"/><path class="solid" d="M450,186 L470,186" marker-end="url(#p3a1)"/><path class="solid" d="M630,186 L650,186" marker-end="url(#p3a1)"/>
</svg>
</div>

<p class="tag">示意圖，非實際比例。藍色粗框是這家公司賣出去的東西。NVIDIA 那一列是它自己公布的分工；Broadcom 那一列的組機廠來自研究機構的整理。[[nvidia-blog-20260601]][[nvidia-blog-20250327]][[broadcom-pr-20251008]][[semianalysis-cpo-book]]</p>

**NVIDIA 是系統商。**它自己設計交換器晶片和光引擎，挑供應商，最後賣的是整台交換器。它的 CPO 放在兩條產品線裡，名字直接掛「Photonics」：InfiniBand（NVIDIA 主導的一種高速網路規格）的 **Quantum-X Photonics**，例如 Quantum-X800 Q3450-LD；乙太網路的 **Spectrum-X Photonics**（也叫 Spectrum-X Ethernet Photonics），例如 SN6800、SN6810[[nvidia-qx800-datasheet-20260911,nvidia-blog-20260106]]。NVIDIA 2026 年 6 月公布的分工是：台積電做矽光子晶片，矽品負責封裝測試、「把電和光的元件組在一起，精度到微米級」，「TFC」把雷射晶粒封成雷射模組，鴻海組整台交換器，最後在 NVIDIA 自己經營的 AI 工廠開機驗證，才出貨給客戶[[nvidia-blog-20260601]]。這份名單和 2025 年 3 月公布的那份不一樣，見 [誰實際在供 NVIDIA](#pl-nv)。

![Quantum-X800 交換器機殼內部。中間藍色那顆是交換器晶片：每秒 28.8 兆位元（Tb/s）、台積電 4N 製程、1,070 億個電晶體。圍著它的一圈白色金屬殼裡裝的是光引擎；右邊露出同一台機器裡的另一顆晶片。一台 Q3450-LD 裡有四顆這樣的晶片。[[semianalysis-cpo-book]]](img/semianalysis/img058.jpeg)

**Broadcom 是晶片商。**它設計交換器晶片和光引擎，賣的是晶片，整台機器交給別人組。每一代 CPO 都有代號，跟著交換器晶片 Tomahawk 走：第一代 Humboldt（Tomahawk 4，25.6 Tb/s，只有一半頻寬走光，一家研究機構認為它主要是概念驗證）、第二代 Bailly（Tomahawk 5，51.2 Tb/s，全部走光）、第三代 Davisson（Tomahawk 6，102.4 Tb/s，交換器晶片用台積電 N3 製程，配 16 顆 6.4 Tb/s 光引擎）[[semianalysis-cpo-book,broadcom-pr-20251008]]。Broadcom 2025 年 10 月宣布 Davisson 開始出貨，先送樣給早期客戶和夥伴，並說正在開發每通道 400G 的第四代[[broadcom-pr-20251008]]。機器由 Micas、Celestica 等代工廠組裝；另有傳聞說日本 NTT 直接買 Tomahawk 6 的裸晶片，配自己的光引擎做 CPO 系統[[semianalysis-cpo-book]]。Broadcom 也幫客戶的 AI 晶片（ASIC，替特定用途客製的晶片）加上 CPO；一家研究機構的了解是，這是 OpenAI 選 Broadcom 的關鍵因素之一[[semianalysis-cpo-book]]。

**Broadcom 這條線的光纖端，公開寫出來的供應商是 Corning。**Corning 2025 年 5 月說成為 Bailly 的合格供應商，供應的線束包含把光纖接到光引擎的 FAU，以及前面板、外部雷射模組的接頭[[corning-pr-broadcom-bailly-20250513]]；Davisson 的新聞稿裡，Corning 說它供應 TH6-Davisson 從前面板到晶片的整套光學組件[[broadcom-pr-20251008]]。Broadcom 自己把它的可拆、被動對位、邊緣耦合的光纖接頭叫 BFC（Broadcom Fiber Connector），說已完成濕熱、溫循、衝擊、振動、粉塵驗證[[broadcom-ecoc2025-202509]]；美國專利裡 Broadcom（以子公司 Avago 的名義）有一件可重複插拔的邊緣耦合準直接頭[[us12216313b2]]。Corning 的新聞稿沒有提 BFC，Broadcom 的簡報沒有提 Corning，所以能寫的是「Corning 供光引擎端的 FAU 和整套線束」，**BFC 本身由誰製造，沒有一方寫**。

**Broadcom 自己對 CPO 時程的說法，三個月內有兩種講法。**執行長陳福陽（Hock Tan）在法說會（轉錄稿）上，2025 年 12 月把順序講成「銅 → 插拔式光 → 矽光子」：「最後一根稻草」是插拔式光學也做不好的時候，「當連銅都做不到時，你就走向矽光子，而且這會發生」，同一段還說「甚至不確定它會不會被完全部署」，因為工程師還在想辦法把機櫃內的 scale-up 留在銅線上[[fool-broadcom-q4fy25-20251212]]。2026 年 3 月：400G 的 SerDes 已能在機櫃內驅動銅線，「你不需要去追一個叫 CPO 的閃亮新東西。即使我們是 CPO 的領先者，CPO 會在它的時候到來，不是今年，也許不是明年」[[broadcom-fy26q1-call-20260304]]。2026 年 6 月致詞：「在 CPO，也就是共封裝光學、1.6T DSP、CW 和 EML 雷射上，我們是業界的事實標準」[[broadcom-fy26q2-call-20260603]]。三句放在一起：「領先、事實標準」講的是供應商的位置，「不是今年、也許不是明年」講的是客戶部署的時間；前後沒有改口，但只引其中一句會讀成相反的意思。

![Broadcom 上一代光引擎（Bailly）的接法：電的晶片（EIC）埋在一層黑色模封材料裡，上面用重佈線層和小凸塊接到光的晶片（PIC），這叫扇出型晶圓級封裝（FOWLP）。和台積電把兩片直接面對面接合（SoIC）不同，中間多了一層線路和凸塊。下排是剖面的顯微照片。[[semianalysis-isscc2026]]](img/media/SemiAnalysis-ISSCC2026-CPO-20260415-04.jpeg)

**台積電是代工平台。**它不設計光引擎，但光引擎的製造和封裝都在它這裡：做光的晶片（PIC，光子積體電路）、電的晶片（EIC，電子積體電路），再把兩片疊起來，這套製程叫 COUPE（Compact Universal Photonic Engine）。NVIDIA 的光引擎走 COUPE，Broadcom 的 Davisson 也寫明以 COUPE 為基礎[[nvidia-blog-20250327,broadcom-pr-20251008]]。

台積電有沒有說過 COUPE 有「標準化插座」，兩邊說法對不上，並排列出：一篇雜誌報導寫台積電說 COUPE 從設計初期就以「標準化插座」為目標，讓各家照同一套規格做[[tianxia-coupe-20260818]]；另一輪查台積電的新聞稿、法說、論壇報導，沒有找到台積電這樣說過，找到的「插座」是別人的：Open CPX MSA 做插座式光引擎介面規格，Oracle 在業界座談主張插座式 CPO，反對綁死單一交換器晶片廠的垂直整合封裝[[opencpx-spec-v1-20260916,stt-ofc2026-cpo-panel-2026]]。COUPE 的時程和往哪裡長，見 [台積電的 COUPE 接下來往哪裡長](inside.md#inside-coupe)和[量產到哪一步](timing.md#q27)。

其他設計方：Marvell 自己設計 3D 光引擎，和客製化運算晶片放在同一片基板上[[marvell-pr-20250106]]，並以約 32.5 億美元買下光互連新創 Celestial AI[[marvell-celestial-20251202]]；AMD 買下矽光子新創 Enosemi[[amd-enosemi-20250528]]；Intel 有自己的光學 I/O 小晶片和矽光子製程[[intel-oci-20240626]]。Meta 也自己設計機器：OCP 的議程摘要寫 Meta 的 102.4T「整合光學」交換器是 1.5 OU 的液冷刀片，64 個光埠走 16 個「四埠 MMC 介面」，用 16 個外部雷射模組，光學耗電比插拔式約少 60%；摘要同時定義了 CPO（光引擎在交換器晶片基板上）和 NPO（光引擎在基板旁），沒寫 Meta 這台是哪一種[[ocp2026-agenda-20261012]]。

把兩家已公開的 CPO 交換器排在一起：

<div class="scroll">

| 公司 | 產品 | 網路 | 交換器晶片 | 總頻寬 | 光引擎 | 狀態 |
|---|---|---|---|---|---|---|
| NVIDIA | Quantum-X Photonics Q3450-LD | InfiniBand | 4 顆 Quantum-X800，每顆 28.8 Tb/s | 115.2 Tb/s | 72 顆 1.6 Tb/s；每顆晶片周圍 6 組、每組 3 顆，可拆下[[semianalysis-cpo-book]] | 2025 年 3 月發表，當時說當年稍晚上市[[nvidia-pr-20250318]] |
| NVIDIA | Spectrum-X Photonics SN6810-LD | 乙太網路 | 1 顆 Spectrum-6 | 102.4 Tb/s | 36 顆 3.2 Tb/s，32 顆在用、4 顆備援，焊死在基板上[[semianalysis-cpo-book]] | 2026 年 6 月 1 日宣布全面量產[[nvidia-blog-20260601]]；8 月 14 日宣布出貨[[cnyes-spectrumx-20260817]] |
| NVIDIA | Spectrum-X Photonics SN6800-LD | 乙太網路 | 4 顆 Spectrum-6 | 409.6 Tb/s | 同上，4 組 | 同上 |
| Broadcom | TH4-Humboldt | 乙太網路 | Tomahawk 4 | 25.6 Tb/s | 4 顆 3.2 Tb/s，只負責一半頻寬 | 已出貨，量很少[[semianalysis-cpo-book]] |
| Broadcom | TH5-Bailly | 乙太網路 | Tomahawk 5 | 51.2 Tb/s | 8 顆 6.4 Tb/s | 已出貨，量很少[[semianalysis-cpo-book]] |
| Broadcom | TH6-Davisson | 乙太網路 | Tomahawk 6（台積電 N3） | 102.4 Tb/s | 16 顆 6.4 Tb/s，台積電 COUPE | 2025 年 10 月宣布出貨，送樣給早期客戶[[broadcom-pr-20251008]]；OCP 前 Broadcom 說 Celestica、台達、Micas 三家的攤位展出實機[[broadcom-ocp-pr-20261008]] |

</div>

NVIDIA 的光互連能不能給別家的晶片用？NVIDIA 有一套 NVLink Fusion，讓別家的晶片接上 NVLink（NVIDIA 自家 GPU 之間的高速連線）；Ayar Labs、Lightmatter 兩家光互連新創 2026 年 6 月都宣布加入[[ayarlabs-nvlink-fusion-20260602,lightmatter-nvlink-fusion-20260602]]。但素材裡沒有任何一份寫 NVLink Fusion 包含 CPO。

## NVIDIA 的 CPO 是跟 GPU 綁在一起賣，還是可以單獨買？ {#q17b}

**現在 NVIDIA 的 CPO 不在 GPU 裡，而是在網路交換器裡**，交換器是單獨的產品。

NVIDIA 的 GPU 之間（scale-up，同一櫃 GPU 互連的 NVLink）目前還是銅線。一家研究機構寫，NVIDIA 在 scale-up 上「仍然力推銅線，想盡辦法避免改用光，甚至到 2027、2028 年」[[semianalysis-cpo-book]]。NVIDIA 在 GTC 2026 說，要到 Feynman 世代，Kyber 機櫃的 scale-up 才是「銅線和共同封裝光學都有」[[nvidia-blog-gtc2026-20260319]]。所以今天買得到的 CPO，是 scale-out（櫃與櫃之間）用的交換器。scale-up、scale-out 兩個詞見 [scale-up 和 scale-out](basics.md#q4b)，scale-up 什麼時候改用光見 [scale-up 什麼時候用光](timing.md#tm-scaleup)。

![Spectrum-X 光子交換器的兩個型號：左邊較高的是 SN6800（四顆交換器晶片），右邊較矮的是 SN6810（一顆）。各是一台獨立的機器，客戶買的是整台交換器。廠商產品照。[[nvidia-blog-20260106]]](img/nvidia-spectrumx-sn6800-sn6810-switches-20260106-03-trimmed.jpg)

這些交換器一台一台有自己的型號和作業系統（NVOS），而且**同一系列裡 CPO 版和插拔式版並排**，客戶自己選。以 InfiniBand 的 Quantum-X800 系列為例[[nvidia-qx800-datasheet-20260911]]：

<div class="scroll">

| 型號 | 光怎麼接 | 交換器 | 前面板 | 冷卻 | 高度 |
|---|---|---|---|---|---|
| Q3450-LD | **CPO** | 115.2 Tb/s | 144 個 MPO 光纖接頭 | 液冷 85%、氣冷 15% | 4U |
| Q3300-LD | 插拔式光模組或銅纜 | 115.2 Tb/s | 72 個 OSFP 插槽 | 液冷 | 3U |
| Q3400-RA | 插拔式 | 115.2 Tb/s | 72 個 OSFP 插槽 | 氣冷 | 4U |
| Q3401-RD | 插拔式 | 115.2 Tb/s | 72 個 OSFP 插槽 | 氣冷 | 4U |
| Q3200-RA | 插拔式 | 一個機殼裝兩台各 28.8 Tb/s 的交換器 | 兩組各 18 個 OSFP 插槽 | 氣冷 | 2U |

</div>

<p class="tag">OSFP 是插拔式光模組的一種插槽規格，這個系列一個插槽接兩個 800G 埠。U 是機櫃高度單位，1U 約 4.4 公分。</p>

乙太網路的 Spectrum-6 系列也一樣：同一顆 102.4 Tb/s 的 Spectrum-6 晶片，有插拔式和 CPO 兩種機器。手冊列出的典型耗電，正好看得出 CPO 省電省在哪裡[[nvidia-sn6000-manual-20260916]]：

<div class="scroll">

| 型號 | 光怎麼接 | 晶片數 | 總頻寬 | 冷卻 | 典型耗電 | 重量 |
|---|---|---|---|---|---|---|
| SN6600 | 插拔式，64 個 OSFP 插槽 | 1 顆 | 102.4 Tb/s | 氣冷 | 3.94 kW（FRO）／3.2 kW（TRO） | 52 kg |
| SN6600-LD | 插拔式，64 個 OSFP 插槽 | 1 顆 | 102.4 Tb/s | 液冷 | 3.3 kW（FRO）／2.79 kW（TRO） | 33 kg |
| SN6810-LD | **CPO**，128 個 MMC-16 光纖接頭 | 1 顆 | 102.4 Tb/s | 液冷 | 1.96 kW（最大 2.2 kW） | 32.5 kg |
| SN6800-LD | **CPO**，512 個 MMC-16 接頭、64 個外部光源 | 4 顆 | 409.6 Tb/s | 液冷 | 8.3 kW | 95 kg |

</div>

FRO、TRO 是兩種插拔式光模組：FRO 收、發兩端都有 DSP（數位訊號處理晶片，把變形的訊號整理回來），TRO 只有發射端有[[nvidia-sn6000-manual-20260916]]；兩種的差別見[拿掉 DSP：LPO、TRO](alternatives.md#alt-lpo)，整台耗電的比較見[同一顆晶片整台耗電比較](alternatives.md#alt-power)。同樣是液冷、同一顆晶片，CPO 版 SN6810-LD 典型 1.96 kW，比搭 FRO 模組的插拔式版（3.3 kW）少約四成，比搭 TRO 的（2.79 kW）少約三成（計算：1 − 1.96 ÷ 3.3 ≈ 41%，1 − 1.96 ÷ 2.79 ≈ 30%）。手冊沒有寫插拔式那兩個數字包含哪些模組、幾支。

NVIDIA 2025 年發表時就把矽光子交換器定位成 Spectrum-X Photonics（乙太網路）和 Quantum-X Photonics（InfiniBand）這兩個**網路平台**的一部分，並說 Spectrum-X Photonics 交換器 2026 年「由主要的基礎設施和系統廠商」供貨[[nvidia-pr-20250318]]。NVIDIA 官網的產品分類也把乙太網路交換器、SuperNIC（網卡）、線材和光模組分開列[[nvidia-sipho-page]]。換句話說，它是透過系統廠賣出去的網路設備。

第一批 Spectrum-X 光子交換器的客戶是 CoreWeave、Lambda、甲骨文，這是 NVIDIA 在官方社群帳號宣布、媒體轉述的[[cnyes-spectrumx-20260817]]。至於客戶能不能只買 NVIDIA 的 CPO 交換器、搭配別家的 GPU 或 ASIC 用，素材裡沒有 NVIDIA 的說法。對照組是 Broadcom：它賣的是交換器晶片，由 Micas、Celestica 等組成交換器，還傳出 NTT 自己買裸晶片配自家光引擎[[semianalysis-cpo-book]]。

NVIDIA 對外講 CPO 的好處，數字換過兩組：2026 年 8 月 Hot Chips 的簡報和量產新聞是雷射少 4 倍、功耗低 5 倍、事故間隔（MTBI）10 倍[[sth-hotchips2026-spectrumx-20260825,storagereview-spectrumx-production-20260815]]；OCP 的議程摘要寫的是功耗效率 3.5 倍、AI 正常運作時間 5 倍[[ocp2026-agenda-20261012]]。兩組的比較基準都沒寫，引用時要寫清楚是哪一場的。Quantum-X 和 Spectrum-X 的光纖接法不一樣（一個密封、一個可拆），見 [固定式和可拆式](fau.md#fau-types)。

### 整機廠和交換器廠自己怎麼說 {#pl-oems}

不是晶片商、也不是 NVIDIA 的幾家整機廠和網路設備商，在法說會（轉錄稿）上談 CPO 的口風：

- **Celestica**（組 Broadcom CPO 交換器的代工廠之一）：2025-10，「我們認為會在 1.6T 看到一些部署，而 CPO 更多的爬升會在 3.2T」[[allmind-celestica-q3-20251028]]。2026-01，量產採用「會更偏向 3.2T」，「但我們還沒看到客戶要求 CPO 大量採用」，3.2T 的樣品大約 2026 年底[[fool-celestica-q4-20260129]]。2026-04，宣布拿到「一家雲端大廠、1.6T 共封裝光學乙太網路交換器」的設計製造案，執行長說這是「第一個用 Broadcom Tomahawk 模組、直接設計進我們系統的大規模量產型共封裝光學部署」（轉錄稿在型號處寫 [inaudible]）；同一場他說各家雲端大廠採用 CPO 的路不同，「有些選擇先做 CPX 再做 CPO，但最終我們認為主要採用會在 3.2」（後面也是 [inaudible]）[[fool-celestica-q1-20260428]]。2026-07，這個案子「樣品上半年出來、量產 2027 下半年開始」[[allmind-celestica-q2-20260728]]。
- **Cisco**（2026-02）：執行長說 CPO「我們絕對相信會發生，但不認為現在迫在眉睫」；2 年前就展示過這項技術，客戶要時會做；現在客戶要的是選擇，「很多情況下客戶希望光學和矽晶片分開，才有選擇、不被綁住」[[fool-cisco-q2-20260211]]。這是和 NVIDIA 把 CPO 與交換器晶片一起賣相反的買方想法。
- **智邦**（台灣交換器品牌，富果的整理，不是逐字稿）：2025-11 法說備忘錄把策略寫成分階段：先做用 DSP 的 CPO 收發器、學製造技術，再做交換器晶片加光引擎整合的 CPO 產品；並寫智邦把 CPO 的定義看成「任何晶片與光學在基板上的整合」[[fugle-accton-20251107]]。

## 光引擎為什麼都找台積電？別的代工廠在做什麼？ {#q18}

台積電做矽光子，起點其實是封裝團隊。2009 年台積電先進封裝團隊被調去做 3D IC 時，就在想電傳輸總有一天不夠用；前董事長劉德音、副共同營運長張曉強念書時都做過矽光子。2020 年前後提案上去，第一個反應是懷疑：「是不是又狼來了？」因為這題做了幾十年都沒開花結果。一位半導體業高層的說法是：「這次不一樣，因為這群研發工程師不是做光的背景，他們是做封裝的。」2021 年發表 COUPE 論文，現在在竹南和嘉義的先進封裝廠生產[[tianxia-coupe-20260818]]。（COUPE 的產線到底在竹南還是嘉義，查不到任何一篇把 COUPE 或 CPO 產線對到哪個廠區。）

封裝的背景直接影響了技術選擇：光學出身的人會追求損耗最低的邊緣耦合（光纖從晶片側邊對進去），封裝出身的人反而選了損耗較大的光柵耦合（光從晶片表面出來），因為從表面出光，面積大、光纖好對準、好量產[[tianxia-coupe-20260818]]。

以前台積電在矽光子比較弱，格芯和 Tower 才是首選代工廠；這幾年台積電追上來，關鍵是它能把**先進製程的 EIC、PIC、3D 堆疊和封裝**一次做完。台積電是唯一大量出貨過晶片對晶圓混合接合（兩片晶片的銅接點直接對接，中間不用凸塊）的代工廠，例如 AMD 的晶片；Intel 在做類似技術，但遇到很大困難[[semianalysis-cpo-book]]。這也帶來綁定：用 COUPE 就等於用台積電做的 PIC，因為台積電不封裝別家代工廠做的矽光子晶圓[[semianalysis-cpo-book]]。NVIDIA 的光引擎走 COUPE；Broadcom 的 Davisson 新聞稿也寫明以台積電 COUPE 為基礎，稿子裡還有台積電的引言[[broadcom-pr-20251008]]。Broadcom 上一代 Bailly 用的是矽品開發的扇出型晶圓級封裝（[誰在主導](#q17)的剖面圖）[[semianalysis-cpo-book]]。NVIDIA 是否在台積電以外準備第二套，沒有公開資料；對下一代的傳聞見 [「NVIDIA 暫離 COUPE」傳聞](#pl-coupe)。

台積電自己怎麼講量產：2026 年 4 月的新聞稿寫 COUPE 放在基板上的真正 CPO「2026 年開始生產」[[tsmc-pr-20260422]]；7 月第二季法說，分析師問 COUPE 何時對營收有實質貢獻，魏哲家答「現在就開始生產，之後會往上爬」，沒有給金額或時程[[allmind-tsmc-q2-20260716]]；8 月底的論壇上，先進封裝技術發展副總說 CPO 從今年下半年開始量產[[youfenxi-tsmc-semicon-20260831]]。一個月產能約 500 片到 2028 年至少 2.5 萬片的估計、良率的估計，都是法人和券商的說法，兩份對不上，見[量產到哪一步](timing.md#q27)。另外，COUPE 的開發者侯上勇 6 月底自台積電退休，報導說他傳將加入聯發科（聯發科表示無法評論）[[udn-tsmc-hou-20260711]]。

![一場產業論壇投影片整理的五家晶圓廠矽光子路線。台積電的平台叫 COUPE：光的晶片用 65 奈米、電的晶片用 7 奈米以下，兩片用 SoIC（台積電的 3D 堆疊）疊在一起，2025 年量產。格芯把電和光做在同一片晶片上（Monolithic）；三星、英特爾的箭頭畫到 2027 年左右；聯電寫 2026 年開發驗證、2027 年風險試產。右下角的講者擋住了格芯和聯電兩列 2029 年那一格。時程是製表者整理的，和各家自己的說法不一定一致，例如聯電自己說 2026 年 7 月已交付首批量產晶圓（見下表）。[[wallstreetcn-wins-forum]]](img/華爾街見聞-穎崴CPO論壇-2026日期不明-04-foundry-table.png)

其他代工廠也在做 PIC，而且有些量不小，但多半是單獨的 PIC，主要用在插拔式光模組和 NPO：

| 代工廠 | 公司自己說的 |
|---|---|
| Tower | 2027 年矽光子合約 13 億美元、已收 2.9 億美元預付款，50 家以上客戶，都沒具名[[tower-pr-20260513]]；和 NVIDIA 2026 年 2 月公開合作，見 [傳聞](#pl-coupe)。2026-02 法說上，執行長說現在的矽光 IC「都是由其他模組廠或整合廠設計並出貨」，Tower 不直接出貨給 NVIDIA[[allmind-tower-q4-20260211]]。2026-05：卡的是 InP 的起始材料、不是雷射成品；2026-08：和 IQE 簽了多年的 III-V 磊晶片供應合約，「處理得很好」[[allmind-tower-q1-20260513,fool-tower-q2-20260804]] |
| 聯電 | 新加坡 12 吋 SOI 產線，SILITH 1.6T 平台首批量產晶圓 2026 年 7 月 14 日交付；產品通過一家領先的雲端基礎設施客戶的認證，沒具名[[umc-silith-20260714]] |
| 意法半導體 | PIC100 平台已在 12 吋（300 mm）晶圓量產，與 AWS 共同開發，2027 年產能要翻成四倍[[st-pic100-20260309]]。法說上：2026-04 執行長說意法是「唯一能在 12 吋晶圓上提供矽光技術」的公司；2026-07 說光連接帶動的營收 2026 年超過 10 億美元、2027 年「遠高於 20 億美元」。這是光連接整體（含微控制器、BiCMOS 電子 IC、矽光 IC），不是單看矽光 IC；7 月的說法是矽光 IC 的營收「從明年開始加速」，用在插拔式收發器裡[[allmind-st-q1-20260423,allmind-st-q2-20260723]]。AWS 與近封裝光學的一句，見 [NPO 誰有產品](alternatives.md#alt-npo) |
| 格芯 | 買下新加坡矽光子代工廠 AMF，自稱最大的純矽光子代工廠[[gf-pr-amf-20251118]]；拿到美國商務部 3 億美元補助意向書[[gf-6k-20260805]]；第二季法說說 2027 年看到 NPO 開始放量、2028 年 CPO 放量，很多客戶「同時有比較早放量的 NPO 和晚一點的 CPO」，沒點名客戶[[fool-gf-q2-20260812]]。2026-05 法說：4 月發表給 NPO 和 CPO 用的完整光模組方案 SCALE（轉錄稿寫成小寫 scale，說是矽光 co-packaged 先進光引擎），執行長說它是「業界第一個符合 OCI MSA 的平台，技術規格超過 MSA 的要求」；第一季有「一對」支援 OCI 標準的 CPO 設計案 tape-out（轉錄稿寫 Multi New York，地點引用前要核對）[[fool-globalfoundries-q1-20260505]] |
| 三星 | 官方只有財報一句「建立矽光子業務基礎」[[samsung-1q2026-20260430]] |
| Intel | 自有製程，自己用[[intel-oci-20240626]] |

AMD 下一代 MI500 的 CPO，傳聞是 PIC 由格芯做、日月光封裝，只有媒體報導[[semimedia-amd-mi500-20260422]]。方向相反的說法也有：媒體寫 2025 年 NVIDIA、Broadcom 把部分產品從格芯轉到 COUPE[[36kr-coupe-20260607]]；一位匿名分析師寫 Ayar Labs 和 Lightmatter 都從格芯轉到 COUPE[[ia-ayar-lightmatter-coupe-20260920]]。

台積電以外，封測廠也在準備光引擎封裝。日月光提出兩種做法：用矽穿孔（TSV，在矽晶片上打通的導電孔）或扇出型堆疊封裝，把 PIC 和 EIC 垂直接起來；2025 年 4 月它展示了把多個光引擎和 ASIC 放進同一個封裝的方案[[technews-sipho-20260317,ase-pr-cpo-20250401]]。日月光、矽品、Amkor、長電各自說做到哪、有沒有做 FAU 對位，見 [封測廠做不做 FAU 對位](equipment-test.md#eq-osat)。

![日月光的兩種光引擎封裝。左：光的晶片（PIC）面朝下蓋在兩顆電的晶片上，PIC 邊緣伸出去，FAU 從側邊接（邊緣耦合）。右：電的晶片和耦合器都放在 PIC 上面，FAU 從上方接。[[technews-sipho-20260317]]](img/media/TechNews-矽光子商轉元年-20260317-06.jpg)

## 「NVIDIA 暫離 COUPE」傳聞 {#pl-coupe}

2026 年 7 月 12 日，一位匿名的分析師在社群文章裡寫：NVIDIA 把下一代光學專案從台積電移到 Tower。文章的內容可以拆成四句：

1. 下一代原本的方案（「方案 A」）是 COUPE 上、每波長 50–64G 的 NRZ（用高低兩種電位傳 0 和 1）、8 個波長的 CPO；
2. 現在改成備案（「方案 B」）：Tower 的矽光平台、每通道 200 或 400G 的 PAM4（四種電位）、16 個波長的 NPO；
3. 原因是台積電的高密度二維光柵耦合器「做壞了」、氮化矽（SiN）的設計套件延誤；
4. 這是「暫時」的。

作者自己揭露持有 Lumentum、減碼了 Tower[[ia-npo-cpo-july-20260712]]。同一天有一則快訊用「消息人士透露」重述，內容和原文逐字對得上，不是第二個獨立來源[[bitget-odaily-coupe-20260712]]；科技新報轉述時寫明唯一訊息來自這位分析師，台積電、NVIDIA 都沒有證實[[technews-nvidia-coupe-tower-20260713]]；本土法人說不宜過度解讀，雲端大廠多先用 NPO 過渡[[setn-nvidia-coupe-20260714]]。7 月 12 日之後到 10 月 12 日，這位作者公開的免費文章沒有再重複「NVIDIA 改 Tower」這句；9 月 20 日那篇反而寫 Ayar Labs 和 Lightmatter 從格芯轉到 COUPE[[ia-ayar-lightmatter-coupe-20260920]]。付費的部分沒有讀到。

把四句分開，看公開資料各自怎麼說：

| 這一句 | 公開資料怎麼說 | 來源的種類 |
|---|---|---|
| 現在出貨的產品用 COUPE | NVIDIA 8 月 25 日 Hot Chips 的簡報寫「3D 堆疊矽光引擎，用台積電 Coupe 製程」；8 月 14 日 NVIDIA 宣布量產出貨時逐段列供應鏈，台積電做矽光子製造[[sth-hotchips2026-spectrumx-20260825,storagereview-spectrumx-production-20260815]]。台積電 7 月法說沒提傳聞、沒提客戶[[allmind-tsmc-q2-20260716]] | NVIDIA 自己的簡報；媒體轉述 NVIDIA 公布的內容 |
| 下一代有 NPO | Lumentum 說「連我們最大的 CPO 客戶，也在看 NPO 的特定新用途」，同一段又說最大客戶的生產計畫「完全照進度」，沒點名[[investing-lumentum-q4fy26-20260811]]；研究機構說 NVIDIA 的 NPO 專案還在送樣，比較確定的訂單可能要到年底或 2027 上半年[[fundaai-ecoc2026-20260929]]；券商估 NVIDIA 平台 3.2T NPO 光引擎 2027 年約 600 萬顆、2028 年約 1,900 萬顆（NVL576 scale-up 用）[[cnyeshao-gf-npo-oe-20260818]]；NVIDIA 的網路主管承認 CPO 和 NPO 會並存[[lightcounting-cpo-npo-20260723]] | 一家公司的說法；研究機構；券商；一場公開的對談 |
| 方案 A 的規格存在 | NVIDIA 研究單位 2026 年發表了多篇相關論文：32 Gb/s 每波長、8 個波長加一個時脈波長、3D 堆疊 7 奈米 EIC 疊 65 奈米 PIC（ISSCC 2026、OFC 2026、VLSI 2026）；標題沒寫代工廠，論文摘要頁抓不到[[nvidia-research-mehta-2026,semianalysis-isscc2026]] | 論文標題；研究機構 |
| 改走 Tower | Tower 2026 年 2 月的新聞稿說，它的矽光用於「為 NVIDIA 網路協定設計的 1.6T 資料中心光模組」，NVIDIA 的網路主管說「NVIDIA 正與 Tower 合作」，這講的是插拔式光模組，不是 NPO 或 CPO[[tower-pr-nvidia-20260205]]。7 月 12 日之後，Tower 的所有公開文件和第二季法說全文沒有出現「NVIDIA」[[fool-tower-q2-20260804]] | 兩家公司具名 |
| 原因是光柵耦合器做壞、設計套件延誤 | 除了原作者，找不到任何技術來源、媒體報導或公司說法。台積電 8 月底只說 COUPE 同時支援光柵耦合器和邊緣耦合器、設計套件涵蓋耦合器，沒有回應這句[[technews-tsmc-coupe-20260831]] | 只有一個來源 |

![NVIDIA 8 月 Hot Chips 簡報的一頁：Spectrum-X 光子交換器的四件事——微環調變器的 CPO 晶片已在生產、3D 堆疊矽光引擎用台積電 Coupe 製程、高功率高效率雷射、可拆式光纖接頭；下方是 4 倍少雷射、5 倍低功耗、10 倍長的事故間隔。右邊是實際機櫃的照片。廠商簡報圖。[[sth-hotchips2026-spectrumx-20260825]]](img/media/ServeTheHome-HotChips2026-NVIDIA網路投影片-202608-05.jpg)

所以對現行產品，傳聞和公開資料沒有矛盾：NVIDIA 說出貨中的 Spectrum-X 用台積電 COUPE，傳聞講的是下一代（scale-up、Rubin Ultra 或 Feynman）的選項[[simpletechtrend-nvidia-cpo-npo-2026]]。NVIDIA 下一代光學用哪家代工，NVIDIA 沒有任何公開說法；8 月 26 日的財報法說，全文沒有出現光學、CPO、台積電、Tower。

**Tower 這邊有什麼。**

- Tower 的矽光年化營收從 2025 年第二季的 1.8 億美元，到 2026 年第二季的 6.8 億美元，目標第四季超過 10 億[[tower-6k-q2-20260804]]。
- 2026 年 5 月公告的 13 億美元 2027 年供貨約，原文是「和它最大的幾家客戶」簽的（複數），預付 2.9 億美元，2028 年承諾更大；另有 50 家以上客戶[[tower-pr-20260513]]。媒體轉述成「最大的一家客戶」（單數）[[36kr-coupe-20260607]]。兩個說法並排，Tower 所有文件都沒有寫客戶名字。
- 第二季法說，Tower 說未來一年規劃了幾個近封裝光學（NPO）的部署；2027 年下半年 NPO 會佔出貨「百分之幾十」；和「非常大的客戶」多代開發通常有雙向獨家，「我們會要求 100% 的份額」[[fool-tower-q2-20260804]]。沒有點名。
- 7 月 14 日日本擴產公告：新井廠改成 300 mm 矽光，2027 年第四季完成；日本 300 mm 產能擴到四倍；Tower 淨投資約 30 億美元、日本政府補助 10 億[[tower-6k-meti-20260714]]。法說說第一階段的產能「已被幾家主要客戶要走、承諾」[[fool-tower-q2-20260804]]。
- **傳聞之前，Tower 在法說上說過什麼。**2026-02：現在的矽光 IC 都由其他模組廠或整合廠設計出貨，Tower 不直接出貨給 NVIDIA；2026-05：NPO、XPO、插拔式到下個十年初仍是主要需求，CPO 才開始有牽引；同一場被問台積電 COUPE 時說「理論上，如果我們的 PIC 比其他都好，台積電沒有理由不買我們的 PIC 給 COUPE」[[allmind-tower-q4-20260211,allmind-tower-q1-20260513]]。這些都在 7 月 12 日的傳聞之前；轉錄稿是 AI 轉寫，說話者標示未必正確。
- Tower 自己公開的 NPO 實例是另一家：9 月 17 日 Tower 和 NewPhotonics 宣布雷射整合的光引擎 PIC 大量出貨，支援 XPO、Open CPX 兩個規格的 NPO 插座，800G 到 1.6T，6.4T 之後量產；新聞稿沒有提 NVIDIA[[tower-6k-newphotonics-20260917]]。XPO、Open CPX 是什麼，見[各種規格](alternatives.md#alt-specs)。

**兩個「慢而寬」不要混。**NVIDIA 在 ECOC 2026 的回顧演講說，NVIDIA 研究單位的 VCSEL 版「慢而寬」概念設計因光纖成本暫停[[stt-ecoc2026-kuchta-20260924]]；傳聞裡的方案 A 是 COUPE 上的微環 DWDM（多個波長共用一根光纖），NVIDIA 研究單位 2026 年還在發表這一條線的論文。之後如果看到「NVIDIA 暫停慢而寬」的標題，要先分清是哪一個。VCSEL 版見[慢而寬：VCSEL、多模光纖](timing.md#tm-wide)。

**如果下一代是 NPO，FAU 會變成什麼樣。**NPO 的光引擎在基板旁邊、可以插拔，FAU 的對位和黏著環境和 COUPE 這種「FAU 接在台積電 3D 堆疊 PIC 上」不同；這些要看[NPO 是什麼、誰在推](alternatives.md#alt-npo)和[各種規格](alternatives.md#alt-specs)。傳聞對 FAU 量的影響，目前沒有任何資料可以算。

接下來能驗證的場合：台積電 10 月 15 日的第三季法說、Tower 的第三季財報（日期還沒公告）、OCP 10 月 14 日 NVIDIA 的演講、NVIDIA GTC Washington D.C.（11/30–12/3），日期見[日曆](calendar.md#cal-events)。

## 新創公司做到哪了？ {#q19}

做光引擎、光互連的新創很多，也募了很多錢，但**目前沒有一家公開具名的量產客戶**，都停在合作、整合，或要先通過驗證的採購單。比較有進展的是被大公司買下。規模的比較基準：Ayar Labs 2026 年募到的 6.5 億美元，約是 NVIDIA 同年 3 月單獨投資 Coherent 一家（20 億美元）的三分之一[[ayarlabs-650m-202609,nvidia-pr-coherent-20260302]]。

| 公司 | 做什麼 | 錢或收購 | 公開的客戶關係 |
|---|---|---|---|
| Ayar Labs | TeraPHY 光學 I/O 小晶片、SuperNova 多波長光源 | 2026 年合計 6.5 億美元，NVIDIA、AMD、聯發科參與[[ayarlabs-650m-202609]] | 與緯穎做機架級 CPO[[ayarlabs-wiwynn-20260311]]；前兩代在格芯做，第三代改用台積電 COUPE[[semianalysis-cpo-book]]；2026 年 6 月加入 NVLink Fusion[[ayarlabs-nvlink-fusion-20260602]]；OCP 議程摘要：和緯穎合作的水冷外部雷射模組 8 通道、每通道 23 dBm，說已確認可上機櫃量產；另有把一個 scale-up 範圍擴到多櫃、最多 1,024 顆 ASIC 的 CPO 網路原型，貢獻給 OCP 的短距光互連工作流[[ocp2026-agenda-20261012]] |
| Lightmatter | Passage 光互連、可拆式 FAU vClick | D 輪 4 億美元（2024）[[lightmatter-pr-list]] | 與創意（GUC）合作生產[[lightmatter-guc-20260126]]；vClick 和 Senko 合作[[lightmatter-vclick-20260311]]；2026 年 6 月加入 NVLink Fusion[[lightmatter-nvlink-fusion-20260602]]；OCP 議程摘要：和 Flex 做開放矽光子 CPO 的測試載具（被動對位、接頭、光路測試），和 Dell 講機櫃托盤要給光學什麼[[ocp2026-agenda-20261012]] |
| Celestial AI | Photonic Fabric 光互連 | Marvell 約 32.5 億美元收購，2026 年 2 月完成[[marvell-celestial-20251202,marvell-celestial-close-20260202]]；Marvell 說的營收數字見 [下面一節](#pl-marvell) | Marvell 給 Amazon 一份認股權證，依 Amazon 買 Photonic Fabric 的量逐步生效[[semianalysis-cpo-book]] |
| Nubis | CPO／NPO 光引擎 | Ciena 2.7 億美元收購，2025 年 10 月完成[[ciena-nubis-8k-20250922,ciena-nubis-8k-20251007]] | Ciena 2026-03 發表 Vesta 206.4T 光引擎（說是第一個高密度、低功耗、開放生態的插拔式 CPO 方案），樣品 2026 年第二季；2026-09 說已從生態系的幾家「錨定客戶」拿到樣品訂單，CPX 營收 2027 年開始、2028 年爬升[[fool-ciena-q1-20260305,fool-ciena-q3-20260909]] |
| Xscale Photonics（Astera Labs 收購） | 光纖與晶片耦合技術 | Astera Labs 2025 年 10 月宣布簽約收購，11 月法說稱要與 Astera 的連接和訊號調理專長結合，做 scale-up 的光學方案；分析師問怎麼補齊完整的 scale-up CPO，執行長說做光方案要三塊（電晶片、光晶片、把光耦合進光纖的封裝技術），收購解決其中兩塊，Astera 也會找第三方的光子方案。轉錄稿拼作 Xscale Photonics，2026-02 稿的詞彙表寫成 XScale，名稱引用前要核對[[allmind-astera-q3-20251104,fool-astera-q4-20260210]]；Astera 也給了 Amazon 一份認股權，依買 Astera 產品的金額分批生效，最多 65 億美元，含 optical engine（轉錄稿的股數以 8-K 為準）[[fool-astera-q4-20260210]] | Astera 沒有點名光學客戶 |
| Dust Photonics（Credo 收購） | 矽光 PIC | Credo 2026 年 5 月底完成，財務長說當季淨流出現金約 7.5 億美元[[fool-credo-q4-20260601]] | Credo 說 Dust 有 800G 和 1.6T 方案、通往 3.2T 的路線圖，架構「大幅減少雷射數量」，CPO 和 NPO 設計案的初期營收預計在 Credo 的 FY28；2026-09 說已認列第一筆矽光 PIC 營收，初期是 800G、1.6T 光收發器[[fool-credo-q4-20260601,fool-credo-fy27q1-20260901]] |
| Polariton（Marvell 收購） | 等離子體（plasmonic）調變器 | Marvell 2026 年 5 月法說稱是「最新的一筆收購」[[fool-marvell-q1-20260527]] | Marvell 說 Polariton 已展示調變器頻寬超過 1 THz，比現行矽光和薄膜鈮酸鋰方案高到 10 倍[[fool-marvell-q1-20260527]] |
| Teramount | 被動對準、可拆的光纖介面 | Molex 2026 年 4 月同意收購、5 月 7 日完成[[molex-teramount-20260415,molex-teramount-close-20260507]] | — |
| POET | 光學中介層 | — | Celestial AI 下的全部採購單被取消：已買下 Celestial AI 的 Marvell 4 月 23 日書面通知，理由是 POET 揭露了採購單和出貨資訊、違反保密義務；POET 4 月 27 日公告[[poet-6k-20260427]]。5 月 14 日和新創 Lumilens 簽供貨協議，首張採購單 5,000 萬美元，五年累計最多 5 億美元，前提是產品開發和認證成功，工程樣品預計 2026 年底[[poet-lumilens-20260514]] |
| NewPhotonics | 雷射整合的光引擎 PIC | — | 2026 年 9 月 17 日和 Tower 宣布 PH18DA 平台的光引擎 PIC 大量出貨，支援 XPO、Open CPX 規格的 NPO 插座；沒寫客戶[[tower-6k-newphotonics-20260917]] |
| Xscape、Scintil | 多波長外部光源 | NVIDIA 都有投資[[xscape-20260311,scintil-20250909]] | 沒有具名客戶 |
| Mixx | 光引擎、光纖接頭、軟體的互連平台 | — | 只有媒體引社群貼文，說 OCP 要推，沒有交易或客戶細節[[tipranks-mixx-ocp2026-202610]] |

### Marvell 說的 scale-up 光學數字，一路改了什麼 {#pl-marvell}

Celestial AI 併進來之後，Marvell 對 scale-up 光學的說法在七個月內換了四次。下表照時間排，都是 Marvell 在法說（轉錄稿）或投資人日（YouTube 自動字幕，未校對、無說話者）上的原話；「FY28」是 Marvell 2027 年 2 月起算的財年。

| 日期 | 說法 |
|---|---|
| 2026-03-05（FY26Q4） | 「我們維持預測：Celestial 的 CPO 營收在 2028 年達到年化 5 億美元，到 2029 年翻倍到年化 10 億美元」。問答：scale-out 的 CPO 部署相對於插拔式收發器會「相對有限」；「明年我們會對一家大客戶出貨 scale-up 的 CPO，之後還在做更多，其餘部署仍以銅為基礎」[[fool-marvell-q4-20260305]] |
| 2026-05-27（FY27Q1） | scale-up 光學明年（FY28）「大幅爬坡」，營收預計是先前展望（約 1.5 億美元，當時只算 Celestial AI）的兩倍以上；問答：scale-up 光學「現在我們實際上算大約 3 億美元，是真正以 NPO 和 CPO 為基礎的方案」。第三代 6.4T 光引擎「與多家 tier 1 客戶深度接洽」，NPO 和 CPO 兩種做法都做[[fool-marvell-q1-20260527]] |
| 2026-08-27（FY27Q2，AI 轉寫稿，說話者標成 Speaker #1） | 「上一季我們把它框成：Celestial AI 的 CPO 光子織網方案，明年約 1.5 億美元」「整體 scale-up 光學，包含它，約 3 億美元，這一類別也包含 NPO」；現在「明年 scale-up 光學機會的規模，比一季前我們想的大很多」，數字沒有給。同一場：CPO 是重要的一塊，但「現在步調快得多的是 NPO」[[allmind-marvell-q2-20260827]] |
| 2026-10-06（投資人日） | 8 月上調 FY28 展望，是由「互連、scale-up 光學、交換器」推動；scale-up 光學「我們今天實際上營收是零，明年起數億美元（multi-hundred million），然後會爬得非常快」；每顆 XPU 的 scale-up 光學內容「在數千美元的量級」；NPO「一定會上量，CPO 仍在進行，不是一個起來另一個就掉下去」；有人說已有客戶在部署共封裝光學（字幕寫成 co-ack）[[youtube-marvell-investor-day-20261006]] |

兩處要分清楚。第一，8 月 FY28 展望上調的 15 億美元（165 億 → 180 億）是整個公司的上調，不是光學一項；法說問答裡的人說上調裡「最有分量的一塊」來自「scale-up of optics switching in other areas」（AI 轉寫稿，標點不清，可讀成 scale-up 光學和 scale-up 交換器兩塊），10 月投資人日也說 8 月那次是互連、scale-up 光學、交換器三者一起推動[[allmind-marvell-q2-20260827,youtube-marvell-investor-day-20261006]]。（原本的筆記寫成「scale-up 光學是 15 億美元裡最有分量的一塊」，對照逐字稿後改成這裡的寫法。）第二，3 月的數字是 Celestial 一項的 2028 年年化營收，5 月以後的 1.5 億、3 億是 FY28 全年的 scale-up 光學營收預期，是不同的口徑，不要接在一起算成長。3 億裡 NPO 和 CPO 各占多少，沒有拆開。

![Lightmatter 的 Passage M1000：一顆封裝的兩條長邊各排 8 個透明的 FAU，每個接一條白色扁平光纖出去，一共 16 條。廠商產品照。[[lightmatter-m1000-page]]](img/vendor/lightmatter-passage-m1000-module3-20261011-03.webp)
![Ayar Labs 的 TeraPHY 光學 I/O 小晶片：大片密密麻麻的小點是接電的凸塊，一端有兩組平行的細溝（圖上沒有標註用途）。它是一顆放在運算晶片旁邊、把電訊號轉成光的小晶片。廠商產品照。[[ayarlabs-teraphy-page]]](img/vendor/ayarlabs-teraphy-optical-io-chiplet-20261011-01.webp)

![新創怎麼想 FAU：一整顆 CPO 封裝切開來看。兩顆運算晶片（130）疊在光的晶片（120）上，最上面是散熱片（160）。光在 PIC 的波導（128）裡走到邊緣，進到貼在側面的耦合器（150），被兩個斜面（151、152）轉向往右射出，經過透鏡（141）進光纖（140）。光纖裝在一個可拆的插頭（142）上，拔下來晶片還在。Lightmatter 的專利圖。[[us20260177761a1]]](img/patents/US20260177761A1-FIG3J.png)

## 整條供應鏈長什麼樣？ {#q20}

把前面講的每一塊串起來就是下面這張圖。從左到右是原料、晶片和零件、封裝和模組、整機組裝、客戶。要先說明一件事：**大部分的買賣關係是不公開的**。圖裡的實線只畫 NVIDIA、Broadcom 或公司自己公開的分工；其他廠商自己說在做某一塊、但沒說賣給誰的，都用虛線。★ 表示出現在 NVIDIA 公布的合作夥伴名單（2025 年 3 月或 2026 年 6 月）。

<div class="scroll">
<svg viewBox="0 0 1300 1125" width="100%" style="min-width:960px" role="img" aria-label="CPO 供應鏈全圖">
<defs><marker id="p3a2" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0,0 L10,5 L0,10 z" class="bar"/></marker><marker id="p3d2" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0,0 L10,5 L0,10 z" class="note"/></marker></defs>
<text class="head" x="20" y="32">原料</text>
<text class="head" x="330" y="32">晶片、零件</text>
<text class="head" x="660" y="32">封裝、模組</text>
<text class="head" x="950" y="32">整機組裝</text>
<text class="head" x="1165" y="32">客戶</text>
<path class="solid" d="M30,70 L80,70" marker-end="url(#p3a2)"/><text class="note" x="92" y="75">公司自己公開的分工</text>
<path class="dash" d="M30,98 L80,98" marker-end="url(#p3d2)"/><text class="note" x="92" y="103">查到在做，沒說賣給誰</text>
<text class="note" x="30" y="131">★ NVIDIA 公布的合作夥伴名單</text>
<text class="note" x="30" y="156">示意圖，非實際比例；路線見下圖</text>
<rect class="box" x="330" y="60" width="300" height="100" rx="4"/>
<text class="head" x="342" y="84">交換器晶片</text>
<text class="item" x="342" y="108">設計：NVIDIA、Broadcom</text>
<text class="item" x="342" y="130">製造：台積電</text>
<text class="note" x="342" y="152">NVIDIA 用 4N，Broadcom TH6 用 N3</text>
<rect class="box" x="20" y="180" width="280" height="120" rx="4"/>
<text class="head" x="32" y="204">SOI 晶圓（PIC 的原料）</text>
<text class="item" x="32" y="228">Soitec（法）、環球晶（台）</text>
<text class="item" x="32" y="250">上海合晶（中，籌組合資）</text>
<text class="note" x="32" y="272">台積電向誰買：未公開</text>
<text class="note" x="32" y="294">信越、SUMCO：查不到說法</text>
<rect class="box" x="330" y="180" width="300" height="140" rx="4"/>
<text class="head" x="342" y="204">光引擎（EIC＋PIC）</text>
<text class="item" x="342" y="228">設計：NVIDIA ★、Broadcom、Marvell</text>
<text class="item" x="342" y="250">製造：台積電 COUPE ★</text>
<text class="note" x="342" y="272">Broadcom Davisson 也用 COUPE</text>
<text class="note" x="342" y="292">Tower、格芯：NPO、插拔式用的 PIC</text>
<text class="note" x="342" y="312">日月光也在準備光引擎封裝</text>
<rect class="box" x="20" y="330" width="280" height="140" rx="4"/>
<text class="head" x="32" y="354">InP 基板、磊晶</text>
<text class="item" x="32" y="378">基板：住友電工、JX 金屬、AXT</text>
<text class="item" x="32" y="400">磊晶：聯亞、全新、IET-KY</text>
<text class="note" x="32" y="422">Coherent、AAOI 自己做磊晶</text>
<text class="note" x="32" y="444">AXT 出貨要中國出口許可</text>
<rect class="box" x="330" y="330" width="300" height="140" rx="4"/>
<text class="head" x="342" y="354">雷射晶片（連續光 CW）</text>
<text class="item" x="342" y="378">Lumentum ★、Coherent ★、住友 ★</text>
<text class="item" x="342" y="400">聯亞、源杰、光迅、光環、AAOI</text>
<text class="item" x="342" y="422">三菱電機、OE Solutions（韓）</text>
<text class="note" x="342" y="444">NVIDIA 3 月各投資 Lumentum、</text>
<text class="note" x="342" y="466">Coherent 20 億美元</text>
<rect class="box" x="20" y="500" width="280" height="170" rx="4"/>
<text class="head" x="32" y="524">FAU 零件</text>
<text class="item" x="32" y="548">V 型槽：炬光、宇瞳、先進光、玉晶光</text>
<text class="item" x="32" y="570">透鏡：奇景、炬光、AGC</text>
<text class="item" x="32" y="592">稜鏡：玉晶光、聯創、宇瞳（送樣）</text>
<text class="item" x="32" y="614">插芯：太辰光、中航光電、揚明光</text>
<text class="note" x="32" y="636">大立光：零件外購，供應商未公開</text>
<rect class="box" x="330" y="500" width="300" height="170" rx="4"/>
<text class="head" x="342" y="524">FAU</text>
<text class="item" x="342" y="548">出貨中：上詮、天孚、太辰光、</text>
<text class="item" x="342" y="570">　中航光電、光庫、仕佳（小批量）</text>
<text class="item" x="342" y="592">開發中：大立光、波若威、合聖、</text>
<text class="item" x="342" y="614">　포스텍（韓）</text>
<text class="note" x="342" y="636">國外：Corning、Senko、Orbray、</text>
<text class="note" x="342" y="656">Coherent、Lightmatter（可拆式）</text>
<rect class="box" x="20" y="700" width="280" height="130" rx="4"/>
<text class="head" x="32" y="724">光纖、預製棒</text>
<text class="item" x="32" y="748">Corning ★、藤倉、住友、古河</text>
<text class="item" x="32" y="770">長飛、亨通、Prysmian</text>
<text class="note" x="32" y="792">預製棒吃緊、光纖漲價</text>
<text class="note" x="32" y="814">（研究機構、媒體的說法）</text>
<rect class="box" x="330" y="700" width="300" height="130" rx="4"/>
<text class="head" x="342" y="724">前面板接頭（MPO、MMC）</text>
<text class="item" x="342" y="748">MMC 設計：US Conec</text>
<text class="item" x="342" y="770">授權生產：Corning、藤倉、住友、</text>
<text class="item" x="342" y="792">　白山、Sanwa、太辰光</text>
<text class="note" x="342" y="814">NVIDIA 用的是哪家做的：未公開</text>
<rect class="box" x="20" y="860" width="280" height="130" rx="4"/>
<text class="head" x="32" y="884">散熱</text>
<text class="item" x="32" y="908">冷卻液：Recochem（NVIDIA 指定）</text>
<text class="item" x="32" y="930">冷板、分歧管：查不到</text>
<text class="note" x="32" y="952">健策：晶片端機構件</text>
<text class="note" x="32" y="974">（只有媒體報導）</text>
<rect class="box" x="330" y="860" width="300" height="130" rx="4"/>
<text class="head" x="342" y="884">封裝載板</text>
<text class="item" x="342" y="908">欣興、AT&amp;S、京東方（驗證中）</text>
<text class="item" x="342" y="930">新光電氣：光引擎上 FCBGA 的簡報</text>
<text class="note" x="342" y="952">三星電機、LG Innotek 測樣品</text>
<text class="note" x="342" y="974">（只有媒體報導）</text>
<rect class="box" x="660" y="60" width="250" height="250" rx="4"/>
<text class="head" x="672" y="84">封裝測試</text>
<text class="item" x="672" y="108">矽品 ★</text>
<text class="note" x="672" y="128">NVIDIA：把電和光的元件</text>
<text class="note" x="672" y="146">組在一起，精度到微米級</text>
<text class="note" x="672" y="170">日月光：年報列「FAU 主動</text>
<text class="note" x="672" y="188">對位封裝」；環旭開發 D-FAU</text>
<text class="note" x="672" y="210">訊芯（鴻海）：說做 FAU 整合</text>
<text class="note" x="672" y="228">Fabrinet＋瑞峰：泰國、美系</text>
<text class="note" x="672" y="246">晶圓廠（待確認）</text>
<text class="note" x="672" y="270">FAU 在哪一步、由誰裝上去：</text>
<text class="note" x="672" y="288">未公開</text>
<rect class="box" x="660" y="330" width="250" height="140" rx="4"/>
<text class="head" x="672" y="354">外部光源模組（ELS）</text>
<text class="item" x="672" y="378">天孚 ★（雷射模組）</text>
<text class="item" x="672" y="400">Lumentum ★、Coherent ★</text>
<text class="item" x="672" y="422">住友 ★、聯鈞、華星光、立碁</text>
<text class="note" x="672" y="444">OE Solutions（韓）：2027 年</text>
<text class="note" x="672" y="466">起（媒體引公司）</text>
<rect class="box" x="660" y="500" width="250" height="170" rx="4"/>
<text class="head" x="672" y="524">光纖組件、整線盒</text>
<text class="item" x="672" y="548">波若威 ★、天孚 ★、Senko ★</text>
<text class="item" x="672" y="570">Corning ★、Coherent ★</text>
<text class="note" x="672" y="592">Corning：預組光纖托盤</text>
<text class="note" x="672" y="612">Coherent：被動光纖組件套件</text>
<text class="note" x="672" y="632">波若威：整線盒 Q3 末出貨</text>
<text class="note" x="672" y="652">還有誰供 NVIDIA：查不到</text>
<rect class="box" x="950" y="60" width="200" height="200" rx="4"/>
<text class="head" x="962" y="84">整台交換器</text>
<text class="item" x="962" y="108">NVIDIA：鴻海 ★、</text>
<text class="item" x="962" y="130">　Fabrinet ★（2025）</text>
<text class="item" x="962" y="152">Broadcom：Micas、</text>
<text class="item" x="962" y="174">　Celestica</text>
<text class="note" x="962" y="198">NVIDIA 自己的 AI 工廠</text>
<text class="note" x="962" y="218">先開機驗證再出貨</text>
<rect class="box" x="1165" y="60" width="120" height="130" rx="4"/>
<text class="head" x="1177" y="84">首批客戶</text>
<text class="item" x="1177" y="108">CoreWeave</text>
<text class="item" x="1177" y="130">Lambda</text>
<text class="item" x="1177" y="152">甲骨文</text>
<text class="note" x="1177" y="174">（Spectrum-X）</text>
<rect class="box" x="20" y="1030" width="1265" height="80" rx="4"/>
<text class="head" x="32" y="1054">設備</text>
<text class="item" x="32" y="1078">對位耦合：高明鐵、萬潤、東佑達＋駿河、光陽、ficonTEC　｜　檢測：均英、致茂、穎崴、FormFactor、旺矽、鴻勁、漢測</text>
<text class="item" x="32" y="1100">雷射加工：大族激光（大立光採購）　｜　多軸平台：PI、Aerotech、MKS</text>
<path class="solid" d="M910,110 L950,110" marker-end="url(#p3a2)"/>
<path class="solid" d="M910,240 L950,240" marker-end="url(#p3a2)"/>
<path class="dash" d="M300,240 L330,240" marker-end="url(#p3d2)"/>
<path class="dash" d="M300,400 L330,400" marker-end="url(#p3d2)"/>
<path class="dash" d="M630,400 L660,400" marker-end="url(#p3d2)"/>
<path class="dash" d="M300,585 L330,585" marker-end="url(#p3d2)"/>
<path class="dash" d="M630,585 L645,585 L645,285 L660,285" marker-end="url(#p3d2)"/>
<path class="dash" d="M300,765 L330,765" marker-end="url(#p3d2)"/>
<path class="dash" d="M630,925 L652,925 L652,270 L660,270" marker-end="url(#p3d2)"/>
<path class="solid" d="M910,180 L950,180" marker-end="url(#p3a2)"/>
<path class="solid" d="M910,400 L922,400 L922,215 L950,215" marker-end="url(#p3a2)"/>
<path class="solid" d="M910,585 L934,585 L934,240 L950,240" marker-end="url(#p3a2)"/>
<path class="dash" d="M630,765 L944,765 L944,252 L950,252" marker-end="url(#p3d2)"/>
<path class="dash" d="M160,990 L160,1013 L1050,1013 L1050,260" marker-end="url(#p3d2)"/>
<path class="solid" d="M1150,125 L1165,125" marker-end="url(#p3a2)"/>
</svg>
</div>

<p class="tag">示意圖，非實際比例。和單篇版本相比，這張圖在封裝測試、光引擎、FAU、整機組裝、設備幾格補了新查到的廠商；各條路線的接法在下一張圖。</p>

上面那張圖把各家擺在零件的位置；公開資料裡「誰接給誰」的線索，分成下面幾條路線。**每一條都只畫公開文件寫了的接法；沒有一份文件把這幾條路線連到「NVIDIA 的 CPO」的，用虛線。**

<div class="scroll">
<svg viewBox="0 0 1270 1122" width="100%" style="min-width:960px" role="img" aria-label="CPO 路線圖">
<defs><marker id="p3a3" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0,0 L10,5 L0,10 z" class="bar"/></marker><marker id="p3d3" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0,0 L10,5 L0,10 z" class="note"/></marker></defs>
<path class="solid" d="M20,22 L70,22" marker-end="url(#p3a3)"/><text class="note" x="82" y="27">公司自己或客戶公開的</text>
<path class="dash" d="M300,22 L350,22" marker-end="url(#p3d3)"/><text class="note" x="362" y="27">查到在做，沒說賣給誰</text>
<text class="head" x="10" y="88">NVIDIA 自己公布的</text>
<rect class="box" x="215" y="50" width="240" height="72" rx="4"/>
<text class="item" x="225" y="78">PIC＋EIC</text>
<text class="note" x="225" y="102">台積電 COUPE</text>
<rect class="box" x="483" y="50" width="240" height="72" rx="4"/>
<text class="item" x="493" y="78">封裝測試</text>
<text class="note" x="493" y="102">矽品（FAU 那一步沒寫）</text>
<path class="solid" d="M457,86 L481,86" marker-end="url(#p3a3)"/>
<rect class="box" x="751" y="50" width="240" height="72" rx="4"/>
<text class="item" x="761" y="78">整機組裝</text>
<text class="note" x="761" y="102">鴻海；Fabrinet（2025）</text>
<path class="solid" d="M725,86 L749,86" marker-end="url(#p3a3)"/>
<rect class="box" x="1019" y="50" width="240" height="72" rx="4"/>
<text class="item" x="1029" y="78">出貨</text>
<text class="note" x="1029" y="102">自家 AI 工廠先驗證</text>
<path class="solid" d="M993,86 L1017,86" marker-end="url(#p3a3)"/>
<text class="note" x="215" y="142">雷射模組：TFC、Lumentum、Coherent、住友；光纖組件：波若威、Corning、Senko、天孚、Coherent</text>
<text class="head" x="10" y="206">未具名紀要說的 FAU</text>
<rect class="box" x="215" y="168" width="240" height="72" rx="4"/>
<text class="item" x="225" y="196">FAU</text>
<text class="note" x="225" y="220">「公司」、天孚（固定式）</text>
<rect class="box" x="483" y="168" width="240" height="72" rx="4"/>
<text class="item" x="493" y="196">可拆式 FAU</text>
<text class="note" x="493" y="220">「公司」、天孚、Senko</text>
<rect class="box" x="751" y="168" width="240" height="72" rx="4"/>
<text class="item" x="761" y="196">樣品測試</text>
<text class="note" x="761" y="220">Fabrinet 泰國、工業富聯</text>
<rect class="box" x="1019" y="168" width="240" height="72" rx="4"/>
<text class="item" x="1029" y="196">光引擎、客戶</text>
<text class="note" x="1029" y="220">紀要沒寫哪一款</text>
<text class="note" x="215" y="260">紀要沒寫「公司」是誰；公開資料裡 Coherent 有多項對得上，沒有任何一方寫出名字</text>
<text class="head" x="10" y="324">天孚與 Fabrinet</text>
<rect class="box" x="215" y="286" width="240" height="72" rx="4"/>
<text class="item" x="225" y="314">天孚（蘇州）</text>
<text class="note" x="225" y="338">泰國廠做 FAU 光纖陣列</text>
<rect class="box" x="483" y="286" width="240" height="72" rx="4"/>
<text class="item" x="493" y="314">Fabrinet（泰國）</text>
<text class="note" x="493" y="338">天孚年報：最大客戶 63.31%</text>
<path class="dash" d="M457,322 L481,322" marker-end="url(#p3d3)"/>
<rect class="box" x="751" y="286" width="240" height="72" rx="4"/>
<text class="item" x="761" y="314">CPO 三家客戶</text>
<text class="note" x="761" y="338">Fabrinet 不說是誰（已出貨）</text>
<path class="dash" d="M725,322 L749,322" marker-end="url(#p3d3)"/>
<rect class="box" x="1019" y="286" width="240" height="72" rx="4"/>
<text class="item" x="1029" y="314">NVIDIA？</text>
<text class="note" x="1029" y="338">一手文件沒有連起來</text>
<path class="dash" d="M993,322 L1017,322" marker-end="url(#p3d3)"/>
<text class="note" x="215" y="378">第一段（天孚賣給 Fabrinet）是天孚年報具名；後兩段沒有任何一方寫</text>
<text class="head" x="10" y="442">Broadcom</text>
<rect class="box" x="215" y="404" width="240" height="72" rx="4"/>
<text class="item" x="225" y="432">光引擎端 FAU、線束</text>
<text class="note" x="225" y="456">Corning（Bailly 合格供應商）</text>
<rect class="box" x="483" y="404" width="240" height="72" rx="4"/>
<text class="item" x="493" y="432">光引擎</text>
<text class="note" x="493" y="456">Bailly：矽品；Davisson：台積電</text>
<path class="solid" d="M457,440 L481,440" marker-end="url(#p3a3)"/>
<rect class="box" x="751" y="404" width="240" height="72" rx="4"/>
<text class="item" x="761" y="432">整機</text>
<text class="note" x="761" y="456">Micas、Celestica</text>
<path class="solid" d="M725,440 L749,440" marker-end="url(#p3a3)"/>
<rect class="box" x="1019" y="404" width="240" height="72" rx="4"/>
<text class="item" x="1029" y="432">測試客戶</text>
<text class="note" x="1029" y="456">Meta 測 Bailly 的可靠度</text>
<path class="solid" d="M993,440 L1017,440" marker-end="url(#p3a3)"/>
<text class="note" x="215" y="496">BFC（Broadcom 的可拆光纖接頭）由誰製造：沒有一方寫</text>
<text class="head" x="10" y="560">美系晶圓廠路線</text>
<rect class="box" x="215" y="522" width="240" height="72" rx="4"/>
<text class="item" x="225" y="550">PIC</text>
<text class="note" x="225" y="574">「美系大廠」（GF、Intel 皆符）</text>
<rect class="box" x="483" y="522" width="240" height="72" rx="4"/>
<text class="item" x="493" y="550">晶圓級凸塊</text>
<text class="note" x="493" y="574">瑞峰（欣銓 24.99%）</text>
<path class="dash" d="M457,558 L481,558" marker-end="url(#p3d3)"/>
<rect class="box" x="751" y="522" width="240" height="72" rx="4"/>
<text class="item" x="761" y="550">光纖貼合</text>
<text class="note" x="761" y="574">Fabrinet（入股瑞峰 13.8%）</text>
<path class="dash" d="M725,558 L749,558" marker-end="url(#p3d3)"/>
<rect class="box" x="1019" y="522" width="240" height="72" rx="4"/>
<text class="item" x="1029" y="550">客戶</text>
<text class="note" x="1029" y="574">沒寫</text>
<path class="dash" d="M993,558 L1017,558" marker-end="url(#p3d3)"/>
<text class="note" x="215" y="614">瑞峰、Fabrinet、GF、Intel 都在美國的認可封測廠名單上；Fabrinet 與 GF 2022 年公開合作被動對位光纖陣列貼合</text>
<text class="head" x="10" y="678">Coherent（公司說）</text>
<rect class="box" x="215" y="640" width="240" height="72" rx="4"/>
<text class="item" x="225" y="668">雷射、ELS</text>
<text class="note" x="225" y="692">德州量產 CW 雷射</text>
<rect class="box" x="483" y="640" width="240" height="72" rx="4"/>
<text class="item" x="493" y="668">隔離器、保偏光纖</text>
<text class="note" x="493" y="692">自己做</text>
<rect class="box" x="751" y="640" width="240" height="72" rx="4"/>
<text class="item" x="761" y="668">FAU</text>
<text class="note" x="761" y="692">OptiAlign、FlexConnect</text>
<rect class="box" x="1019" y="640" width="240" height="72" rx="4"/>
<text class="item" x="1029" y="668">客戶</text>
<text class="note" x="1029" y="692">雷射：「NVIDIA 合作的」</text>
<text class="note" x="215" y="732">FAU 的客戶沒寫；雷射以外 NVIDIA 沒有點名它的 FAU</text>
<text class="head" x="10" y="796">Lumentum、住友</text>
<rect class="box" x="215" y="758" width="240" height="72" rx="4"/>
<text class="item" x="225" y="786">Lumentum</text>
<text class="note" x="225" y="810">CPO 雷射晶片；ELS 模組首張訂單</text>
<rect class="box" x="483" y="758" width="240" height="72" rx="4"/>
<text class="item" x="493" y="786">住友電工</text>
<text class="note" x="493" y="810">NVIDIA 2025 列 ELS 組裝</text>
<rect class="box" x="751" y="758" width="240" height="72" rx="4"/>
<text class="item" x="761" y="786">住友另有</text>
<text class="note" x="761" y="810">MMC 授權、InP 基板</text>
<rect class="box" x="1019" y="758" width="240" height="72" rx="4"/>
<text class="item" x="1029" y="786">客戶</text>
<text class="note" x="1029" y="810">Lumentum 只說「主要 CPO 客戶」</text>
<text class="note" x="215" y="850">Lumentum 的 ELS 模組 2027 下半年交貨；紀要說住友的 400 mW CW 份額非常小</text>
<text class="head" x="10" y="914">日月光集團與其他封測</text>
<rect class="box" x="215" y="876" width="240" height="72" rx="4"/>
<text class="item" x="225" y="904">日月光</text>
<text class="note" x="225" y="928">年報列 FAU 主動對位封裝</text>
<rect class="box" x="483" y="876" width="240" height="72" rx="4"/>
<text class="item" x="493" y="904">環旭（成都光創聯）</text>
<text class="note" x="493" y="928">ELSFP、D-FAU 開發</text>
<rect class="box" x="751" y="876" width="240" height="72" rx="4"/>
<text class="item" x="761" y="904">訊芯（鴻海）</text>
<text class="note" x="761" y="928">說做 FAU 整合、驗證</text>
<rect class="box" x="1019" y="876" width="240" height="72" rx="4"/>
<text class="item" x="1029" y="904">Amkor、長電</text>
<text class="note" x="1029" y="928">Amkor 列 CPO 研發、長電送樣</text>
<text class="note" x="215" y="968">客戶都沒寫；詳見設備、封測筆記</text>
<text class="head" x="10" y="1032">中國廠</text>
<rect class="box" x="215" y="994" width="240" height="72" rx="4"/>
<text class="item" x="225" y="1022">天孚、中航光電、光庫、仕佳</text>
<text class="note" x="225" y="1046">FAU、ELS、保偏光纖</text>
<rect class="box" x="483" y="994" width="240" height="72" rx="4"/>
<text class="item" x="493" y="1022">中際旭創、新易盛</text>
<text class="note" x="493" y="1046">NPO、插拔式光模組</text>
<rect class="box" x="751" y="994" width="240" height="72" rx="4"/>
<text class="item" x="761" y="1022">華為、阿里、騰訊</text>
<text class="note" x="761" y="1046">NPO（華為內建光源）</text>
<text class="note" x="215" y="1086">詳見中國的路線</text>
</svg>
</div>

<p class="tag">示意圖，非實際比例。每一列是一條路線。有箭頭的由左到右是接手的順序，實線是公司自己或客戶公開的，虛線是查到在做、但沒有一份文件寫賣給誰；沒有箭頭的是並列的零件或公司，彼此沒有先後。</p>

**★ 是哪兩份名單。**NVIDIA 2025 年 3 月公布 11 家合作開發 COUPE 製程和系統組裝的夥伴：台積電、矽品、Lumentum、住友電工、Coherent、波若威、Corning、Senko、天孚、鴻海、Fabrinet[[nvidia-pr-20250318,nvidia-blog-20250327]]；其中外部光源的組裝、對位和測試是 Lumentum、住友電工、Coherent，連接雷射和光引擎的保偏光纖、把資料送到前面板的光纖接頭和光纖組件是波若威、Corning、Senko、天孚、Coherent[[nvidia-blog-20250327]]。2026 年 6 月 NVIDIA 宣布 Spectrum-X 光子交換器量產時，點名的是台積電（矽光子製造）、矽品（封測）、「TFC」（雷射模組）、鴻海（整機）[[nvidia-blog-20260601]]。上詮、大立光不在這兩份名單裡。名單是合作開發的夥伴，不是完整的供應商名單。兩份名單的差別、「TFC」是誰，見 [誰實際在供 NVIDIA](#pl-nv)。

圖裡比較少人提、這次查到的幾格，各自的主場在別份筆記，這裡只帶重點：

- **SOI 晶圓。**PIC 做在 SOI 晶圓（矽晶圓上隔一層氧化層、再鋪一層薄矽）上。Soitec 說 FY26（到 2026 年 3 月）光子用 SOI 營收超過 1 億美元，FY27 預估再翻一倍以上，也和多家客戶簽了付訂金的多年期產能保留協議[[soitec-fy26-20260527,soitec-fy27q1-20260722]]。環球晶董事長說矽光子是它光學領域著墨最多的一塊，以 12 吋 SOI 做光波導為主[[gvm-globalwafers-20260902]]；美國密蘇里廠的矽光子產品已小量生產[[technews-globalwafers-20260804]]。上海合晶要成立 SOI 合資公司，應用列了 AI 光互連和矽光子晶片[[10jqka-hejing-soi-20260614]]。台積電的 SOI 向誰買，三家都沒有點名客戶。SOI 是什麼見 [PIC 是怎麼做出來的](inside.md#q8)。
- **光纖整線盒（shuffle）。**交換器機殼裡要把幾千根光纖重新排線，NVIDIA 說 SN6800 用的是整合式光纖整線[[nvidia-blog-20260106]]。波若威說它的光纖接線盒第三季末開始出貨[[ctee-browave-agm-20260617]]；Corning 展示預先組好的光纖托盤[[corning-ir-ofc2026-20260316]]；Coherent 展示整合光纖貼合、微透鏡、托盤的被動光纖組件套件[[coherent-ecoc2026-20260920]]。誰是主力，兩份資料對不上，見 [機內整線盒是誰做](#pl-shuffle)；細節見[機內整線](passive.md#pas-shuffle)。
- **散熱。**三台 CPO 交換器都是液冷。NVIDIA 指定的冷卻液是 Recochem 的 25% 丙二醇溶液，這是手冊裡唯一被點名的外部廠商；冷板、分歧管是誰做的，NVIDIA 沒寫，也查不到公司說法[[nvidia-q3450ld-cooling,nvidia-sn6000-manual-20260916]]。健策供應 CPO 交換器晶片端的機構件（保護插座的零件、防翹曲的補強板），不是冷板，這只有媒體報導[[wantrich-jentech-20260408]]。細節見[怎麼散熱](inside.md#q10b)。
- **韓國。**OE Solutions 做 InP 雷射晶片和外部光源模組，對媒體說 2027 年起以外部光源進入 CPO 市場[[mt-oesolutions-20260508]]；AlphaChips 的關係企業 포스텍（POSTECH，不是那所大學）目標 2027 年量產 CPO 用 FAU，也是媒體引述公司[[financescope-postech-20260910]]；三星電機、LG Innotek 測試 CPO 載板樣品只有媒體報導，公司沒有證實[[trendforce-semco-lg-20260420]]。

圖上每一格在哪一份筆記講：

| 圖上這一格 | 詳細在 |
|---|---|
| 交換器晶片、光引擎、代工廠 | 本篇[誰在主導](#q17)、[代工廠](#q18)、[傳聞](#pl-coupe)；COUPE 的路線見[台積電的 COUPE 往哪裡長](inside.md#inside-coupe) |
| 新創 | 本篇[新創](#q19) |
| InP 基板、雷射晶片、外部光源 | [從銦到外部光源模組](lasers.md#las-layers)、[各國雷射廠商](lasers.md#q21) |
| FAU 和它的零件 | [誰在做 FAU](fau-makers.md#q22)；[為什麼做得了、設備從哪來](fau-makers.md#q24)、[擺在一起比](fau-makers.md#q24b)、[大立光、上詮](fau-makers.md#q25) |
| 可拆式的 FAU 和接頭 | [可拆式誰在做](detachable.md#det-who) |
| 封裝測試、誰把 FAU 裝上去 | [封測廠做不做 FAU 對位](equipment-test.md#eq-osat)、[賣給誰](fau-makers.md#q23)；本篇[誰貼 FAU](#pl-attach) |
| 光纖、前面板接頭、載板 | [光纖和預製棒](passive.md#pas-fiber)、[前面板接頭](passive.md#pas-mmc)、[載板](passive.md#pas-substrate) |
| 設備 | [對位貼合設備](equipment-test.md#eq-align)、[測試分幾段](equipment-test.md#eq-test) |
| 中國廠 | [中國的 FAU 和零件廠](china.md#cn-fau) |
| 專利 | 本篇[專利](#q26b) |

## 誰實際在供 NVIDIA？ {#pl-nv}

NVIDIA 自己公布的供應商，只有前面兩份名單。下面這張表把「誰被點名做哪一件事」全部排在一起，右欄寫是誰這樣說的，讓你感覺到每一格可信到哪裡：NVIDIA 自己寫的最可靠，公司對投資人自己說的次之，分析師、媒體、未具名的紀要依序更弱。

<div class="scroll">

| 零件或工序 | 被點名的 | 這樣說的是誰 |
|---|---|---|
| 光引擎（PIC 加 EIC，COUPE） | 台積電 | NVIDIA 自己寫（2025 年 3 月、2026 年 6 月）[[nvidia-blog-20250327,nvidia-blog-20260601]] |
| CPO 多晶片模組的封裝、測試；把電和光的元件以微米級精度組在一起 | 矽品 | NVIDIA 自己寫（同上）。兩篇都沒有寫 FAU |
| 外部光源的組裝、光學對位、和矽光子引擎一起測試 | Lumentum、住友電工、Coherent | NVIDIA 自己寫（2025 年 3 月）[[nvidia-blog-20250327]] |
| 雷射晶粒封成雷射模組 | 「TFC」 | NVIDIA 自己寫（2026 年 6 月，列在台灣生態系的段落）[[nvidia-blog-20260601]] |
| CPO 用的超高功率連續光雷射 | Coherent：德州廠量產，說「包含和 NVIDIA 合作的那些」，12 月季起有營收 | 公司自己說[[futurum-coherent-q4fy26-20261009,webull-coherent-q4fy26-20260812]] |
| 同上 | Lumentum：「主要的 CPO 客戶」，scale-out 已在出貨，沒點名客戶 | 公司自己說[[investing-lumentum-q4fy26-20260811]] |
| 雷射通過 NVIDIA 認證 | Lumentum 已通過，Coherent 是下一個 | 一位產業分析師[[supercomputing-cpo-laser-202609]] |
| 400 mW 連續光雷射（外部光源模組用） | 「公司」、Lumentum；住友的份額很小 | 未具名的調研紀要[[eastmoney-dfau-survey-20260531]] |
| 外部光源模組（ELSFP）封裝 | 「公司」自產自封；天孚、中際旭創、新易盛用 Lumentum 的雷射封 | 未具名紀要（同上） |
| CPO 配套的 FAU、外部光源 | 天孚「穩定量產交付」，沒寫客戶 | 公司自己說[[cninfo-tfc-irm-20261009,cninfo-tfc-irm-20260709]] |
| 固定式 FAU（18 通道） | 「公司」、天孚；上詮有相關業務、和台積電合作 | 未具名紀要 |
| 可拆式 FAU（DFAU，36 埠） | 「公司」、天孚、Senko；上詮、波若威、Corning 計畫加入 | 未具名紀要 |
| 可拆的 PIC 接頭（Spectrum-X、Quantum-X） | Senko | Senko 自己說（2025 年 3 月）[[senko-nvidia-ecosystem-20250318]]；2026 年 Senko 沒有新的 NVIDIA 相關新聞稿 |
| 光纖接頭、光纖組件（外部光源到光引擎的保偏光纖、光引擎到前面板） | 波若威、Corning、Senko、天孚、Coherent | NVIDIA 自己寫（2025 年 3 月）[[nvidia-blog-20250327]] |
| 系統級 CPO 組裝測試、把 CPO 組件裝進機殼 | 鴻海、Fabrinet（2025 年 3 月）；Spectrum-X 整機只列鴻海（2026 年 6 月） | NVIDIA 自己寫（同上） |
| 機內整線盒 | 波若威（外資估約 50% 份額、第四季放量） | 媒體引外資[[udn-browave-foreign-20260818]]；另一份專家紀要點名太辰光、Corning、訊芯，沒提波若威[[cnyes-hao-expert-spectrum-20260930]] |
| MMC 接頭 | US Conec 設計；Corning、藤倉、住友取得授權；太辰光「在 US Conec 的供應支持下」批量產銷 | 聯合新聞稿[[usconec-prizm-20260311]]；太辰光回覆投資人[[stockstar-tfc-sunsea-mmc-20260731]] |
| 保偏光纖 | 紀要中「公司」的供應商：Corning、長飛等三家 | 未具名紀要 |
| DFAU 的 V 槽和光纖部件 | 蘅東光、光庫（賣給「公司」） | 未具名紀要 |
| DFAU 樣品測試 | Fabrinet 泰國廠；工業富聯台灣廠少量 | 未具名紀要 |
| **NVIDIA 光引擎上的 FAU 貼合** | **沒有任何一方寫** | 見[誰貼 FAU](#pl-attach) |

</div>

這張表裡，凡是「未具名紀要」的格子，都出自同一份 2026 年 5 月底刊在財經平台的機構調研紀要，受訪者沒有寫名字；沒有第二個來源可以對。

### NVIDIA 兩份名單不一樣 {#pl-lists}

2025 年 3 月的名單有 11 家，其中 Fabrinet 負責系統級 CPO 的組裝和測試，以及把 CPO 組件和子組件裝進交換器機殼，Lumentum、住友電工、Coherent 負責外部光源，波若威、Corning、Senko、天孚、Coherent 負責光纖接頭和光纖組件[[nvidia-blog-20250327]]。2026 年 6 月 Spectrum-X 量產那篇只列台積電、矽品、「TFC」、鴻海四家，沒有 Fabrinet、Lumentum、住友電工、Coherent、Senko、Corning、波若威[[nvidia-blog-20260601]]。那篇的標題是台灣的半導體和系統生態系，所以不能從這裡推誰退出。但「NVIDIA 公布的供應商名單」不是固定的一份。

另一個對不上的地方在 Lumentum：NVIDIA 2025 年 3 月寫它做外部光源的組裝、對位、測試；Lumentum 2026 年 8 月說的是剛拿到第一張外部光源模組的訂單，交貨在 2027 年下半年[[nvidia-blog-20250327,investing-lumentum-q4fy26-20260811]]。兩邊講的「外部光源」範圍可能不同（雷射晶片和整個模組），但照字面對不上；細節見[從銦到外部光源模組](lasers.md#las-layers)。

### 「TFC」是誰 {#pl-tfc}

NVIDIA 2026 年 6 月的原文是：「與台灣的半導體和系統生態系深度共同工程，包括台積電、矽品、TFC 和鴻海」，以及「TFC 的雷射晶粒被封裝成雷射模組，並驗證 24 小時全年無休的 AI 工作負載所需的可靠度」[[nvidia-blog-20260601]]。10 月 12 日重抓頁面，字句沒有改。同一篇另一則短文裡的「TFC」是黃仁勳說的台灣炸雞，和這段無關。

照「描述逐項對照、一項對不上就不配對」的規則，拿蘇州的天孚（TFC Communication）來對：

| 對照項 | NVIDIA 寫的 | 天孚 | 結果 |
|---|---|---|---|
| 名字 | TFC | NVIDIA 2025 年 3 月把「TFC Communication」列在光纖接頭、光纖組件[[nvidia-blog-20250327]] | 對得上 |
| 做的事 | 把雷射晶粒封成雷射模組 | 港股申請版本寫以外部光源多通道高功率雷射模組為核心產品[[hkex-tfc-application-20260410]] | 對得上 |
| 進度 | Spectrum-X 全面量產 | 天孚說 CPO 配套的 FAU、外部光源穩定量產交付[[cninfo-tfc-irm-20261009]] | 對得上 |
| 「台灣」 | 列在台灣生態系 | 總部蘇州，廠在中國和泰國；申請版本裡的「台灣」只出現在一位台灣籍的執行董事和兩家台灣供應商[[hkex-tfc-application-20260410]] | 對不上 |

對得上 3 項、對不上 1 項（對照）。台灣證交所、櫃買中心登記的英文簡稱是 TFC 的上市、上櫃、興櫃公司只有 3 家：台肥、環泰、大同精化，分別是化學工業、食品工業、化學工業，都不做雷射；未上市的台灣公司沒有查[[twse-tpex-abbrev-tfc-20261012]]。**沒有任何一方寫明這個 TFC 是誰。**這段常被讀成「台灣供應鏈全包」，原文不支持這種讀法。

### 那份未具名的調研紀要，和裡面的「公司」 {#pl-memo}

紀要是 2026 年 5 月底刊在財經平台的機構調研紀要，受訪的是一家沒有寫名字、自稱「公司」的企業[[eastmoney-dfau-survey-20260531]]。它對 NVIDIA 交換器的 FAU 分配是這樣說的：固定式 FAU 主要是「公司」和天孚；可拆式 FAU 是「公司」、天孚、Senko；上詮「也有相關業務」，可拆式的合作「似乎並不順利」；NVIDIA 2026 年在台灣扶持了其他供應商。這是目前唯一講到 NVIDIA 交換器 FAU 供應商分配的資料，而它的等級是未具名紀要。

「公司」是誰？沒有任何一方寫明。把紀要對「公司」的描述，和 Coherent 的公開資料逐條對照（只列事實，不下結論）：

| 紀要怎麼說「公司」 | Coherent 的公開資料 | 對得上嗎 |
|---|---|---|
| NVIDIA 對「公司」和 Lumentum 各投資 20 億美元，用來擴 400 mW 連續光雷射產能 | 2026 年 3 月 2 日 NVIDIA 以每股 256.80 美元買進 Coherent 普通股，共 20 億美元；同日以 20 億美元買 Lumentum 特別股。協議含數十億美元採購承諾和先進雷射的取得與產能權；康寧是認股權證，不是 20 億美元[[sec-coherent-10k-20260814,sec-lumentum-10k-20260817,nvidia-pr-coherent-20260302]] | 對得上 |
| 自產法拉第晶體、自己做隔離器 | Coherent 說 CPO 的內容包含雷射、外部光源、隔離器、保偏光纖、整套光纖貼合組件、矽光 PIC[[webull-coherent-q4fy26-20260812]] | 對得上 |
| 自己做連續光雷射，從雷射到封裝全流程做 ELSFP，不單獨外賣 | Coherent 德州廠量產 CPO 用超高功率雷射，「包含和 NVIDIA 合作的那些」，12 月季起有營收[[futurum-coherent-q4fy26-20261009]] | 對得上 |
| 可拆式 FAU「整個光路無膠化」，全用玻璃件 | Coherent 的可拆 FAU 接頭 FlexConnect「光路不用膠、撐得住高功率雷射」[[coherent-ecoc2026-20260920]] | 對得上 |
| V 槽和光纖等前道部件外購（蘅東光、光庫），自己做透鏡和最終組裝 | 蘅東光 2025 年報：第二大客戶是 Coherent，2.77 億元人民幣、12.52%[[cninfo-hdg-ar2025-20260424]]。但 Coherent 的 OptiAlign FAU 寫用「自己開發的 V 槽」[[coherent-ecoc2026-20260920]] | 一半對得上；V 槽外購還是自製，兩邊說法不一樣 |
| 光開關（OCS）樣品用液晶方案 | Coherent 的 OCS 產品線以數位液晶技術為基礎[[sec-coherent-10k-20260814]] | 對得上 |
| 「先進光學事業部」年銷售約 2 億美元 | Coherent 的報告分部只有兩個，沒有這個事業部 | 查不到 |
| 2027 年外部光源模組指引從約 200 萬顆上修到 500 萬顆、約 40% 份額 | Coherent 沒有公布顆數 | 不能對 |

對得上 5 項、一半對得上 1 項、查不到或不能對 2 項（對照，沒有一項明確對不上）。另有一條旁證：天孚港股申請版本的第四大客戶「C」描述是在紐約證交所上市、做雷射、工程材料、光電元件，同時是天孚的供應商；上市地、業務用詞對得上 Coherent，Lumentum 在 Nasdaq，對不上上市地[[hkex-tfc-application-20260410,sec-lumentum-10k-20260817]]。**兩個都只是對照，沒有任何文件寫出名字。**

紀要有一句話，和 NVIDIA 公開資料不一致：另一份 2026 年 9 月底的專家調研說「客戶後續設計砍掉外接光源方案」，但 NVIDIA 所有公開資料裡，外部光源都是 Spectrum-X、Quantum-X 的一部分[[cnyes-hao-expert-spectrum-20260930]]。不知道它講的是哪一款產品。外部光源為什麼放在外面，見[雷射為什麼在外面](inside.md#q10)。

紀要裡 FAU 的通道數、單價，和固定式、可拆式分別對應哪一款交換器，見[固定式和可拆式](fau.md#fau-types)和[FAU 值多少錢](fau-makers.md#fau-value)。

### Fabrinet 做什麼？天孚和 Fabrinet 的關係 {#pl-fabrinet}

**Fabrinet 自己說的。**NVIDIA 2025 年 3 月把它列在系統級 CPO 組裝和測試；2026 年 6 月的名單沒有它[[nvidia-blog-20250327,nvidia-blog-20260601]]。Fabrinet 2026 財年（到 2026 年 6 月底）的年報寫 NVIDIA 佔營收 16.3%（前一年 27.6%、再前一年 35.1%），Cisco 19.9%、Nokia 10.7%、Amazon 10.5%；年報全文沒有出現 co-packaged 或 CPO 的字眼[[sec-fabrinet-10k-20260818]]。媒體換算 NVIDIA 對 Fabrinet 的 2026 財年營收約 7.5 億美元[[opticsorg-fabrinet-q4-20260818]]。三場法說的說法（法說會轉錄稿）：2026 年 2 月，執行長說「已經看到一些 CPO 營收，雖然金額目前相對很小」，在做三家不同客戶的共封裝光學專案，「不只一家客戶」，營收什麼時候變得重要取決於客戶的時程表[[fool-fabrinet-fy26q2-20260202]]。5 月，分析師問三個專案是不是現在都有營收、是 scale-out 還是 scale-up，財務長答「We are shipping to all three customers」（三家客戶都在出貨），執行長補「兩種都有」，並說「我們對 CPO 很興奮，但營收到目前為止大部分還在前面」；工作內容包括光學元件、外部光源插拔模組、其他整合式精密光學封裝，客戶的時程他們「不代客戶講」；被問機內大量的光纖貼合和 FAU 是不是機會，沒有直接回答 FAU，只說可以在食物鏈上爬得比以前高[[fool-fabrinet-q3-20260504,earningswhispers-fabrinet-fy26q3-20260504]]。8 月，執行長說「現在跟少數幾家客戶做 CPO，已經在做元件（devices），但還沒到全量」，NPO「從我們在客戶那裡看到的，大概是比 CPO 更近期的機會」，NPO 往 6.4T、12.8T 走，製造的複雜度和良率「變得關鍵」；被問 NVIDIA 1.6T 時程，答「要問 NVIDIA」[[allmind-fabrinet-q4-20260817,webull-fabrinet-q4-20260817]]。**所以「三家都已出貨」要帶日期**：2 月的原話只有「少量營收、三家客戶的專案」，三家都在出貨是 5 月財務長的一句回答；其他場合都是營收「大部分還在前面」「還沒到全量」。Fabrinet 沒有說三家客戶是誰、出貨的東西是什麼、金額多大，也沒有說它組不組 FAU。

**Fabrinet 入股瑞峰。**Fabrinet 2026 年 3 月 25 日簽約，以約 10.2 億元新台幣（3,240 萬美元）取得台灣興櫃公司瑞峰半導體（7873）13.8% 的股權；執行長說瑞峰是「先進晶圓級封裝」夥伴、「已有不少共同客戶」，8 月說瑞峰「會在我們的泰國園區加產能」[[sec-fabrinet-10k-20260818,earningswhispers-fabrinet-fy26q3-20260504,webull-fabrinet-q4-20260817]]。瑞峰自己的年報寫：2026 年 4 月私募 2,000 萬股、每股 51 元（計算：20,000,000 × 51 ＝ 10.2 億元，和 Fabrinet 的數字相同），5 月 18 日 Fabrinet 持股 13.35%、是第二大股東；轉投資欄寫「無此情形」，也就是到年報刊印時沒有揭露泰國子公司[[mops-raytek-ar2025-20260618]]。13.8% 和 13.35% 兩個口徑沒有解釋。

瑞峰是 2016 年成立的晶圓級封裝廠，做線路重佈、銅柱凸塊；它自己寫 2024 年 6 月開發完成「有 V 形光導溝槽的側面導光型矽光子晶片」的晶圓級封裝製程，並說在這類矽光子晶片上是唯一供應商，搭配的是一家代稱「美系半導體製造大廠」的夥伴和一家光收發器製造商，組成 CPO 聯盟[[mops-raytek-ar2025-20260618]]。也就是說，瑞峰在 CPO 做的是矽光晶片的晶圓級凸塊和焊墊，不是 FAU、不是光纖貼合。2025 年營收 10.53 億元，CPO 營收沒有單獨揭露，美洲營收 0.94 億元，約 8.9%（計算）。那家「美系大廠」是不是格芯：格芯對得上 4 項、無法對 1 項，Intel 對得上 3 項、無法對 1 項、1 項沒查，也有 V 槽專利和論文，同樣描述對得上不只一家，**不配對**[[gf-fabrinet-fiber-attach-20221110,gf-corning-glassbridge-20250929]]。能寫的是：美國商務部公布的認可封測廠名單上，同時有瑞峰、Fabrinet、格芯、Intel、Amkor、日月光、台積電；格芯和 Fabrinet 2022 年就公開合作過被動對位的光纖陣列貼合[[ecfr-bis-osat-20260924,gf-fabrinet-fiber-attach-20221110]]。

**天孚和 Fabrinet。**天孚 2025 年報前五大客戶第 1 名具名是 Fabrinet，32.69 億元人民幣，佔年度銷售 63.31%，前五大合計 89.73%[[cninfo-tfc-ar2025-20260408]]；港股申請版本寫同一位「客戶 A」金額相同、比例 63.9%（2023、2024 年 54.0%、62.2%），業務關係始於 2018 年；兩份文件的分母不同，原因沒寫[[hkex-tfc-application-20260410]]。天孚的泰國子公司「生產電子及光電子元件，即 FAU 光纖陣列、線纜及光引擎」，2025 年開始運營[[hkex-tfc-application-20260410]]；天孚 2026 年 7 月說泰國 A 棟 2024 年通過客戶驗證、無源產品投產，B 棟 2025 年交付、有源產品通過客戶驗證，CPO 配套的 FAU「已設計定型，處於訂單交付狀態」，沒有寫 CPO 用的 FAU 在中國還是泰國做[[cninfo-tfc-irm-20260709]]。紀要說可拆式 FAU 的樣品「最終會發往 Fabrinet 在泰國的工廠」[[eastmoney-dfau-survey-20260531]]。

**第一手文件沒有一份把「天孚賣給 Fabrinet 的東西」和「NVIDIA 的 CPO」連在一起：**天孚年報只寫 Fabrinet 的金額，Fabrinet 不揭露供應商，NVIDIA 只把天孚（TFC）列在接頭、光纖組件和雷射模組兩格。所以公開資料裡，在「台廠 FAU 經台積電 COUPE 供 NVIDIA」之外，多了一條「天孚賣給 Fabrinet」的線；賣的是什麼、最後接到哪個客戶，都沒有寫。天孚港股申請版本的客戶 B（美國、Nasdaq、無晶圓廠、2018 年起往來）是 NVIDIA 還是 Marvell：描述同時對得上不只一家，不配對；2017 到 2020 年的前五大客戶地區表也分不出來[[hkex-tfc-application-20260410,cninfo-tfc-2020-reply-20200911]]。

### 光引擎上的 FAU 是誰貼的？ {#pl-attach}

NVIDIA 寫矽品負責封裝測試、把電和光的元件以微米級精度組在一起，沒有寫 FAU[[nvidia-blog-20250327,nvidia-blog-20260601]]；說 Spectrum-X 的光纖「在最後一步由精密機台全自動接上」，沒寫在哪家廠[[nvidia-blog-20260106]]。公開文件裡有人講「這一步在我的流程裡」的：

- **日月光**：2024 和 2025 年報都列「FAU 光學主動式對位封裝」為已開發成功的技術，2024 年報還列「V 槽 PIC 光學被動式對位封裝」；2025 年的部落格流程圖把「光纖貼合、透鏡貼合」畫在自己的流程裡[[mops-ase-ar2024-20250625,mops-ase-ar2025-20260624,ase-blog-cpo-20250106]]。年報是集團合併的技術清單，沒有寫是哪個子公司、替哪個客戶。2026 年 7 月 30 日法說，說話的是營運長吳田玉（Dr. Tien Wu），不是董事長：他說年底前後 CPO 會開始上線、「一開始可能是小量」，會有頻寬、系統效能、散熱的關鍵基準資料；被分析師問集團在 CPO 要做什麼服務和 EMS 事業的連結，答「CPO 我想等兩季再給更多細節，CPO 服務、營收、2027 年展望，我想多一點時間再談」，並說「兩季後」應該就能談[[ase-ir-q2-20260730,ew-ase-q2-20260730]]。從 7 月 30 日起算，「兩季後」是第四季結果的法說（約 2027 年 2 月），不是約 10 月底的第三季法說。（原本寫成「董事長說…要再等兩季」，對照官方逐字稿後更正說話者和時點。）
- **矽品**：專利把 FAU 當成封裝結構的一部分，有一件設計成「先封膠、後接 FAU」，說是為了簡化 CPO 製程；專利只代表設計，不代表量產，也沒有寫 FAU 由誰製造[[us20260047486a1,us20260186216a1]]。
- **訊芯（鴻海集團）**：2026 年 6 月股東會說正與台積電合作 COUPE，「主要負責後段包括 FAU、光柵耦合等技術整合與驗證」，102.4T 的 CPO 樣品已出貨給客戶、51.2T 小量生產[[cnyes-shunsin-agm-20260626]]。
- **台積電**：自己有多件 FAU 貼到 PIC 的專利，沒有公開說誰在量產線上貼。
- **設備端**：萬潤的自動光耦合機簡報寫適用 COUPE（晶粒或封裝層級）、貼合種類含 FAU；台積電是萬潤的客戶，萬潤人員進台積電廠裝機維修；日月光投控 2024 到 2026 年向萬潤公告的設備訂單，公告沒寫機台種類[[mops-allring-h1-slides-20260827,mops-allring-ar2025-20260626]]。

**到 10 月 12 日，日月光、矽品、台積電、NVIDIA 都沒有一手說法講明「NVIDIA COUPE 光引擎的 FAU 在誰的廠貼」。**詳細的設備、公告和對照，見 [封測廠做不做 FAU 對位](equipment-test.md#eq-osat)和[對位貼合設備](equipment-test.md#eq-align)。

### 機內整線盒是誰做？ {#pl-shuffle}

兩份說法並排，對不上：外資說波若威是 CPO 整線盒的重要供應商、約 50% 份額、第四季放量[[udn-browave-foreign-20260818]]；3 月有媒體寫「供應鏈透露」波若威負責 NVIDIA CPO 的整線盒，驗證完成、今年量產[[ctee-browave-shufflebox-20260309]]。9 月 30 日的專家調研點名的是太辰光、Corning（規格相近）和訊芯（因最終產品在富士康整合「可能參與部分工作」、份額不高），沒有提波若威[[cnyes-hao-expert-spectrum-20260930]]。訊芯自己 2025、2026 年的說法談的是 FAU 和 CPO 封測，沒有提整線盒或 MMC[[cnyes-shunsin-agm-20260626]]。MMC 接頭：太辰光說批量出貨，被問到是轉售 Corning 還是直供 NVIDIA 的供應鏈，答「供應鏈信息屬於商業秘密」[[stockstar-tfc-sunsea-mmc-20260731]]；Corning 對投資人說 CPO 把光學帶進機殼內，機殼內原本沒有的部分都是「潛在的」Corning 內容[[bullfincher-corning-q2-20260728]]。細節見[機內整線](passive.md#pas-shuffle)和[前面板接頭](passive.md#pas-mmc)。

### 台廠 FAU 廠的最大客戶 {#pl-foci-customer}

上詮 2025 年營收的 70.16% 來自一家只寫代號「C 公司」的客戶，年報、公開說明書、法說簡報都沒有寫名字；照同一套對照規則，C 公司對 Corning 對得上 5 項、對不上 0 項、無法對 3 項，其中最硬的一項是美國海運艙單上，上詮台灣、中山上詮的具名美國進口人全部是 Corning 的實體[[foci-ar2025,importgenius-foci-20261012]]。這是對照，不是公司說的，細節和上詮其他的事見 [大立光、上詮各走到哪](fau-makers.md#q25)。上詮自己的一手文件（年報、公開說明書、財報、重訊）全文沒有出現「台積電」「COUPE」；簡報裡畫了「ReLFACon Packaging on PIC/COUPE」，引用台積電的圖；台積電的 3DFabric 聯盟成員名單沒有光學類、沒有上詮；上詮在美國專利局的 34 筆文件，全部只有上詮一個申請人，沒有共同申請人，也沒有台積電[[mops-foci-slides-20260902,tsmc-3dfabric-alliance-20261012]]。「合作至少三年」是媒體寫「業界指出」[[udn-foci-tsmc-20260423]]；董事長 8 月說公司與客戶均簽有保密協議，不便評論個別合作[[bnext-foci-20260814]]。

## OCP 2026 會前公開了什麼 {#pl-ocp}

OCP Global Summit 2026 的日期是 10 月 12 日到 15 日（聖荷西）；查詢當下是美西 10 月 11 日晚上，大會還沒開幕，所以**手上只有會前的新聞稿、講者提交的議程摘要和媒體預告，沒有任何一場已經講完**。時間一律是美西時間，台灣時間是它加 15 小時（例如 10/14 09:15 美西是 10/15 00:15 台灣）。議程摘要是講者自己寫的，等級是公司自己說。

會前沒有任何一則新產品發表；各家新聞稿都是「將展出」。和供應鏈有關的：

| 誰 | 會前公開的 |
|---|---|
| Broadcom | 展 Tomahawk 6 和「第三代 TH6-Davisson CPO」；Davisson 實機在 Celestica、台達、Micas 三個攤位。Davisson 是 2025 年 10 月就發表的產品，所以這是整機廠的展示，不是新晶片。台達自己的新聞稿寫攤位在另一個位置、內容只有電源和液冷，沒提 CPO[[broadcom-ocp-pr-20261008,delta-ocp-pr-202610]]。OCP 執行長在 Broadcom 新聞稿的引言裡提到 Broadcom 的貢獻包含「新的寬型 CPO」，本文沒有解釋[[broadcom-ocp-pr-20261008]] |
| NVIDIA | 10/14 09:15 網路主管演講的摘要列：首顆用新的微環調變器做的 1.6T CPO 晶片、3D 堆疊矽光引擎、高功率雷射、可拆式光纖接頭；說 CPO 交換器正進入量產，並說這場會「更詳細地回顧它的製造流程」。另有一場 10/13 光學演講（摘要空白）[[ocp2026-agenda-20261012]] |
| Meta | 10/14 08:00 講 51.2T CPO 驗證到 102.4T 整合光學交換器：64 個光埠、16 個四埠 MMC 介面、16 個外部雷射模組讓雷射壽命和晶片脫鉤，光學耗電比插拔式約少 60%、系統耗電約少 30%；接頭數量和 NVIDIA SN6810 的 128 個 MMC-16 數量級不同，用 NVIDIA 一台推算接頭用量不一定適用[[ocp2026-agenda-20261012,nvidia-sn6000-manual-20260916]] |
| Credo | 展和 Senko 合作的 micro-emitter 盲插光學背板，頻寬最多是最新銅背板的 10 倍；這是 NPO 光學背板，不是 Credo 的 ALC 光纜產品；ALC 的光學次組件誰做仍未公開[[credo-ocp-pr-20261009]] |
| 啟碁 | 展三台 102.4T 的 1.6TbE 交換器，其中一台是 NPO 交換器，用 Open CPX 規格的 6.4T 光引擎；另展全光交換器（OCS）[[cnyes-gigabyte-ocp-20261007]] |
| 貿聯 | 展 CPO、XPO 互連，整合 FAU、MMC 多芯接頭、光纖整線、光纖分支[[ltn-bizlink-ocp2026-20261008]] |
| Ayar Labs 和緯穎 | 水冷外部雷射模組；多櫃 CPO scale-up 原型，貢獻給 OCP 的短距光互連工作流[[ocp2026-agenda-20261012]] |
| 華為 | 10/14 講 Open NPO 標準：6.4T、單通道 200 Gb/s、內建光源；之後要做多廠互通和可靠度測試，商用部署 2026 到 2027 年[[ocp2026-agenda-20261012]] |
| Samtec | 10/14 講 Meta、Ciena、Marvell、TeraHop、Coherent、Samtec 的聯合 CPO 方案，訴求可在現場更換[[ocp2026-agenda-20261012]] |
| Corning | 10/14 講以透鏡為基礎的擴束式超小外形接頭，用在前面板和背板[[ocp2026-agenda-20261012]] |

10/13 下午另有一整段 NPO 研討會（14 場，Meta、微軟、Oracle、阿里、華為、NVIDIA、Lumentum 都有人講）；XPO、Open CPX 相關的場次有鴻海集團的連接器廠、微軟和 Arista、Ciena、TeraHop、Celestica 等[[ocp2026-agenda-20261012]]。這些規格是什麼，見[各種規格](alternatives.md#alt-specs)。

**台廠出現的位置。**在議程光學相關的場次裡，台廠出現的是系統廠和連接器廠：緯穎、鴻海集團的連接器廠、啟碁、貿聯，廣達、英業達、鴻海 Ingrasys、智邦各有一場但摘要沒提光學。議程 621 場的講者公司欄裡，沒有大立光、上詮、波若威、光聖、台積電（計算：全文搜尋）。這不代表它們不在供應鏈裡，只是 OCP 不是它們公開的場合。10 月 11 日有一篇媒體前瞻稿重述了兩則台廠說法，都不是 OCP 現場：鴻海說今年開始出貨 CPO 交換器、會達到 1 萬台的水準、明年數倍成長；大立光說 FAU 已過客戶認證、10 月洽談產能規劃和合作細節、2027 年中量產[[udn-ocp-preview-20261011]]。鴻海 1 萬台和另一份報告引用的「5 萬台」對不上，見[誰在做 FAU](fau-makers.md#fau-value)。

大會講完之後才能補的場次，見[每場要看什麼](calendar.md#cal-watch)。

## FAU 的技術握在誰手上？從專利看 {#q26b}

專利是另一個看「誰握有技術」的角度。下面是這批收集到的專利：美國專利商標局 2026 年 1 月 1 日到 10 月 8 日公開或公告、跟光纖耦合、光引擎、CPO 有關的案子，共 88 件[[uspto-2026-collection]]。**這只是這一批收到的，不是完整檢索**：只查了美國案，台灣、中國的案子沒有拿到（查詢網站擋住自動查詢）；每家公司 2026 年以前的專利也不在裡面。件數只看得出誰在這段時間公開了比較多相關申請，不能拿來排名。

<figure>
<div class="scroll">
<svg viewBox="0 0 1000 380" width="100%" style="min-width:640px" role="img" aria-label="各申請人專利件數">
<text class="item" x="205" y="30" text-anchor="end">台積電</text>
<rect class="bar" x="215" y="17" width="570" height="18"/>
<text class="note" x="791" y="31">19</text>
<text class="item" x="205" y="60" text-anchor="end">Lightmatter</text>
<rect class="bar2" x="215" y="47" width="360" height="18"/>
<text class="note" x="581" y="61">12</text>
<text class="item" x="205" y="90" text-anchor="end">NVIDIA（含 Mellanox）</text>
<rect class="bar2" x="215" y="77" width="300" height="18"/>
<text class="note" x="521" y="91">10</text>
<text class="item" x="205" y="120" text-anchor="end">矽品</text>
<rect class="bar" x="215" y="107" width="270" height="18"/>
<text class="note" x="491" y="121">9</text>
<text class="item" x="205" y="150" text-anchor="end">上詮</text>
<rect class="bar" x="215" y="137" width="210" height="18"/>
<text class="note" x="431" y="151">7</text>
<text class="item" x="205" y="180" text-anchor="end">Corning</text>
<rect class="bar2" x="215" y="167" width="150" height="18"/>
<text class="note" x="371" y="181">5</text>
<text class="item" x="205" y="210" text-anchor="end">Ayar Labs</text>
<rect class="bar2" x="215" y="197" width="150" height="18"/>
<text class="note" x="371" y="211">5</text>
<text class="item" x="205" y="240" text-anchor="end">萬潤</text>
<rect class="bar" x="215" y="227" width="90" height="18"/>
<text class="note" x="311" y="241">3</text>
<text class="item" x="205" y="270" text-anchor="end">II-VI（現 Coherent）</text>
<rect class="bar2" x="215" y="257" width="60" height="18"/>
<text class="note" x="281" y="271">2</text>
<text class="item" x="205" y="300" text-anchor="end">其他 16 家</text>
<text class="note" x="215" y="300">各 1 件（Broadcom、Senko、波若威、日月光、奇景、三星、POET、Teramount、Celestial AI、Cisco 等）</text>
<text class="item" x="205" y="330" text-anchor="end">大立光等 5 家</text>
<text class="note" x="215" y="330">0 件（大立光、揚明光、玉晶光、先進光、天孚：這批條件下查不到）</text>
<line class="grid" x1="215" y1="10" x2="215" y2="344"/>
</svg>
</div>
<figcaption>這批 88 件裡，各申請人的件數。深色是台灣公司。NVIDIA 的光通訊專利很多用子公司 Mellanox 的名義申請，一起算；Broadcom 的用 Avago 名義。示意圖，非實際比例。[[uspto-2026-collection]]</figcaption>
</figure>

| 申請人 | 件數 | 在講什麼 |
|---|---|---|
| 台積電 | 19 | 整合式 FAU（內嵌矽透鏡、反射鏡）和它的製法；FAU 接到光學封裝（凸塊加溝槽被動對位、主動對位、上膠）；FAU 基板的槽；FAU 點膠設備；邊緣耦合 FAU 和翹曲控制；光引擎、光學中介層、CPO 封裝結構 |
| Lightmatter | 12 | 可拆、可插拔的 FAU（插座、磁吸、側面和頂面耦合器）；封裝翹曲補償；玻璃耦合器；多排錯開的耦合器；光纖陣列晶片 |
| NVIDIA（含 Mellanox） | 10 | 可拆式 CPO 接頭；整顆封裝的接頭組；V 槽 FAU 和插座；帶對位光纖的 FAU；機殼內的光纖整線盒（含外部雷射插座）；多接頭光纖組件；分波多工 |
| 矽品 | 9 | CPO 封裝結構：散熱片開孔、光纖從側邊出、被動對位凸點、斜面導光件、3D 堆疊 |
| 上詮 | 7 | 光耦合裝置、保偏光纖組裝校準、被動對位連接結構、透鏡式多排光纖陣列、多層波導、波導端微透鏡、分波多工元件 |
| Corning | 5 | FAU 轉接件、可旋轉光纖座、擴束式接頭和插座、翻轉式 FAU 插座、空芯光纖 FAU |
| Ayar Labs | 5 | 從 PIC 背面耦合光纖、晶圓級扇出、可拆式擴束接頭 |
| 萬潤 | 3 | FAU 耦合機台：整機配置、耦合方法（兩種膠加紫外光／雷射固化）、多軸夾持裝置 |
| II-VI（現 Coherent） | 2 | 光電模組封裝、二維準直器陣列 |
| 其他 16 家 | 各 1 | 波若威（可拆式光學組件）、Senko（可拆式二維接頭）、Broadcom、日月光、奇景（光纖陣列的奈米壓印製法）、三星、POET、Teramount、Celestial AI、Cisco 等 |
| 大立光、揚明光、玉晶光、先進光、天孚 | 0 | 這批條件下查不到 2026 年的相關美國案。大立光 2026 年有 178 件美國案，沒有一件命中這些關鍵字[[uspto-2026-collection]] |

表上看得到的：台積電的件數最多，而且 FAU 本身（結構、製法、怎麼接、點膠設備）都有；NVIDIA 集中在可拆式接頭和機殼內的光纖；Lightmatter、Ayar Labs、Corning、Senko、波若威、AIP、Teramount 都在做可拆或可插拔的接法；台廠裡上詮 7 件（FAU 結構、保偏光纖、被動對位），萬潤 3 件（耦合機台），矽品 9 件（封裝）。做 FAU 的台廠裡，大立光和天孚在這批裡沒有相關美國案。

台積電、上詮、萬潤的專利圖，分散在講 FAU 結構和組裝的 [FAU 是什麼](fau.md#q11)、[怎麼做](fau.md#q13)、[怎麼對準](fau.md#q14)，Lightmatter 的在[新創](#q19)，上詮的另一件在[大立光、上詮各走到哪](fau-makers.md#q25)。這裡放一件「可拆式」的：

![Corning：一個會翻的 FAU 插座。插座（150）繞著轉軸（170）掀起來，把 FAU（20）放進去，再壓下來，被後面的卡榫（138a、138b）扣住，FAU 就落到對準的位置。要換的時候扳開卡榫、掀起來拿出來。Corning 的專利圖。[[us20260276918a1]]](img/patents/US20260276918A1-FIG1.png)

### 封測廠和 FAU 廠的專利，另一批查詢 {#pat-osat}

上面 88 件的時間範圍是 2026 年 1 月到 10 月 8 日。後來又針對封測廠和上詮另查了美國專利商標局（時間範圍不同，件數不能和上面的表加總或比較）：

- **上詮**：以 FOCI 為申請人或受讓人查，共 22 個專利家族、34 筆文件（1998 年起），**全部只有上詮一個申請人，沒有共同申請人，也沒有台積電**。2026 年公開 8 件：2 月 5 日的 3 件（被動對位連接結構、多層堆疊波導的製法、透鏡式多排光纖陣列）、2 月 26 日的 1 件（波導側面微透鏡）、5 月 21 日的 1 件（CPO 用保偏光纖的組裝校準）、6 月 18 日的 1 件（透鏡式全反射分波多工被動元件）、7 月 21 日核准的 1 件（光耦合裝置）；**9 月 24 日新公開的第 8 件是跳線的接頭（限位殼、牽引殼的結構），不是 FAU**，不在上面那 88 件裡[[patent-us20260287829a1]]。上詮的簡報寫「已核准 33 件以上（2022 年起）、審查中 39 件」[[mops-foci-slides-20260902]]。引用上詮已核准專利的美國專利只有 1 件。
- **日月光**：2025 年 1 月以後公開、提到光纖陣列的 32 件（27 個專利家族），2026 年公開 23 件；說明書提到 FAU 的 26 件（計算）[[uspto-osat-fiber-20261012]]。其中一件直接寫主動對位的缺點：要開光源、邊移邊量，所以「每小時產出顯著下降」，改用焊接讓光學元件自己對準定位[[us20250321388a1]]；另有被動卡合的超穎表面光連接器、控制凹槽深度的被動對位（並提到可拆的光學元件）、用光導向件取代邊緣耦合的結構、降翹曲的補強件[[uspto-osat-fiber-20261012]]。
- **矽品**：2025 年 1 月以後公開、跟光子元件或 CPO 有關的美國案，這次讀到 17 件；說明書都把 FAU 寫成封裝裡的一個零件。例如封膠時先蓋遮蔽層、封膠後移除，「讓之後可以接光學元件」；散熱片開槽讓 FAU 穿過去；光子元件側面和 FAU 各做對位結構、卡合連接[[us20260047486a1,us20260186216a1]]。17 件的說明書裡「主動對位」「被動對位」字樣都是 0 次；**沒有一件寫 FAU 由誰製造、由誰在哪個廠貼**[[uspto-osat-fiber-20261012]]。
- **Amkor**：2025 年以後公開、提光子或光纖的 4 件（2 個家族），一件把電子元件稱為 CPO 的光引擎結構，連接件可有凹槽接光纖[[uspto-osat-fiber-20261012]]。
- **長電**：1 件（2026 年 10 月 1 日公開），光子中介層晶圓接合，在透光層上留光纖焊接區[[us20260299201a1]]。

## 還不知道的 {#players-open}

- **NVIDIA 下一代光學（scale-up、Rubin Ultra、Feynman）用哪家代工、是 CPO 還是 NPO**：NVIDIA 沒有公開說法，8 月 26 日的財報法說全文沒談光學；看 OCP 10 月 14 日 NVIDIA 網路主管的演講、台積電 10 月 15 日的第三季法說有沒有被問到 COUPE 和 Tower、NVIDIA GTC Washington D.C.（11/30–12/3）、GTC 2027（2027-03-14～18）。另外，只在搜尋摘要看到、沒存剪報的一則：NVIDIA 在柏林有一場 GTC 主題演講，日期 10 月 21 日，沒有確認。
- **「台積電光柵耦合器做壞、氮化矽設計套件延誤」的第二個來源**：查不到，除了原作者沒有任何技術來源、媒體報導或公司說法；NVIDIA 研究單位 ISSCC、OFC、VLSI 2026 論文用哪家製程，論文摘要頁抓不到，等論文全文或作者的預印本。
- **Tower「最大矽光客戶」的名字**：Tower 的所有文件都沒寫；看 Tower 第三季財報（日期還沒公告，Q2 是 8/4），重點是 13 億美元合約有沒有更新、「非常大的客戶」的 NPO 時程、2028 年預付款；另有 Tower 技術論壇 2026 年 11 月 17 日（聖塔克拉拉）。
- **紀要裡的「公司」是誰**：沒有任何一方寫明；Coherent 的下一場法說（FY27Q1，11 月初，日期還沒公告；FY27Q2，2027 年 2 月初）看它說不說 NVIDIA、說不說 FAU 和 FlexConnect。
- **Fabrinet 的三家 CPO 客戶是誰、出貨的是元件還是整機、有沒有組 FAU**：Fabrinet 不說（5 月只說三家都在出貨、營收大部分還在前面）；下一場法說（FY27Q1，11 月初，日期還沒公告）。瑞峰在 CPO 的客戶、泰國產能：看瑞峰第三季財報、公開資訊觀測站的重大訊息。
- **天孚的客戶 B 是誰**：天孚港股申請版本只有描述；披露易到 10 月 12 日沒有聆訊後資料集，每週看一次申請版本清單；天孚三季報（10/29）不會寫客戶名。
- **NVIDIA 光引擎上的 FAU 是誰貼的、可拆接頭的接座是誰黏的**：日月光投控 Q3 法說（去年是 10/30，今年日期還沒公告；營運長吳田玉 7 月 30 日說「再等兩季」，所以較可能是約 2027 年 2 月的 Q4 法說，Q3 法說只可能提前講）、訊芯 Q3 法說（去年 11/21）、OCP 10 月 14 日 NVIDIA 說要回顧的製造流程。
- **Broadcom BFC 的製造商、Davisson 每顆光引擎幾個 FAU**：Broadcom、Corning 都沒寫；看 OCP 10 月 14 日 Broadcom 光學部門的兩場、OFC 2027（2027-03-07～11）。Broadcom 說的「新的寬型 CPO」是什麼，也要看 OCP 的主題演講。
- **整線盒的主力是波若威還是太辰光、Corning**：兩份資料對不上；看 Corning 第三季法說（10/27）、太辰光三季報（10/30）、波若威的法說（還沒申報）。
- **Marvell 的 scale-up 光學金額裡，NPO 和 CPO 各占多少、明年「大很多」是多少**：8 月沒給數字，10 月說「數億美元」；等 Marvell FY27Q3 財報（12 月初，日期未公告）。
- **Astera Labs 的光學客戶、被收購公司的正式名稱**：法說沒點名客戶；名稱在不同稿子拼法不同；看 Astera Q3 法說（11 月初，日期未公告）與 SEC 文件。
- **Celestica 那個 1.6T CPO 案用的 Broadcom 型號、客戶是誰**：轉錄稿型號處是 [inaudible]，客戶沒點名；看 OCP 10 月 14 日的 Broadcom 光學場次、Celestica 下一場法說（2026 年第三季，日期未公告）。
- **Lumentum「最大 CPO 客戶看 NPO 的特定新用途」是哪些用途**：看 Lumentum FY27Q1 財報（11/5）。
- **新創的量產客戶**：目前沒有一家公開具名；Lightmatter 在 OCP 的工作流第一批規格預計 Q4 提交，會前摘要沒說已提交。
- **NVLink Fusion 是否包含 CPO**：素材裡沒有任何一份寫。
- **專利**：台灣、中國的案子沒有查到（查詢網站擋住自動查詢）；台積電台灣公開案 TW202603422A（把 FAU 貼到 PIC 晶粒的方法）只有書目。上詮的專利有沒有被台積電引用：美國案只查到 1 件被別家引用，台灣的沒有重試。
- **台積電向誰買 SOI、COUPE 產線在竹南還是嘉義**：台積電沒有公開；見[台積電的 COUPE 往哪裡長](inside.md#inside-open)。
