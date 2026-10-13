# CPO 是什麼、為什麼需要光

2026-10-12。用問答把 CPO（Co-Packaged Optics，共同封裝光學）的起點講清楚：AI 機房裡晶片之間怎麼傳資料、今天的光模組卡在哪、CPO 怎麼改、從插拔式到 CPO 中間有哪些做法、scale-up 和 scale-out 差在哪。拆開來每一塊怎麼運作見 [拆開來：一道光在 CPO 裡怎麼走](inside.md#q5)；插拔式自己的折衷（LPO、TRO、XPO、NPO）見 [插拔式的折衷](alternatives.md#alt-power)；什麼時候變大見 [現在到哪](timing.md#q27)。自己畫的示意圖都標「示意圖，非實際比例」。

## AI 資料中心裡，晶片之間怎麼傳資料？ {#q1}

一座 AI 資料中心裡有成千上萬顆 GPU 和交換器晶片，訓練和推論的時候，它們要不停地互相傳資料。傳法只有兩種：用**銅線傳電訊號**，或用**光纖傳光訊號**。今天兩種都在用，分工看距離：近的用銅，遠的用光。

**最近的一段在機櫃裡面**。NVIDIA 的 NVL72 機櫃把 72 顆 GPU 連成一個「scale-up」群組，讓它們像一顆大晶片一樣工作[[sth-hotchips2026-nvidia-network]]。連法是機櫃背後一整片銅纜匣（cable cartridges），把運算托盤和 NVLink 交換器托盤接在一起[[lenovo-gb300-nvl72-rear]]。Blackwell 這一代的 NVL72 有 4 個一樣的銅纜匣（NVIDIA 叫它 spine cartridge）、5,184 條銅纜，每條跑 200 Gb/s、長約 0.2 到 1.0 公尺；機櫃裡由上到下是 10 個運算托盤、9 個交換器托盤（每個托盤 2 顆 NVSwitch 交換晶片）、8 個運算托盤，每個運算托盤 4 顆 GPU[[ascii-ohara-nvl576-20260810]]。這套 NVLink 每顆 GPU 的頻寬是 7.2 Tbit/s，下一代 Rubin 要到 14.4 Tbit/s，但銅線最多只能走 2 公尺，所以能直接連在一起的 GPU 只能擠在一兩個機櫃裡[[semianalysis-cpo-book]]。

![一櫃 72 顆 GPU 靠中間這組銅纜連成一體。左：整個 NVL72 機櫃；中：四條直立的銅纜匣，投影片叫它 NVLink Spine（脊椎）；右：NVLink 交換器托盤。[[sth-hotchips2026-nvidia-network]]](img/ServeTheHome-HotChips2026-NVIDIA網路投影片-202608-02-nvlink-spine.jpg)
![GB300 NVL72 機櫃背面線稿。中間標 2 的整片都是銅纜匣，把運算托盤和交換器托盤接在一起；1 是供電銅排，3 是冷卻液接頭。銅線佔掉機櫃背面一大半。[[lenovo-gb300-nvl72-rear]]](img/vendor/lenovo-gb300-nvl72-rack-rear-cable-cartridges-20261011-01.png){.xs}

![NVIDIA 自己的投影片：Blackwell（GB200）NVL72 的 scale-up 連線。左：72 顆 GPU 經 18 顆 NVSwitch 全部互連，每顆 GPU 7.2 Tb/s；中：機櫃由上到下 10 個運算托盤、9 個交換器托盤、8 個運算托盤；右上：4 個銅纜匣、5,184 條銅纜、每條 200 Gb/s、長約 0.2 到 1.0 公尺；右下：銅纜匣（NVLink Spine）從機櫃背面插進去。左下三行字：銅線便宜、可靠，除了距離短，用在 scale-up 很理想；但距離限制逼得東西擠在一起，功率密度變高，最後限制了 scale-up 能做多大。投影片出自 2026 年 VLSI 研討會短課程，經日本媒體轉貼。[[ascii-ohara-nvl576-20260810]]](img/media/ASCII-VLSI2026-SCT8-NVIDIA-slide10-GB200-NVL72銅背板5184條-20260810.jpg){.s}

NVIDIA 為什麼盡量留在銅？它的超大規模與 HPC 副總 Ian Buck 在 GTC 2026 的記者問答說：機櫃背後超過 5,000 條銅纜，因為短距離的銅「又快又便宜」，不用 retimer（中繼重整訊號的晶片），也最省電；改用液冷的真正原因之一，不只是 GPU 效能，而是「把盡量多的 GPU 用銅線連在一起」；72 顆 GPU 全部用光纖和光模組也做得到，但貴、耗電[[tomshardware-ianbuck-qa-20260323]]。下一代 Vera Rubin NVL72 在 Hot Chips 2026 的投影片副標寫「全銅 scale-up 機櫃」，列出銅線 scale-up、沒有 retimer、托盤裡沒有線[[sth-hotchips2026-rubin-nvl72]]。NVIDIA 網路資深副總 Gilad Shainer 在同年 8 月的 Hot Interconnects 說，只要距離允許，銅線仍是 NVIDIA 偏好的連接，包括 NVLink 的 scale-up 網域內[[convergedigest-shainer-hoti-202608]]。

![Vera Rubin NVL72 在 Hot Chips 2026 的投影片，副標「全銅 scale-up 機櫃」。右邊是機櫃拆開：最左是一整片散熱或走線的背板，中間四條就是銅纜匣，右邊是機櫃本體和液冷管。左欄列 45°C 液冷、沒有 retimer、800 V 直流供電、托盤可熱插拔、托盤內沒有線、銅線 scale-up。[[sth-hotchips2026-rubin-nvl72]]](img/media/ServeTheHome-HotChips2026-NVIDIA-Rubin-slide17-全銅scale-up機櫃-202608.jpg){.s}

**出了機櫃就換成光**。機櫃和機櫃之間、伺服器和交換器之間，距離是幾公尺到幾百公尺，銅線到不了，只能用光纖。NVIDIA 把一般雲端機房和 AI 機房的照片並排：AI 機房每一櫃都插滿光纖，投影片副標寫，這些光互連的耗電約等於運算的 10%[[sth-hotchips2026-nvidia-network]]。

![左：一般雲端機房，每櫃只有少數紅色網路線；右：AI 機房，每一櫃都插滿青綠色光纖。投影片標題是「Scale-out 的 AI 靠光」，副標是「（光互連的耗電）等於運算的 10%」。[[sth-hotchips2026-nvidia-network]]](img/media/ServeTheHome-HotChips2026-NVIDIA網路投影片-202608-03.jpg)

**為什麼銅線走不遠**？銅線便宜、好接，本身幾乎不耗電：每條通道 100G 那一代的被動銅纜最長 3 公尺，功耗不到 0.1 瓦[[nvidia-linkx-100g-overview]]。問題是物理上的限制：**訊號跑得越快，在銅線上衰減得越厲害，能傳的距離就越短**[[tianxia-coupe-20260818]]。具體一點：每條通道從 112G 升到 224G，訊號的主要頻率（奈奎斯特頻率）從 26 GHz 變成 53 GHz；在 53 GHz，常見的 30AWG 雙軸銅纜每公尺損失約 10.23 dB，粗一點的 26AWG 約 7.14 dB[[asteralabs-224g-copper-20260715]]。dB（分貝）是訊號衰減的單位，每多 10 dB，訊號就再弱 10 倍。一條連線能容忍的總損耗大約 40 dB，要分給電路板走線、接頭、封裝；光是機櫃裡 1.2 公尺的銅纜就先吃掉約 12.3 dB，拉到 1.75 公尺時接近 18 dB[[asteralabs-224g-copper-20260715]]。粗的線損耗小，但同樣 64 對線的線束截面積大約多 50%，機櫃背面塞不下[[asteralabs-224g-copper-20260715]]。

所以每一代速度翻倍，銅線就再縮一截。標準組織訂的目標寫得很清楚：IEEE 802.3 工作組 2022 年訂的目標，每條通道 200 Gb/s 的銅纜要能走「至少 1 公尺」；上一代用 8 條、每條 100G 組成 800G 的銅纜，目標是「至少 2 公尺」（這是工作組的目標，不是最終條文）[[ieee-8023df-objectives-20220914]]。產品也是同一個方向：NVIDIA 每條 100G 一代的被動銅纜到 3 公尺，加線性放大晶片的主動銅纜可到 3、4、5 公尺[[nvidia-linkx-100g-overview]]；到每條 200G 的 Spectrum-6 交換器，能用的銅纜只剩主動式，1.6T 線性主動銅纜 1.1 公尺、1.6T 分成兩條 800G 的分支線 1 公尺，沒有列被動銅纜[[nvidia-sn6000-manual-20260916]]。到了每條 200G PAM4（PAM4 見[下一題](#q2)），被動銅纜只能走不到 1 公尺[[arxiv-2601-14342]]。也有晶片廠在 2026 年 10 月的投資人日給了比較寬的數字：每條 200G 時銅線能走 2.5 公尺，今天 XPU（GPU 這類運算晶片）之間的連線 100% 是銅[[futurum-marvell-investor-day-20261009]]。2.5 公尺和上面的「1 公尺」「不到 1 公尺」量的是不是同一種銅纜，素材裡看不出來，下表並排列出。

![速度越快，銅線走得越短；光走得遠，但速度越快越耗電。上：銅線從 1G 的約 25 公尺，一路縮到 400G、800G 的約 2 公尺。下：一條光鏈路（兩端各一支光模組）的耗電，800G 約 24 瓦。[[microsoft-mosaic-paper]]](img/papers/sigcomm25-mosaic-copper-reach-optical-power-fig1.png){.s}

| 每條通道的速度 | 銅線能走多遠 | 是什麼數字 |
|---|---|---|
| 100G | 被動銅纜最長 3 公尺（功耗不到 0.1 W）；加線性放大晶片的主動銅纜 3–5 公尺 | NVIDIA 產品規格[[nvidia-linkx-100g-overview]] |
| 100G（8 條組成 800G） | 至少 2 公尺 | IEEE 工作組目標[[ieee-8023df-objectives-20220914]] |
| 200G | 至少 1.0 公尺 | IEEE 工作組目標[[ieee-8023df-objectives-20220914]] |
| 200G | 被動銅纜不到 1 公尺 | 論文[[arxiv-2601-14342]] |
| 200G | 2.5 公尺 | Marvell 投資人日簡報（研究機構轉述）[[futurum-marvell-investor-day-20261009]] |
| 200G（224G 訊號） | 30AWG 每公尺約 10.23 dB、26AWG 約 7.14 dB；1.2 公尺吃掉約 12.3 dB（總預算約 40 dB） | 銅纜晶片廠的計算[[asteralabs-224g-copper-20260715]] |
| 200G（Spectrum-6 交換器） | 手冊只列主動銅纜：1.1 公尺、分支線 1 公尺 | NVIDIA 手冊[[nvidia-sn6000-manual-20260916]] |
| 200G（GB200 NVL72 機櫃內） | 每條約 0.2–1.0 公尺 | NVIDIA 投影片[[ascii-ohara-nvl576-20260810]] |
| NVLink（GPU 直連） | 最多 2 公尺 | 研究機構[[semianalysis-cpo-book]] |

銅線的距離也直接決定 scale-up 能做多大。Meta 的 Drew Alduino 在 OFC 2026 的論壇上說，GB300 這一級的機櫃已經要用有數千對差動訊號的電背板，一個網域超過 144 顆加速器就碰到銅線在距離、功耗、密度上的實際極限；超過 256 顆的網域很可能需要光[[convergedigest-meta-ofc2026]]。scale-up 是什麼見[第 5 題](#q4b)。

**光纖是另一個量級**。光在光纖裡的損耗以「每公里」計算，不到 0.2 dB；電訊號在封裝和電路板走線上的損耗以「每公分」計算，在 53 GHz 約 1 dB[[wallstreetcn-wins-forum]]。所以電只適合在封裝裡走幾毫米到幾公分，光可以跨整個資料中心；光的頻寬大、幾乎不發熱[[tianxia-coupe-20260818]]。NVIDIA 交換器配的單模光纖直連線最長 500 公尺，長距模組可到 2 公里[[nvidia-sn6000-manual-20260916]]。代價是兩端都要有東西把電轉成光、再把光轉回電，這一步要耗電：一條 800G 光鏈路兩端模組合計約 24 瓦[[microsoft-mosaic-paper]]。

![電和光並排比。左欄電：銅線加絕緣材料，集膚效應（高頻電流擠到導體表面）讓損耗約每公分 1 dB（53 GHz），適合毫米到公分、封裝之內，怕電磁干擾。右欄光：光在矽和二氧化矽做的波導裡反射前進，損耗每公里不到 0.2 dB（1550 nm），可以從公分走到公里、跨資料中心，不受電磁干擾。下方小圖：晶片左邊是晶片對晶片的短距電訊號；右邊兩個 FAU（光纖陣列單元，把一排光纖接到晶片上的零件）是光出封裝的出口。[[wallstreetcn-wins-forum]]](img/華爾街見聞-穎崴CPO論壇-2026日期不明-02-copper-vs-optical-slide.png)

FAU 本身見 [FAU 是什麼](fau.md#q11)。

|  | 銅線（電） | 光纖（光） |
|---|---|---|
| 損耗 | 封裝、電路板走線約每公分 1 dB（53 GHz）[[wallstreetcn-wins-forum]]；銅纜每公尺約 7–10 dB（53 GHz）[[asteralabs-224g-copper-20260715]] | 每公里不到 0.2 dB（1550 nm）[[wallstreetcn-wins-forum]] |
| 能走多遠（每條 200G） | 銅纜約 1 公尺[[ieee-8023df-objectives-20220914,nvidia-sn6000-manual-20260916]]；Marvell 說 2.5 公尺[[futurum-marvell-investor-day-20261009]] | 單模光纖 500 公尺到 2 公里[[nvidia-sn6000-manual-20260916]] |
| 電磁干擾 | 會受影響[[wallstreetcn-wins-forum]] | 不受影響[[wallstreetcn-wins-forum]] |
| 兩端要轉換嗎 | 不用，電進電出；被動銅纜不到 0.1 W（100G 一代）[[nvidia-linkx-100g-overview]] | 要，兩端各一支光模組或光引擎；800G 一條約 24 W[[microsoft-mosaic-paper]] |
| 用在哪 | 機櫃內 GPU 互連（NVLink）[[semianalysis-cpo-book]] | 機櫃之間、伺服器到交換器[[sth-hotchips2026-nvidia-network]] |

**而且需求一直在翻倍**。一顆交換器晶片的封裝能進出的資料量，大約每兩年翻一倍，到 2025 年約 100 Tbps[[lsa-review-202601]]。速度越快，銅線越短；要連得更遠、更多，就得改用光。光要先經過一道「電轉光」，這一步在哪裡做、花多少電，是下一題。

![交換器晶片一顆封裝的頻寬（縱軸，Tbps，對數刻度）。只看藍點那條線：插拔式光模組時代，大約每兩年翻一倍（圖上標 ~2x/2yr）。紫色三角形是已經做出來的 CPO（共同封裝光學）交換器；右邊虛線是往後的推估。[[lsa-review-202601]]](img/lsa-s41377-025-02048-w-waveguide-couplers-review-fig16b-switch-bandwidth-trend.png){.s}

## 現在的光是怎麼接到晶片上的？ {#q2}

**今天的做法叫插拔式光模組**。光模組長得像一根加長的隨身碟，比手掌略長，一頭插進交換器前面板的插槽，另一頭接光纖[[chargerlab-nvidia-800g-teardown-20260708]]。一台 51.2T 的交換器前面板有 64 個插槽，每個插一支 800G 光模組[[sth-marvell-teralynx10-202407]]。打開機殼，交換器晶片在主機板中間，插槽在最前緣，兩者之間隔著一段電路板。

![一台 51.2T 交換器的前面板：上下兩排共 64 個插槽，每個插一支 800G 光模組（照片裡是空的）。[[sth-marvell-teralynx10-202407]]](img/media/ServeTheHome-Marvell51.2T交換器-202407-01.jpg)
![同一台開蓋：中央那顆方形大晶片是交換器晶片，前緣（照片下方）是插槽。晶片到插槽之間這段電路板走線，就是電訊號變成光之前要先跑的銅線。[[sth-marvell-teralynx10-202407]]](img/media/ServeTheHome-Marvell51.2T交換器-202407-02.jpg)

**光模組裡面有什麼**？拆開一支 NVIDIA 的 800G 光模組來看：從插光纖那一端往裡，是光纖接頭、兩組雷射、一顆 DSP，最後是插進交換器的金手指；電訊號從金手指進來，光從光纖接頭出去[[chargerlab-nvidia-800g-teardown-20260708]]。要先說清楚：這支是 850 nm VCSEL（垂直面射型雷射，從晶片表面往上發光的小雷射）的短距模組，配多模光纖，最遠 50 公尺[[chargerlab-nvidia-800g-teardown-20260708,nvidia-linkx-100g-overview]]，**不是** CPO 用的那種矽光子模組。走 500 公尺的單模模組用 1310 nm 雷射，裡面的光學零件不一樣[[nvidia-mms4x00-nm]]。拿它來看「模組裡有雷射、DSP、光纖」沒問題。

![一支 800G 光模組拿在手上，帶拉環和散熱鰭片。這支是 850 nm VCSEL 短距模組（多模光纖、最遠 50 公尺），不是矽光子模組。[[chargerlab-nvidia-800g-teardown-20260708,nvidia-linkx-100g-overview]]](img/media/ChargerLAB-NVIDIA800G光模組拆解-20260708-01.jpg)
![拆開來，從左到右：拉環、兩個光纖接頭、兩組雷射（黃色方塊，透明細光纖直接接進雷射封裝）、DSP（銀色方塊）、金手指。電從右邊進來，光從左邊出去。[[chargerlab-nvidia-800g-teardown-20260708]]](img/media/ChargerLAB-NVIDIA800G光模組拆解-20260708-02.jpg)

![拿出來的電路板：左邊兩組 VCSEL 雷射負責發光，右邊那顆大晶片是 DSP，最右是金手指。[[chargerlab-nvidia-800g-teardown-20260708]]](img/media/ChargerLAB-NVIDIA800G光模組拆解-20260708-04.jpg)
![DSP 特寫，晶片上印 MARVELL IN080C0C，負責整理訊號和驅動。[[chargerlab-nvidia-800g-teardown-20260708]]](img/media/ChargerLAB-NVIDIA800G光模組拆解-20260708-05.jpg)

用矽光子做的模組裡面多了一片光的晶片（PIC）和一個 FAU。下面這張是一片 400G 矽光子模組電路板的專利圖，雷射、PIC、FAU、光纖、金手指都在一張裡；可以看到 FAU 不是 CPO 才有，今天的光模組裡就有一顆[[us12742940b2]]。一般整理的說法是：光模組的光引擎由 **EIC**（電的晶片：DSP、驅動器 Driver、轉阻放大器 TIA，TIA 把光偵測器送來的微弱電流放大成電壓）和 **PIC**（光的晶片：雷射、調變器、光偵測器）組成，再加上高階電路板、石英振盪器、光纖陣列和外殼散熱；DSP 是成本和功耗都排第一的零件[[stockfeel-dsp-20260930]]。EIC 和 PIC 在 CPO 裡怎麼分工，見 [光引擎、EIC、PIC](inside.md#q6)。

![一片插拔式矽光子模組的電路板，從上往下看。右邊一排長條（13）是插進交換器的金手指；12 是 IC；中間 2 是光的晶片（PIC），裡面的細線是光走的波導；4 是雷射，裝在晶片旁邊的導熱基板上；3 是 FAU，把光纖（31 送出、32 收進）對準晶片，左邊再接到光纖接頭。[[us12742940b2]]](img/patents/US12742940B2-FIG2.png){.s}

**問題出在晶片和光模組之間那一段**。交換器晶片在機器中間，光模組在前面板，晶片送出的電訊號要先走 **15 到 30 公分**的電路板銅線或跳線，才到得了光模組[[semianalysis-cpo-book]]。為了把訊號推過這段銅線，晶片要配長距離的 SerDes（把平行的資料轉成一條高速電訊號的電路，LR 是長距版），訊號到了光模組，還要先由 DSP 重新整理，才交給光引擎變成光[[semianalysis-cpo-book]]。一篇論文把這段路一站一站算出來：每條 200G 時，訊號從晶片經過封裝、電路板走線、穿孔到達模組，累積損耗約 22 dB，光是把資料從處理器搬到模組，每 bit 就要約 3.5 pJ（皮焦耳）[[arxiv-2601-14342]]。NVIDIA 的規格書也用同一個數字形容插拔式：22 dB[[nvidia-qx800-datasheet-20260911]]。

![插拔式的結構。交換器晶片（Switch ASIC）坐在封裝基板上，電訊號沿主機板上的長銅線（橘線，約 15 到 30 公分）跑到前面板的插槽（QSFP Connector），進了光模組（Transceiver Module）才變成光，再從光纖出去。[[semianalysis-cpo-book]]](img/semianalysis/img020.png){.s}

![訊號從晶片走到前面板模組，每一站都在流失（每條 200G）。橫軸四站：晶片到電路板、電路板走線、穿孔、插拔式模組。藍線是累積損耗，到模組時約 22 dB；紅線是每傳 1 bit 花的電，約 3 pJ 多。這些都是資料還沒變成光之前，在銅線上花掉的。[[arxiv-2601-14342]]](img/arxiv-2601.14342-vcsel-cpo-scaleup-fig2-loss-to-pluggable.png){.s}

**DSP 在做什麼**？速度越高，走線把訊號弄得越「髒」。這一代用的是 **PAM4**：用 4 個電壓高度代表資料，每一拍帶 2 個位元，比舊的 2 階訊號多送一倍，但 4 個高度擠在同樣的電壓範圍裡，更容易被雜訊干擾[[stockfeel-dsp-20260930]]。DSP（數位訊號處理晶片）在發射端負責重新對時、等化（補償走線造成的失真）和加上錯誤更正碼（FEC），在接收端做時脈回復、等化和糾錯，把被線路弄髒的訊號還原乾淨[[stockfeel-dsp-20260930]]。

<div class="scroll"><figure>
<svg viewBox="0 0 820 240" width="100%" role="img" aria-label="兩階訊號與 PAM4 四階訊號示意">
<text class="item" x="20" y="24">兩階（NRZ）：每一拍 1 位元</text>
<line class="dash" x1="60" y1="70" x2="380" y2="70"/><line class="dash" x1="60" y1="170" x2="380" y2="170"/>
<text class="note" x="34" y="75">1</text><text class="note" x="34" y="175">0</text>
<path class="solid" d="M60 70 H100 V170 H140 V70 H220 V170 H260 V70 H300 V170 H380"/>
<text class="note" x="74" y="196">1</text><text class="note" x="114" y="196">0</text><text class="note" x="154" y="196">1</text><text class="note" x="194" y="196">1</text><text class="note" x="234" y="196">0</text><text class="note" x="274" y="196">1</text><text class="note" x="314" y="196">0</text><text class="note" x="354" y="196">0</text>
<text class="item" x="430" y="24">四階（PAM4）：每一拍 2 位元</text>
<line class="dash" x1="475" y1="60" x2="795" y2="60"/><line class="dash" x1="475" y1="97" x2="795" y2="97"/><line class="dash" x1="475" y1="133" x2="795" y2="133"/><line class="dash" x1="475" y1="170" x2="795" y2="170"/>
<text class="note" x="440" y="65">11</text><text class="note" x="440" y="102">10</text><text class="note" x="440" y="138">01</text><text class="note" x="440" y="175">00</text>
<path class="solid" d="M475 60 H515 V133 H555 V170 H595 V97 H635 V60 H675 V170 H715 V133 H755 V97 H795"/>
<text class="note" x="486" y="196">11</text><text class="note" x="526" y="196">01</text><text class="note" x="566" y="196">00</text><text class="note" x="606" y="196">10</text><text class="note" x="646" y="196">11</text><text class="note" x="686" y="196">00</text><text class="note" x="726" y="196">01</text><text class="note" x="766" y="196">10</text>
<text class="note" x="20" y="228">同樣 8 拍：左邊送 8 個位元，右邊送 16 個。右邊四個高度之間的間隔只有左邊的三分之一，雜訊一大就容易看錯。</text>
</svg>
<figcaption>PAM4 是什麼。示意圖，非實際比例。[[stockfeel-dsp-20260930]]</figcaption></figure></div>

![「眼圖」：把一長串 0 和 1 疊在一起畫，中間空出來的「眼睛」越大，接收端越容易分辨。上：乾淨的訊號；中：走線損耗讓眼睛變小；下：訊號嚴重變形，眼睛快閉起來。DSP 的工作就是把下面這種訊號整理回來。[[arxiv-2601-14342]]](img/arxiv-2601.14342-vcsel-cpo-scaleup-fig4-eye-diagrams.png){.s}

**「800G」是怎麼組成的**？800G 指一個埠每秒 800 Gb，由好幾條「通道」（lane）並起來：可以是 8 條每條 100G，也可以是 4 條每條 200G[[nvidia-sn6000-manual-20260916]]。在平行單模光纖上，每條通道各佔一根送、一根收的光纖，所以 4 條通道的接頭要用 8 芯[[nvidia-sn6000-manual-20260916]]。

| 例子 | 通道 | 光纖接頭 | 功耗 |
|---|---|---|---|
| NVIDIA 800G 雙埠插拔式模組（MMS4X00-NM，單模 500 公尺）[[nvidia-mms4x00-nm,nvidia-sn6000-manual-20260916]] | 8 條 × 100G PAM4（兩個 400G 埠） | 兩個 MPO-12/APC，每個用 8 芯（4 送 4 收） | 最大 17 W |
| Spectrum-6 插拔式交換器 SN6600-LD 的一個 OSFP 插槽[[nvidia-sn6000-manual-20260916]] | 8 條 × 200G PAM4（雙 800G） | 插光模組 | — |
| Spectrum-6 CPO 交換器 SN6810-LD 的一個 MMC-16 接頭[[nvidia-sn6000-manual-20260916]] | 4 條 × 200G PAM4（一個 800G） | 16 芯 MMC 只用 8 芯（第 1–4、13–16 芯），中間 8 芯是不傳訊號的假光纖 | — |

MMC 這種接頭見 [MPO、MMC](passive.md#pas-mmc)。

**DSP 有多耗電、多貴**？它是光模組裡最耗電、也最貴的零件之一[[semianalysis-cpo-book]]。各方的數字不完全一樣，下面並排列出，不取平均。

| 說法的來源 | 800G 模組 | 其中 DSP | 1.6T 模組 | 其中 DSP | DSP 佔模組耗電 |
|---|---|---|---|---|---|
| 研究機構估計[[semianalysis-cpo-book]] | 16–17 W（DR4） | 6–7 W | — | 12–14 W | 約 50%（800G SR8） |
| 科技媒體[[tomshardware-npo-20260813]] | 14–17 W | 6–8 W | — | — | — |
| 投資網站整理[[stockfeel-dsp-20260930]] | 約 18 W | — | — | 10–14 W（DSP 加 SerDes，券商估） | 約 50% |
| NVIDIA 規格[[nvidia-mms4x00-nm]] | 最大 17 W（2xDR4） | — | — | — | — |
| 模組廠產品頁[[naddod-1p6t-2xdr4]] | — | — | 最大 25 W 以內（2xDR4，3 奈米 DSP） | — | — |
| 媒體報導[[36kr-coupe-20260607]] | — | — | 約 30 W | — | — |
| 媒體引 Arista 創辦人[[nextplatform-xpo-20260417]] | — | — | 1.6T OSFP 每支 30–40 W | — | — |

| 說法的來源 | DSP 佔模組成本 | DSP 單價 |
|---|---|---|
| 研究機構估計[[semianalysis-cpo-book]] | 20–30% | — |
| 券商估計（投資網站整理）[[stockfeel-dsp-20260930]] | 1.6T 插拔式模組物料約 450–550 美元，DSP 約 130–180 美元；另一家估 DSP 約 110 美元、佔 1.6T 矽光子模組約 29% | — |
| 券商專家會議紀要（媒體轉述）[[cnyes-hao-nomura-dsp-20260923]] | — | 長約價：800G 每顆 45–70 美元、1.6T 每顆 120–150 美元 |

放大到一座叢集來看：一個 1.8 萬顆 GPU 的 GB300 叢集、兩層網路，要用 18,432 支 800G 模組和 27,648 支 1.6T 模組，光是這些模組裡的 DSP 就要約 480 kW，平均每個機櫃約 1.8 kW；一個 20 萬顆 GPU 的叢集總共約 435 MW，其中約 17 MW 花在光模組上（研究機構估計）[[semianalysis-cpo-book]]。

**今天的光模組幾乎都還是兩端都有 DSP 的那種**。Marvell 說目前 800G 產品約 95% 是收發兩端都有 DSP 的 FRO，5% 是整顆 DSP 拿掉的 LPO（研究機構轉述）[[fundaai-cioe-20260916]]。1.6T 的 DSP 要用 3 奈米製程，一份券商專家會議的紀要說：2026 年需求超過 2,000 萬顆、實際出貨 1,600 萬到 1,700 萬顆，缺 300 萬到 400 萬顆；2027 年缺口擴大到 2,000 萬顆以上，產能要到 2027 年下半年才明顯開出[[allweather-nomura-dsp-202609,cnyes-hao-nomura-dsp-20260923,stockfeel-dsp-20260930]]。DSP 缺貨推動的是哪一種做法（只拿掉一半的 TRO、整顆拿掉的 LPO、第二供應商，還是 CPO），見 [DSP 缺貨推向哪裡](alternatives.md#alt-dsp)。

![一台交換器的電花在哪：藍色是交換器晶片，綠色是風扇和 CPU，黃色是光模組。102.4T 那一列，光模組吃掉的電（約 1,200 瓦）比晶片（約 1,000 瓦）還多。標 LD 的兩列是把模組裡的 DSP 拿掉之後（LPO，見第 4 題），整機少約 25%。[[synopsys-224g-lpo-2025q1]]](img/vendor/synopsys-ld-optics-switch-power-2025Q1-01.png)

換句話說，資料還沒變成光之前，已經在銅線和 DSP 上花掉不少電。交換器的速度一代一代翻倍，這段銅線越來越吃力。

## CPO 怎麼解決這個問題？ {#q3}

CPO（Co-Packaged Optics，共同封裝光學）的想法很直接：**把光引擎從前面板的光模組裡拿出來，搬到晶片旁邊，跟晶片封在同一個封裝裡**。電訊號只要在封裝基板裡走幾毫米就變成光，原本 15 到 30 公分的電路板走線縮短到毫米級[[cnyes-spectrumx-20260817,nvidia-qx800-datasheet-20260911]]。路變短，損耗從插拔式的約 22 dB 降到約 4 dB[[nvidia-qx800-datasheet-20260911]]；也因為路很短，模組裡的 DSP 可以拿掉，晶片上也能改用比較省電的短距 SerDes[[semianalysis-cpo-book]]。

![CPO 的結構（和上一題的插拔式圖同一套畫法）。左邊灰色是交換器晶片，旁邊 10 mm 就是光引擎：下面淺藍色的 EIC（電的晶片），上面藍色的 PIC（光的晶片）。PIC 右邊的棕色小塊是 FAU。一條光纖從 FAU 接到前面板的接頭，另一條接到外部雷射光源（Remote Laser Source）。橘色那段銅線只剩晶片到光引擎這一小段。[[semianalysis-cpo-book]]](img/semianalysis/img018.png){.s}

**實物長這樣**。NVIDIA Spectrum-X 光子交換器的封裝大約一個手掌大：中間那塊是交換器晶片，四周一圈 32 個小方塊就是光引擎，每邊 8 個[[sth-ces2026-spectrumx-202601,nvidia-blog-20260106]]。光引擎裡面有什麼見 [拆開來](inside.md#q5)。

![交換器晶片和光引擎封在一起的實物，拿在手上。中間是交換器晶片，四周一圈 32 個小方塊是光引擎。[[sth-ces2026-spectrumx-202601]]](img/ServeTheHome-CES2026-SpectrumX-CPO-202601-01-package-in-hand.jpg)
![同一顆封裝的廠商渲染圖：中間的大晶片由多塊拼成，四邊各 8 個光引擎，外圍是金屬框。[[nvidia-blog-20260106]]](img/vendor/nvidia-spectrumx-photonics-mcm-package-20260106-02.webp)

**裝進交換器之後，前面板就不插光模組了**。光纖直接從機器裡面的光引擎拉到前面板的光纖接頭。InfiniBand 的 Quantum-X800 Q3450-LD 規格寫 144 個 MPO 接頭（MPO：一個接頭裡排一整排光纖的多芯接頭）[[nvidia-qx800-datasheet-20260911]]；乙太網路的 SN6810-LD 前面板是 128 個更小的 MMC-16 接頭，四顆晶片的 SN6800-LD 是 512 個 MMC-16，另外有 64 個外部雷射模組（ELS）[[nvidia-sn6000-manual-20260916]]。三台都是液冷[[nvidia-qx800-datasheet-20260911,nvidia-sn6000-manual-20260916]]。光纖怎麼從封裝走到前面板見 [光纖怎麼接到前面板](passive.md#q16b)。

![CPO 交換器 Quantum-X800 Q3450-LD 的前面板（廠商產品照）。下面 4 排共 72 個方孔接光纖；規格書寫這台總共 144 個 MPO 光纖接頭，圖上看不出一個方孔裡是一個還是兩個接頭。上方 18 個較大的插槽圖上沒有標用途。面板上沒有插光模組的位置。[[nvidia-qx800-datasheet-20260911]]](img/vendor/nvidia-quantumx-q3450ld-switch-datasheet-20260911-01.jpg){.s}

![CPO 交換器 SN6810-LD（一顆 Spectrum-6），上：前面板，左右兩側成排的小方孔是 MMC-16 光纖接頭（規格寫 128 個）；下：背面，四個圓形是液冷快接頭（規格寫 2 進 2 出）。[[nvidia-sn6000-manual-20260916]]](img/nvidia-sn6810ld-front-rear-manual-p12-20260916-crop.png)
![四顆 Spectrum-6 的 SN6800-LD，上：前面板左右兩大片都是 MMC-16 接頭（規格寫 512 個）；下：背面十個圓形液冷快接頭（規格寫 5 進 5 出）。這台還有 64 個可抽換的外部雷射模組，手冊沒寫在前面還是背面。[[nvidia-sn6000-manual-20260916]]](img/nvidia-sn6800ld-front-rear-manual-p13-20260916-crop.png)

**整台機器省多少電**？最好懂的比法是同一顆晶片、兩種做法。NVIDIA 的 Spectrum-6 交換器晶片（102.4 Tb/s）同時有插拔式和 CPO 兩種機器，都是液冷：插拔式 SN6600-LD 裝兩端都有 DSP 的模組（FRO）時，典型功耗 3.3 kW；裝只有發射端有 DSP 的模組（TRO）時 2.79 kW；CPO 版 SN6810-LD 典型 1.96 kW、最大 2.2 kW[[nvidia-sn6000-manual-20260916]]。計算：CPO 比 FRO 版少 (3.3 − 1.96) ÷ 3.3 ≈ 41%，比 TRO 版少 (2.79 − 1.96) ÷ 2.79 ≈ 30%。手冊只寫插拔式是「裝 FRO／TRO 模組」時的典型值，沒寫裝了幾支、哪種模組。氣冷的插拔式 SN6600 更高，3.94 kW（FRO）、3.2 kW（TRO）[[nvidia-sn6000-manual-20260916]]。這是到 2026 年 10 月為止，唯一一組「同一顆晶片、整台機器」的公開數字；Broadcom、Arista、Cisco、Celestica 都沒有公布同一顆晶片插拔式對 CPO 的整台功耗。

<div class="scroll"><figure>
<svg viewBox="0 0 820 200" width="100%" role="img" aria-label="同一顆 Spectrum-6 晶片的三種交換器典型功耗">
<line class="grid" x1="310" y1="8" x2="310" y2="160"/>
<text class="item" x="10" y="38">插拔式 SN6600-LD（FRO 模組）</text>
<rect class="bar2" x="310" y="18" width="420" height="30"/>
<text class="item" x="740" y="38">3.3 kW</text>
<text class="item" x="10" y="88">插拔式 SN6600-LD（TRO 模組）</text>
<rect class="bar2" x="310" y="68" width="355" height="30"/>
<text class="item" x="675" y="88">2.79 kW</text>
<text class="item" x="10" y="138">CPO SN6810-LD</text>
<rect class="bar" x="310" y="118" width="249" height="30"/>
<text class="item" x="569" y="138">1.96 kW</text>
<text class="note" x="10" y="186">同一顆 Spectrum-6（102.4 Tb/s）、都是液冷的整台典型功耗。FRO：模組收發兩端都有 DSP；TRO：只有發射端有 DSP。</text>
</svg>
<figcaption>整台交換器的典型功耗，單位 kW。數據來自手冊[[nvidia-sn6000-manual-20260916]]，圖自己畫。</figcaption></figure></div>

**「省 70%」和「省 30%」量的不是同一件事**。常被引用的「CPO 比插拔式省 70% 以上」，是 Broadcom 對**光學部分**（每個埠的光引擎加雷射，對比一支光模組）講的；整台機器還有交換器晶片、風扇、CPU 的電，這些不會因為改 CPO 就變少。同一家 Broadcom 的晶片，做成整台 51.2T CPO 交換器的 Micas 說整機比插拔式省 40% 以上，同一篇報導裡 Broadcom 對光互連本身的說法是省 70%[[convergedigest-micas-cpo-2025]]。NVIDIA 的整台數字，對兩端都有 DSP 的插拔式省約 41%，對只留發射端 DSP 的插拔式只剩約 30%（上面的計算）。插拔式自己也在變省電：拿掉 DSP 的 LPO、只留一半 DSP 的 TRO，各家宣稱的省電幅度和整台比較見 [同一顆晶片整台耗電比較](alternatives.md#alt-power)。

**各家自己公布的效果**，比較的基準都不一樣，不能直接互相比：

| 誰 | 比的是什麼 | 數字 |
|---|---|---|
| NVIDIA | Spectrum-X 光子交換器，每個 1.6T 埠的功耗 vs 插拔式 | 少到五分之一[[nvidia-blog-20260106]] |
| NVIDIA | 光子交換器 vs 傳統做法：能效、訊號品質、雷射數量 | 能效 3.5 倍、訊號品質 63 倍、雷射少 4 倍[[nvidia-pr-20250318,nvidia-blog-20250826]] |
| NVIDIA（2026 年 8 月 Hot Interconnects 主題演講） | 光網路 vs 插拔式：耗電、雷射數、平均故障間隔（MTBI） | 耗電最多少 5 倍、雷射少 4 倍、MTBI 高 10 倍[[convergedigest-shainer-hoti-202608]] |
| NVIDIA | Q3450-LD 晶片到光的電訊號損耗 vs 插拔式 | 約 4 dB vs 22 dB[[nvidia-qx800-datasheet-20260911]] |
| NVIDIA（手冊） | 同一顆 Spectrum-6，整台 CPO vs 插拔式 | 1.96 kW vs 3.3 kW（FRO）／2.79 kW（TRO）[[nvidia-sn6000-manual-20260916]] |
| 台積電 | COUPE 放在封裝基板上 vs 電路板上的插拔式 | 能效 2 倍、延遲少 10 倍[[tsmc-pr-20260422]] |
| Broadcom | Tomahawk 6 Davisson 的光互連功耗 | 少 70%[[broadcom-pr-20251008]] |
| Broadcom（媒體轉述） | 每個 800G 埠，三代 CPO vs 插拔式 | 第一代（Tomahawk 4）約 6.4 W，同一台用插拔式約 16–18 W；第二代 Bailly 5.5 W；第三代 Davisson 約 3.5 W，比 Bailly 少 36.4%、比插拔式少 70% 以上[[nextplatform-broadcom-cpo-20251017]] |
| Micas（用 Broadcom Bailly） | 整台 51.2T CPO 交換器 vs 用插拔式模組的交換器 | 省 40% 以上[[convergedigest-micas-cpo-2025]] |
| 研究機構估計 | 每 800G：Q3450 的光引擎加外部雷射 vs 800G DR4 模組 | 約 4–5 W vs 16–17 W（少 73%）[[semianalysis-cpo-book]] |
| Meta 測試（研究機構轉述） | 每 800G：Broadcom Bailly 的光引擎加雷射 vs 800G 2xFR4 模組 | 約 5.4 W vs 約 15 W（少 65%）[[semianalysis-cpo-book]] |
| 媒體報導 | NVIDIA 給的 1.6T 一條連線 | 約 30 W 降到 9 W[[tomshardware-npo-20260813]] |
| NVIDIA Research（投影片，標明是業界通用的示意數字） | 假想一台 200 Tb/s 交換器的總 I/O 功耗 | 插拔式（FRO）約 4,000 W、CPO 約 1,200 W、光引擎放到矽中介層上約 600 W[[ascii-ohara-nvl576-p3-20260810]] |

![NVIDIA Research 在 2026 年 VLSI 研討會短課程的投影片：假想一台 200 Tb/s 交換器，三種做法的 I/O 耗電。第一列綠色是插拔式（FRO，晶片的長距介面走電路板）：晶片端介面 800 W、模組端介面 800 W、模組其他部分 2,400 W，總 I/O 約 4,000 W；第二列藍色是 CPO（短距介面走多晶片模組）：200＋200＋600 W，雷射 200 W，總共約 1,200 W；第三列橘色是 2.5D 光學（光引擎和晶片放在同一片矽中介層上，平行介面）：總共約 600 W。右邊小表的「封裝內 I/O 功耗」反而是 CPO 最高（1,000 W），因為原本在模組裡的電搬進了封裝。投影片右上註明：這些是業界通用的示意數字，不是任何一家的實作。[[ascii-ohara-nvl576-p3-20260810]]](img/media/ASCII-VLSI2026-SCT8-NVIDIA-slide49-200T交換器IO功耗-20260810.jpg)

上面這張投影片還點出一件事：CPO 把總耗電降下來，但原本散在前面板模組裡的電，有一部分搬進了晶片封裝（封裝內 I/O 功耗從 800 W 變成 1,000 W），封裝本身更熱[[ascii-ohara-nvl576-p3-20260810]]。CPO 交換器怎麼散熱見 [散熱](inside.md#q10b)。

**放到整座叢集，比例就小很多**。網路本身只佔一個 AI 叢集總耗電的約 9%（三層網路），所以一家研究機構估計，scale-out 網路全面改用 CPO，網路耗電少 23% 到 48%（看能不能從三層減成兩層），但整座叢集的總耗電只少 2% 到 4%[[semianalysis-cpo-book]]。另一個算法是 Arista 創辦人 Andy Bechtolsheim 2024 年算的：一個 10 萬顆、每顆 4 kW 的 XPU 叢集，GPU 本身 400 MW，連接它們的 640 萬支插拔式光模組要 192 MW，換成 LPO 降到 64 MW，換成 CPO 降到 42 MW（媒體轉述）[[nextplatform-broadcom-cpo-20251017]]。兩個算法的叢集大小、網路層數、模組種類都不同，數字不能互相換算。研究機構認為 CPO 真正的大用途在 scale-up（[第 5 題](#q4b)）[[semianalysis-cpo-book]]。

## 從插拔式到 CPO，中間有哪些階段？ {#q4}

光引擎不是一下子就從前面板跳到晶片旁邊，中間有好幾個階段。越往後越靠近晶片，電要走的路越短、省的電越多，但也越難做、越難維修。下面三張圖從不同角度畫同一件事。

![光引擎一步步靠近晶片。最上面是今天的插拔式：電訊號走長銅線（紅線）才到光模組。往下依序是板上光學（OBO，光引擎放在機殼內的主機板上）、近封裝光學（NPO，光引擎放在晶片旁另一塊基板上、插座式可拆）、2.5D 共同封裝（CPO，光引擎和晶片放在同一片基板上），最後是 3D 共同封裝（光的晶片直接疊在晶片的基板上）。圖上的年份是製圖者的預估，(e) 表示預估；OBO 和 NPO 兩欄註明「停在概念驗證」。圖上的 150 mm、50 mm 照原圖。[[technews-sipho-20260317]]](img/TechNews-矽光子商轉元年-20260317-01-roadmap-cross-sections.png)

![差別就在紅線那段電要走多遠。(a) 光引擎放在主機板上（板上光學），電要穿過兩層封裝再走主機板；(b) 放在晶片的封裝基板上，紅線短很多；(c) 放在中介層上、緊貼晶片，紅線最短。三種做法的雷射（ELS，外部光源）都在外面，用光纖送進光引擎。SerDes 是把資料轉成高速電訊號的電路；D2D 是晶片對晶片的短距介面。[[semianalysis-isscc2026]]](img/media/SemiAnalysis-ISSCC2026-CPO-20260415-02.jpeg){.s}

![另一種畫法：縱軸是電要走多長（公分 → 毫米 → 微米），橫軸是要傳多遠。右上是插拔式，電先走幾公分才變成光；往下是 OBO、2.5D CPO、3D CPO，電線縮到微米級。框裡的數字是兩端的對照：每傳 1 bit 從上百 pJ 降到 1 pJ 以下。紫色是 EIC，淺藍是 PIC。[[lsa-review-202601]]](img/lsa-s41377-025-02048-w-waveguide-couplers-review-fig16a-packaging-ladder.png){.s}

### 還插在前面板的折衷：TRO、LPO、XPO {#q4-pluggable}

**第一種折衷：模組還插在前面板，但把 DSP 拿掉一半或整顆拿掉**。這條路的出發點是 DSP 太耗電、太貴（[第 2 題](#q2)）。**LPO**（Linear Pluggable Optics，線性驅動插拔式模組）把模組裡的 DSP 整顆拿掉，由交換器晶片自己的 SerDes 直接驅動模組裡的雷射驅動器和接收端[[semianalysis-cpo-book,synopsys-224g-lpo-2025q1]]。每個 800G 埠的耗電降到約 7 到 8.5 W，代價是傳輸距離和不同廠牌互通變麻煩，光引擎也還是在前面板[[tomshardware-npo-20260813]]。一家研究機構估計，叢集的後端網路從 DSP 模組換成 LPO，光模組耗電少 36%、網路總耗電少 16%，但它也說 LPO 到現在還沒普及[[semianalysis-cpo-book]]；Marvell 說 800G 產品裡 LPO 約佔 5%[[fundaai-cioe-20260916]]。中間還有只拿掉一半的做法：NVIDIA 的 **TRO**（Transmit Retimed Optics）模組只在發射端放 DSP，接收端不放；兩端都放的叫 FRO[[nvidia-sn6000-manual-20260916]]。同一台 SN6600-LD 裝 TRO 比裝 FRO 少約 0.5 kW（[第 3 題](#q3)）。LPO、TRO 卡在哪、誰在推，見 [拿掉 DSP：LPO、TRO](alternatives.md#alt-lpo)。

![上：一般光模組，交換器晶片和雷射之間夾一顆 PAM-4 DSP 重新整理訊號；下：線性直驅（LPO 的做法），DSP 拿掉，交換器晶片的 SerDes 直接把訊號推到模組裡的驅動器（DRV）和雷射。DRV 是雷射驅動器，TIA 是接收端放大器，PD 是光偵測器。[[synopsys-224g-lpo-2025q1]]](img/vendor/synopsys-retimed-vs-linear-drive-2025Q1-02.png){.s}

**第二種折衷：XPO，一支更大的插拔式模組**。這是 Arista 主導、2026 年 3 月成立聯盟的新外形，成員有鴻騰精密、中際旭創、Coherent 等[[technews-trendforce-forum-20260529]]。它常被說成「可插拔式 CPO」，但照 Arista 公布的規格，**XPO 還是插在前面板的光模組，光引擎沒有離開前面板，不是 CPO**。一支模組 12.8 Tbps、64 條 200G 電通道，約 OSFP（今天常見的光模組外形）的 2.7 倍寬；裡面是兩片各 32 通道的電路板，腹對腹夾住中間一塊液冷冷板，發熱元件朝內貼著冷板；光纖接頭用 MPO-16[[arista-xpo-whitepaper-202603]]。DSP 可有可無，規格同時支援線性（沒有 DSP）、半 retimed 和全 retimed[[arista-xpo-whitepaper-202603]]。Arista 的說法是 CPO、OBO 在現場維修、擴充、製造上有重大挑戰，難以在雲端大量部署[[arista-xpo-whitepaper-202603]]；預計 2027 年量產[[nextplatform-xpo-20260417]]。誰加入、省不省電，見 [XPO](alternatives.md#alt-xpo)。2026 年 3 月同時成立了三個光互連標準組織：OCI、Open-CPX 和 XPO[[technews-trendforce-forum-20260529]]；其中 Open CPX MSA 由 Ciena、Coherent、Marvell、Molex、Samtec、TeraHop 發起，要統一「插座式光引擎」的介面，NPO 和 CPO 都適用[[tomshardware-npo-20260813]]。各種規格見 [各種規格](alternatives.md#alt-specs)。

![XPO 的爆炸圖（廠商渲染圖）：中間一塊液冷冷板，上下兩片電路板夾住它，前端是光纖接頭。[[arista-xpo-whitepaper-202603]]](img/vendor/arista-xpo-whitepaper-exploded-view-p4-202603.png){.s}

### 光引擎離開前面板：OBO、NPO {#q4-npo}

**板上光學（OBO）和近封裝光學（NPO）**。OBO 把光引擎放在機殼內的主機板上，比前面板近，但一家研究機構說它「兩邊的缺點都有」：有 CPO 的複雜，又留著插拔式的限制[[semianalysis-cpo-book]]。NPO 的光引擎放到晶片旁邊另一塊基板上，而且可以拆；晶片和光引擎之間還有一段短銅線[[semianalysis-cpo-book]]。媒體的整理是：NPO 夠近，可以拿掉 DSP，光引擎插在插座上，壞了能在現場換；焊在 CPO 基板上的光引擎就不行[[tomshardware-npo-20260813]]。

也有廠商認為 NPO 會撐好幾年：華星光預計 2027 到 2029 年 NPO 是主要出貨架構，理由是 CPO 良率不足、壞了難維修[[luxnet-slides-20260828,udn-luxnet-20260828]]。Broadcom 在 OFC 2026 另外推出了 3.2T、用 VCSEL 的 NPO 產品線，和它的 CPO 交換器並行[[tomshardware-npo-20260813]]。後來查到，多家雲端大廠和中國模組廠也被描述為先上 NPO，誰在推、什麼時候交貨，見 [NPO 是什麼、誰在推](alternatives.md#alt-npo) 和 [雲端大廠要買什麼](alternatives.md#alt-buyers)。

**界線也不總是很清楚**。NVIDIA 的兩款 CPO 交換器，封裝做法就不一樣。NVIDIA Research 在 2026 年 VLSI 研討會的投影片把它們並排：InfiniBand 的 Quantum-X（Q3450）是 28.8T 封裝，「插座式、外部雷射、光纖直接連在光引擎上（pigtailed）」；乙太網路的 Spectrum-X 是 102.4T 封裝，「焊死、外部雷射、光纖接頭可拆」[[ascii-ohara-nvl576-p3-20260810]]。Quantum-X 的光引擎裝在可拆的光學子模組上，雷射模組可以從面板抽出來，一家研究機構說嚴格一點的人會把它算成 NPO；NVIDIA 自己稱兩者都是 CPO[[semianalysis-cpo-book,tomshardware-npo-20260813]]。光纖接頭可拆不可拆的差別見 [為什麼要可拆](detachable.md#det-why)。

![NVIDIA 兩款 CPO 的封裝（廠商渲染圖，NVIDIA 投影片）。左：Quantum-X 光子交換器（Q3450），28.8T 封裝，標「插座式、外部雷射、光纖直接連在光引擎上」；中間是交換器晶片，四周的金屬件是插在插座上的光學子模組。右：Spectrum-X 光子交換器，102.4T 封裝，標「焊死、外部雷射、光纖接頭可拆」；四邊排著光引擎。右欄列：第一顆 1.6T 矽光子 CPO 晶片（新的微環調變器）、第一顆用台積電製程的 3D 堆疊矽光子引擎、高功率高效率雷射、可拆式光纖接頭、數百件專利授權給夥伴。[[ascii-ohara-nvl576-p3-20260810]]](img/media/ASCII-VLSI2026-SCT8-NVIDIA-slide19-CPO兩種封裝-Pigtailed與Detachable-20260810.jpg)

### 真正的 CPO 又分兩步 {#q4-cpo}

第一步是光引擎和交換器晶片放在**同一片封裝基板**上（上一題的圖），2026 年開始量產[[bnext-coupe-20260521]]。不是每一家都這樣分：測試介面廠穎崴 2026 年 5 月的法說（第三方整理，不是原話）說，「真正的 CPO 是將 Optical Engine 直接封裝在 Interposer (中介層) 上」，而不是早期放在基板上的 NPO，並預計 2028 年後才真正導入量產[[fugle-winway-20260514,fugle-winway-20260526]]；它的簡報趨勢頁（引 Counterpoint 的圖）把 NPO 寫在 2025、2.5D CPO（COUPE Switch）寫在 2027、3D CPO（COUPE XPU）寫在 2030 年起。這是穎崴的分類，和上面台積電、NVIDIA 把基板上的光引擎叫 CPO 的用法不同；兩種叫法並列，哪一種都不取。第二步是放到**中介層**（一片佈滿細密線路的薄板，夾在晶片和封裝基板之間）上，緊貼 GPU 這類運算晶片，連線更短更密[[semianalysis-cpo-book]]。台積電把自己的光引擎 COUPE 分成三階段，並說第一階段（用在插拔式模組上）「還不算真正的 CPO」；放到中介層上的那一步還沒有公布時程[[bnext-coupe-20260521]]，供應鏈預估 2028 年以後才會實現[[tianxia-coupe-20260818]]。越貼近 GPU 越難，業界有一句說法：「光怕熱，把光子引擎放在運算晶片旁，良率很難提高。」[[tianxia-coupe-20260818]]

![CPO 的下一步：交換器晶片和光引擎都放到同一片中介層（TSV 或有機中介層）上，EIC 和 PIC 之間用垂直的通孔接起來。和上一題的圖比，光引擎從另一塊小基板搬到了跟晶片同一片中介層上。[[semianalysis-cpo-book]]](img/semianalysis/img019.png)
![專利圖裡的同一件事：光引擎（170）和運算晶片（150，專利寫可以是 ASIC、CPU、GPU 等）並排放在同一片中介層（140）上；160 是另一顆晶片。光引擎右邊掛著 FAU（1016），裡面的光纖（1018）對準光引擎側邊的出光面，1402 是聚光的小透鏡。[[us20260283013a1]]](img/patents/US20260283013A1-FIG14.png)

![台積電 COUPE 的三階段（投影片頁尾標 2024）。左：用 COUPE 光引擎做的插拔式模組（1.6T，2025），放大框裡標 FAU、Si、EIC、PIC、基板；中：光引擎（SiPh 是矽光子晶片）圍著交換器晶片放在封裝基板上（6.4T，2026）；右：圍著 XPU（GPU 這類運算晶片）放在中介層上（12.8T，標「Pathfinding」，探索中）。下方 Power、Latency 是以插拔式為 1 的相對值：中間功耗不到 0.5、延遲不到 0.1，右邊功耗不到 0.1、延遲不到 0.05。[[semianalysis-cpo-book]]](img/semianalysis/img040.jpeg)

### 擺在一起看 {#q4-compare}

把這幾種做法放在一起，差別在三件事：光引擎離晶片多遠（也就是電要走的銅線多長）、DSP 還在不在、壞了能不能拔下來換。

<div class="scroll"><figure>
<svg viewBox="0 0 960 560" width="100%" role="img" aria-label="五種做法的光引擎位置與銅線長度示意">
<!-- row 0: pluggable -->
<text class="item" x="10" y="44" font-weight="600">插拔式</text><text class="note" x="10" y="64">（DSP 模組；XPO 同位置）</text>
<line class="grid" x1="220" y1="90" x2="940" y2="90"/>
<rect class="box" x="230" y="30" width="90" height="36"/><text class="item" x="260" y="54">晶片</text>
<path class="cu" d="M320 48 H332 V84 H770 V48 H782"/>
<rect class="hl" x="782" y="26" width="128" height="44"/>
<rect class="box" x="788" y="34" width="44" height="28"/><text class="note" x="794" y="53">DSP</text>
<rect class="box" x="838" y="34" width="66" height="28"/><text class="note" x="842" y="53">光引擎</text>
<path class="light" d="M910 48 H950"/>
<text class="note" x="230" y="112">光模組插在前面板；電先走 15–30 公分電路板，模組裡的 DSP 整理訊號，再變成光</text>
<!-- row 1: LPO -->
<text class="item" x="10" y="154" font-weight="600">LPO</text><text class="note" x="10" y="174">（模組裡沒有 DSP）</text>
<line class="grid" x1="220" y1="200" x2="940" y2="200"/>
<rect class="box" x="230" y="140" width="90" height="36"/><text class="item" x="260" y="164">晶片</text>
<path class="cu" d="M320 158 H332 V194 H770 V158 H782"/>
<rect class="hl" x="782" y="136" width="128" height="44"/>
<rect class="box" x="810" y="144" width="80" height="28"/><text class="note" x="828" y="163">光引擎</text>
<path class="light" d="M910 158 H950"/>
<text class="note" x="230" y="222">模組還在前面板，DSP 拿掉，由晶片的 SerDes 直接把訊號推過這段長銅線</text>
<!-- row 2: NPO -->
<text class="item" x="10" y="264" font-weight="600">NPO</text><text class="note" x="10" y="284">（近封裝）</text>
<line class="grid" x1="220" y1="310" x2="940" y2="310"/>
<rect class="box" x="230" y="250" width="90" height="36"/><text class="item" x="260" y="274">晶片</text>
<rect class="box" x="225" y="290" width="100" height="8"/>
<rect class="box" x="410" y="250" width="90" height="36"/><text class="note" x="430" y="273">光引擎</text>
<rect class="hl" x="404" y="290" width="102" height="10"/>
<path class="cu" d="M320 268 H340 V304 H392 V268 H410"/>
<path class="light" d="M500 268 H950"/>
<text class="note" x="230" y="332">光引擎在晶片旁另一片基板上，插在插座裡可拆；中間還有一段短銅線</text>
<!-- row 3: CPO on substrate -->
<text class="item" x="10" y="374" font-weight="600">CPO</text><text class="note" x="10" y="394">（同一片封裝基板）</text>
<line class="grid" x1="220" y1="420" x2="940" y2="420"/>
<rect class="hl" x="222" y="398" width="230" height="12"/>
<rect class="box" x="230" y="360" width="90" height="36"/><text class="item" x="260" y="384">晶片</text>
<rect class="box" x="345" y="360" width="90" height="36"/><text class="note" x="365" y="383">光引擎</text>
<path class="cu" d="M320 380 H345"/>
<path class="light" d="M435 378 H950"/>
<text class="note" x="230" y="442">光引擎和晶片在同一片封裝基板上，電只走幾毫米；光引擎焊在基板上，光纖接頭和雷射模組可拔</text>
<!-- row 4: CPO on interposer -->
<text class="item" x="10" y="484" font-weight="600">CPO</text><text class="note" x="10" y="504">（中介層上）</text>
<line class="grid" x1="220" y1="530" x2="940" y2="530"/>
<rect class="box" x="222" y="514" width="250" height="10"/>
<rect class="hl" x="226" y="504" width="200" height="9"/>
<rect class="box" x="230" y="466" width="90" height="36"/><text class="item" x="260" y="490">晶片</text>
<rect class="box" x="327" y="466" width="90" height="36"/><text class="note" x="347" y="489">光引擎</text>
<path class="cu" d="M320 486 H327"/>
<path class="light" d="M417 484 H950"/>
<text class="note" x="230" y="552">光引擎和運算晶片坐在同一片中介層上，貼得最近；還在探索</text>
</svg>
<figcaption>五種做法：灰框是晶片和光引擎，藍框是插拔式模組外殼（第一、二列）或光引擎所在的那一層（NPO 的小基板、CPO 的封裝基板、中介層），橘線是電要走的銅線，藍粗線是光纖。TRO 和 XPO 的光引擎位置跟第一列一樣，都在前面板模組裡；TRO 只留發射端 DSP，XPO 的 DSP 可有可無。雷射都沒畫，CPO 和 NPO 的雷射放在外面另外接光纖進來。示意圖，非實際比例。[[semianalysis-cpo-book,tomshardware-npo-20260813,semianalysis-isscc2026,arista-xpo-whitepaper-202603]]</figcaption></figure></div>

| 做法 | 光引擎在哪 | 晶片到光引擎的電路 | DSP | 壞了能不能拔 | 現況 |
|---|---|---|---|---|---|
| 插拔式（FRO） | 前面板的光模組裡 | 15–30 公分電路板[[semianalysis-cpo-book]] | 收發兩端都有[[nvidia-sn6000-manual-20260916]] | 整支拔[[tomshardware-npo-20260813]] | 主流；800G 約 95%（Marvell 說）[[fundaai-cioe-20260916]] |
| TRO | 同上 | 同上 | 只有發射端[[nvidia-sn6000-manual-20260916]] | 整支拔 | NVIDIA SN6600-LD 可選用[[nvidia-sn6000-manual-20260916]] |
| LPO | 同上 | 同上，由晶片 SerDes 直接驅動[[synopsys-224g-lpo-2025q1]] | 沒有[[semianalysis-cpo-book]] | 整支拔 | 還沒普及（研究機構說法）[[semianalysis-cpo-book]]；800G 約 5%（Marvell 說）[[fundaai-cioe-20260916]] |
| XPO | 前面板的光模組裡（一支 12.8T，兩片電路板夾液冷冷板）[[arista-xpo-whitepaper-202603]] | 同插拔式 | 可有可無（線性、半 retimed、全 retimed）[[arista-xpo-whitepaper-202603]] | 整支拔，可熱插拔[[arista-xpo-whitepaper-202603]] | 2026 年 3 月成立聯盟[[technews-trendforce-forum-20260529]]；預計 2027 年量產[[nextplatform-xpo-20260417]] |
| OBO | 機殼內主機板上[[semianalysis-cpo-book]] | 比插拔式短 | — | — | 製圖者註「停在概念驗證」[[technews-sipho-20260317]] |
| NPO | 晶片旁另一片基板[[semianalysis-cpo-book]] | 一段短銅線[[semianalysis-cpo-book]] | 可以拿掉（媒體）[[tomshardware-npo-20260813]] | 可以，插座式[[semianalysis-cpo-book]] | Broadcom 2026 年推出 NPO 產品線[[tomshardware-npo-20260813]]；華星光預計 2027–2029 年為主要出貨架構[[luxnet-slides-20260828]] |
| CPO（封裝基板上） | 和晶片同一片封裝基板[[bnext-coupe-20260521]] | 幾毫米[[nvidia-qx800-datasheet-20260911]] | 不需要[[semianalysis-cpo-book]] | 光引擎焊死；光纖接頭、雷射模組可拔[[nvidia-blog-20260106,tomshardware-npo-20260813]]（Quantum-X 是插座式）[[ascii-ohara-nvl576-p3-20260810]] | NVIDIA、Broadcom 的 CPO 交換器已出貨[[tomshardware-npo-20260813]]；台積電說 2026 年開始生產[[bnext-coupe-20260521]] |
| CPO（中介層上） | 和運算晶片同一片中介層[[semianalysis-cpo-book]] | 更短 | 不需要 | 不能單獨換光引擎 | 台積電「探索中」[[semianalysis-cpo-book]]；供應鏈預估 2028 年以後[[tianxia-coupe-20260818]] |

各種折衷的耗電、規格、誰在推，見 [插拔式的折衷](alternatives.md#alt-power)；CPO 量產到哪一步，見 [量產到哪一步](timing.md#q27)。

## Scale-up、scale-out 是什麼？CPO 用在 GPU、ASIC 還是 CPU？ {#q4b}

**先看 NVIDIA 怎麼分**。NVIDIA 在 Hot Chips 2026 的投影片把 AI 機房的網路分成五種，每種配一個產品[[sth-hotchips2026-nvidia-network]]：

![AI 機房的五種網路。左下 scale-up 是一個機櫃裡 GPU 之間（NVLink 交換器）；scale-out 是一排排機櫃之間（Spectrum-X 交換器、ConnectX 網卡）；scale-across 的箭頭指向另一整座資料中心；scale-in 從上方的 BlueField DPU 指進來；context scale 指向下方的儲存處理器。[[sth-hotchips2026-nvidia-network]]](img/media/ServeTheHome-HotChips2026-NVIDIA網路投影片-202608-01.jpg)
![五格並排：Scale-In（BlueField-4 DPU）、Scale-Up（NVLink）、Scale-Out（Spectrum-X 乙太網路）、Scale-Across（Spectrum-XGS 乙太網路，標多個機房的效能）、Context Scale（Vera BlueField-4 儲存處理器）。每格下面的倍數是 NVIDIA 自己宣稱的改善幅度。[[sth-hotchips2026-nvidia-network]]](img/media/ServeTheHome-HotChips2026-NVIDIA網路投影片-202608-04.jpg)

| 名稱 | 連的是什麼 | NVIDIA 的產品 | 今天用什麼線 | CPO 進度 |
|---|---|---|---|---|
| Scale-up（往上擴） | 同一組 GPU 之間直接相連，讓幾十、幾百顆 GPU 像一顆大晶片[[sth-hotchips2026-nvidia-network]] | NVLink | 銅線，最多 2 公尺[[semianalysis-cpo-book]]；Rubin 的 NVL72 仍是全銅[[sth-hotchips2026-rubin-nvl72]] | GTC 2026 路線圖上「NVLink 8 CPO」排在 2028 年的 Feynman 世代[[glennklockwood-gtc2026-recap-20260323]] |
| Scale-out（往外擴） | 伺服器和伺服器、機櫃和機櫃之間 | Spectrum-X 乙太網路（另有 Quantum InfiniBand） | 光纖加插拔式光模組 | 第一批 CPO 產品就在這裡，已進入量產部署[[semianalysis-cpo-book,tomshardware-npo-20260813,convergedigest-shainer-hoti-202608]] |
| Scale-across（跨機房） | 資料中心和資料中心之間[[sth-hotchips2026-nvidia-network]] | Spectrum-XGS 乙太網路 | 長距光纖 | 查不到 CPO 產品；Broadcom 也用這個詞[[broadcom-pr-ofc2026-20260312]] |
| Scale-in | 投影片標 BlueField-4 DPU（NVIDIA 的資料處理晶片）[[sth-hotchips2026-nvidia-network]] | BlueField-4 | — | 查不到 CPO 產品 |
| Context scale | 投影片標儲存處理器[[sth-hotchips2026-nvidia-network]] | Vera BlueField-4 儲存處理器 | — | 查不到 CPO 產品 |

跟 CPO 最有關的是前兩種。**Scale-out** 是伺服器和伺服器、機櫃和機櫃之間的網路，靠交換器把成千上萬台機器連起來。**Scale-up** 是同一組 GPU 之間直接連在一起，NVIDIA 的 NVLink 就是這種，今天用銅線，最多 2 公尺（[第 1 題](#q1)）[[semianalysis-cpo-book]]。Broadcom 的新聞稿也用 scale-up、scale-out、scale-across 三個詞，說它的乙太網路交換器三種都有[[broadcom-pr-ofc2026-20260312]]。

**兩種網路的量差很多**。Rubin 世代的 NVLink 6 每顆 GPU 3.6 TB/s[[nvidia-devblog-vera-rubin-pod-20260316]]；scale-out 用的網卡 CX9 是 1,600G[[glennklockwood-gtc2026-recap-20260323]]。Corning 在 2026 年 7 月的法說把它寫成：scale-up 每顆 GPU 14.4 Tb/s、scale-out 1.6 Tb/s，計算 14.4 ÷ 1.6 = 9 倍；它再用每條 200G、每條通道 2 根光纖去換算，如果 scale-up 全部改用光，每顆 GPU 要 144 根光纖，scale-out 只要 16 根，合計 160 根，是現在 scale-out 的 10 倍[[bullfincher-corning-q2-20260728]]。上一代也是同樣的比例：Blackwell 的 NVLink 每顆 GPU 單向 7,200 Gb/s，GB300 的 CX-8 網卡 800 Gb/s（研究機構整理）[[semianalysis-cpo-book]]。Corning 說今天 scale-up 是「100% 銅線，但光開始滲透」[[bullfincher-corning-q2-20260728]]。光纖用量怎麼算、每顆 GPU 實際會用多少，見 [scale-up 什麼時候用光](timing.md#tm-scaleup)。

**兩家公司對「scale-up 有多大」的說法**，範圍和量法不同，不能直接比。MaxLinear 執行長 2026 年 4 月的法說說：「Today, about 30% of optical transceiver TAM is for scale-up and 70% is for scale-out.」（光模組可服務市場裡，約 30% 是 scale-up 用、70% 是 scale-out 用）[[fool-maxlinear-q1-20260423]]。這是 MaxLinear 替自己的市場做的分法，算的是光模組，不是 NVLink 那種機櫃內的連線；上面表裡說機櫃內今天是銅線，兩句不矛盾，只是範圍不同。另一個數字量的是流量：Marvell 2026 年 10 月投資人日上，講者說「today scaleup represents greater than 85% of the data center traffic」（scale-up 佔資料中心流量的 85% 以上），其餘 15% 是 scale-out，並說 scale-up 的光學「is here and now」[[youtube-marvell-investor-day-20261006]]。這是 Marvell 的說法，不是第三方量測；來源是 YouTube 自動字幕，沒有說話人，未校對。（兩者一個量市場金額，一個量流量，沒有共同基準。）

**CPO 先進的是 scale-out**。NVIDIA 在 2025 年 GTC 宣布的第一批 CPO 產品就是 scale-out 網路交換器[[semianalysis-cpo-book,nvidia-pr-20250318]]，也就是 Quantum-X 和 Spectrum-X 光子交換器；Broadcom 的 Bailly、Davisson 也是交換器[[broadcom-pr-20251008]]。NVIDIA 的 Shainer 在 2026 年 8 月說，CPO 已經進入量產，用在 scale-out 那種要跨整座 AI 工廠的距離；短距的 scale-up 盡量用銅[[convergedigest-shainer-hoti-202608]]。

**下一步是 scale-up，光引擎要貼到 GPU 或 ASIC 旁邊，但各家說的時間點不一樣**。NVIDIA 在 GTC 2026 的路線圖投影片上，Rubin 那一欄（2026）的 CPO 只有 scale-out 用的「Spectrum6 102T, CPO」，scale-up 的「NVLink 8 CPO」要到 Feynman 那一欄（2028）才出現[[glennklockwood-gtc2026-recap-20260323]]；官方部落格的寫法是 Feynman 世代用 Kyber 做 scale-up，「銅線和共同封裝光學都有」，scale-out 用 Spectrum 系列光學[[nvidia-blog-gtc2026-20260319]]。只看這一句，容易讀成 scale-up CPO 很快就來；路線圖上的位置是 2028 年。在那之前，NVIDIA 的 8 櫃、576 顆 GPU 的 NVL576 寫的是「銅線和直接光學連接」，NVIDIA 的投影片寫「第一層交換器以上用光、以下用銅」，都沒有說是 CPO[[nvidia-devblog-vera-rubin-pod-20260316,ascii-ohara-nvl576-20260810]]。大家拿來當 NVL576 照片的那排機櫃，NVIDIA 自己註明是 Blackwell（GB200）做的原型 Polyphe[[nvidia-devblog-vera-rubin-pod-20260316,ascii-ohara-nvl576-20260810]]。NVL576 櫃與櫃之間到底是插拔式、NPO 還是 CPO，各家說法對不上，見 [NVL576 和 Rubin Ultra](timing.md#tm-nvl576)。

![GTC 2026 主題演講的路線圖投影片（直播截圖）。三欄：Blackwell（2024）、Rubin（2026）、Feynman（2028）。Rubin 欄的晶片有 Rubin、Rubin Ultra、NVLink 6 Switch、NVLink 7 Switch（都標 3600 GB/s）、Spectrum6 102T CPO、CX9 1600G；機櫃有 Oberon NVL72／NVL576、Oberon ETL256、Kyber NVL144。Feynman 欄才出現「NVLink 8 CPO」和「Spectrum7 204T, CPO」，機櫃有 Kyber NVL144／NVL1152。也就是 scale-out 的 CPO 交換器在 2026 年，scale-up 的 CPO 交換晶片排在 2028 年。[[glennklockwood-gtc2026-recap-20260323]]](img/vendor/glennklockwood-gtc26-optical-scaleup-slide-202603-01.png)

![NVIDIA 在 2026 年 VLSI 研討會短課程的投影片，標題「NVIDIA Vera Rubin Ultra NVL576」，副標「兩層全互連的 NVLink scale-up 拓撲，576 顆 GPU」。左邊標「第一層（L1）以上用光、以下用銅」。照片下方的說明寫的是：NVIDIA Polyphe，一套能完整運作、以 Blackwell 做的多機櫃 NVL576 原型。照片裡中間 8 櫃各拉出黃色光纖往上進走線架；解析度太低，數不出每個托盤幾條線，也看不出接頭種類。[[ascii-ohara-nvl576-20260810]]](img/media/ASCII-VLSI2026-SCT8-NVIDIA-slide12-NVL576-Polyphe光上銅下-20260810.jpg){.s}

銅線這一側也在往後撐。最大的客製 ASIC 廠 Broadcom 的執行長 Hock Tan，同一個人在三個月內對 CPO 講過兩種口風：2026 年 3 月：「Even as we are the lead in CPO, CPOs will come in its time. Not this year, maybe not next year.」（CPO 的時間會到，不是今年，也許也不是明年）[[broadcom-fy26q1-call-20260304]]；2026 年 6 月：「in CPOs, which is co-packaged optics, 1.6 terabit DSPs, CW and EML lasers, we are the de facto standard in the industry」（在 CPO，我們是業界的事實標準）[[broadcom-fy26q2-call-20260603]]。前一句講客戶大量用的時間，後一句講 Broadcom 在供應商裡的位置，兩句放在一起看。他在 2026 年 3 月的法說還說，2028 年走到 400G SerDes 時，XPU 客戶「很可能會繼續用直連銅纜」，因為光學更貴、要多很多電；scale-up 在機櫃內「能用直連銅纜就用越久越好」[[broadcom-fy26q1-call-20260304]]。6 月的法說又說，機櫃內的 scale-up 用 200G、400G SerDes 的直連銅纜，推動「共同封裝銅線」（co-packaged copper，把銅纜接頭直接做在封裝旁）[[broadcom-fy26q2-call-20260603]]。另一邊，AMD、Broadcom、Meta、Microsoft、NVIDIA、OpenAI 在 2026 年 3 月成立了 OCI MSA（光學 scale-up 的共同規格），目的是「讓 scale-up 從銅線架構遷移到光學架構」，支援插拔式、板上、CPO 三種外形，不綁 CPO[[broadcom-pr-oci-msa-20260312]]。誰說銅線撐到什麼時候、scale-up 的第一個光學產品是什麼，見 [scale-up 什麼時候用光](timing.md#tm-scaleup)。

台積電 COUPE 的第三階段就是「CPO with XPU」，光引擎圍著 GPU 這類運算晶片（[第 4 題](#q4-cpo)）[[semianalysis-cpo-book]]。一家研究機構的看法是：CPO 對 scale-out 有些幫助，但會是 scale-up 頻寬成長的主要推手；scale-up 互連的市場規模已經比 scale-out 網路大得多，CPO 的市場也會以 scale-up 為主[[semianalysis-cpo-book]]。

scale-up 改用光，也不一定是 CPO。Google 的 TPU 在 scale-up 裡已經有一段是光，但用的是光路交換器（OCS）加光模組，見 [Google 的光路交換器](timing.md#tm-ocs)；另一條是用很多條慢速通道、VCSEL 或 Micro LED 加多模光纖的「慢而寬」，見 [慢而寬](timing.md#tm-wide)。

Computex 2026 上，緯穎和 Ayar Labs、創意（GUC）、Corning、Molex、上詮、TE、Senko 一起展示了一套 scale-up 用的 CPO 機器：Ayar Labs 的光引擎和外部雷射模組（ELSFP），配上機櫃級整合、液冷和光纖走線[[senko-wiwynn-computex2026]]。

![給 scale-up 用的 CPO 展示機（廠商展示照）。右邊打開的托盤裡，兩顆標 GUC 的晶片封裝各自拉出黃色光纖，銅色的是液冷板和水管。左邊展板列出這條路上的零件：Ayar Labs 的 TeraPHY 光引擎（標「專為 AI scale-up 打造」）、Senko 的可拆式光纖接頭和 SN-MT 接頭、ELSFP 主機端接頭，以及 Ayar Labs 的外部雷射模組 SuperNova（ELSFP，一種可插拔的雷射光源模組規格）。[[senko-wiwynn-computex2026]]](img/vendor/senko-wiwynn-computex2026-components-202607-05.jpeg)

![處理器（190）、記憶體（180）和光引擎（EN）放在同一片中介層（110）上。光引擎由光的晶片（120）和電的晶片（140）組成；FAU（170）從上方插進插座（70），對準 PIC 表面的光柵耦合器（20）。[[us20260191101a1]]](img/US20260191101A1-FIG10I-processor-memory-optics-package.png)
![光引擎貼著運算晶片的另一種提案：左邊 XPU 是運算晶片（GPU、ASIC 都算），旁邊的 UCIe 是晶片之間接線的介面標準，再過去是光引擎（OE），直接拉出一束光纖。右邊放大：光引擎用的是 VCSEL 和光偵測器（PD），光經過透鏡進光纖。這是 VCSEL 路線，不是 NVIDIA、台積電用的矽光子。[[arxiv-2601-14342]]](img/arxiv-2601.14342-vcsel-cpo-scaleup-fig1-ucie-vcsel-link.png)

**ASIC**：Broadcom 幫客戶的 AI ASIC 加 CPO；一家研究機構的了解是，這是 OpenAI 選 Broadcom 的關鍵因素之一，同一份分析也說 Google 是對 CPO 最猶豫的大型雲端業者[[semianalysis-cpo-book]]。Marvell 的 3D 光引擎和客製 XPU 放在同一片基板上[[marvell-pr-20250106]]；Marvell 在 2026 年 10 月的投資人日說，scale-up 光學今天幾乎沒有營收，明年開始有數億美元，每顆 XPU 的光學含量是「數千美元，連結兩端都有」（研究機構轉述）[[futurum-marvell-investor-day-20261009]]。三星有一件專利把處理器、記憶體和光引擎放在同一片中介層上（上圖左）[[us20260191101a1]]。**CPU**：Intel 有給 CPU、GPU 用的光學 I/O chiplet[[intel-oci-20240626]]；除此之外，素材裡沒有 CPU 用 CPO 的產品或時程。

**需求在哪**：在 AI 叢集的網路。一家研究機構算過，網路是整個 AI 叢集裡僅次於伺服器的第二大成本，在一個 GB300 NVL72 叢集、三層 InfiniBand 網路裡佔總成本 15%，四層網路佔 18%；三層網路裡，光模組佔網路成本的 60%（用 NVIDIA 自家模組時）、網路耗電的 45%[[semianalysis-cpo-book]]。這也是為什麼省下光模組的電和錢，會被當成一件大事。

## 還不知道的 {#basics-open}

- Marvell 說的「scale-up 佔流量 85%」怎麼算：講者沒說基準（哪一年、哪些客戶、是 GPU 之間的流量還是全部）；投資人日的簡報原檔，或 Marvell 12 月初 FY27Q3 法說（日期見 [日曆](calendar.md#cal-events)）。

- 除了 NVIDIA 之外，同一顆交換器晶片「插拔式對 CPO」的整台功耗：Broadcom 只給每埠瓦數，Micas 只給百分比，Cisco、Arista、Celestica 沒有 CPO 機種的整機數字。可以等 OCP Global Summit 2026（10/12–15，Broadcom 預告展 CPO）看展出的整機規格（日期見 [日曆](calendar.md#cal-events)）。
- 200G 時銅線到底能走多遠：IEEE 工作組目標「至少 1 公尺」、論文說被動銅纜不到 1 公尺、NVIDIA 手冊只列 1.1 公尺主動銅纜、Marvell 說 2.5 公尺；Marvell 的 2.5 公尺是被動還是主動、量的是什麼線，要看投資人日簡報原檔（Marvell IR 網站），或 12 月初 Marvell FY27Q3 法說。
- 「共同封裝銅線」會不會讓 scale-up 改光再往後延：Broadcom、NVIDIA 都在推，出貨量查不到；可以看 12 月中 Broadcom FY26Q4 法說。
- NVL576 櫃與櫃之間用插拔式、NPO 還是 CPO：NVIDIA 書面只寫「銅線和直接光學」；要等 GTC Washington, D.C.（11/30–12/3）和 GTC 2027（2027-03-14～18）。細節見 [NVL576 還不知道的](timing.md#tm-open)。
- NVIDIA 在 2026 年 VLSI 短課程的完整投影片：日本媒體只轉貼了約 8 頁，完整講義可能有 NVL576 光學形式和更多 CPO 封裝細節；從 VLSI Symposium 官網短課程頁、IEEE Xplore 查。
- NVIDIA Hot Chips 2026 的完整投影片（五種網路那幾頁之外）要會員帳號，只看得到媒體轉貼的部分。
- OCI MSA 第一代規格（一個 scale-up 埠用幾根光纖、要不要 FAU、雷射放哪）：本輪沒抓到 oci-msa.org；可以等 OCP Global Summit 2026（10/12–15）。
