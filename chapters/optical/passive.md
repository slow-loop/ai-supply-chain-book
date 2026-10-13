# 光纖、前面板接頭、機內整線

光從光引擎出來，經過 FAU（光纖陣列，把一排光纖對準貼在光引擎上的零件，見 [FAU 是什麼](fau.md#q11)）進到光纖之後，還要走一段路才出得了機器：機殼裡的光纖要重新排線，再接到前面板一排排的多芯接頭上。這份筆記講 FAU 以外、同樣因為 CPO（共同封裝光學，把光引擎和交換器晶片放進同一個封裝）才多出來的被動零件：機內整線、前面板接頭、光纖本身的供應，以及光引擎底下的載板。光纖的構造（單模、多模、保偏）在 [光纖本身](fau.md#q16) 講過，這裡只講供應鏈。

先講這幾輪查到、跟「錢都在 FAU、台廠靠台積電 COUPE 吃到」這個看法對不上的地方：

- **整線和接頭不經過台積電 COUPE**。 光纖柔性板、MMC 接頭、MT／TMT 插芯都是交換器整機那一層的零件，跟光引擎封裝無關，走的是另一條路（見 [機內整線](#pas-shuffle)、[誰在做](#pas-makers)）。
- **前面板接頭的設計和授權在 US Conec 手上**，而 US Conec 的報表 2026 年起併進 Corning（見 [MMC 和授權](#pas-mmc)）。
- **中國被動件廠最大的客戶是美國的連接器、配線品牌商**，不是 NVIDIA 或台積電；其中一家品牌商的光纖業務 2026 年 1 月剛被 Amphenol 買下（見 [誰在做](#pas-makers)）。
- **每台交換器裡，FAU 以外的被動件可能和 FAU 同一個等級的錢**，只是各方數字互相對不上（見 [值多少錢](#pas-shuffle-value)）。
- **中國的 NPO 另有一套自己的接頭**（見 [MMC 和授權](#pas-mmc)）。

## 光纖怎麼從機器裡面接到前面板？ {#q16b}

[拆開一台 CPO 交換器](inside.md#q5) 那張機殼內部照上，一顆交換器晶片周圍就有 324 條光纖，在機殼溝槽裡繞好再拉到前面板[[semianalysis-cpo-book]]。從光引擎到前面板，中間有兩樣東西：機內的**光纖整線**（shuffle），和前面板的**多芯光纖接頭**。另外還有一條反方向的路：外部雷射（ELS）的光，用保偏光纖送進光引擎（見 [光從哪裡來](inside.md#q10)）。

<div class="scroll"><figure><svg viewBox="0 0 900 330" width="100%" role="img" aria-label="CPO 交換器內光纖的路徑">
<rect x="15" y="15" width="745" height="250" rx="8" class="dash"/><text x="30" y="40" class="note">交換器機殼內</text>
<rect x="35" y="130" width="110" height="70" rx="6" class="box"/><text x="90" y="170" text-anchor="middle" class="item">交換器晶片</text>
<rect x="150" y="130" width="90" height="70" rx="6" class="box"/><text x="195" y="170" text-anchor="middle" class="item">光引擎</text>
<rect x="245" y="145" width="52" height="40" rx="4" class="hl"/><text x="271" y="170" text-anchor="middle" class="item">FAU</text>
<path d="M297,158 L420,150" class="solid"/><path d="M297,165 L420,165" class="solid"/><path d="M297,172 L420,180" class="solid"/>
<text x="358" y="140" text-anchor="middle" class="note">光纖線束</text>
<rect x="420" y="115" width="140" height="100" rx="6" class="box"/><text x="490" y="160" text-anchor="middle" class="item">機內整線</text><text x="490" y="182" text-anchor="middle" class="note">shuffle／柔性板</text>
<path d="M560,150 L645,150" class="solid"/><path d="M560,165 L645,165" class="solid"/><path d="M560,180 L645,180" class="solid"/>
<rect x="645" y="125" width="110" height="80" rx="6" class="box"/><text x="700" y="160" text-anchor="middle" class="item">前面板接頭</text><text x="700" y="182" text-anchor="middle" class="note">MPO／MMC</text>
<path d="M755,165 L880,165" class="solid"/><text x="820" y="150" text-anchor="middle" class="note">機外跳線</text>
<rect x="645" y="40" width="110" height="55" rx="6" class="box"/><text x="700" y="64" text-anchor="middle" class="item">外部雷射</text><text x="700" y="84" text-anchor="middle" class="note">ELS，前面板插拔</text>
<path d="M645,68 C450,68 260,80 205,130" class="cu"/><text x="420" y="60" text-anchor="middle" class="note">保偏光纖（送雷射光進來）</text>
<text x="271" y="290" text-anchor="middle" class="note">① FAU</text><text x="358" y="290" text-anchor="middle" class="note">② 光纖</text><text x="490" y="290" text-anchor="middle" class="note">③ 整線</text><text x="700" y="290" text-anchor="middle" class="note">④ 接頭</text>
<text x="450" y="318" text-anchor="middle" class="note">①在 FAU 筆記，②③④在這份</text>
</svg><figcaption>一道光出機器要經過的被動零件：光引擎旁的 FAU、一束光纖、機內整線，最後到前面板接頭，再用跳線接到別台機器。橘線是另一個方向：外部雷射的光經保偏光纖送進光引擎。示意圖，非實際比例。</figcaption></figure></div>

**NVIDIA 三台 CPO 交換器的前面板**。 InfiniBand 的 Quantum-X800 Q3450-LD 前面板是 144 個 MPO-12 接頭[[nvidia-qx800-datasheet-20260911]]；乙太網路的 Spectrum-X 改用更小的 MMC-16：SN6810-LD 有 128 個，SN6800-LD 有 512 個[[nvidia-sn6000-manual-20260916]]。MPO 和 MMC 是兩種多芯接頭，一個接頭同時接好幾根光纖，差別見 [下一節](#pas-mmc)。

![SN6800-LD 的前面板：左右兩大片一格一格的小方孔就是 MMC-16 光纖接頭，共 512 個；中間是管理介面和 QSFP112 插槽。[[nvidia-sn6000-manual-20260916]]](img/nvidia-sn6800ld-front-manual-p13.png)

| | Q3450-LD | SN6810-LD | SN6800-LD |
|---|---|---|---|
| 交換器晶片 | Quantum-X800 | 1 顆 Spectrum-6 | 4 顆 Spectrum-6 |
| 總頻寬 | 115.2T | 102.4T | 409.6T |
| 前面板光纖接頭 | 144 個 MPO-12 | 128 個 MMC-16 | 512 個 MMC-16 |
| 每個接頭的速度 | 800G | 800G（4 條 200G） | 800G，或拆成 4 個 200G |
| 走資料的光纖（計算） | 1,152 根 | 1,024 根 | 4,096 根 |
| 外部雷射（ELS） | 18 個（計算，見 [一台用幾顆雷射](lasers.md#las-count)） | 手冊零件號沒列 | 64 個 |
| 機內整線 | 機殼內建光纖走線 | 沒寫 | 機內光纖 shuffle，最多 2,048 個分支連線 |
| 散熱 | 液冷為主 | 沒有風扇，全液冷 | 沒有風扇，全液冷 |

<p class="tag">表的出處：[[nvidia-qx800-datasheet-20260911,nvidia-sn6000-manual-20260916,nvidia-blog-20250826,semianalysis-cpo-book]]。「走資料的光纖」是計算：接頭數 × 每個接頭實際用的 8 芯；Q3450 假設每個 800G 的 MPO-12 也用 8 芯。</p>

**16 芯只用 8 芯**。SN6810-LD、SN6800-LD 的 MMC-16 接頭有 16 個光纖位置，但只用 8 個（第 1–4、13–16 芯），中間第 5–12 芯是不傳訊號的假光纖；每個接頭走 4 條 200G 的通道，每條一發一收用 2 根光纖[[nvidia-sn6000-manual-20260916]]。所以 SN6810-LD 前面板有 2,048 個光纖位置，實際走資料的是 1,024 根（計算）。手冊附了一張對照圖，教你怎麼用跳線把 MMC-16 接到傳統的 MPO-12：MMC 的 8 芯分別對到 MPO 的第 1–4、9–12 芯。用 MMC 直連的單模光纖最長 500 公尺；用 MPO 分支線最長 50 公尺[[nvidia-sn6000-manual-20260916]]。

![左邊是 MMC-16 的 16 個光纖位置，右邊是 MPO-12 的 12 個位置。只有 MMC 的 1–4、13–16 有連線，對到 MPO 的 9–12、1–4；MMC 的 5–12、MPO 的 5–8 是不傳訊號的假光纖（dummy fibers）。[[nvidia-sn6000-manual-20260916]]](img/nvidia-sn6000-mmc16-mpo12-pinout-p61-map.png) ![兩種接頭的正面。左：MMC 接頭，中間一排小點是光纖，上下兩個圓孔是定位孔；右：MPO 接頭的線稿。綠色箭頭指的 Key 是防止插反的定位鍵。[[nvidia-sn6000-manual-20260916]]](img/nvidia-sn6000-mmc16-mpo12-pinout-p61-faces.png)

**NVIDIA 自己的文件前後寫的不一樣**。NVIDIA 1 月的規格寫「512 MMC-12」「128 MMC-12」[[nvidia-sn6000-datasheet-20260119]]；9 月的硬體手冊 v1.3 寫「512 MMC-16」「128 MMC-16」[[nvidia-sn6000-manual-20260916]]。一份未具名的專家紀要說，客戶內部驗證時發現 12 芯 MMC 的穩定性不如預期，所以改成 16 芯、外觀尺寸也微調[[cnyes-hao-expert-spectrum-20260930]]；NVIDIA 自己沒有說明為什麼改、哪一版改的。

**每台的光纖數，別家的設計不一定一樣**。Meta 在 OCP 2026 發表的 102.4T 光學交換器，摘要寫的是 64 個光學埠、走 16 個「四埠 MMC 介面」，另有 16 個外部雷射模組，100% 液冷、沒有風扇[[ocp2026-agenda-20261012]]。同樣是 102.4T，NVIDIA SN6810-LD 是 128 個 MMC-16；Meta 的「四埠 MMC」是什麼外形、一台幾芯，摘要沒寫。所以用 NVIDIA 一台機器推算整個市場的接頭和光纖用量，不一定適用別家。

Corning 在 OFC 2025 展過一台機內光纖的樣機：1RU、102.4T 交換器，前面板 64 個 MMC 接頭，最多 1,024 根訊號光纖接到 16 顆光的晶片（PIC），另有 16 個面板雷射模組用保偏光纖接到同一批 PIC[[corning-blog-cpo-fau-harness-2025]]。

![廠商產品照：Corning 在 OFC 2025 展出的 1RU 102.4T CPO 交換器光纖樣機，從上往下看。中間是交換器晶片和四周的光引擎，藍色光纖從四邊繞出，左邊是前面板的接頭區；右邊紅、藍兩條是水冷管。[[corning-blog-cpo-fau-harness-2025]]](img/vendor/corning-ofc2025-102t-cpo-1ru-mockup-fiber-routing-20250617.jpg)

**以前機殼裡沒有光纖**。插拔式光模組的交換器，光纖只接到前面板的光模組，機殼裡全是電；Corning 說今天插拔式交換器的機殼內「沒有 Corning 的東西」，CPO、NPO（近封裝光學，光引擎放在晶片旁另一塊板子上）之後，所有在機殼內搬光、管光的被動光學都是新的生意[[corning-investor-event-20260506]]。Corning 的 CPO 業務開發總監 2025 年說，組裝交換器的人以前沒處理過光纖，所以光纖要設計成好組裝、好維修，彎太緊會影響可靠度；Corning 用的光纜一條 32 根光纖[[sdxcentral-corning-fleury-20250604]]。下面這張 Corning 簡報圖把機殼內新多出來的被動零件畫在一起：黃色是 Corning 說「可能是 Corning 產品」的部分，包括 FAU、從外部雷射拉到光引擎的保偏光纖（PMF）、左下的光纖交叉重排盒和面板接頭、機殼裡的光纖[[corning-q2-slides-20260728]]。

![廠商簡報圖：Corning 2026 Q2 法說簡報第 26 頁。左邊是一台多晶片交換器的示意：上下兩組光引擎（PIC）旁各貼一個 FAU，左上兩個外部雷射（ELS）用保偏光纖（PMF）送光進來，左下黃色方框是光纖交叉重排，再接到機外。黃色＝Corning 說可能是它的產品。[[corning-q2-slides-20260728]]](img/vendor/corning-q2-2026-slide26-inside-the-box-passive-photonics-20260728.png)

## 機內整線：shuffle、光纖柔性板 {#pas-shuffle}

### 整線在做什麼

光引擎排在交換器晶片四周，前面板的接頭排成一排排；中間要有東西把每顆光引擎的光纖重新分配、拉到對的接頭上。NVIDIA 說 SN6800 用「整合式光纖 shuffle」加上共同封裝的矽光子，提供 512 個 800G 或 2,048 個 200G 埠[[nvidia-blog-20260106]]；SN6800 的 4 顆晶片之間，光纖在機器內部重新排線（internal fibers shuffling）[[nvidia-sn6000-manual-20260916]]；同一份規格也寫光纖由機內走線直接拉到封裝上[[nvidia-sn6000-datasheet-20260119]]。NVIDIA 的專利把這個整線盒畫成一個盒子：前面一大片是對外接頭，裡面重新排線，上方還有外部雷射的插座（見 [光從哪裡來](inside.md#q10) 那張圖）[[us20260276934a1]]。

<div class="scroll"><figure><svg viewBox="0 0 900 325" width="100%" role="img" aria-label="機內光纖整線概念">
<rect x="20" y="20" width="140" height="56" rx="6" class="box"/><text x="90" y="54" text-anchor="middle" class="item">光引擎 1</text>
<rect x="20" y="92" width="140" height="56" rx="6" class="box"/><text x="90" y="126" text-anchor="middle" class="item">光引擎 2</text>
<rect x="20" y="164" width="140" height="56" rx="6" class="box"/><text x="90" y="198" text-anchor="middle" class="item">光引擎 3</text>
<rect x="20" y="236" width="140" height="56" rx="6" class="box"/><text x="90" y="270" text-anchor="middle" class="item">光引擎 4</text>
<rect x="250" y="10" width="400" height="285" rx="8" class="dash"/><text x="450" y="314" text-anchor="middle" class="note">整線盒（shuffle）</text>
<rect x="740" y="20" width="140" height="56" rx="6" class="box"/><text x="810" y="54" text-anchor="middle" class="item">前面板接頭 A</text>
<rect x="740" y="92" width="140" height="56" rx="6" class="box"/><text x="810" y="126" text-anchor="middle" class="item">前面板接頭 B</text>
<rect x="740" y="164" width="140" height="56" rx="6" class="box"/><text x="810" y="198" text-anchor="middle" class="item">前面板接頭 C</text>
<rect x="740" y="236" width="140" height="56" rx="6" class="box"/><text x="810" y="270" text-anchor="middle" class="item">前面板接頭 D</text>
<path d="M160,40 C450,40 450,40 740,40" class="solid"/><path d="M160,48 C450,48 450,112 740,112" class="solid"/><path d="M160,56 C450,56 450,184 740,184" class="solid"/><path d="M160,64 C450,64 450,256 740,256" class="solid"/>
<path d="M160,112 C450,112 450,48 740,48" class="solid"/><path d="M160,120 C450,120 450,120 740,120" class="solid"/><path d="M160,128 C450,128 450,192 740,192" class="solid"/><path d="M160,136 C450,136 450,264 740,264" class="solid"/>
<path d="M160,184 C450,184 450,56 740,56" class="solid"/><path d="M160,192 C450,192 450,128 740,128" class="solid"/><path d="M160,200 C450,200 450,200 740,200" class="solid"/><path d="M160,208 C450,208 450,272 740,272" class="solid"/>
<path d="M160,256 C450,256 450,64 740,64" class="solid"/><path d="M160,264 C450,264 450,136 740,136" class="solid"/><path d="M160,272 C450,272 450,208 740,208" class="solid"/><path d="M160,280 C450,280 450,280 740,280" class="solid"/>
</svg><figcaption>整線盒在做的事的概念：每顆光引擎出來的光纖，被重新分配到不同的前面板接頭。這張只畫概念，不是 NVIDIA 實際的接法；實際的對應方式沒有公開。示意圖，非實際比例。</figcaption></figure></div>

### 「shuffle box」其實指兩種東西

新聞和券商報告裡的「shuffle box」，多數沒寫清楚是哪一種：

- **機房配線用的**。機房裡一台 leaf 交換器要接到每一台 spine 交換器，光纖會交叉成一團；shuffle 機箱把這些交叉先在盒子裡做好。太辰光的 4U MMC shuffle 機箱就是這種，用 24 芯 MMC 時一台 9,216 芯[[tscom-shuffle-enclosure-20260401]]。
- **CPO 交換器機殼裡面的**。NVIDIA 手冊講的是這一種，把光引擎的光纖排到前面板。

兩種的方向可能相反。研究機構說，Q3450、SN6800 這種埠數很多的 CPO 交換器，能讓網路從三層變兩層，客戶可以省掉機房裡的 shuffle box、配線架和一分多的「八爪魚線」[[semianalysis-cpo-book]]。也就是機殼裡的整線變多，機房配線用的整線可能變少。

![廠商渲染圖：機房配線用的 4U shuffle 機箱。中間橘色那片是光纖柔性板，兩側綠色是 MMC 轉接座；這種是放在機房機櫃裡，不是裝在交換器裡面。[[tscom-shuffle-enclosure-20260401]]](img/vendor/tscom-mmc-shuffle-enclosure-fofc-datasheet-20260401-01.jpg){.s}

### 光纖柔性板怎麼做

整線最常見的做法是**光纖柔性板**（Fiber Optic Flex Circuit，FOFC）：把很多根裸光纖用膠固定在一片柔性基板上，照事先設計好的路徑交叉重排，取代一根根手拉的跳線。太辰光型錄寫的結構是「裸光纖／膠／基板」三層；規格是厚度 1.0 毫米以下、光纖定位精度 ±0.01 毫米、插入損耗小於 0.1 dB（不含接頭）、最大 800 × 1,000 毫米；用途列了三種：機房 spine-leaf 之間的整線、CPO 晶片級走線、狹小空間走線。它也說自己有走線用的 CAD 工具和自動佈纖機[[tscom-fofc-brochure-20260324]]。

![廠商渲染圖：光纖柔性板。上方是剖面：一排黃色圓圈是裸光纖，用膠（Adhesive）黏在橘色基板（Substrate）上；下方是整片柔性板，光纖在板上交叉繞線後從邊緣伸出。[[tscom-fofc-brochure-20260324]]](img/vendor/tscom-fofc-what-is-cross-section-brochure-p2-20260324-03.jpg) ![廠商示意圖：柔性板放進 CPO 交換器機殼的樣子。中間是晶片，黃色光纖從四邊出來，鋪在橘色的平面柔性板上，再拉到左邊前面板的接頭。這是廠商畫的示意，不是 NVIDIA 實機。[[tscom-fofc-brochure-20260324]]](img/vendor/tscom-fofc-cpo-switch-planar-flex-brochure-p4-20260324-02.jpg)

一份未具名的專家紀要說，CPO 用的整線板是在兩片基板之間壓光纖，通常壓 5 到 6 層，一片的光纖總數可到 1,024 或 1,152 根；光纖很脆，多層壓合時每一根都不能斷，所以報廢率高、良率難拉[[cnyes-hao-expert-shuffle-20260819]]。另一份紀要說，難的是組裝工藝不是材料：V 型槽、光纖、濾波片都外購，精度要到 0.1 微米，量測設備以日本廠為主[[cnyes-hao-expert-spectrum-20260930]]。

蘅東光上市時交給北京證券交易所的問詢回覆，畫了它的「光纖柔性線路產品」的結構：一端一排 MT 插芯，中間是柔性板或模組盒，另一端是 6 個 MXC 接頭；芯數有 576、768、1,112 芯，最大 2,000 多芯[[bse-hdg-inquiry-2025]]。愛德泰的港股招股書把柔性板寫成「柔性光背板」：連接光引擎和前面板，解決光引擎到前面板距離不一、光纖長短不齊造成的製造和可靠度問題[[hkex-adt-prospectus-20260515]]。

![監管文件裡的公司線稿：蘅東光柔性線路產品的結構。左邊 A 端是一排 MT 插芯，中間方框是柔性板或模組盒，右邊 B 端是 6 個 MXC 接頭；左下是彩色示意，紅綠線代表兩組光纖；左上、右下分別是 MT 插芯和 MXC 接頭的分解圖。[[bse-hdg-inquiry-2025]]](img/vendor/hdg-fiber-flex-circuit-mt-to-mxc-structure-bse-inquiry-reply-2025.png){.s}

### 一台交換器用幾片

三種說法，互相對不上。把 NVIDIA 手冊的接頭數換算成光纖數，再跟說法比（計算，每條 200G 通道一發一收 2 根光纖）：

| 機種 | 前面板接頭 | 走資料的光纖 | 除以 1,024 | 除以 1,152 |
|---|---|---|---|---|
| Q3450-LD（115.2T） | 144 個 MPO-12 | 1,152 | 1.12 | 1.00 |
| SN6810-LD（102.4T，1 顆晶片） | 128 個 MMC-16 | 1,024 | 1.00 | 0.89 |
| SN6800-LD（409.6T，4 顆晶片） | 512 個 MMC-16 | 4,096 | 4.00 | 3.56 |

<p class="tag">接頭數出處：[[nvidia-qx800-datasheet-20260911,nvidia-sn6000-manual-20260916]]；除法是計算。</p>

- **「一片 1,024 或 1,152 根」對得上**。1,152 剛好是一整台 Q3450 的前面板資料光纖；1,024 剛好是一整台 SN6810，或 SN6800 的一顆晶片。如果 SN6800 一顆晶片配一片，一台就是 4 片（計算）[[cnyes-hao-expert-shuffle-20260819]]。
- **1,152 還有另一種拆法**。一篇 2024 年的社群文章說，51.2T CPO 內部約 1,152 根＝一般光纖 1,024 根＋保偏光纖 128 根；同一篇說 Quantum 那一代每根外部光纖進來後，由 shuffle 拆成四路接到四顆交換晶片[[tencent-kol-shuffle-1152-20241229]]。
- **「每台 4 到 8 套、每套 20 個 MMC」對不上**。一份專家紀要說一套標準 CPO 交換器由 8 套 shuffle 組成（4 到 8 套或更多），每套用 20 個 MMC，所以 10 萬台交換器要約 80 萬套[[cnyes-hao-expert-spectrum-20260930]]。但 8 × 20 = 160、4 × 20 = 80，都不等於 128 或 512 個前面板接頭（計算）；紀要沒寫是哪一台、20 個是前面板端還是光引擎端。
- 另一份紀要說每顆光引擎接 4 個 16 芯 MMC，一台已知的 CPO 交換器約 32 顆光引擎；32 × 4 = 128，和 SN6810-LD 的前面板對得上（計算）[[cnyes-hao-expert-mmc-20260909]]。

### 值多少錢 {#pas-shuffle-value}

各方數字差很多，並排列出，不取平均：

| 說法從哪來 | 整線（shuffle） | FAU | 接頭、光纖 | 可信度 |
|---|---|---|---|---|
| 媒體轉述一份來源不明的 1.6T CPO 交換器成本估算圖 | 每台 2,500 美元 | 72 個 × 50 美元 = 3,600 美元 | MPO 接頭和線材 5,760 美元；單模光纖 12,343 美元 | 媒體報 |
| 投資人在問答平台轉述的「市場說法」 | 每台約 2,500 美元（太辰光沒回答這一點） | — | — | 投資人提問 |
| 未具名專家紀要（8 月） | 每片 6,000–7,000 美元 | 18 通道 80–90 美元、36 通道 170–190 美元 | 16 芯 MMC 接頭約 20 美元（一對 40），MPO 18 美元；同長度 MMC 跳線約為 MPO 的 2 倍；保偏光纖每台 7,000–8,000 元人民幣 | KOL |
| 未具名專家紀要（9 月） | — | — | 1 公尺 16 芯 MMC 跳線約 800 元人民幣 | KOL |
| 券商估計（媒體轉述） | CPO 的整線內含價值約為 NPO 的 8 倍 | — | — | 第三方 |

<p class="tag">表的出處：[[moneyweekly-cpo-cost-20260713,stockstar-tfc-sunsea-mmc-20260731,cnyes-hao-expert-shuffle-20260819,cnyes-hao-expert-mmc-20260909,ctee-browave-gf-20261001]]</p>

對不上的地方：

- 如果「每片 6,000–7,000 美元」和「每台 8 套」講的是同一個東西，一台就是 48,000–56,000 美元（計算），是成本圖上 2,500 美元的 20 倍左右，也比成本圖整台的 FAU（3,600 美元）多一個數量級。兩份說法裡的「一片」「一套」「一台」各指什麼，原文都沒寫清楚，算不出可以並排比的數字。
- 成本圖本身的乘法有錯：單模光纖那一列寫 1,152 × 11 = 12,343，但應該是 12,672（計算）；圖和 FAU 的估算見 [一台交換器裡 FAU 值多少錢](fau-makers.md#fau-value)。
- 不管用哪一份，成本圖上整線、接頭線材、光纖加起來約 2 萬美元（計算），FAU 是 3,600 美元；FAU 以外的被動件都被放在和 FAU 同一級或更高的位置。這兩份都不是一手資料。
- 「8 倍」只有一句轉述，沒有寫 NPO 的基準是多少、是每台還是每 Tbps，原始報告找不到[[ctee-browave-gf-20261001]]。同一段寫的出貨估計是 NVIDIA CPO 交換器 2026 年第四季 1.5 萬台、2027 年 10 萬台，整線 2027 年第一季加速生產，這些是券商的估計。

**唯一查得到的一手單價**是蘅東光的上市問詢回覆，但賣的不是 CPO 交換器的整線，是超級電腦和設備內部連線用的柔性線路產品[[bse-hdg-inquiry-2025]]：

| 期間 | 營收（萬元人民幣） | 銷量（套） | 平均每套（元，計算） | 主要賣給 |
|---|---|---|---|---|
| 2021 | 1,632.49 | 1,055 | 約 15,474 | Jabil |
| 2022 | 4,935.75 | 3,875 | 約 12,737 | Jabil |
| 2023 | 1,948.69 | 2,022 | 約 9,637 | Jabil |
| 2024 上半年 | 1,780.41 | 7,700 | 約 2,312 | 新增分支器類，主要賣 AFL |

<p class="tag">出處：[[bse-hdg-inquiry-2025]]。平均每套是營收除以銷量，混了不同芯數和用途。</p>

每套平均單價從 2021 年約 1.5 萬元降到 2024 上半年約 2,300 元人民幣，同時銷量變多；問詢回覆說這類產品「能夠與 CPO 交換機、算力數據中心光纖配線盒、光模塊等產品共同使用」，但數字本身不是 CPO 出貨[[bse-hdg-inquiry-2025]]。專家講的是 CPO 交換器裡 1,024／1,152 芯多層壓合的大片，蘅東光這些是另一種東西，兩邊沒有同規格的價格可以比。

**市場規模的估計**。愛德泰招股書裡、它委託的研究機構估計，CPO 用柔性板的市場在 2025、2026 年比 CPO 用 FAU 還大，2027 年起 FAU 超過；到 2030 年柔性板約 160 億元、FAU 約 213 億元人民幣，柔性板是 FAU 的四分之三（計算）[[hkex-adt-prospectus-20260515]]。

<div class="scroll"><figure><svg viewBox="0 0 900 320" width="100%" role="img" aria-label="CPO 柔性板和 CPO FAU 市場估計，2025 到 2030 年">
<line x1="80" y1="270" x2="880" y2="270" class="grid"/>
<rect x="620" y="22" width="18" height="14" class="bar2"/><text x="646" y="34" class="item">CPO 柔性板</text>
<rect x="760" y="22" width="18" height="14" class="bar"/><text x="786" y="34" class="item">CPO FAU</text>
<text x="80" y="34" class="note">單位：十億元人民幣（讀圖值）</text>
<rect x="100" y="269" width="40" height="1" class="bar2"/><text x="120" y="263" text-anchor="middle" class="note">0.1</text>
<rect x="144" y="270" width="40" height="0" class="bar"/><text x="164" y="263" text-anchor="middle" class="note">0.0</text>
<text x="142" y="292" text-anchor="middle" class="item">2025</text>
<rect x="230" y="267" width="40" height="3" class="bar2"/><text x="250" y="261" text-anchor="middle" class="note">0.3</text>
<rect x="274" y="268" width="40" height="2" class="bar"/><text x="294" y="261" text-anchor="middle" class="note">0.2</text>
<text x="272" y="292" text-anchor="middle" class="item">2026</text>
<rect x="360" y="260" width="40" height="10" class="bar2"/><text x="380" y="254" text-anchor="middle" class="note">1.0</text>
<rect x="404" y="258" width="40" height="12" class="bar"/><text x="424" y="252" text-anchor="middle" class="note">1.2</text>
<text x="402" y="292" text-anchor="middle" class="item">2027</text>
<rect x="490" y="238" width="40" height="32" class="bar2"/><text x="510" y="232" text-anchor="middle" class="note">3.2</text>
<rect x="534" y="219" width="40" height="51" class="bar"/><text x="554" y="213" text-anchor="middle" class="note">5.1</text>
<text x="532" y="292" text-anchor="middle" class="item">2028</text>
<rect x="620" y="193" width="40" height="77" class="bar2"/><text x="640" y="187" text-anchor="middle" class="note">7.7</text>
<rect x="664" y="154" width="40" height="116" class="bar"/><text x="684" y="148" text-anchor="middle" class="note">11.6</text>
<text x="662" y="292" text-anchor="middle" class="item">2029</text>
<rect x="750" y="110" width="40" height="160" class="bar2"/><text x="770" y="104" text-anchor="middle" class="note">16.0</text>
<rect x="794" y="57" width="40" height="213" class="bar"/><text x="814" y="51" text-anchor="middle" class="note">21.3</text>
<text x="792" y="292" text-anchor="middle" class="item">2030</text>
</svg><figcaption>研究機構對 CPO 用柔性板和 CPO 用 FAU 市場的估計（愛德泰委託，招股書柱狀圖的讀圖值，我們依數字重畫）。2026 年以前柔性板比 FAU 大，2027 年起 FAU 超過。這是估計，不是實際出貨。[[hkex-adt-prospectus-20260515]]</figcaption></figure></div>

### 做到哪一步

- 一份未具名的專家紀要（9 月）說，CPO 交換器的整線還在改款驗證，驗證會持續到 2026 年底，還在試產、沒有實際產能；新供應商認證至少要半年；量產後半年內會有很多廠做得出來，到時候比的是品質[[cnyes-hao-expert-spectrum-20260930]]。
- 公司自己講出時程的，台廠只有波若威（第三季末開始出貨，見 [誰在做](#pas-makers)）；中國廠裡太辰光的半年報寫整線的客製需求「日益增加」[[tfc-sunsea-h1-2026]]，蘅東光的 2025 年報和 2026 年半年報對整線產品兩年都寫「持續推動開發和應用」[[cninfo-hdg-ar2025-20260424,cninfo-hdg-h1-2026-20260821]]。

## 前面板接頭：MPO、MMC 和授權 {#pas-mmc}

### MPO 和 MMC 是什麼

一個多芯接頭同時接好幾根光纖。最常見的是 MPO：接頭裡一塊 MT 插芯（插芯是固定光纖端面的小零件），中間一排小孔是光纖，兩側兩個大孔讓定位針插進去對準。MMC 是更小的一種，前端換成 TMT 插芯，同樣面積可以塞更多接頭；這類比 MPO 小很多的接頭統稱 VSFF（超小型）接頭。

![多芯光纖接頭（MTP 是 MPO 的一種）：一個接頭裡同時接好幾根光纖。[[commons-mtp-connector]]](img/explain/commons-mtp-connector-8-fiber.jpg) ![接頭的正面（MT 插芯）：中間一排小點是光纖，兩側的大孔讓定位針插進去對準。[[commons-mt-ferrule]]](img/explain/commons-mt-ferrule-closeup.jpg)

![廠商渲染圖：MMC 接頭。綠色接頭前端是 TMT 插芯和兩根導針，比 MPO 小，一個接頭塞更多根光纖。左上是廠商的品牌字樣。[[corning-ir-ofc2026-20260316]]](img/vendor/corning-ofc2026-mmc-connector-prizm-tmt-20260316-03.jpg) ![廠商宣傳圖：接頭越做越小。左邊是常見的 MPO 接頭，約 12.4 × 8.2 毫米；右邊是另一種更窄的 SN-MT 接頭，寬 3.85 毫米。廠商說同樣面積能塞進約 2.7 倍的接頭。[[senko-wiwynn-computex2026]]](img/vendor/senko-wiwynn-computex2026-sn-mt-202606-04.png)

### 為什麼從 MPO 換成 MMC

NVIDIA 的 Quantum-X 那台還是 MPO，Spectrum-X 兩台改成 MMC（見 [上一節的表](#q16b)），密度差很多。MMC 已經有 12、16、24 芯，Corning 在 OFC 2026 加了 32 芯；MMC 配 TMT 擴束插芯，插入損耗可以低到 0.5 dB[[corning-ir-ofc2026-20260316,corning-pr-ecoc2026-20260917]]。CPO 這類新架構，機器內部和對外的光學 I/O 都用 MMC 的高密度[[sanwa-usconec-20260217]]。

但市場整體還是 MPO 為主，換代的速度各方說法不同：

- 藤倉說，MPO 佔多芯接頭市場八成以上，MMC 約一成、成長比較快，但不認為明年會急速變成五成；國際標準（傳輸設備、光模組介面）還是 MPO[[fujikura-qa-mmc-20251113,fujikura-qa-mt-20260217]]。
- 一份未具名的專家紀要說，1.6T 時 MPO、MMC 都可以選，到 3.2T 以上 MMC 會變成必需[[cnyes-hao-expert-mmc-20260909]]。
- 另一份紀要（8 月）說「MMC 2027 年底才用，2026 年底的 CPO 交換器還是 MPO」[[cnyes-hao-expert-shuffle-20260819]]；但 NVIDIA 9 月的手冊上 SN6810-LD、SN6800-LD 已經是 MMC-16[[nvidia-sn6000-manual-20260916]]。這份紀要和一手文件對不上。

### 誰設計、誰拿到授權

MMC 和 TMT 插芯是 **US Conec** 設計的。US Conec 是 Corning、藤倉、NTT-AT 三家的合資公司；2026 年起 Corning 的 10-Q 把它寫成光通訊部門裡的「變動利益實體」，Corning 是主要受益人，也就是報表併進 Corning，藤倉和 NTT-AT 那部分算少數股東權益[[sec-corning-10q-2026q2-20260729]]。藤倉說它的持分法投資利益增加，是因為插芯需求強、US Conec 業績好；2025 年 11 月時藤倉全年持分法投資利益預估 89 億日圓，大部分來自 US Conec[[fujikura-qa-mmc-20251113,fujikura-qa-usconec-20260818]]。US Conec 收多少權利金，查不到。

要做 MMC，得先拿到 US Conec 的授權或供應：

| 誰 | 跟 US Conec 的關係 | 時間 | 可信度 |
|---|---|---|---|
| Corning、藤倉、住友電工（Sumitomo Electric Lightwave） | 各自取得授權，可以生產 PRIZM TMT 插芯和 MMC 零件 | 2026-03 | 一手[[usconec-prizm-20260311]] |
| 白山、Sanwa | 和 US Conec 簽 MMC／TMT 插芯多源供應，白山做 12 芯和 16 芯 TMT 插芯 | 2026-02 | 一手[[sanwa-usconec-20260217]] |
| 太辰光 | 取得 US Conec 的 MDC 專利非獨占授權，「在 US Conec 的供應支持下」批量產銷 MMC，相關產品「均已批量出貨」 | 2026-07 | 公司說[[stockstar-tfc-sunsea-mmc-20260731]] |
| 愛德泰 | 自研的 MMC 方案通過 US Conec 官方認證 | 2025-11 | 一手[[hkex-adt-prospectus-20260515]] |
| 蘅東光 | 2025 年向 US Conec 採購 1.81 億元人民幣，是第二大供應商（12.39%）；MMC 接頭「已實現量產並規模交付」 | 2025–2026 | 一手[[cninfo-hdg-ar2025-20260424]] |
| 台廠 | 這幾輪沒有查到任何一家取得 MMC 或 TMT 授權 | — | — |

一份未具名的專家紀要說，要做 MMC 跳線得先通過 US Conec 的製程認證（付費、派人去美國受訓），插芯受 US Conec 專利保護要授權才能做；它服務的那家光連接廠 2026 年 MMC 跳線產能比 2025 年增加 4 到 5 倍，和藤倉有排他約定到 2026 年底，和康寧的商務談判已基本完成[[cnyes-hao-expert-mmc-20260909]]。這家是誰，紀要沒寫。

**日本廠的擴產**。

- 住友電工的「光コネクタ」產能從 2024 到 2028 年擴 13 倍，中期計畫在資料中心段點名的產品裡有 MMC 接頭；它說 MMC 的低損耗靠插芯精度和光纖外徑精度的組合[[sumitomo-results-briefing-20260522,sumitomo-qa-20260610]]。
- 藤倉的 MT 插芯 2025 年度實際產量約為前一年 1.7 倍，產能到 2025 年度末約 2 倍[[fujikura-qa-mt-20260217]]。
- 古河電工 2025 年 1 月買下白山約 67%；當時的報導寫白山的多芯 MT 插芯全球份額第 2[[nihonma-furukawa-shirayama-20241107]]。古河 2026 年 6 月的新聞稿說白山在古河旗下的 Lightera Japan 之下，低損耗 MT 插芯有世界頂級的份額；白山在石川縣蓋新廠，約 50 億日圓、2028 年 4 月左右量產，設備約為現在 1.5 倍以上，新廠前先用既有設施開暫時產線；擴產理由寫的是以雲端大廠為主的需求[[furukawa-pr-shirayama-tmt-20260602]]。古河自己的資料中心產品線同時列 MPO、MMC 和 SN-MT 的插芯與接頭；SN-MT 是 Senko 的設計，所以古河同時做 US Conec 系和 Senko 系的接頭[[furukawa-optosol-briefing-20260604]]。

**價格**。愛德泰招股書引研究機構的行業均價：光纖接頭用的插芯 2025 年平均每個 3.5 元人民幣（2024 年 2.6 元），2026 年第一季「高端插芯結構性短缺」，價格續漲[[hkex-adt-prospectus-20260515]]。MMC 接頭和跳線的單價只有專家紀要的說法（見 [值多少錢](#pas-shuffle-value)）。

NVIDIA 交換器上的 MMC 是哪一家做的，NVIDIA 手冊、規格書和上面這些新聞稿都沒寫，查不到。太辰光被投資人問到是經康寧轉售還是直供 NVIDIA，回答「具體供應鏈信息屬於商業秘密，不便披露」[[stockstar-tfc-sunsea-mmc-20260731]]。

### 中國自己的接頭

中國的 NPO 路線有自己的接頭，不一定用 MMC（中國的規格見 [中國自己的接頭](china.md#cn-connectors)）：

- **中航光電的 UCM**：1RU 面板 264 個埠、16 芯 miniMT 共 4,224 芯，端口密度是 MPO 的 3 倍；插入損耗 0.35 dB 以下；可擴到 12、24、32 芯；導銷間距和 MPO 相同、可以轉接[[cfol-jonhon-ucm-20260527]]。中航光電說 UCM「具有自主知識產權」，正和國內頭部互聯網廠商、設備商深入合作；投資人說「MMC 是美國企業專利產品，需要授權才能生產」，公司沒回應這句[[cninfo-irm-china-npo-20261012]]。1RU 4,224 芯這個數字和 US Conec 對 MMC 公布的數字相同，中航光電的文字裡沒提 MMC。
- **阿里的 SNPO**：光的那一側用 4 個「UTU16/MOFC16」高密連接器，尺寸比 OIF 既有規範小約 25%[[c114-alibaba-al64-snpo-20260922]]。MOFC16 是什麼，查不到。
- **騰訊的 3.2T NPO 規格**：一條鏈路最多 4 個附加接頭、支援引入光 shuffle、補定義了尾纖[[iccsz-tencent-npo-spec-20260127]]。

![廠商渲染圖：中航光電 UCM 的插頭和轉接座。[[cfol-jonhon-ucm-20260527]]](img/vendor/jonhon-ucm-connector-plug-adapter-render-20260527.jpg) ![廠商渲染圖：UCM 的 1RU 面板，一排插滿綠色接頭，官方數字是 264 個埠。[[cfol-jonhon-ucm-20260527]]](img/vendor/jonhon-ucm-1ru-panel-264-ports-render-20260527.jpg)

所以中國廠同時有兩條：太辰光、愛德泰、蘅東光走 US Conec 授權的 MMC；中航光電走自研的 UCM。

晶片那一端可以拔插的接頭（玻璃橋、各家可拆式 FAU）是另一件事，見 [可拆式接頭誰在做](detachable.md#det-who)。

## 光纖和預製棒 {#pas-fiber}

**光纖主要是 Corning 和日本三家**。NVIDIA 在 2026 年 5 月付給 Corning 5 億美元取得認股權證，Corning 要把美國的光學連接產能擴大 10 倍、光纖產能增加 50% 以上，在北卡和德州蓋 3 座新廠[[nvidia-pr-corning-20260506,sec-corning-8k-20260506]]。Corning 的 10-Q 多寫了兩件事：Q2 收到一筆 10 億美元的客戶預付款，對應一份到 2029 年 12 月 31 日的長期供應合約；同季另外發給同一客戶的認股權證公允價值 2.96 億美元，之後在這份合約的銷售發生時從營收扣掉[[sec-corning-10q-2026q2-20260729]]。10-Q 寫的是「一位客戶」，沒點名；同一季只有 NVIDIA 這一次認股權證，所以這位客戶就是 NVIDIA（對照 8-K 和 10-Q）。合約沒寫買什麼產品。Corning 的財務長說，scale-up（同一櫃內 GPU 互連）時最會卡的是連接產能，Corning 正大幅擴充[[investing-corning-cfo-citi-20260909]]。

Corning 執行長說 Meta 到 2030 年最多付 60 億美元[[cnbc-meta-corning-20260127]]。日本方面，藤倉最多投資 3,000 億日圓、產能擴到約 3 倍[[itmedia-fujikura-20260522,dcd-fujikura-20260914]]；住友電工在資料中心相關投資 2,000 億日圓[[nikkei-sumitomo-20260512]]；古河電工約 1,000 億日圓、光纖產能倍增[[nikkei-furukawa-20260804]]。藤倉也說，接頭和插芯的投資小、可以很快擴，光纖不夠的部分要外購補[[fujikura-qa-mmc-20251113]]。這段回答的問題裡，分析師說的是「CPO 之後交換器的數量會變成 16 倍、18 倍」，光連接器和光纜的需求可能更大；這個倍數是提問者的前提，藤倉的回答沒有確認或否認，只講產能怎麼補[[fujikura-qa-mmc-20251113]]。中國的長飛說資料中心用光纖「仍存在一定短缺」[[mydrivers-yofc-20261004]]。這些擴產講的都是資料中心，沒有一家說是為了 CPO。

**CPO 有自己的光纖產品**。上面的大擴產沒有一家講 CPO，但已經有廠商推出 CPO 專用的光纖：

- Corning 有一款叫 **CPO FlexConnect** 的光纖，2025 年 OFC 推出：抗彎的單模光纖，用在 O 波段，模場直徑（光斑大小）9.2 微米，針對 2 公尺以內的短距離降低多路徑干擾，彎成 10 毫米半徑時每圈只多 0.025 dB 損耗[[corning-oem139-flexconnect-202604]]。Lightmatter 的 NPO 模組 Passage L20 規格表寫，32 根資料光纖用的就是「Corning CPO Flexconnect」[[lightmatter-l20-20261012]]。
- Coherent 的保偏光纖寫「production ready now」，說資料中心累計已用超過 1.2 億公尺[[coherent-photonlink-deck-20260921]]。
- 古河電工的資料中心產品線列了「PMF ファイバ（CPO）」，也就是 CPO 用的保偏光纖[[furukawa-optosol-briefing-20260604]]。

要注意名字撞了：Corning 的 FlexConnect 是光纖品牌；Coherent 也有一個 FlexConnect，是可拆式 FAU 接頭[[coherent-ecoc2026-20260920]]。兩家指的是不同東西（可拆接頭見 [可拆式接頭誰在做](detachable.md#det-who)）。

**每台用多少保偏光纖**。只有一份未具名專家紀要的說法：一台 CPO 交換器內部有 144 根保偏光纖，每根 60–70 公分，合計約 100 公尺，每台 7,000–8,000 元人民幣[[cnyes-hao-expert-shuffle-20260819]]。保偏光纖會不會因為雷射內建而被拿掉，見 [保偏光纖會不會被拿掉](detachable.md#det-pm)。

**多芯光纖**。一根光纖裡做好幾個纖芯，同樣粗細可以傳更多路。2026 年 3 月 AFL、Corning、住友、TeraHop（中際旭創子公司）成立 SDM4 多芯光纖的規格組織（四芯，用在園區內短距）[[afl-sdm4-mcf-20260311]]；住友說多芯光纖的採用「比原先預想慢」[[sumitomo-qa-20260610]]。如果一根光纖有 4 芯，接光引擎的 FAU 排法就跟現在一根一芯的 V 槽陣列不同，誰做扇入扇出這一段，這幾輪沒查到。

![資料中心用的光纜，外皮剝開，裡面塞滿上百根彩色光纖。廠商產品照。[[corning-ir-ofc2026-20260316]]](img/vendor/corning-ofc2026-contour-flow-micro-cable-20260316-05.jpg) ![多芯光纖：一根光纖裡做 4 個纖芯，同樣粗細可以傳 4 倍的路數。廠商產品照。[[corning-ir-ofc2026-20260316]]](img/vendor/corning-ofc2026-multicore-fiber-20260316-04.jpg)

**預製棒**。光纖的原料是預製棒：一根高純度石英玻璃棒，放進拉絲塔的高溫爐裡加熱軟化，往下拉成約 0.125 毫米粗的細絲。這一段也吃緊。一家研究機構說預製棒已是光纖產業的關鍵瓶頸，中國廠商的有效產能多數接近滿載，中國一般電信光纖（G.652.D）的價格 2025 年 11 月到 2026 年 1 月漲超過 80%[[cru-preform-20260226]]；媒體報導預製棒新產能要 18–24 個月才開得出來，中國大廠訂單排到 2027 年初，廠商把產能從電信用光纖轉去做資料中心用的抗彎光纖[[tomshardware-fiber-20260516]]。

光纖價格的說法並排：

| 說法 | 數字 | 可信度 |
|---|---|---|
| 抗彎光纖 G.657.A2，媒體引中國官媒 | 每芯公里從 32 元漲到 240 元人民幣 | 媒體報[[udn-fiber-price-20260419]] |
| 光纖行業平均價（愛德泰招股書引研究機構） | 2025 年每芯公里 90.7 元人民幣，2024 年 79.2 元 | 第三方[[hkex-adt-prospectus-20260515]] |
| 中國一般電信光纖 G.652.D | 2025-11 到 2026-01 漲超過 80% | 第三方[[cru-preform-20260226]] |

三個數字講的光纖種類和期間都不同，不能直接比。這些講的都是一般資料中心或電信光纖，沒有一則講 CPO 專用光纖的價格。

![光纖的原料「預製棒」：一根高純度玻璃棒，加熱後拉成細絲就是光纖。[[commons-preform]]](img/explain/commons-silica-fiber-preform-in-hand.jpg) ![光纖是這樣拉出來的：預製棒在拉絲塔的爐子裡加熱到軟化，底部垂下一滴發光的玻璃，往下拉成細絲。這是一所大學的研究用拉絲塔，原理和量產線相同。[[bfh-draw-tower-20220518]]](img/explain/bfh-fiber-draw-tower-furnace-glass-drop-20220518.jpg)

## 被動件廠和它們的客戶 {#pas-makers}

### 先看整條路

整線、接頭、光纖這一段的供應鏈，和 FAU 那一段不一樣：

- **不經過台積電 COUPE**。光纖柔性板、MMC 接頭、MT／TMT 插芯都是交換器整機那一層的零件，跟光引擎封裝無關。NVIDIA 2025 年的夥伴名單也把「光纖接頭和光纖組件」另外列給波若威、Corning、Senko、天孚、Coherent[[nvidia-blog-20250327]]。所以「靠 COUPE 吃到」這條路只適用於 FAU（見 [不經過 COUPE 的幾條路](fau-makers.md#fau-routes)）。
- **上游是 US Conec 的授權**（見 [上一節](#pas-mmc)）。
- **中間隔著一層美國品牌商**。中國被動件廠最大的客戶是美國的連接器、配線廠，品牌廠拿中國廠的貨再賣出去；CPO 交換器裡的接頭最後掛誰的牌子、誰做的，NVIDIA 沒寫。

| 中國廠 | 最大的客戶 | 佔營收 | 這個客戶是誰 |
|---|---|---|---|
| 蘅東光 | 年報寫「H」 | 55.81%（2025） | 年報沒寫；上市時第一大客戶、也是前五大供應商的是藤倉旗下的 AFL，和 H 的條件對得上（對照） |
| 愛德泰 | 招股書寫「客戶 B」：Nasdaq 上市的美國通信基礎設施廠，也是它的供應商 | 63.2%（2025） | 招股書沒寫；和 CommScope 對得上五項、沒有對不上的（對照） |
| 致尚 | 「PH 客戶」：美國某光纖連接解決方案提供商 | 2026 年 1 月到 6 月 4 日下單約 6,640 萬美元 | 公告豁免披露；和 Senko 美國公司對得上四項、對不上兩項，不配對 |

<p class="tag">表的出處：[[cninfo-hdg-ar2025-20260424,bse-hdg-inquiry-2025,hkex-adt-prospectus-20260515,sec-commscope-10q-20251030,cninfo-zhishang-ph-order-20260604,cninfo-zhishang-ipo-20230704,cninfo-zhishang-h1-2026-20260826]]。「對照」是拿公開文件互相比對描述、金額、上市地，不是文件寫出的名字。</p>

CommScope 在 2026 年 1 月 9 日把光纖連接與線纜業務（CCS）以約 105 億美元賣給 Amphenol，公司改名 Vistance Networks[[sec-commscope-8k-20260115]]；Amphenol 的 10-K 說這筆收購為資料中心帶來大量光纖互連能力[[sec-amphenol-10k-20260211]]。愛德泰還有一個客戶 D（紐約證交所上市的美國公司，做高科技互連、感測器和天線），描述和 Amphenol 對得上三項、沒有對不上的，但同類公司沒有逐一排除（對照）[[hkex-adt-prospectus-20260515,sec-amphenol-10k-20260211]]。如果兩個對照都成立，愛德泰最大的客戶 2026 年起已經併進客戶 D 的集團；這是兩個對照加上 8-K 推出來的，不是任何文件寫的。

### 各家做到哪

| 公司 | 整線（shuffle、柔性板） | 接頭、插芯 | 公司自己說的進度 | 可信度 |
|---|---|---|---|---|
| 太辰光（中國） | 有，型錄有 CPO 晶片級走線的柔性板 | MMC 批量出貨；子公司特思路的 MT 插芯批量供貨 | 整線客製需求「日益增加」；上半年營收 10.01 億元人民幣，北美 6.20 億 | 一手、公司說 |
| 波若威（台灣） | Shuffle Module 已完成客戶驗證 | — | 第三季末開始出貨、第四季逐步放量 | 媒體報（引公司說） |
| 蘅東光（中國） | 柔性線路產品「持續推動開發」 | MMC 量產、規模交付；2026 上半年擴 MMC 產能 | CPO／NPO 無源內連光器件 2026 上半年「已完成產品開發」，在驗證、小批量試產 | 一手 |
| 愛德泰（中國） | 研發重點有「高密度混洗光學柔性電路」 | MMC、SN-MT；也做可拆式 FAU、保偏光纖接頭 | 微光連接器（含 FAU、柔性板）2025 年營收 343 萬元，佔 0.2% | 一手 |
| 貿聯（台灣） | 展出「光纖交錯光路」 | SN-MT／MMC 多芯接頭；收購做 MTP/MPO 的新富生光電 | 「CPO 交換器線束」已送樣客戶認證 | 媒體報（引公司說） |
| Corning（美國） | 預組光纖托盤、機殼內整套光纖管理 | MMC（US Conec 併表） | 2026 年 Q2 法說：營收裡還看不到 photonics | 公司說 |
| Coherent（美國） | 「Fiber shuffles… All products in production」；被動光纖組件套件 | — | 見左 | 公司說 |
| 中航光電（中國） | 定製的光柔板 | UCM 自研接頭、FA 組件 | NPO 已成立項目組，擴無源產線、建光引擎產線 | 公司說 |
| Senko、天孚、訊芯 | 只有專家紀要點名 | — | — | KOL |

<p class="tag">表的出處：[[tfc-sunsea-h1-2026,tscom-fofc-brochure-20260324,stockstar-tfc-sunsea-mmc-20260731,ctee-browave-agm-20260617,cninfo-hdg-ar2025-20260424,cninfo-hdg-h1-2026-20260821,hkex-adt-prospectus-20260515,technews-bizlink-computex-20260603,technews-bizlink-xinfusheng-20251201,corning-oem166-oms-202605,bullfincher-corning-q2-20260728,coherent-photonlink-deck-20260921,coherent-ecoc2026-20260920,cninfo-irm-china-npo-20261012,cnyes-hao-expert-spectrum-20260930,cnyes-hao-expert-shuffle-20260819]]</p>

**台廠和中國廠的差別**。在整線和 MMC 上，中國廠白紙黑字寫在財報裡的進度比台廠具體：太辰光的半年報和投資人問答寫 MMC 已批量出貨、MT 插芯已批量供貨、整線客製需求增加[[tfc-sunsea-h1-2026,stockstar-tfc-sunsea-mmc-20260731]]；台廠裡講得出時程的只有波若威，而且多半是媒體轉述。

### 波若威

波若威是台廠裡查得到最多整線說法的一家，但多半是媒體和券商：

- 波若威總經理在 2026 年股東會說，光纖接線盒（Shuffle Module）已完成客戶驗證，預計第三季末開始出貨、第四季逐步放量[[ctee-browave-agm-20260617]]。
- 媒體寫，波若威的 CPO 光纖套件與配線盒第三季小量試產、第四季月產能可望到千級[[cnyes-browave-20260621]]；更早有報導引「供應鏈」說它的 Shuffle Box 已完成驗證、負責光纖路由管理與訊號分配[[ctee-browave-shufflebox-20260309]]。
- 「波若威約佔 CPO Shuffle Box 五成份額」是券商的說法，不是公司說的[[udn-browave-foreign-20260818]]。

誰是 NVIDIA 整線的主力，兩邊說法不同：券商說波若威約五成；一份未具名專家紀要說，在 NVIDIA Spectrum 的整線上太辰光和康寧「規格相近」在競爭，另一份把波若威、Senko 列為全球做得比較好的供應商，天孚「即將進入」，蘅東光、愛德泰有能力但還沒拿到重要客戶[[udn-browave-foreign-20260818,cnyes-hao-expert-spectrum-20260930,cnyes-hao-expert-shuffle-20260819]]。沒有一手資料可以分出高下。

### 蘅東光、愛德泰

**蘅東光**（深圳，2025 年 12 月在北京證券交易所上市）2026 年上半年營收 18.05 億元人民幣，年增 76.75%，其中境外 16.76 億，佔 92.8%（計算）；泰國廠做無源內連光器件，越南廠做光纖接頭等布線產品[[cninfo-hdg-h1-2026-20260821,cninfo-hdg-irm-20260921]]。2025 年前五大客戶：「H」55.81%、Coherent 12.52%、致尚 4.72%、飛速創新 2.74%、青島海信 2.55%；前五大供應商：「H」28.37%、US Conec 12.39%（1.81 億元）、上海景倉 9.79%、華景光通信 8.58%、長飛 5.69%[[cninfo-hdg-ar2025-20260424]]。同一張表 Coherent、US Conec 都寫了名字，只有 H 不寫。上市問詢期間，「AFL 為發行人報告期各期第一大客戶」，也是前五大供應商，佔營收比重從 2021 年 38% 一路升到 2024 上半年 50%[[bse-hdg-inquiry-2025]]；這和 H 的條件對得上（對照）。賣給 Coherent 的，問詢回覆寫明是插拔式光模組用的被動件，不是 CPO 用的 FAU[[bse-hdg-inquiry-2025]]。問到 MMC 會不會取代 MPO，公司說兩者都有應用前景、看客戶的布線方案[[cninfo-hdg-irm-20260921]]。

**愛德泰**（深圳，2026 年 5 月遞交港股申請）2025 年光纖接頭營收 19.72 億元人民幣，佔 93.7%；微光連接器（FAU、可拆式 FAU、保偏光纖接頭、光纖柔性電路接頭）只有 343 萬元，佔 0.2%，毛利率 −188.3%；專做微光連接器的深圳光明廠 2025 年產能 50.26 萬條，利用率 19.4%[[hkex-adt-prospectus-20260515]]。它的供應商 A（美國，「高密度光互連無源器件」，買組件和插芯，2025 年 4.59 億元、佔採購 31.8%）和 US Conec 對得上四項（對照）；供應商 G 是日本的光纖接頭廠，2025 年 2.79 億元，沒有能對金額的資料[[hkex-adt-prospectus-20260515]]。

招股書還有一張全球光纖接頭的營收排名（研究機構，2025 年）：愛德泰 20 億元（9.7%），公司 A 15 億、B 13 億、C 11 億、D 10 億[[hkex-adt-prospectus-20260515]]。用成立年份、地點、交易所、主營業務去對：A 和蘅東光對得上五項，C 和太辰光對得上五項，D 和長芯博創（原博創科技）對得上三項、一項只對一半；B（1992 年成立、香港上市、做銅纜光纜組件和伺服器）沒對（對照）[[hkex-adt-prospectus-20260515,cninfo-hdg-ar2025-20260424]]。

### 致尚和 Senko

致尚 2026 年 6 月公告：1 月 1 日到 6 月 4 日累計收到「PH 客戶」MPO 光纖跳線等訂單約 6,640 萬美元、已交貨約 4,480 萬美元[[cninfo-zhishang-ph-order-20260604]]；9 月 30 日的備忘錄說，PH 客戶 2027 年預計採購 MPO 跳線等光纖接頭的需求預測目標是 5 億美元，沒有約束力[[cninfo-zhishang-ph-memo-20260930]]。5 億美元約為 2026 年前五個月訂單的 7.5 倍（計算）。致尚也是蘅東光的第三大客戶[[cninfo-hdg-ar2025-20260424]]。

致尚和 Senko（日本光纖接頭廠）之間有股權和錢的往來[[cninfo-zhishang-ar2025-20260421,cninfo-zhishang-h1-2026-20260826]]：

- Senko 的香港公司是致尚越南子公司 WeSum 的少數股東之一；致尚和少數股東約定，少數股東或其關聯公司在一定期間內向 WeSum 越南採購不低於一定金額的產品。
- 致尚 2025 年付給 Senko 香港的「居間服務費」3,534.9 萬元人民幣（2024 年 1,105.2 萬），2026 上半年又付 2,578.9 萬。
- 致尚說它配合客戶的「MPC 方案」；MPC 和 SEAT 都是 Senko 新聞稿裡的產品名，MPC 是晶片端可拆接頭的插頭，插在 SEAT 接座上[[senko-gf-detachable-20250924]]。投資人在問答平台上三次問到和 Senko 的 CPO 合作，公司都沒回[[cninfo-irm-passive-20261012]]。

PH 客戶是不是 Senko 美國公司？國別、業務用詞、產品、股權與採購承諾四項對得上；但致尚 2023 年招股書把 Senko Advanced Components, Inc. 寫成「日本公司」，2026 上半年賣給 Senko 香港的金額只有 3,156.6 萬元人民幣，和 PH 客戶的交貨金額差約 10 倍（計算）。有兩項對不上，所以不配對[[cninfo-zhishang-ipo-20230704,cninfo-zhishang-h1-2026-20260826]]。一家券商把兩者並稱「PH&Senko 鏈」，也沒寫 PH 是誰[[kysec-ph-chain-20261008]]。

Senko 在晶片端可拆接頭上的角色見 [可拆式接頭誰在做](detachable.md#det-who)。這條「日系品牌＋中國代工＋越南廠」的路，在「台廠對中國廠」的比較裡看不到。

### 貿聯、鴻海、Corning、Coherent

**貿聯**資深副總說「CPO 交換器線束」進度略優於預期，已送樣給客戶認證；Computex 2026 展的 CPO 方案有 SN-MT／MMC 多芯接頭、FAU、「光纖交錯光路」（shuffle）[[technews-bizlink-computex-20260603]]。線束指的是整線、MMC 跳線還是電源訊號線束，公司沒說明。貿聯 2025 年 12 月宣布收購深圳新富生光電（做跳線、尾纖、多芯光纖、MTP/MPO 高密度接頭，約 305 人），說是為了強化矽光子和 CPO 能力[[technews-bizlink-xinfusheng-20251201]]。同一位主管 2026 年 2 月也說 CPO 普及「沒那麼快」，插拔接頭還要一兩年[[udn-bizlink-cpo-20260226]]。更早的 2025 年 11 月 7 日法說簡報（公司自己的投影片）就寫「攜手 SENKO、ficonTEC 等 CPO 戰略夥伴，實現光銅無縫整合」；富果的備忘錄（第三方整理）把它寫成與 SENKO 和 ficonTEC 戰略合作，開發 CPO 和矽光子製造的自動化、封裝和測試方案，並整理公司說 CPC（銅的連接器）和 CPO 是「互補演進，而非互相取代」[[mops-bizlink-slides-20251107,fugle-bizlink-20251107]]。SENKO 是可拆式接頭的一方，ficonTEC 是對位設備商（見 [對位與測試](equipment-test.md#eq-orders)）；兩家各合作什麼，簡報和整理都沒有寫。

**鴻海集團**內部有做被動光纖件的單位，但查不到它在 NVIDIA CPO 交換器內做哪一段：

- 一件 2019 年申請的美國專利 US10969557B1「光纖 shuffle」，申請人是富晉精密工業（晉城）[[us10969557b1]]。工業富聯 2018 年的招股書把富晉精密列為關聯方：中堅公司的合營或聯營企業，而鴻海精密間接持有中堅公司 100%[[cninfo-fii-ipo-20180523]]。之後股權有沒有變，查不到。
- 這件專利寫的是機房裡兩台交換器之間的 shuffle（兩組各 16 個光模組交叉重排），不是 CPO 交換器機殼內那種。富晉精密在美國的 13 件專利裡，2019–2021 年有 shuffle、交叉光纜、FAU；2026 年公告的兩件和鴻海精密共同受讓，一件是保偏光纖的預接頭，一件是光電複合接頭；這些說明書都沒有出現 CPO 或光引擎字樣（全文搜尋）[[uspto-fujin-search-20261012,us12601878b2,us12571974b2]]。
- 訊芯（鴻海旗下封測廠）自己講的 CPO 角色是光引擎後段封裝和 FAU，沒提機內整線[[uanalyze-shunsin-20251121,cnyes-shunsin-agm-20260626]]；一份專家紀要說訊芯因為整機在富士康組裝，可能分到一部分整線，但份額不高[[cnyes-hao-expert-spectrum-20260930]]。工業富聯 2025 年報只寫「積極推進 CPO/NPO 等新一代技術應用」，沒有拆 CPO 營收[[cninfo-fii-ar2025-20260311]]。

**Corning** 賣的單位比較大：FAU → FAU 線束 → 預裝卡匣（裡面是它自己的 CPO FlexConnect 光纖和 PANDA 保偏光纖）→ 系統層光纖托盤，型錄把這一整套叫光學管理系統[[corning-oem166-oms-202605]]；ECOC 2026 新聞稿說它已有「端到端被動 CPO、NPO 產品組合」：可拆光纖對晶片接頭、抗彎光纖、預組光纖托盤，另展示機櫃內的 CPO 光學背板[[corning-pr-ecoc2026-20260917]]。Corning 2025 年 5 月成為 Broadcom 第一代 CPO 交換器（Bailly）的合格供應商，供的線束包括接光引擎的 FAU，以及前面板、外部雷射模組的接頭[[corning-pr-broadcom-bailly-20250513]]。一篇演講筆記說，Broadcom 和 Corning 的 102.4T 設計一台用 32 條線束、每條 36 芯[[stt-ecoc2025-broadcom-corning-20251001]]。Corning 自己說 2026 年 Q2 營收裡還看不到 photonics（機殼內的光學），目標 2030 年做到 100 億美元[[bullfincher-corning-q2-20260728]]。Corning 在 FAU 上的角色和這 100 億美元，見 [一台交換器裡 FAU 值多少錢](fau-makers.md#fau-value)、[誰在做 FAU](fau-makers.md#q22)。

**Coherent** 的投資人簡報把光路分成四段，「Guide」那段列了保偏光纖、微透鏡陣列、FAU、精密光纖組件；其中整線（fiber shuffles）寫「All products in production」[[coherent-photonlink-deck-20260921]]；ECOC 2026 也展示整合光纖貼合、微透鏡、托盤、端接的被動光纖套件[[coherent-ecoc2026-20260920]]。

### 光聖

光聖是台灣做光纖連接和被動元件的公司，主力在機櫃之間的高芯數光纜，CPO 是它對 2026 年的預期。它自己的簡報和第三方整理的差別要分開看：

- **簡報（公司自己的投影片）**：2026 年 6 月 8 日的法說簡報寫 scale-up 的產品是「active silicon photonic CPO-ELS modules」，提升速度、降低 GPU 的耗電，預期 2026 年；註腳說明 CPO-ELS 是「co-packaging optics with external laser source」。9 月 8 日凱基場的簡報相同，沒有改日期。簡報從頭到尾沒有寫 FAU[[mops-ezconn-slides-20260608,mops-ezconn-kgi-20260908]]。
- **富果的備忘錄（第三方整理，不是原話）**：2025 年 12 月 3 日的整理寫公司開發外部光源模組（ELS）裡的光纖陣列單元（FAU），已與國內外廠商合作[[fugle-ezconn-20251203]]；2026 年 3 月 12 日的整理寫利用既有的機構和光學技術開發 FAU 等關鍵元件，與夥伴共同開發 CPO ELS 模組，預計 2026 年有進展[[fugle-ezconn-20260312]]；到 9 月 10 日，整理的句子只剩「開發用於 GPU 的 CPO-ELS（外部雷射光源）模組，預計 2026 年開始貢獻」，FAU 沒有了[[fugle-ezconn-20260910]]。所以「光聖做 FAU」只出現在 12 月和 3 月的第三方整理，簡報沒有。
- **現在的營收主力**：9 月的整理寫光纜芯數已從 288 芯推進到 864、1,728、3,456 芯，甚至 6,912 芯，並持續開發 13,824 芯；2026 上半年高芯數產品佔比超過五成；光被動元件約佔 2026 上半年營收 80%，光主動元件約 5%[[fugle-ezconn-20260910]]。

### AGC：透鏡陣列和玻璃波導

日本的 AGC（玻璃與化學大廠）在 2026 年 6 月 2 日的半導體事業說明會（講稿與問答全文，公司官網）講到光電融合（光電整合，也就是 CPO 這類做法）：它在開發光學控制和連接用的 MLA（微透鏡陣列）、傳輸用的聚合物，以及玻璃波導兩種東西[[agc-semi-script-20260602]]。問答裡有幾點：

- 光電融合用的光學部材被列為開發品，不在「2030 年前營收倍增」的計畫裡。
- 被問採用的時程，負責的主管說「現在 NVIDIA 剛推出的交換器這些，光電融合的採用已經開始」；AGC 現在能提案的是 MLA（把光變成平行光再導向光柵的零件），詢問很多；更未來更高集成之後的波導，現在也有樣品提供和詢問。
- 營收規模：沒有具體數字，他們的目標是「數百億日圓級」的事業規模；市場在 2028、2029 年開始立起來，真正長大是 2030 年代。
- 被追問已經有被採用的嗎：「目前是開發和試作，量產還在之後」。主管也說光電融合「說不定會比較早普及」，市場規模要看價值鏈做到哪裡。
- 玻璃核心基板（見 [載板](#pas-substrate)）AGC 另外在做，說當初以為 2028 年左右開始、現在感覺是 2029 年左右才會立起來[[agc-semi-script-20260602]]。

AGC 在供應鏈圖裡的位置（透鏡）見 [誰主導、供應鏈全圖](players.md#q20)。

### 傳聞：光庫接手 Lumentum 的被動產品線

問答平台上有投資人三次說光庫（中國）接手了 Lumentum 的被動產品線、在深圳設新公司，公司回「以指定媒體刊登的公告為準」或沒回[[cninfo-irm-passive-20261012]]。查不到任何公告：光庫半年報唯一新設的子公司是 2026 年 4 月設立的光庫科技（深圳），自有資金 8,000 萬元，目的寫「整合資源、拓展華南地區市場業務」[[o-net-h1-2026]]；Lumentum 2026 年沒有申報完成資產處分的 8-K[[sec-lumentum-filings-20261012]]。

## 載板 {#pas-substrate}

載板是交換器晶片和光引擎底下的封裝基板。公開談到 CPO 的不多：

- 欣興說光復二廠將導入 CPO 相關方案（法說的第三方整理）；整理還寫：光復二廠現有建物已完成，將投入約 30–40 億元建置無塵室與裝機，預計 2027 年下半年量產；問到光學互連的時間，答「我們確實與數個客戶在光學互連解決方案上有合作…許多客戶的目標時間點確實是在 2027 年左右」，也說「技術突破是一回事，但更重要的是如何讓這些高技術產品能帶來長期且合理的利潤回報」；光學模組歸在載板業務；導入 CPO 後部分元件可能被取代，但載板價值（ASP）「或許會更高」[[fugle-unimicron-20260225]]。
- AT&S 說 CPO 是玻璃核心基板最重要的機會之一[[iconnect-ats-20260422]]。
- 新光電氣 2026 年 2 月在一場日本政府單位的簡報裡，說封裝內的電線路會逐步換成光線路，並畫出 FCBGA 基板（一種覆晶封裝載板）上放光引擎（PIC、EIC、光纖陣列）的結構，標題是「光引擎（光電轉換模組）的開發」[[shinko-meti-20260206]]。
- 三星電機、LG Innotek 在測 CPO 載板樣品只有媒體報導，公司沒有證實[[trendforce-semco-lg-20260420]]；景碩、南電這批沒有剪報，Ibiden 的法說問答沒提 CPO。

**玻璃基板**是另一條線。玻璃基板用穿過玻璃的導電孔（TGV）取代有機基板，平整、不易翹曲：

- 友達和康寧在 SEMICON 2026 展出玻璃核心基板[[auo-press-20260831]]；Corning 同場展「整合式被動光學系統支援 CPO」和 TGV 玻璃核心基板[[technews-corning-semicon-20260831]]。
- **友達自己在法說會上說的**（轉錄稿，AI 轉寫，說話者是 AI 指派的，下面的名字照稿）：2026 年 4 月 30 日（簡體中文場），分析師問 Micro LED CPO 的中介層（interposer）是用矽還是玻璃，董事長彭双浪答：「我们在 CPO 这一块，我们做的就是 glass 的这个 interposer，包含 TGV 也是一样」；又說「先進封裝」指的是 COB，Fan-out（轉錄稿寫成 POP）沒有直接拿來做 IC 封裝，而是用在低軌衛星的玻璃天線[[allmind-auo-q1-20260430]]。7 月 30 日，UBS 分析師問 TGV 和 RDL 的進度，並說台積電在日本的研討會提到與供應鏈合作開發玻璃基板、合作對象之一是台灣的面板同業（這是分析師的話，友達沒有確認也沒有否認）。友達答 TGV 和 RDL「其實有在進行」，但不方便說跟誰；玻璃製程做了快 30 年；Glass Core 也在發展，「目前有合作伙伴，但还不算是很成熟」，預計還要兩三年才會成熟；資本支出裡有一塊是 TGV、RDL、Glass Core 的試產線[[allmind-auo-q2-20260730]]。富果的整理（第三方）寫的是「Glass core 技術成熟約需 2–3 年」「董事會已核准投資建置相關試產線」[[fugle-auo-20260730]]。所以友達的 CPO 這條線是 Micro LED 光源模組用的**玻璃中介層**，玻璃核心基板則是另一條，還要兩三年。
- 京東方成立了玻璃載板 CPO 專案組，還在驗證，並說和英偉達「暫未開展業務合作」[[cninfo-irm-search]]。
- 通富微電被問 CPO，只回「具備使用 TGV 玻璃基板進行封裝的技術能力」[[cninfo-irm-china-npo-20261012]]。
- 華工科技子公司的 3.2T CPO 光引擎用玻璃基板 TGV 封裝，只有投資人在問答平台上這樣說，公司沒有正面回應[[cninfo-irm-china-npo-20261012]]。
- AGC（日本）在開發玻璃中介層（連接晶片與基板）和玻璃核心基板，講稿說玻璃核心基板是它最大的潛在市場，立起來的時間從原本的 2028 年左右延到約 2029 年[[agc-semi-script-20260602]]。

玻璃上直接做光波導、取代 FAU 的玻璃橋是另一件事，見 [康寧玻璃橋](detachable.md#q29)。

## 還不知道的 {#pas-open}

- **NVIDIA 交換器上的 MMC、整線是哪一家供的**：手冊、規格書、各家新聞稿都沒寫；Corning 2026 年 10 月 27 日的 Q3 法說、太辰光 10 月 30 日的三季報、波若威 11 月的法說（觀測站還沒申報日期）可以對照。
- **一台交換器到底幾片整線**：「一片 1,024／1,152 芯」「每台 4 到 8 套、每套 20 個 MMC」對不上，要 NVIDIA 的專利圖、OCP 或 GTC 的開蓋照（GTC 2027 在 2027 年 3 月 14–18 日）。
- **「CPO 整線約為 NPO 的 8 倍」的原始報告**：只有一句媒體轉述，原報告可能是付費報告，查不到 NPO 的基準。
- **NVIDIA 什麼時候、為什麼把 MMC-12 改成 MMC-16**：比對 SN6000 硬體手冊 v1.0 到 v1.3 的改版紀錄。
- **US Conec 的營收和權利金**：Corning 10-Q 的 VIE 附註、藤倉有價證券報告書的持分法投資收益可能有數字；Corning Q3 10-Q 在 10 月 27 日法說前後出。
- **NVIDIA 那筆 10 億美元預付款買的是什麼**：看 Corning Q3 10-Q 的合約負債附註，和 NVIDIA 11 月中下旬 Q3 財報的預付供應合約附註。
- **致尚 PH 客戶是誰、實際交貨多少**：致尚 10 月 23 日的三季報可以對照 6 月公告的 4,480 萬美元；WeSum 2022 年的少數股東 GCIH, LLC 是誰也沒查到。
- **蘅東光的「H」、愛德泰的客戶 A、B、D 正式是誰**：蘅東光 10 月 28 日三季報；愛德泰等港交所下一版申請文件或聆訊後資料集（到 10 月 12 日沒有）。愛德泰排名裡的公司 B 還沒對。
- **愛德泰 2026 年客戶結構**：CommScope 光纖業務併入 Amphenol 後，客戶 B、D 會不會合併計算，看下一版申請文件。
- **富晉精密現在是不是鴻海的關聯企業、在 CPO 整線做什麼**：查國家企業信用信息公示系統、鴻海年報的關係企業報告書；鴻騰精密（FIT）的 CPO 光纖接頭角色從它的年報和法說查。
- **貿聯「CPO 交換器線束」是什麼**：沒有逐字稿；貿聯在 OCP 2026（10 月 12–15 日）有場次，可看簡報。
- **天孚做不做整線**：只有專家紀要說「即將進入」；看天孚 10 月 29 日三季報和問答平台。
- **光庫有沒有接手 Lumentum 的被動產品線**：光庫 10 月 23 日三季報、Lumentum 11 月 5 日 FY27 Q1 財報和 10-Q 的處分段落。
- **白山的客戶和 TMT 插芯營收**：白山沒上市；古河電工的有價證券報告書和光ソリューション分部的業績說明可能有數字。
- **中航光電 UCM 的規格和客戶，國內 NPO 用 UCM 還是 MMC**：中航光電 10 月 29 日三季報；阿里 SNPO 指定的 MOFC16 是什麼還查不到。
- **Meta 102.4T 交換器的「四埠 MMC 介面」是什麼外形、一台幾芯**：等 Meta 10 月 14 日 OCP 場次的投影片。
- **多芯光纖接光引擎時，扇入扇出元件誰做**：從 SDM4 多芯光纖規格組織、住友的 OCP 投影片查。
- **光聖的 FAU 有沒有、做到哪**：簡報只寫 CPO-ELS 外部光源模組預期 2026 年，沒有 FAU；富果 12 月和 3 月的整理有，9 月的整理沒有。看光聖下一場法說簡報和問答（去年 12 月 3 日，今年日期未申報）。
- **AGC 的 MLA 和波導誰在用**：AGC 說現在只有詢問和樣品，沒有量產；看 AGC 之後的決算說明會問答，以及 NVIDIA 交換器的拆解資料。
- **友達玻璃中介層的客戶和 Micro LED CPO 送樣的結果**：友達說已與國際級互連方案廠商進入設計與送樣（富果整理，沒有點名）[[fugle-auo-20260730]]；看友達下一場法說和 2027 年初的展會。
- **載板廠（欣興、景碩、南電、Ibiden、三星電機、LG Innotek）的 CPO 載板進度**：各家 10–11 月法說；台股法說日期觀測站多數還沒申報。
