# CPO 與 FAU

2026-10-12。CPO（共同封裝光學）和 FAU（光纖陣列單元）的研究筆記，按主題拆成 13 份，互相連結。每份筆記句尾的小數字是參考資料編號，點了跳到那份筆記最後的參考資料；每條都標了可信度（一手、公司說、媒體報、第三方、KOL）。查不到的寫查不到，每份最後一節是「還不知道的」。

## 一頁講完 {#summary}

**CPO 是什麼。** AI 資料中心裡，晶片之間的資料越傳越快，銅線走得越來越短。現在的做法是在交換器前面板插光模組，晶片的電訊號要先走一段 15 到 30 公分的銅線才變成光。CPO 把負責電光轉換的「光引擎」搬到晶片旁邊、封在一起，銅線只剩幾毫米。同一顆 NVIDIA 交換器晶片，CPO 版整台比插拔式省約 30% 到 41% 的電，看比的是哪一種插拔式模組（[基礎](basics.md#q3)、[折衷方案](alternatives.md#alt-power)）。

**光怎麼走。** 雷射放在機器外面，經保偏光纖把光送進光引擎；光引擎由電的晶片（EIC）疊在光的晶片（PIC）上，NVIDIA 和 Broadcom 的都在台積電做（COUPE）。資料印到光上之後，經過 FAU 接到光纖，再經機內整線送到前面板（[拆開來](inside.md#q5)）。FAU 就是把一整排光纖排好、固定、對準晶片入口的零件，難在微米以下的精度一路疊上去，對位和固定的良率決定成本（[FAU 本身](fau.md#q11)）。

**現在到哪。** 已經出貨的 CPO 全部是交換器（scale-out），量還小。GPU 之間（scale-up）NVIDIA 現在全用銅線，自己的路線圖把 NVLink 的 CPO 放在 2028 年；NVL576 機櫃之間用什麼，NVIDIA 沒有寫過「CPO」，流傳的照片是 Blackwell 的原型（[時間點](timing.md#tm-scaleup)）。在這之前，雲端大廠多半被描述成先走 NPO（光引擎插在晶片旁的插座上，由模組廠做），插拔式也在拿掉 DSP、變成 XPO（[折衷方案](alternatives.md#alt-npo)）。

**誰在做 FAU。** 台廠說已在交貨的只有上詮，小量；大立光目標 2027 年中。中國的天孚說穩定量產，主要經泰國的 Fabrinet 出去。Corning、Coherent、住友電工都說自己做 CPO 用的 FAU，雷射廠和光纖廠在把整條光路一起賣。封測廠日月光的年報也寫了 FAU 主動對位封裝。誰實際把 FAU 貼上 NVIDIA 的光引擎，NVIDIA、台積電、日月光、矽品都沒有公開說（[誰在做 FAU](fau-makers.md#q22)、[玩家](players.md#pl-nv)）。

**值多少錢。** 一台 Quantum-X CPO 交換器 72 個 FAU；單價沒有公司公開，照調研紀要的單價算，一台約 3,600 到 7,200 美元，而整台材料成本 7 萬多美元。同一份紀要裡，雷射那一層的金額比 FAU 高（[誰在做 FAU](fau-makers.md#fau-value)、[雷射](lasers.md#las-count)）。

## 原本的看法怎麼被改寫 {#rewrite}

一開始的看法是「FAU 是 CPO 的瓶頸，台廠（大立光、上詮）靠台積電 COUPE 吃到這塊」。四輪調查之後，查到的事實是：

| 原本以為 | 查到的 | 在哪份筆記 |
|---|---|---|
| FAU 是瓶頸 | 「瓶頸」在不同報告裡指不同東西：雷射產能、測試、光引擎良率、FAU 耦合都有人說。台積電副總列的瓶頸是雷射、光纖、光纖連接器和測試，沒有單獨講 FAU。雷射廠自己說做不夠 | [雷射](lasers.md#las-shortage)、[設備測試](equipment-test.md#eq-test) |
| FAU 是一塊大生意 | 一台交換器的 FAU 約佔整機材料成本的一成以下（計算）；有出處的 CPO FAU 市場估計 2027 年 12 億人民幣 | [誰在做 FAU](fau-makers.md#fau-value) |
| FAU 經過 COUPE 給台廠做 | 至少五條路不經台廠 FAU：天孚經泰國 Fabrinet；Corning、Coherent、住友自己做；NPO 由模組廠做；Broadcom 的 FAU 線束由 Corning 供；華為整套自己做 | [誰在做 FAU](fau-makers.md#fau-routes)、[中國](china.md#cn-overview) |
| FAU 是一個固定黏死的零件 | 可拆式接頭把它拆成兩半：黏在晶片上的接座、裝著 FAU 的插頭。最精密的一步可能移到接頭廠、晶圓廠或封測廠。NVIDIA 兩款交換器一款固定、一款可拆 | [可拆式](detachable.md#det-structure)、[FAU 本身](fau.md#fau-types) |
| 大量很快就來 | 現在只有交換器。scale-up 的 CPO 在 NVIDIA 路線圖上是 2028；有研究機構說放量在 2029。「Rubin Ultra 用 CPO」在 NVIDIA 的話裡找不到 | [時間點](timing.md#tm-nvl576) |
| 上詮已經在吃 CPO | 上詮 2026 年第二季跳接線佔營收 78%、毛利率約 0.2%；FAU 機台預算到第三季只花了 7%；泰國廠做的是跳接線，不是 CPO 封裝；最大客戶的公開資料和 Corning 對得上 | [誰在做 FAU](fau-makers.md#q25) |
| 設備商吃到 CPO | 設備商的光通訊訂單大多是插拔式模組；CPO 設備營收各家都很小；公告看得到的大買家是封測廠 | [設備測試](equipment-test.md#eq-orders) |
| 中國 FAU 廠比台廠前面 | 前面的是零件和插拔式用的 FAU；CPO 用的 FAU，兩邊各只有一兩家說在交貨 | [中國](china.md#cn-fau) |

上面每一格都只寫查到的事實。哪些說法還沒有一手資料、要等哪一場法說才知道，在 [日曆](calendar.md#x2)。

## 筆記 {#notes}

照這個順序讀最順：

| 筆記 | 回答什麼 |
|---|---|
| [CPO 是什麼、為什麼需要](basics.md) | 銅線為什麼不夠、現在的光怎麼接、CPO 省多少電、從插拔式到 CPO 有哪些階段、scale-up 和 scale-out |
| [插拔式的折衷：LPO、TRO、XPO、NPO](alternatives.md) | 不做 CPO 也能省電的幾種做法、各種規格、DSP 缺貨推向哪裡、雲端大廠要買什麼 |
| [拆開來：一道光在 CPO 裡怎麼走](inside.md) | 光引擎、EIC、PIC、SOI、透鏡、雷射為什麼在外面、散熱、台積電 COUPE 的下一步 |
| [FAU 本身](fau.md) | FAU 是什麼、一台用幾個、固定和可拆、為什麼難、怎麼做、怎麼對位、怎麼測、光纖 |
| [誰在做 FAU、值多少錢、賣給誰](fau-makers.md) | 台、中、日、美各家的進度，一台值多少，賣給誰，不經 COUPE 的路，大立光和上詮 |
| [可拆式接頭、玻璃橋](detachable.md) | FAU 會變成什麼、誰在做、有沒有標準、保偏光纖會不會被拿掉、康寧玻璃橋 |
| [雷射、外部光源、InP](lasers.md) | 從銦到雷射模組的幾層、誰說缺、一台用幾顆、台廠在哪一層、擴產 |
| [對位設備、測試、封測廠](equipment-test.md) | 對位機台、測試分段、訂單看得到多少、公告裡誰向誰買、封測廠做不做 FAU、可靠度 |
| [光纖、前面板接頭、機內整線](passive.md) | MPO 到 MMC、授權、機內整線、光纖和預製棒、被動件廠和它們的客戶、載板 |
| [誰主導、代工廠、新創、供應鏈全圖](players.md) | NVIDIA、Broadcom、台積電的角色，誰實際在供 NVIDIA，「暫離 COUPE」傳聞，專利 |
| [現在到哪、什麼時候變大](timing.md) | 量產到哪、scale-up 什麼時候用光、NVL576、Google OCS、VCSEL 和 Micro LED、市場多大 |
| [中國自己的路線](china.md) | 華為、阿里、騰訊的 NPO，中國的規格和接頭，中國 FAU 廠，出口管制 |
| [接下來能驗證什麼](calendar.md) | 法說和大會日曆、每場要看什麼、最初三篇 Threads 的說法查到什麼、還查不到的 |

最近的幾場：台積電第三季法說 10/15、OCP 大會 10/12–15、Corning 10/27、Lumentum 11/5、台股第三季財報 11/14 前（[日曆](calendar.md#cal-events)）。
