# 現在到哪、什麼時候變大、會被什麼取代

這份筆記回答三件事：CPO 現在做到哪一步、GPU 之間（scale-up）的光什麼時候才會真的用到、市場會長多大又會被什麼取代。先分清楚兩種網路：**scale-out** 是機櫃和機櫃之間的網路，靠交換器把成千上萬台機器連起來，CPO 現在出貨的就是這裡；**scale-up** 是同一組 GPU 之間直接相連（NVIDIA 的 NVLink），今天還是銅線。兩者的定義和差別見 [Scale-up、scale-out 是什麼](basics.md#q4b)。

原本的看法是「FAU 是 CPO 的瓶頸，台廠（大立光、上詮）經由台積電 COUPE 吃到這塊，2027 年隨 Rubin Ultra 起量」。後來幾輪查到的事，有幾件讓時間點和量都要重新看，先列在這裡，細節在各節：

- **已經出貨的 CPO 全是 scale-out 交換器，沒有任何一家出貨 scale-up 用的 CPO。** 量大的 scale-up CPO，NVIDIA 自己的路線圖投影片排在 2028 年的 Feynman 世代；有研究機構的付費報告把量產時點推到 2029。（[scale-up 什麼時候用光](#tm-scaleup)）
- **「NVL576 用 CPO」在 NVIDIA 的書面資料裡找不到。** NVIDIA 只寫過「銅線和直接光學連接」和「L1 以上用光、L1 以下用銅」；各方對櫃與櫃之間用插拔式、CPO、NPO 還是 OCS 的說法有七種，彼此對不上。大家拿來當「NVL576 長這樣」的照片，是 Blackwell（GB200）做的原型。（[NVL576 和 Rubin Ultra](#tm-nvl576)）
- **「Rubin Ultra Kyber 2H27 CPO」這句話，查得到的源頭都不是 NVIDIA。** 台灣報導裡把訂單掛在 Rubin Ultra 上的說法，沒有一則是公司自己說的。Rubin Ultra 本身也傳出從四顆運算晶粒改成兩顆，Kyber 機櫃傳出延到 2028；NVIDIA 只回「路線圖不變」。（[NVL576 和 Rubin Ultra](#tm-nvl576)）
- **銅線還在加碼。** Broadcom 說客戶到 2028 年 400G SerDes 都「很可能繼續用直連銅纜」；Amphenol 推 448G 的共同封裝銅線；NVIDIA 說改液冷有一部分是為了在銅線裡塞更多 GPU。（[scale-up 什麼時候用光](#tm-scaleup)）
- **scale-up 光學最早的營收，出現在 NPO 和光纜，不是 CPO。** Credo 的 scale-up NPO 和 LED 光纜、Marvell 的 scale-up 光引擎，都說 2027 年中到 2028 年開始有營收。（[scale-up 什麼時候用光](#tm-scaleup)）
- **Google 的 scale-up 早就有光，但是光路交換器（OCS），不是 CPO。** 這是 FAU 以外的另一個光纖陣列市場，供應鏈裡幾乎看不到台廠。（[Google 的 OCS](#tm-ocs)）
- **NVIDIA 把「慢而寬」研究專案暫停，理由是光纖和連接器太貴，不是光學做不出來。** 同時有 NVIDIA 工程師具名支持一種新的 1060 nm 小芯徑多模光纖，進了 IEEE 802.3ds 的討論。（[慢而寬](#tm-wide)）
- **台積電說「量產」，但沒給量，也沒給中介層版本的年份。** 2027 年光引擎出貨，券商的模型和市場預期差了 3 到 4 倍。（[量產到哪一步](#q27)、[卡在哪](#q27b)）
- **「COUPE 加台廠 FAU」這組合沒有任何公開的可靠度數據。** 公開的大量數據全來自 Meta 實驗室裡的 Broadcom 交換器。（[量產到哪一步](#q27)）
- **公司自己的口風這半年多半是往前拉或沒變，沒有一家公開把 CPO 的時點往後改。** 這次對過逐字稿的公司裡：Marvell 的 scale-up 光學數字從 1.5 億美元一路改到「比一季前想的大很多」；Corning 一月還不把 scale-up 放進預測，四月說近期有機會；Astera Labs 從「最早 2028、2029 年」改成「2027 年 NPO、2028 年起 CPO」。唯一往後挪的是新易盛對外部 OCS 需求的時點（六月「明年下半年或 2028 年」，七月只剩 2028 年）。Broadcom 執行長三個月內有兩種說法：三月「CPO 不是今年，也許不是明年」，六月「CPO 我們是業界事實標準」。（[同一家公司的說法，隨季度怎麼變](#tm-quotes)）

## CPO 現在量產到哪一步？ {#q27}

交換器已經在出貨，但量還小，而且出貨的全是 scale-out 用的交換器。最早出貨的是 Broadcom：51.2T 的 Bailly 從 2024 年起在系統廠 Micas 量產，102.4T 的 Davisson 2025 年 10 月開始交貨給客戶[[tomshardware-npo-20260813]]；不過到 2026 年初，這些交換器的出貨量都還「非常低」[[semianalysis-cpo-book]]。

### 台積電說的「量產」

台積電的說法前後換過幾次口徑，值得並排看：

- **2024 年的投影片**：2025 年做插拔式（OSFP）用的 1.6T 光引擎；2026 年「CPO with Switch」，6.4T 光引擎放在基板上；第三階段「CPO with XPU」，12.8T 光引擎放在中介層上，標明還在探索（pathfinding）[[tomshardware-cpo-foundry-20260803]]。
- **2026 年 4 月北美技術論壇新聞稿**：COUPE 放在基板上的真正 CPO「beginning production in 2026」，比電路板上的插拔式省 2 倍功耗、延遲降 10 倍，用在 200G 的微環調變器（MRM）上[[tsmc-pr-20260422]]。
- **2026 年 5 月台灣技術論壇**：投影片改用銅線當基準，COUPE 放在電路板上功耗效率 2 倍，放在基板上 4 倍，延遲都低於銅線的 0.1 倍；放在中介層上 10 倍、延遲低於 0.05 倍。同場的說法是放在基板上的版本是「2026 年下半年」，中介層版是「下一步」，沒有給年份[[technews-coupe-forum-20260514]]。
- **2026 年 7 月 16 日第二季法說**：分析師問 COUPE 什麼時候對營收有實質貢獻，魏哲家答「We start the production right now, and it will be ramped up.」，沒有給金額或時程[[allmind-tsmc-q2-20260716]]。
- **2026 年 8 月 31 日 SEMICON 論壇**：先進封裝技術發展副總說 CPO 自今年下半年開始量產[[youfenxi-tsmc-semicon-20260831]]。

<div class="pair">

![台積電 2024 年投影片：COUPE 三階段。2025 年插拔式的 1.6T 光引擎，2026 年基板上的 6.4T 光引擎，第三階段中介層上的 12.8T 光引擎，標「in Pathfinding」。圖上有 FAU 的位置。（台積電投影片，媒體轉載）[[tomshardware-cpo-foundry-20260803]]](img/media/TomsHardware-TSMC-COUPE路線圖-20260803-01.png)
![台積電 2026 年台灣技術論壇投影片（台積電提供的現場照）：以銅線為基準的四欄比較，電路板上、基板上、中介層上的功耗效率和延遲。圖上標有 FAU。（台積電投影片）[[technews-coupe-forum-20260514]]](img/media/TechNews-台積電2026技術論壇COUPE三階段-20260514-01.jpg)

</div>

台積電的新聞稿和法說都沒有點名客戶[[tsmc-pr-20260422,allmind-tsmc-q2-20260716]]。客戶這邊自己說的只有 NVIDIA：Spectrum-X CPO 交換器用台積電的 COUPE，已經開始向合作夥伴出貨[[udn-nvidia-tsmc-cpo-20260603]]。法人和媒體說 2026 到 2027 年的量產客戶可能是 NVIDIA、Broadcom、AMD，2028 年才是聯發科、Marvell、Ayar Labs[[trendforce-pic-capacity-20260708]]。

至於「NVIDIA 暫離 COUPE、改走 Tower」的傳聞，沒有任何一手資料證實或否認，見[「NVIDIA 暫離 COUPE」傳聞](players.md#pl-coupe)。

同一個詞，不同人的用法不同。測試介面廠穎崴 2026 年 5 月法說（第三方整理，不是原話）說：真正的 CPO 是把光引擎直接封在中介層上，放在基板上的是 NPO；預計 2028 年後才真正導入量產[[fugle-winway-20260514,fugle-winway-20260526]]。它法說簡報的趨勢頁（引用市調機構的圖）把 NPO 標 2025 年、2.5D CPO（COUPE Switch）標 2027 年、3D CPO（COUPE XPU）標 2030 年起[[mops-yingwei-slides-20260514]]。這和台積電把放在基板上的 COUPE 也叫 CPO、NVIDIA 已在 2026 年 8 月出貨的用法不同；看到穎崴的時點，要知道它指的是中介層版。

### NVIDIA 的交換器

NVIDIA 在 2026 年 1 月 CES 的主題演講上拿出了 Spectrum-X 光子交換器的封裝實物[[sth-ces2026-spectrumx-202601]]；6 月 1 日 Computex 期間說這款交換器「已全面量產」，並點名台積電做矽光子晶片、矽品做封裝測試、天孚和鴻海也各負責一段[[nvidia-blog-20260601]]。產品在 2026 年 5 到 7 月進入生產，8 月 14 日 NVIDIA 宣布正式出貨，首批客戶是 CoreWeave、Lambda 和甲骨文[[cnyes-spectrumx-20260817]]。

![NVIDIA 在 Computex 2026 宣布量產時的配圖（廠商渲染圖）：CPO 交換器是一台裝在機櫃裡的抽屜式機器，拉開就是裝著光引擎的封裝。[[nvidia-blog-20260601]]](img/vendor/nvidia-computex2026-spectrumx-photonics-production-20260601-01.jpg)

### 模組廠、設備商怎麼說量產，被問到「延後」怎麼回 {#tm-delay}

模組龍頭中際旭創在 2026 年 8 月 23 日的投資人記錄裡說：CPO 目前看到客戶已宣布量產，主要用在 scale-out，未來逐步用在 scale-up；未來的光連接不會是單一方案，而是可插拔、NPO、CPO 等多種並存[[cninfo-innolight-irm-20260823]]。

市場上有「CPO 延後、NPO 提前」的說法（NVIDIA 暫離 COUPE 的傳聞見[這一節](players.md#pl-coupe)）。查得到的公司回應如下；這些都是被問到一般性「有沒有延後」時的回答，不是對 COUPE 傳聞的回應：

- **Coherent**（2026-08-12 法說會轉錄稿，AI 轉寫）：執行長說 "we have seen absolutely no push out of CPO demand. In fact, it is been the opposite."；NPO 和 CPO 單一應用裡的內容金額「很接近」，客戶有先 NPO 再轉 CPO 的，也有直接上 CPO 的；過去三到六個月，客戶對 CPO、NPO 的接洽強度大幅上升[[allmind-coherent-q4fy26-20260812]]。
- **Corning**（2026-07-28 法說會轉錄稿，AI 轉寫）：分析師問過去兩個月有沒有變、市場傳 scale-up 供應鏈準備度不足和延後。執行長答：圈外看起來的「戲劇性」比實際少得多，公司在做的是建一個 100 億美元新光子平台的穩定工作；圈內人都知道，依其他零件供應商和出貨狀況，可以做哪些取捨來照樣交付 scale-up，所以實際的變動比外面猜的少很多[[allmind-corning-2026q2-20260728]]。
- **羅博特科**（設備商，ficonTEC 母公司，投資人記錄）：2025-12-25 答「CPO 产业落地节奏并未如您所说的市场传言般放缓，目前呈现正常推进甚至加快的态势」；2026-07-21 被問到市場上的延遲傳聞，答「公司关注到市场上关于 CPO 延迟的各类传言，但作为设备端，公司未从任何客户处获得 CPO 延迟的消息。」相隔七個月被問同一件事，答法一致；同一份七月記錄還說客戶的訂單和交貨時間壓力持續加強[[cninfo-ficontec-irm-20251225,cninfo-robotechnik-irm-20260721]]。這是設備端的說法，不是證實。
- **Cisco**（2026-02-11 法說會轉錄稿）：執行長說 "we absolutely believe it's going to happen. We don't believe it's actually imminent right now."，又說很多客戶希望光學和矽晶片分開買，「才有選擇、不被綁住」[[fool-cisco-q2-20260211]]。NVIDIA 把 CPO 和 GPU 一起賣的做法見[CPO 是跟 GPU 綁在一起賣，還是可以單獨買](players.md#q17b)。

另一邊，零件廠談時程的口徑不一，見[卡在哪](#q27b)的最後一段。

### 接下來的時間點

接下來的時間點，大多是公司自己說的計畫，還沒發生。Coherent 的說法（經轉述）是：手上有 10 個以上 CPO 客戶專案，scale-out 用的 CPO 在 2026 年第四季開始放量，scale-up 用的 CPO 和 NPO 在 2027 年下半年[[futurum-coherent-photonlink-20260923,futurum-coherent-q4fy26-20261009]]。Lumentum 在 2026 年 2 月說拿到一筆數億美元的追加訂單，買的是支援 scale-out 光學的超高功率雷射（不是整套 CPO 模組），2027 年出貨，5 月法說說是 2027 年上半年[[lumentum-q2fy26-20260203,fool-lumentum-q2fy26-20260203,fool-lumentum-q3fy26-20260506]]。大立光的 FAU 目標 2027 年中出貨[[cna-largan-q3-20261008]]。Credo 說 scale-up 用的 NPO 有確定的設計導入，2027 年 5 月起算的會計年度（FY28）開始量產；LED 光纜也是 FY28 開始有營收（Credo 的 FY2026 結束於 2026-05-02，所以 FY28 約是 2027-05 到 2028-04，計算）[[fool-credo-fy27q1-20260901,sec-credo-10k-20260615]]。Marvell 簡報上自家 400G 光引擎和 OCI 規格的光引擎標 2027 年[[marvell-investor-day-deck-20261006]]。

更遠的一步，光引擎放上中介層、貼著 GPU：供應鏈的估計是 2028 年以後[[tianxia-coupe-20260818]]；NVIDIA 的 GTC 2026 路線圖投影片把「NVLink 8 CPO」排在 2028 年 Feynman 欄[[glennklockwood-gtc2026-recap-20260323]]，黃仁勳的說法是 Feynman 世代的 scale-up「銅線和共同封裝光學都有」，沒有給年份[[nvidia-blog-gtc2026-20260319]]。有研究機構的付費報告把 scale-up CPO 的量產時點從市場預期的 2027 到 2028 年推到 2029 年，理由是幾個專案要到那時才會匯集、矽中介層上的光引擎整合要到那時才成熟（只有媒體轉述，原報告要付費）[[techflow-semianalysis-powereddown-20260610]]。Corning 的說法是 Feynman「大概要到 2029、2030 才會是主力系統」[[bullfincher-corning-q2-20260728]]。這些時點的出處和彼此的差別，在 [scale-up 什麼時候用光](#tm-scaleup)。

<div class="scroll"><figure>
<svg viewBox="0 0 960 800" width="100%" role="img" aria-label="CPO 出貨與預定時間表">
<text class="head" x="20" y="28">CPO 出貨與預定時間表</text>
<circle class="bar" cx="470" cy="23" r="7"/><text class="note" x="484" y="28">已經發生</text>
<circle class="hl" cx="580" cy="23" r="7"/><text class="note" x="594" y="28">公司說的計畫</text>
<circle class="dash" cx="720" cy="23" r="7"/><text class="note" x="734" y="28">估計、傳聞，或沒給年份</text>
<line class="grid" x1="180" y1="50" x2="180" y2="785"/>
<g>
<text class="item" x="20" y="75">2024</text><circle class="bar" cx="180" cy="70" r="7"/><text class="item" x="200" y="75">Broadcom 51.2T Bailly 在系統廠 Micas 量產</text>
<text class="item" x="20" y="111">2025 年 10 月</text><circle class="bar" cx="180" cy="106" r="7"/><text class="item" x="200" y="111">Broadcom 102.4T Davisson 開始交貨</text>
<text class="item" x="20" y="147">2026 年 1 月</text><circle class="bar" cx="180" cy="142" r="7"/><text class="item" x="200" y="147">NVIDIA 在 CES 台上展示 Spectrum-X 光子交換器封裝</text>
<text class="item" x="20" y="183">2026 年 4 月</text><circle class="hl" cx="180" cy="178" r="7"/><text class="item" x="200" y="183">台積電新聞稿：COUPE 放在基板上的版本「2026 年開始生產」</text>
<text class="item" x="20" y="219">2026 年 5–7 月</text><circle class="bar" cx="180" cy="214" r="7"/><text class="item" x="200" y="219">NVIDIA Spectrum-X 光子交換器進入生產（6 月 1 日宣布全面量產）</text>
<text class="item" x="20" y="255">2026 年 7 月 16 日</text><circle class="bar" cx="180" cy="250" r="7"/><text class="item" x="200" y="255">台積電法說：「We start the production right now」，沒給量</text>
<text class="item" x="20" y="291">2026 年 8 月 14 日</text><circle class="bar" cx="180" cy="286" r="7"/><text class="item" x="200" y="291">NVIDIA 宣布出貨，首批客戶 CoreWeave、Lambda、甲骨文</text>
<text class="item" x="20" y="327">2026 年第四季</text><circle class="hl" cx="180" cy="322" r="7"/><text class="item" x="200" y="327">Coherent：scale-out 用的 CPO 開始放量（10 個以上 CPO 專案）</text>
<text class="item" x="20" y="363">2027 上半年</text><circle class="hl" cx="180" cy="358" r="7"/><text class="item" x="200" y="363">Lumentum：數億美元的超高功率雷射追加訂單交貨（scale-out 用）</text>
<text class="item" x="20" y="399">2027 年中</text><circle class="hl" cx="180" cy="394" r="7"/><text class="item" x="200" y="399">大立光：FAU 加 Carrier 目標出貨；Credo scale-up NPO、LED 光纜（2027-05 起）</text>
<text class="item" x="20" y="435">2027 下半年</text><circle class="hl" cx="180" cy="430" r="7"/><text class="item" x="200" y="435">Coherent：scale-up 用的 CPO、NPO</text>
<text class="item" x="20" y="471">2028</text><circle class="hl" cx="180" cy="466" r="7"/><text class="item" x="200" y="471">NVIDIA 路線圖投影片：「NVLink 8 CPO」配 Feynman NVL1152</text>
<text class="item" x="20" y="507">2028</text><circle class="dash" cx="180" cy="502" r="7"/><text class="item" x="200" y="507">台積電 MRM 路線表：單排 FAU 換成雙排 FAU（媒體整理）</text>
<text class="item" x="20" y="543">2028 以後</text><circle class="dash" cx="180" cy="538" r="7"/><text class="item" x="200" y="543">光引擎放上中介層、貼著 GPU（供應鏈估計，台積電沒給年份）</text>
<text class="item" x="20" y="579">2029</text><circle class="dash" cx="180" cy="574" r="7"/><text class="item" x="200" y="579">研究機構付費報告：scale-up CPO 量產（媒體轉述）</text>
<text class="item" x="20" y="615">2029–2030</text><circle class="dash" cx="180" cy="610" r="7"/><text class="item" x="200" y="615">Corning：Feynman 才會是主力系統</text>
<text class="item" x="20" y="651">年份沒公布</text><circle class="dash" cx="180" cy="646" r="7"/><text class="item" x="200" y="651">NVIDIA Feynman 世代：scale-up「銅線和共同封裝光學都有」</text>
<text class="note" x="200" y="700">已經發生的（實心點）全是交換器，也就是 scale-out；GPU 之間的 scale-up 還沒有出貨的 CPO。</text>
<text class="note" x="200" y="722">NVL576 櫃與櫃之間用什麼，NVIDIA 沒有書面說明（見 NVL576 和 Rubin Ultra 一節）。</text>
</g>
</svg>
<figcaption>CPO 出貨與預定時間表。示意圖，非實際比例；時間軸不等距。[[tomshardware-npo-20260813,sth-ces2026-spectrumx-202601,tsmc-pr-20260422,nvidia-blog-20260601,allmind-tsmc-q2-20260716,cnyes-spectrumx-20260817,futurum-coherent-photonlink-20260923,lumentum-q2fy26-20260203,cna-largan-q3-20261008,fool-credo-fy27q1-20260901,glennklockwood-gtc2026-recap-20260323,tomshardware-cpo-foundry-20260803,tianxia-coupe-20260818,techflow-semianalysis-powereddown-20260610,bullfincher-corning-q2-20260728,nvidia-blog-gtc2026-20260319]]</figcaption></figure></div>

### 量有多小

先看埠數。一家研究機構的執行長估計，2025 年全世界 CPO 加 NPO 的埠數不到 100 萬個，五年內每年的出貨埠數會超過 1 億個[[tomshardware-npo-20260813]]。再看台數。2026 年和 2027 年一年會出幾台 CPO 交換器，各家估計差得很遠，範圍也不同（有的算全市場，有的只算 NVIDIA 的 scale-out）：

| 誰估 | 範圍 | 2026 年 | 2027 年 | 更遠 |
|---|---|---|---|---|
| 美國券商[[technews-sipho-20260317]] | CPO 交換器 | 約 2.3 萬台（主要是 NVIDIA 的 100T Spectrum） | 樂觀 5.9 萬台 | 2030 年 20 萬台 |
| 中國券商[[technews-gf-cpo-axt-20260818,ctee-browave-gf-20261001]] | NVIDIA 的 scale-out CPO 交換器 | 1.5 萬台（全落在第四季） | 10 萬台（第一季 1.6 萬、第二季 3 萬） | — |
| 美國券商[[ltn-bofa-cpo-switch-20260717]] | NVIDIA 的 CPO 交換器 | — | 年增 2.7 倍 | 2028 年再年增 2.65 倍，2028–2029 年放量 |
| 法人（經媒體）[[ltn-bofa-cpo-switch-20260717]] | 鴻海集團工業富聯的 CPO 交換器 | 出貨目標上看 5 萬台以上，製造市佔約 9 成 | — | — |
| 鴻海董事長[[caixun-foxconn-agm-20260609]] | CPO 交換器 | 今年開始出貨，將達到萬台水準 | 「數倍成長」 | — |
| 專家（用連續波雷射供應量反推）[[cnyes-hao-cpo-shipments-20260608]] | 全球 CPO 交換器 | 約 3 萬台（450 萬顆雷射 ÷ 每台約 130 顆） | 25–30 萬台 | — |
| 未具名公司的調研紀要[[eastmoney-dfau-survey-20260531]] | CPO 交換器 | — | 約 30 萬台 | 2028 年 50–60 萬台 |
| 閉門會紀要[[gewo168-cpo-passive-20260530]] | CPO 交換器 | 若 1 萬台 | 至少 10 萬台級 | 2028 年數十萬台 |
| 研究機構[[trendforce-cpo-bottleneck-20260727]] | CPO 交換器 | 已進入量產（只有定性） | 2027–2028 放量 | — |

2027 年的估計從 5.9 萬台到 30 萬台，差五倍。券商在 10 月初還在更新：台積電為了支援 NVIDIA 的量產，已擴充 CPO 測試與檢測產能、新增 Insertion 2 和 3 的設備，系統整合 9 月初起在無塵室進行[[ctee-browave-gf-20261001]]。鴻海方面，10 月 11 日的報導重述的仍是「今年開始出貨、會達到 1 萬台的水準，明年數倍成長」；這和上表 5 萬台的法人估計對不上，也沒有新的一手數字[[udn-ocp-preview-20261011]]。

光引擎的數量也有兩種模型。一家投行（經媒體轉述）的模型是 2027 年光引擎出貨 600 到 700 萬顆，市場預期是 2,000 到 3,000 萬顆；差距來自 SoIC 接合的良率（約 50–60%）和下游組裝的良率（約 20–50%）[[udn-ms-cpo-yield-20260611]]。PIC 晶圓的產能，法人的說法是月產能約 500 片，到 2026 年第二季 1 萬片、第四季 1.5 萬片、2028 年至少 2.5 萬片；以每片 648 顆算，1 萬片一個月約年產 7,800 萬顆 PIC[[trendforce-pic-capacity-20260708]]；同一家投行寫的則是 2027 年第一季才擴到每月 1 萬片[[udn-ms-cpo-yield-20260611]]。台積電的 COUPE 產線在竹南還是嘉義，查不到任何一篇報導。

一位投信董事總經理說得直接：裝了 COUPE 交換器托盤的機櫃今年頂多貢獻一季，「今年比較是宣示、象徵性量產，明後年量才比較明朗。」[[tianxia-coupe-20260818]]

FAU 這一頭，一台交換器用幾個 FAU、單價多少、整個 FAU 市場有多大，見[一台交換器裡 FAU 值多少錢](fau-makers.md#fau-value)和[對營收的貢獻](fau-makers.md#fau-revenue)。

### 可靠度：有多少真實數據

CPO 到底可不可靠，公開的大量數據只有一組：Meta 在實驗室裡用 15 台 Broadcom 的 51.2T Bailly 做的測試，累積時數隨場合越講越大（論文是 104.9 萬個 400G 埠裝置小時，後來的演講講到 1,500 萬、5,000 萬、9,000 萬小時），口徑不一。這些都不是台積電 COUPE 的交換器，也沒有任何大規模正式部署的數據。主要故障來源是外部雷射模組，不是光引擎。細節和各說法的對照見[可靠度數據](equipment-test.md#eq-reliability)。

### OCP 這一週

OCP Global Summit 2026 在 10 月 12 日到 15 日舉行。這份筆記寫成時（10 月 12 日）還沒有任何一場講完，能查到的只有會前的新聞稿和講者自己提交的摘要，沒有新產品發表：

- Broadcom 會在 Celestica、台達、Micas 三個攤位展出第三代 TH6-Davisson CPO 的整機；Davisson 是 2025 年 10 月就發表的產品，所以這是第三方整機展示，不是新晶片[[broadcom-ocp-pr-20261008]]。
- Meta 的三位工程師 10 月 14 日講 102.4T 的整合光學交換器：1.5 OU、100% 液冷、無風扇；64 個光學埠走 16 個「四埠 MMC」介面；16 個 ELSFP 模組供外部雷射，讓雷射的壽命和交換晶片脫鉤；和插拔式比，光學功耗約少 60%、系統功耗約少 30%。摘要用「整合光學」一詞，同時涵蓋 CPO 和 NPO，沒寫這台是哪一種[[ocp2026-agenda-20261012]]。
- NVIDIA 的 Gilad Shainer 10 月 14 日的演講摘要列出首顆用新微環調變器的 1.6T CPO 晶片、3D 堆疊矽光引擎、高功率雷射、可拆式光纖接頭，說 CPO 交換器正在進入量產，並說會「更詳細地回顧它的製造流程」[[ocp2026-agenda-20261012]]。
- 台灣廠商出現在 OCP 光學場次的，是系統廠和連接器廠：緯穎、鴻海集團的 FIT、啟碁、貿聯；2026 年 621 場議程裡沒有大立光、上詮、波若威、光聖、台積電的場次（計算：議程講者公司欄全文搜尋）[[ocp2026-agenda-20261012]]。這不代表他們不在供應鏈裡，只是 OCP 是雲端客戶講架構的場合。

這幾場講完、投影片上線之後要補查的清單，在本篇最後的[還不知道的](#tm-open)。

## scale-up 什麼時候才會用光？ {#tm-scaleup}

**先看現在長什麼樣。** NVIDIA 的 Vera Rubin NVL72 機櫃，72 顆 GPU 靠第六代 NVLink 的「銅脊椎」連在一起：每顆 GPU 3.6 TB/s，整櫃 260 TB/s；機櫃背面 4 個銅纜匣、約 5,000 條銅纜，總長超過 2 英里[[nvidia-devblog-vera-rubin-pod-20260316]]。NVIDIA 在 2026 年 VLSI 研討會短課程的投影片寫的是 5,184 條、每條 200 Gb/s、每條約 0.2 到 1.0 公尺[[ascii-ohara-nvl576-p3-20260810]]。Hot Chips 2026 的 Rubin 演講投影片寫「全銅 scale-up 機櫃」、沒有 retimer、托盤無線無風扇[[sth-hotchips2026-rubin-nvl72]]。

<div class="pair">

![NVL72 機櫃背面的銅纜脊椎：4 個銅纜匣（NVIDIA 技術部落格的圖，廠商產品照）。[[nvidia-devblog-vera-rubin-pod-20260316]]](img/vendor/nvidia-mgx-rack-copper-spine-cartridges-20260317-01.webp)
![NVIDIA 在 VLSI 2026 短課程投影片裡畫的 GB200 NVL72 銅背板：4 個 spine cartridge、5,184 條銅纜，每條 200 Gb/s、約 0.2–1.0 公尺。（NVIDIA 投影片，經日本媒體轉貼）[[ascii-ohara-nvl576-p3-20260810]]](img/media/ASCII-VLSI2026-SCT8-NVIDIA-slide10-GB200-NVL72銅背板5184條-20260810.jpg)

</div>

**為什麼銅線會走不下去？** 速度越高，銅線能走的距離越短。Microsoft 的論文畫了一張圖：每條銅線 100 Gbps 以上，最遠只剩 2 到 3 公尺；光的連結則是速度越高越耗電[[microsoft-mosaic-paper]]。各家對「200G 以上銅線還能走多遠」的說法並不一致：

![銅線和光連結的速度對照。上：銅線連結的最遠距離，隨速度提高縮到 2–3 公尺（800 Gbps 約 2 公尺）；下：光連結的耗電（一條連結兩端各一個收發器），800 Gbps 約 24 W。（Microsoft 研究院論文的圖）[[microsoft-mosaic-paper]]](img/papers/sigcomm25-mosaic-copper-reach-optical-power-fig1.png){.s}

| 誰 | 怎麼說 |
|---|---|
| Microsoft | 銅線可靠省電，但「小於 2 公尺」，所以 scale-up 只能塞在單一機櫃、每櫃幾百 kW[[microsoft-mosaic-blog-20261010]] |
| Marvell | 200G 時銅線只能走 2.5 公尺[[futurum-marvell-investor-day-20261009]] |
| Lightmatter | SerDes 接近 448G 時，銅線能走的距離縮到「幾十公分」[[lightmatter-ocp-initiative-20260813]] |
| Broadcom | 銅線支援到 4 公尺（業界常見 2 公尺）；櫃內 scale-up 現在最多 1.04 Pb/s，下一步 2.08 Pb/s，跨出單櫃就要別的方案[[broadcom-khamisy-blog-202610]] |
| Meta | GB300 機櫃已有數千對差動訊號的電背板，超過 144 顆就碰到銅的極限；超過 256 顆的網域「很可能需要光」[[convergedigest-meta-ofc2026]] |
| OpenAI | 機櫃內短距銅仍是最佳選擇，銅不夠時用插拔式[[fundaai-ecoc2026-20260929]] |
| 一家做 AEC 的美國公司 | 以 72 顆 GPU 當銅線上限，說光纜一跳可以把 GPU 網域擴到 300 顆以上[[fundaai-ecoc2026-20260929]] |

反過來，**銅線這邊也有人說能撐更久**：

| 誰 | 怎麼說 |
|---|---|
| Broadcom 執行長 | 「當我們在 2028 年走到 400G SerDes，我們的 XPU 客戶很可能會繼續用直連銅纜」，光學「更貴、要多很多電」；「你不需要跑去追一個叫 CPO 的閃亮東西……CPO 會在它的時候來。不是今年，也許不是明年」[[broadcom-fy26q1-call-20260304]]。2026 年 6 月又說機櫃內 scale-up 用 200G、400G SerDes 的直連銅纜，並推動共同封裝銅線[[broadcom-fy26q2-call-20260603]] |
| NVIDIA 網路資深副總 Gilad Shainer | 銅線在距離允許處仍是首選，「包括 NVLink scale-up 網域內」；CPO 用在 scale-out 那種要跨整座 AI 工廠的距離[[convergedigest-shainer-hoti-202608]] |
| NVIDIA 的 Ian Buck | NVL72 背後超過 5,000 條銅纜、沒有 retimer，「短距銅又快又便宜」；改液冷的真正原因之一是「為了在銅線裡連起盡量多的 GPU」[[tomshardware-ianbuck-qa-20260323]] |
| 一家研究機構 | NVIDIA 對 scale-up「用盡極端手段避免改用光，甚至到 2027、2028」；NVIDIA 在做共同封裝銅線（CPC），據說叫供應鏈全力做[[semianalysis-cpo-book,semianalysis-gtc2026-kingdom-20260320]] |
| Corning | scale-up「今天 100% 銅線，但光開始滲透」[[bullfincher-corning-q2-20260728]] |
| Marvell | 客戶 scale-up 一開始部署銅線；從銅到光「預計要好幾年，兩者並存」[[bullfincher-marvell-fy27q2-20260827]] |
| AMD | Helios（MI450）機架「整個是銅線」；2027 年的 MI500「銅線和光學連接都有」[[sdxcentral-amd-mi500-20260724]] |

共同封裝銅線（CPC）是把銅線的接頭直接裝在基板上，少走一段電路板。Amphenol 的 CPC 產品是 448 Gbps 等級，說這種外型已用在乙太網路、NVLink、InfiniBand 平台[[designworld-amphenol-cpc-20260408]]；它的執行長說客戶「什麼都要更多：更多高速銅、更多光纖、更多電源」，被問到某客戶把銅纜背板改成 PCB：核心問題不是背板或 PCB，而是互連總含量有沒有增加[[fool-amphenol-q2-20260729]]。TE 在 OCP 的摘要把 448G 的 CPC 說成「通往 CPO 的過渡」[[ocp2026-agenda-20261012]]。Meta 的 MTIA 300 scale-up 交換器，OCP 摘要寫的還是每顆加速器 8 條 800GbE 被動銅線；下一代 102.4T 晶片、每櫃 72 顆，改用 OCP 的 ESUN 規格（摘要沒提光學）[[ocp2026-agenda-20261012]]。CPC 的出貨量查不到。

### NVIDIA 自己怎麼排

NVIDIA 公開的資料，要分「投影片」、「技術部落格」和「人在台上說的」看：

| 世代 | 公開資料怎麼寫 |
|---|---|
| Rubin（2026）NVL72 | Hot Chips 2026 投影片：全銅 scale-up[[sth-hotchips2026-rubin-nvl72]]。GTC 2026 路線圖的 Rubin 欄只有 scale-out 的「Spectrum6 102T, CPO」[[glennklockwood-gtc2026-recap-20260323]] |
| Rubin Ultra NVL576（8 個機櫃） | 技術部落格：「用銅線和直接光學連接」，兩層全互連[[nvidia-devblog-vera-rubin-pod-20260316]]。細節見 [NVL576 和 Rubin Ultra](#tm-nvl576) |
| Rubin Ultra Kyber NVL144 | 技術部落格沒寫光；Ian Buck 在 GTC 記者問答說 Kyber「同樣全部銅線」[[tomshardware-ianbuck-qa-20260323]] |
| Feynman Kyber NVL1152 | 部落格：Kyber 會用類似的直接光學互連做機櫃對機櫃的 scale-up，擴展成 NVL1152[[nvidia-devblog-vera-rubin-pod-20260316]]；投影片 2028 年欄有「NVLink 8 CPO」；黃仁勳：「第一次，我們會同時用銅線和共同封裝光學做 scale-up」[[tomshardware-gtc2026-roadmap-20260317]] |

![NVIDIA 在 GTC 2026 主題演講的路線圖投影片（直播截圖）。三欄：Blackwell 2024、Rubin 2026、Feynman 2028。Rubin 欄的晶片有「Spectrum6 102T, CPO」，Feynman 欄第一次出現「NVLink 8 CPO」和「Spectrum7 204T, CPO」。機櫃列 Rubin 欄是 Oberon NVL72／NVL576、Oberon ETL256、Kyber NVL144，Feynman 欄是 Oberon NVL72、ETL256、Kyber NVL144／NVL1152。[[glennklockwood-gtc2026-recap-20260323]]](img/vendor/glennklockwood-gtc26-optical-scaleup-slide-202603-01.png){.s}

黃仁勳在台上還說過：「很多人問，copper 還重要嗎？答案是重要。scale up 會用光嗎？會。scale out 用光嗎？會。……我們需要更多銅線產能、更多光學產能、更多 CPO 產能。」[[hpcwire-gtc2026-roadmap-20260318]]

有一件事要分清楚：NVIDIA 的原文沒有寫 Kyber NVL144 的 CPO，也沒有寫 NVL576 的光是 CPO。部落格的摘要段又把 Kyber NVL144 寫成「for the Feynman era」，和內文「先用在 Rubin Ultra」並存[[nvidia-devblog-vera-rubin-pod-20260316]]。研究機構對此的解讀是：Rubin 世代只有銅線，Kyber 機櫃內也只有銅線；機櫃之間的光，NVL1152 的基準情境是「機櫃內銅線、機櫃間 CPO」，並說 NVL1152「還要好幾年，路線圖很可能會變」[[semianalysis-gtc2026-kingdom-20260320]]。Shainer 在 GTC 之後的訪談說 NVLink 交換網路「顯然會用 CPO，因為我們要把很多機櫃連在一起」，但在 HPCwire 的上下文裡，這句話緊接在 Feynman 世代的 NVL1152 之後，Shainer 沒有點名世代、也沒提 NVL576；NVL1152 機櫃內是不是全銅，他說「還太早談」[[hpcwire-nvidia-sipho-roadmap-20260420]]。

### 要用多少光纖

如果 scale-up 真的改用光，光纖會多很多。Corning 在法說上給了最直接的算法：每顆 GPU 的 scale-up 頻寬 14.4 Tb/s、scale-out 是 1.6 Tb/s（相差 9 倍，計算：14.4 ÷ 1.6）[[bullfincher-corning-q2-20260728]]。

| 項目 | 算式 | 每顆 GPU 的光纖 |
|---|---|---|
| scale-out（現在） | 1.6 Tb/s ÷ 200G ＝ 8 條通道，每條 2 根光纖 | 16 根 |
| scale-up 全改光 | 14.4 Tb/s ÷ 200G ＝ 72 條通道，每條 2 根光纖 | 144 根 |
| 兩者合計 | | 160 根，是現在的 10 倍 |

以上是 Corning 法說的算法[[bullfincher-corning-q2-20260728]]。Corning 說 NVL576 這種混合式會落在「全銅（每顆 GPU 16 根）」和「全光（160 根）」之間；NVL576 的光學埠比例它知道，但「保密不能說」。Corning 也說 BiDi、WDM 可以減少每顆 GPU 要的光纖[[bullfincher-corning-q2-20260728]]。它的執行長說每顆 GPU 的光學含量到 2028 年增加 1.3 到 1.5 倍，2030 年「可能高很多」，CPO「可能從 scale-out 開始」，但「scale-up 讓機會規模大幅增加」[[sdxcentral-corning-opportunity-20260730]]。

換一種接法，數字就不同：OCI MSA（光學運算互連，2026 年 3 月由 AMD、Broadcom、Meta、Microsoft、NVIDIA、OpenAI 創立）第一代是一根光纖雙向各 200 Gb/s（4 個波長 × 50G，同一根光纖收發）[[broadcom-pr-oci-msa-20260312]]。照同樣的 14.4 Tb/s 算，每顆 GPU 72 根光纖，是 Corning「每通道 2 根」算法 144 根的一半（計算）；Lightmatter 也說雙向光鏈路讓光纖和接頭需求「減少 50%」[[lightmatter-nvlink-fusion-20260602]]。但 Meta 的講者又主張用「更多條、每條頻寬較低」的光鏈路[[convergedigest-oci-hoti-202608]]，兩個方向互相抵銷，還沒有定論。OCI 規格本身見[各種規格](alternatives.md#alt-specs)。

再看絕對量。Ayar Labs 和緯穎的參考設計：每櫃 32 個運算托盤、64 顆 ASIC，16 櫃組成 1,024 顆以上加速器的 scale-up 叢集，每顆加速器超過 100 Tbps 的光連接；部落格寫「1,024 顆加速器、每顆 8 個光引擎、每個光引擎 32 條光纖線」[[ayarlabs-blog-rack-scaleup-20260527]]。算式：1,024 × 8 × 32 ＝ 262,144 條光纖線（計算；原文沒寫每條是單芯還是多芯）。對照 scale-out：一台 NVIDIA SN6800-LD 有 512 個 MMC-16、每個用 8 芯，共 4,096 芯（計算：512 × 8）[[nvidia-sn6000-manual-20260916]]。

NVIDIA 自己研究部門的「慢而寬」概念設計，一顆 GPU 單向就要 1,152 芯（見[慢而寬](#tm-wide)），也說明光纖成本壓在這一層。

### 第一個 scale-up 的光學產品，誰、什麼時候

沒有任何一家已經出貨 scale-up 用的 CPO。查得到的全是計畫：

| 誰 | 什麼 | 時間 |
|---|---|---|
| NVIDIA | Rubin Ultra NVL576 機櫃之間「直接光學連接」（是不是 CPO，原文沒寫） | 沒給年份；有報導寫 Rubin Ultra 2027 年推出（見 [NVL576 和 Rubin Ultra](#tm-nvl576)） |
| NVIDIA | NVLink 8 CPO 交換晶片，配 Feynman Kyber NVL1152 | 投影片標 2028[[glennklockwood-gtc2026-recap-20260323]] |
| Marvell（收購 Celestial AI） | Photonic Fabric 小晶片，和客製 XPU、scale-up 交換器共同封裝；單一小晶片 16 Tbps | 營收從 FY2028 下半年開始（約 2027 年 8 月到 2028 年 1 月，計算：Marvell 的 FY2028 約是 2027 年 2 月到 2028 年 1 月）[[marvell-celestial-20251202]] |
| Marvell | 投資人日口頭說 scale-up 光學「今天幾乎零營收，明年開始數億美元」，每顆 XPU 的光學含量「數千美元，連結兩端都有」；簡報標自家 200G NPO 驅動／TIA「Now」、400G 光引擎 25.6T「2027」[[futurum-marvell-investor-day-20261009,marvell-investor-day-deck-20261006]] | 2027 |
| AMD | MI500「銅線和光學連接都有」、更大的 scale-up 網域；「MI500 的光學是格芯做 PIC、日月光封裝」只有媒體引未具名來源，AMD 沒證實[[sdxcentral-amd-mi500-20260724,wccftech-amd-mi500-20260420]] | 2027 |
| Coherent | scale-up 用的 CPO 和 NPO | 2027 下半年[[futurum-coherent-photonlink-20260923]] |
| Lightmatter | CPO（台積電、格芯）；NPO 2027–28 | 2028 出貨[[tomshardware-optical-battle-20260723]] |
| Credo | scale-up NPO（確定的設計導入）、LED 光纜 | FY28（約 2027 年 5 月起）[[fool-credo-fy27q1-20260901]] |
| Ayar Labs | TeraPHY 光引擎加 SuperNova 外部雷射；2026 年募資 6.5 億美元轉量產；加入 NVLink Fusion | 沒給出貨年份[[ayarlabs-650m-202609]] |
| 廣發證券 | NVIDIA 基於 NVL576 的 scale-up CPO、NPO 2027 下半年開始導入；Trainium 4 可能用 NVLink Fusion 並比照導入 NPO | 2027 下半年[[technews-gf-cpo-axt-20260818]] |
| Broadcom | 第一個量產的 CPO 系統，研究機構說會是客戶的 AI ASIC（scale-up），沒給年份[[semianalysis-cpo-book]] | — |

「Rubin Ultra Kyber 平台的 2H27 CPO 方案」這種說法的源頭，見 [NVL576 和 Rubin Ultra](#tm-nvl576)。

### 其他家怎麼做

- **AMD**：2026 年 Computex 展出的 Helios MI455X 72 顆 GPU 機架，scale-up 走 UALink-over-Ethernet，不是原生 UALink，因為 UALink 交換晶片趕不上；量產延到 2027 年第二季[[tomshardware-optical-battle-20260723]]。AMD 在 2025 年收購矽光子公司 Enosemi[[amd-enosemi-20250528]]。
- **Broadcom**：Tomahawk Ultra 是給 scale-up 的低延遲乙太網路交換器，「這一季開始部署，FY27 會用在 scale-up」；已 tape-out Tomahawk 7（200 Tbps、400G SerDes）[[fool-broadcom-q3fy26-20260909]]。ESUN（Ethernet for Scale-Up Networking）和 UALink 講的是協定和交換，沒有一份說 scale-up 用銅或用光[[ocp-esun-blog-20251013]]。Broadcom 在 OCP 前的說法是支援 CPO／整合光學、前面板插拔、傳統銅背板三種，讓營運商自己混搭[[broadcom-khamisy-blog-202610]]。
- **OCI MSA**：目的是讓 scale-up 從銅線架構遷移到光學架構；支援插拔式、板上、CPO 三種形式，刻意不規定外型和光纖線束[[broadcom-pr-oci-msa-20260312,convergedigest-oci-hoti-202608]]。第一代 200 Gbps 雙向已定，400 Gbps 的第二代預計 2027 年公開[[hpcwire-cpo-ecosystem-20261005]]。
- **Google**：TPU 的 scale-up 早就有一段是光，但走的是光路交換器，見 [Google 的 OCS](#tm-ocs)。
- **AWS**：Trainium 4 整合 NVLink 6 和 MGX 機架，NVIDIA 的文章沒提光[[nvidia-devblog-trainium4-20251202]]。一家研究機構認為 Celestial 的營收主要來自搭 Trainium 4 的 scale-up CPO[[semianalysis-cpo-book]]；AWS 自己沒說。
- **Microsoft 的 Maia 200**：兩層、標準乙太網路的 scale-up，每顆 2.8 TB/s 雙向，叢集最多 6,144 顆；沒寫用銅或光[[sdxcentral-maia200-20260127]]。
- **Meta**：OCI 創始成員；MTIA scale-up 現在還是銅（見上）。

### 先走的是 NPO 和光纜，不是 CPO

幾家公司自己說的營收時點，都落在 NPO、光引擎和光纜，不是台積電 COUPE 上的 CPO：Credo 的 scale-up NPO 和 LED 光纜（FY28）、Marvell 的光引擎（2027）。專家調研紀要說 2027 年 NVL576 的交換托盤「CPO 和 NPO 兩種」並行、博通 2027 年的 CPO 交換器「未必 100% CPO，會搭配部分 NPO」，這是未具名專家的說法[[cnyes-hao-rubinultra-nvl576-20260912,threads-allen-citi-kyber-20260709]]。NPO 的光引擎也接 FAU（Lightmatter 的 NPO 引擎最多 3 個 FAU、每個 40 根光纖，共 120 根[[semianalysis-cpo-book]]），但不一定在台積電 COUPE 上做。NPO 是什麼、各種規格見 [NPO](alternatives.md#alt-npo)。

scale-up 光引擎也不全在 COUPE：Lightmatter 的 CPO 在台積電和格芯做[[tomshardware-optical-battle-20260723]]，Ayar Labs 第三代 TeraPHY 改用 COUPE、每個光引擎單向 13.5 Tb/s[[semianalysis-cpo-book]]，AMD 那條是媒體報導的格芯加日月光。

### 同一家公司的說法，隨季度怎麼變 {#tm-quotes}

上面各表多半引一季的說法；這一節把同一家公司前後幾季並排，看口風是變快、變慢還是沒變。引的是法說會轉錄稿（Motley Fool、Investing.com 等第三方轉錄）和公司自己的投資人記錄；標「AI 轉寫稿」的（AllMind）說話者標示常有錯，說話者不確定時我會註明。英文原句照錄，是因為這些句子的口氣本身就是重點。

**Broadcom：三個月內兩種說法。**

| 日期 | 說法 |
|---|---|
| 2025-12-11（FY25Q4） | 執行長 Hock Tan：「I could see a point in time in the future when silicon photonics methods as the only way to do it. We're not quite there yet.」順序是先銅線、再插拔式光學，插拔式也做不好的時候才走矽光子：「The final straw is when you can't do it well in pluggable optics. Of course, when you can't do it even in copper, then you're right. You go to silicon photonics. And it will happen.」[[fool-broadcom-q4fy25-20251212]] |
| 2026-03-04（FY26Q1） | 「We have SerDes now running 400G that can drive distance on a rack to run copper. All I am trying to say is you do not need to go run into some bright shiny object called CPO. Even as we are the lead in CPO, CPOs will come in its time. Not this year, maybe not next year.」[[broadcom-fy26q1-call-20260304]] |
| 2026-06-03（FY26Q2，另一家第三方轉錄） | 「in CPOs, which is co-packaged optics, 1.6 terabit DSPs, CW and EML lasers, we are the de facto standard in the industry.」[[broadcom-fy26q2-call-20260603]] |

三月那句談的是客戶部署的時間（不是今年，也許不是明年），六月那句談的是 Broadcom 在 CPO 供應商裡的位置（業界事實標準）；兩句講的不是同一件事，並排列出，不互相抵消。十二月和三月的順序相同：銅線到不夠才換光。

**Marvell：scale-up 光學的數字一路改。**

| 日期 | 說法 |
|---|---|
| 2026-03-05（FY26Q4 法說會轉錄稿） | scale-out 的 CPO 部署「相對有限」，尤其相對於插拔式的數量。「明年」只會有一家大客戶出貨 scale-up 的 CPO，其餘部署仍是銅線：「we will be shipping next year CPO for scale-up at one large customer, and then we are working on more for beyond that. And the rest of those deployments would be still copper-based.」來自 Celestial 的 CPO 營收，2028 年達到 5 億美元的年化營收率，2029 年 10 億美元[[fool-marvell-q4-20260305]] |
| 2026-05-27（FY27Q1 法說會轉錄稿） | 下一會計年度 scale-up 光學「明顯成長」，營收預測超過先前展望（約 1.5 億美元，當時只算 Celestial AI）的兩倍。問答中說現在大約 3 億美元，是 NPO 和 CPO 兩種方案加起來。第三代 6.4T 光引擎，與多家 tier 1 客戶深度接洽，NPO、CPO 都做[[fool-marvell-q1-20260527]] |
| 2026-08-27（FY27Q2，AI 轉寫稿，未標說話者） | 回顧上一季的說法（Celestial 的 CPO 約 1.5 億、含 NPO 的 scale-up 光學整體約 3 億），然後說整體「比上一季給的數字又更快」，「明年 scale-up 光學的機會比一季前想的大很多」，沒有給新數字。又說：CPO 是重要的一塊，但「現在步調快得多的機會是 NPO」，與既有的 CPO 專案並行[[allmind-marvell-q2-20260827]] |
| 2026-10-06（投資人日，YouTube 自動字幕，未校對） | 字幕把 NPO 轉成「NO」。大意：NPO 一定會起量，CPO 仍照進度走，不是一個先起來、另一個掉下去；NPO 是一列會一直跑的火車，替多數客戶最終走向 CPO 鋪路[[youtube-marvell-investor-day-20261006]] |

3 月的 5 億美元是 2028 年的年化營收率，5 月的 1.5 億和 3 億是下一會計年度的全年營收，兩個口徑不同，不能直接相減。同一場投資人日，Celestial 團隊的講者說公司對 NPO 或 CPO「沒有偏好」：客戶若重視光學可以現場更換、故障影響範圍小、可重新配置，就用 NPO 插在板子上；並說已有客戶在部署 CPO（字幕寫成 co-ack，依上下文應是 co-packaged）。另一位講者說今天 scale-up 佔資料中心資料流量的 85%，這是 Marvell 自己的說法，不是第三方量測[[youtube-marvell-investor-day-20261006]]。scale-up、scale-out 的定義見[這一節](basics.md#q4b)。

**Credo：三季從「短期看不到」到「FY28 開始有營收」。**

- 2025-12-01（FY26Q2，AI 轉寫稿）：展示很多，但「沒看到很多客戶大規模往前走」；連線的可靠度是優先順序的最頂端，量最大的那一塊「短期不會轉到 CPO」[[allmind-credo-q2fy26-20251201]]。
- 2026-03-02（FY26Q3）：NPO 和 CPO 要拿出「防彈級」可靠度之前，部署會相當有限，這也是許多預測師給 CPO 在交換器市場未來三年低個位數佔比的原因。這個佔比是 Credo 轉述預測師的看法，不是 Credo 自己的預測[[fool-credo-q3fy26-20260302]]。
- 2026-06-01（FY26Q4）：剛收購的 Dust Photonics（矽光 PIC）的路線圖「直接通往 CPO 和 NPO 架構」；依目前的客戶接洽，CPO、NPO 設計的第一筆營收預期在 FY28（2027 年 5 月起的會計年度）[[fool-credo-q4-20260601]]。
- 2026-09-01（FY27Q1）：客戶對 scale-up 用 NPO 的動作增加，「確定的設計導入」預期在 FY28 開始起量；並加入 Open CPX MSA。XPO、CPX、NPO、CPO 都在解決同一件事，即密度提高 10 倍[[fool-credo-fy27q1-20260901]]。

**Coherent：scale-up CPO「2027 下半年」連續說了一年。**

| 日期 | 說法 |
|---|---|
| 2025-11-05（FY26Q1） | 初期 CPO 部署在 2026 年[[fool-coherent-q1fy26-20251106]] |
| 2026-02-04（FY26Q2） | 剛拿到一位市場領先的 AI 資料中心客戶「極大的」採購單，內容是包含新高功率連續波雷射的 CPO 方案，客戶沒點名；預期今年底前後有第一筆營收，明年起更顯著。問 scale-up 還要幾年，答「I wouldn't call it years out, I think it's sooner than that」。又說 scale-up CPO 的機會會讓 scale-out「相形見絀」（orders of magnitude larger），scale-out 網路至少到本十年結束仍以插拔式為主。選 Coherent 的原因之一是高功率連續波雷射在德州 6 吋線生產[[fool-coherent-q2fy26-20260204]] |
| 2026-05-06（FY26Q3） | scale-out CPO 營收今年下半年開始放量，scale-up CPO 營收在 2027 年下半年開始放量[[fool-coherent-fy26q3-20260506]] |
| 2026-08-12（FY26Q4，AI 轉寫稿） | 「We continue to expect revenue from CPO for scale up applications to start to flow in the second half of calendar 27. And, yeah, that is been a consistent view for quite a while for us.」[[allmind-coherent-q4fy26-20260812]] |

**Lumentum：三次說法的時點一致。** 2026-02-03：「By late calendar 2027, we would expect our first scale-up CPO shipments replacing longer copper connections.」公司已深入參與設計導入，用的是超高功率雷射和外部光源模組[[fool-lumentum-q2fy26-20260203]]。2026-05-05：已描述過的數十億美元訂單多半來自 scale-out，scale-up 的營收機會預期「明顯更大」，「大約超過 50 億美元的增量營收，如果執行得好」；也說「CPO 會有很大的供需失衡」；致詞中說 scale-up CPO「仍在嬰兒期」，scale-out CPO 和 OCS 的初期貢獻「還相當小」[[fool-lumentum-q3fy26-20260506]]。2026 年 8 月的說法（scale-up CPO 雷射 2027 下半年高量出貨、客戶 2028 年部署）見[雷射筆記](lasers.md#las-shortage)；三次的時點一致，沒有延後。

**Corning：把 scale-up 營收往前拉。**

- 2026-01-28：Corning 的 SpringBoard 成長計畫最近一次上調，「沒有包含重要的 scale-up 營收」，那是額外的，看你怎麼判斷時點；「也有情境是 2028 年起立刻成為主要部分」[[fool-corning-q4-2025-20260128]]。
- 2026-04-28：執行長說「直到最近，我都不相信從現在到 2028 年之間，scale-up 這一塊會讓我們的營收明顯增加」；改變的原因是與幾家關鍵客戶很深入的對話裡出現技術進展，提高了 scale-up 在近期影響營收展望的機率[[fool-corning-q1-2026-20260428]]。
- 2026-07-28：scale-up「今天 100% 銅線」（見上面的表）；對延後傳聞的回答見[上面](#tm-delay)。

**Astera Labs：從「最早 2028、2029」到「NPO 2027、CPO 2028」。**

- 2025-11-04（AI 轉寫稿，財務長）：「More likely, the earliest for scale-up optical connections will be in the '28, 2029 time frame.」[[allmind-astera-q3-20251104]]
- 2026-02-10：執行長 Jitendra Mohan 說預期 scale-up 的共同封裝光學第一批部署在 2028 年前後；轉換的順序「先是插拔式光學，然後可能是近封裝光學，最後才是聖杯，共同封裝光學」；初期的 CPO 部署可能先出現在 scale-out，早於 scale-up[[fool-astera-q4-20260210]]。
- 2026-08-11：總裁 Sanjay Gajendra：「We look at it as 2027 being the year where NPO gets deployed; 2028 and beyond is when CPO gets deployed.」又說這一代和下一代，機櫃內的 scale-up 仍是銅線[[fool-astera-2026q2-20260811]]。
- 2026-02 同一場，財務長說明 Astera 給 Amazon 的第二份認股權：依績效條件分批解鎖，對應最高 65 億美元的購買，內容包含交換器、訊號調節和光引擎；轉錄稿裡的股數以公司的 8-K 為準[[fool-astera-q4-20260210]]。Marvell 給 Amazon 的認股權見[誰在主導 CPO](players.md#q17)。

**代工廠、整機廠、交換器廠：**

| 誰 | 說法 |
|---|---|
| GlobalFoundries | 2025-11：CPO 從 2027 年起明顯起量，矽光子在本十年結束前成為年營收速度 10 億美元以上的業務；2026-02：矽光子營收速度 2028 年達 10 億美元，比原目標「大幅加速」，並拿到 scale-up 網路用的 CPO 設計案（光 IC 的設計案在網路兩端都有）；2026-08：「27 年 NPO 開始放量，28 年 CPO 開始放量」，這是過去幾季一致的看法。NPO 焊在主機板上，CPO 在封裝裡；EIC 接合 PIC、微光學、光纖貼合單元，兩者都需要[[allmind-gf-q3-2025-20251112,fool-gf-q4-2025-20260211,fool-gf-q2-20260812]] |
| Tower | 2025-11：CPO 要強力商用化還要「兩三年」（與 Tower 無關）；2026-05：NPO 會在未來幾年起量，早於主要客戶的 CPO 大量起量，「插拔式不會消失，至少到 2030 年都會非常強」；2026-08 的說法見[「NVIDIA 暫離 COUPE」傳聞](players.md#pl-coupe)。三個時點一致[[allmind-tower-q3-20251110,allmind-tower-q1-20260513,fool-tower-q2-20260804]] |
| Celestica（整機廠） | 2025-10：1.6T 會看到一些部署，CPO 的起量更多在 3.2T；2026-01：大量採用「更偏向 3.2T」，3.2T 的研發專案樣品預計 2026 年底，「還沒看到客戶要求 CPO 大量採用」[[allmind-celestica-q3-20251028,fool-celestica-q4-20260129]] |
| Arista（交換器廠） | 2026-02：scale-up 的承諾綁在新產品與新的 ESUN 規格，規格最早在今年第四季，真正量產是 2027 年；2026-05：scale-up 現在「幾乎是零、不存在」，要到 ESUN 規格之後，算 2027–2028 年的數字；兩三公尺內「還是會看到很多共同封裝銅線」；CPO 仍是「科學實驗」，各家私有，Arista 擁抱幾年後的開放 CPO，但認為 XPO 有十年的路，尤其是需要液冷的 1.6T、3.2T；目前它接的光學市場 99% 是插拔式；2026-08：CPO 明年出現實例和試用，世界多數仍是插拔式與銅線，2028、2029 年才有一定量的 CPO。Arista 不喜歡五種各自私有的實作，要的是開放 CPO：插座式光引擎、尾纖、可預先測試，這種開放 CPO「常被叫做 NPO」[[fool-arista-q4-2025-20260212,fool-arista-q1-20260505,fool-arista-q2-20260811]] |

**模組廠自己對 scale-up 規模的預估。** 中際旭創：2025-10-31 說 scale-up 的頻寬需求成長很快，可能達到 scale-out 的十倍；2026-02-01 改成 5 到 10 倍，機櫃內的光連接產品預計 2027 年開始起量；2026-04-17 補了一句，因為 scale-out 的基數更大，2027 年 scale-out 產品的占比仍高於 scale-up[[cninfo-innolight-irm-20251031,cninfo-innolight-irm-20260201,cninfo-innolight-irm-20260417]]。模組廠自己的說法是頻寬 5 到 10 倍，營收占比 2027 年仍小。

### NPO 的口風：模組廠怎麼說，隨時間怎麼變 {#tm-npo-wording}

中際旭創對 NPO 的說法，依日期排：

| 日期 | 說法 |
|---|---|
| 2025-10-31 | 相對可行的方案包括 LPO、XPO 和 NPO 等，預計 2027 年有望看到應用和部署[[cninfo-innolight-irm-20251031]] |
| 2026-02-01 | NPO 是雲端客戶比較青睞和重視的方案，並有可能成為一個較為長期的技術選擇[[cninfo-innolight-irm-20260201]] |
| 2026-04-17 | NPO 有望率先在 scale-up 場景應用，已有雲端客戶給了明確的需求指引，預計 2027 年量產[[cninfo-innolight-irm-20260417]] |
| 2026-07-12 | NPO 今年 3 月開始呈現明顯加速的趨勢，部分客戶已明確提出 27–28 年的需求指引[[cninfo-innolight-irm-20260712]] |
| 2026-07-28 | 2027 年下半年開始，預計業界有兩個有影響力的重點客戶開始批量採購 NPO 產品[[cninfo-innolight-irm-20260728]] |
| 2026-08-23 | 光連接形態不會單一化，可插拔、NPO、CPO 並存；CPO 已有客戶宣布量產，主要在 scale-out[[cninfo-innolight-irm-20260823]] |

這條線從「可行方案之一」走到「雲端客戶青睞」再到「已有明確需求指引」；公司自己把轉折點放在 2026 年 3 月前後（7 月 12 日那句）。

其他中國廠商的說法，並排：

| 公司 | 日期 | 說法 |
|---|---|---|
| 新易盛 | 2026-07-20 | 預計 2027 年下半年有訂單交付需求，2028 年出貨量級逐步提升；從現有進度看，預計 2027 年下半年開始商業起量[[cninfo-eoptolink-irm-20260720]] |
| 新易盛 | 2026-09 | 互動易回覆：預計 2027 年逐步有訂單交付需求；集體接待日（9 月 11 日）：預計 2027 年開始交付，2028 年 NPO 產品交付的規模進一步提升，預計成為公司主要產品之一[[szse-irm-eoptolink-cpo-20260907,p5w-eoptolink-collective-20260911]] |
| 華工科技 | 2026-03-26 | 3.2T NPO 產品 2026 年已有在手訂單、正在交付，與頭部廠商及交換器晶片廠合作，今年實現批量，明年爭取更大規模訂單[[cninfo-hgtech-irm-20260326]] |
| 華工科技 | 2026-08-27 | NPO 產品目前與國內外多家頭部 AI 廠商小批交付並細化確定最終方案；「1.6T NPO 头部客户需求指引 500 万只」是客戶的需求指引，不是華工的訂單；預計明年海外市場有幾百萬套的需求、國內百萬套以上，這是公司對市場的估計，沒說是哪一種 NPO[[cninfo-hgtech-irm-20260827]] |
| 光迅科技 | 2026-05-14 | 3 月 OFC 2026 推出全球首款 3.2T 矽光單模 NPO 模組，並已在國內頭部雲端大廠完成驗證（同一場有「全系列驗證」和「系統驗證」兩種說法），沒說客戶是誰[[p5w-accelink-results-20260514]] |
| 天孚通信 | 2026-07-09 | 具備 NPO 各相關產品的技術和能力，目前配合多個客戶做配套產品研發[[cninfo-tfc-irm-20260709]] |

新易盛的 7 月版限定「2027 年下半年」，9 月起不再限定半年；時間點可能沒變，只是說得更寬。華工的「批量」指小批交付和在手訂單，中際旭創和新易盛指大客戶批量採購，所以「多家模組廠說 2027 年開始交」不是大家一致：華工說 2026 年就已經在小批交付。

## NVL576 和 Rubin Ultra：到底是什麼、用什麼連 {#tm-nvl576}

台廠 FAU 的成長故事，不少掛在「2027 年下半年的 Rubin Ultra」上。所以要先把 Rubin Ultra 和 NVL576 分清楚，再看 NVIDIA 寫了什麼、別人怎麼說。

Rubin Ultra 有三種機櫃：NVL72、NVL144（Kyber 機櫃，每櫃 144 顆 GPU）、NVL576。NVL576 是 8 個 MGX 機櫃、每櫃 72 顆，組成一個 576 顆 GPU 的 NVLink 網域，用兩層全互連的拓撲；NVIDIA 的說法是「用銅線和直接光學連接」[[nvidia-devblog-vera-rubin-pod-20260316]]。NVIDIA 另一篇部落格說：576 顆 GPU 跨 8 櫃，「銅線無法把訊號傳過這個距離」，在 NVL576 的規模，光是最省電的選項[[nvidia-blog-coherent-texas-20260616]]。

### NVIDIA 公開的那張「NVL576」照片

NVIDIA 技術部落格和 VLSI 2026 短課程（NVIDIA Research 的講者）都放了一張機房照片當 NVL576 的示範。**照片是 Blackwell（GB200）做的原型 Polyphe，不是 Rubin Ultra。** 部落格的圖說是「a fully functional GB200-based multirack NVL576 scale-up system」[[nvidia-devblog-vera-rubin-pod-20260316]]；VLSI 投影片的標題是「NVIDIA Vera Rubin Ultra NVL576」，照片左邊標「Optics above L1／Copper below L1」（第一層以上用光、以下用銅），照片下面註明是 Blackwell 做的原型[[ascii-ohara-nvl576-p3-20260810]]。這是目前唯一一份 NVIDIA 自己針對 NVL576 光學寫的字：沒有寫 CPO、插拔式或 OCS。

<div class="pair">

![Polyphe：NVIDIA 內部用 GB200 做的多機櫃 NVL576 原型（NVIDIA 技術部落格的實拍）。一排 12 個機櫃，中間 8 個機櫃每櫃拉出左右兩束黃色線進天花板走線架；左邊兩櫃和各櫃上下段是淺藍色和白灰色細線。[[nvidia-devblog-vera-rubin-pod-20260316]]](img/vendor/nvidia-polyphe-gb200-multirack-nvl576-prototype-20260317-01.webp)
![NVIDIA 在 2026 IEEE VLSI 研討會短課程的投影片第 12 頁：同一張 Polyphe 照片，標題寫 Vera Rubin Ultra NVL576，左側標「Optics above L1／Copper below L1」。（NVIDIA 投影片，經日本媒體轉貼）[[ascii-ohara-nvl576-p3-20260810]]](img/media/ASCII-VLSI2026-SCT8-NVIDIA-slide12-NVL576-Polyphe光上銅下-20260810.jpg)

</div>

照片本身能看出多少？原圖最大 1296 × 629，黃色線糊成一束。每個托盤幾條線數不出來，接頭是 MPO、MMC 還是插拔式模組也無法辨認。黃色外皮依業界顏色慣例是單模光纖、淺藍色是多模光纖[[wikipedia-fiber-colors-20261012]]，但照片本身證明不了光纖種類。日本專欄作家說他數出「每個托盤看起來 16 條（每顆交換晶片 8 條）」，集中到另一個機櫃；他的接線圖是自己畫的推定圖，不是 NVIDIA 的[[ascii-ohara-nvl576-20260810,ascii-ohara-nvl576-p2-20260810]]。他的文章第一頁把照片稱作 Vera Rubin 版原型，第二頁才改口說是 GB200 原型。研究機構的說法則是 Polyphe 用的是插拔式光模組[[semianalysis-gtc2026-kingdom-20260320]]。

### 櫃與櫃之間用什麼：七種說法

NVIDIA 沒有書面說明，各方的說法如下，彼此對不上：

| # | 說法 | 性質 |
|---|---|---|
| 0 | NVIDIA 技術部落格：「銅線和直接光學連接」；VLSI 投影片：「L1 以上光、以下銅」[[nvidia-devblog-vera-rubin-pod-20260316,ascii-ohara-nvl576-p3-20260810]] | 公司書面 |
| 1 | Ian Buck：第一層在機櫃內用銅線，「第二層 spine 會用插拔式模組」；記者自己補一句也可能改用 NPO。原始場合找不到：GTC 記者問答逐字稿裡沒有這句，只講 NVSwitch 前面有埠、可做第二層 NVLink 擴到 576[[theregister-nvidia-scaleup-20260405,tomshardware-ianbuck-qa-20260323]] | 媒體引公司說，場合不明 |
| 2 | 研究機構：櫃間用插拔式還是 CPO「嚴格說還沒確認，但 CPO 看起來可能性高得多」，NVL576 是「低量、測試用途」[[semianalysis-gtc2026-kingdom-20260320]]；7 月又說 NVL576 可能因 CPO 的困難延後或只少量出貨[[tomshardware-kyber-delay-20260706]] | 第三方 |
| 3 | 另一家研究機構：為 NVL576 推出特別的「NVLink 6 交換器 CPO 版」；但同一段又說 scale-up 埠用 OSFP-XD 接頭、線纜是「線性、被動光纖」，前後不一致[[counterpoint-blackwell-feynman-202604]] | 第三方 |
| 4 | 光學市場研究機構：NVIDIA 會把 OCS 放進 NVL576，2028 年起有明顯量[[cignal-ocs-2030-20260730]] | 第三方 |
| 5 | 日本專欄：L2 是光纜；在 CPO 出現前要靠光電轉換器；NVSwitch 要到 2028 年的 NVSwitch 8 才有 CPO（作者自己的推測）[[ascii-ohara-nvl576-p2-20260810]] | KOL 推測 |
| 6 | 未具名專家調研（9 月 12 日）：2027 年 NVL576 交換托盤有 CPO 和 NPO 兩種，8 櫃直連、不另加外部交換機；OCS「最早也要到 2028 年」；CPO 版每托盤 4 顆 NVLink 交換晶片各 4 個 3.2T 光引擎、共 16 個，外部光源在前面板可抽換，用保偏光纖送光；NPO 版每托盤 16 個 3.2T 模組[[cnyes-hao-rubinultra-nvl576-20260912]] | KOL，未具名 |
| 7 | 未具名專家調研（9 月 10 日）：Rubin Ultra 可擴展版的面板「密佈 MMC 光纖連接器」；CPO 是 NVIDIA 內部第一優先，NPO 是 2027 年的保險；2027 年 NPO 備貨約 7,000 個 NVL72 機櫃、CPO 近 9,000 個[[cnyes-hao-rubinultra-999-20260910]] | KOL，未具名 |

如果第 6 條屬實，可擴展托盤每個 16 個 3.2T 光引擎，等於每托盤 51.2 Tb/s 的光學上聯；每櫃 9 個托盤共 144 個、8 櫃共 1,152 個光引擎（計算：16 × 9 × 8，假設 9 個托盤全是可擴展版）。一份流傳的券商說法是「NVL576 要 324 個光引擎、162 個外部光源、5,184 根光纖」，原報告找不到，兩者差很多，兩個來源都不是一手。

這件事重要在於：只有 CPO 版和 NPO 版需要 FAU 貼在 NVLink 交換晶片旁邊，而且 NPO 版不一定在 COUPE 上做；插拔式模組、OCS 用的是一般光纖連接件。

### 「Rubin Ultra Kyber 2H27 CPO」這句話從哪來

這句話是台灣報導裡反覆出現的說法，把查得到的版本依時間排：

| 日期 | 說法 | 誰 |
|---|---|---|
| 2024-12-31 | 「Rubin 世代將採用 CPO，其中以 2027 年 Rubin Ultra 首度採用機率高」[[ctee-rubinultra-cpo-20241231]] | 法人（經媒體） |
| 2026-03-20 | 「Rubin Ultra NVL144 Kyber 不會用 CPO 做 scale-up……儘管其他分析師傳言 Kyber 會導入 scale-up CPO」[[semianalysis-gtc2026-kingdom-20260320]] | 研究機構 |
| 2026-03-23 | Kyber 144 顆「同樣全部銅線」[[tomshardware-ianbuck-qa-20260323]] | NVIDIA Ian Buck |
| 2026-03-24 | 「Vera Rubin Ultra 會採用銅或銅加 CPO，而 2028 年的 Feynman 則會全面採用 CPO」[[technews-us-bank-rubinultra-20260324]] | 美系外資 |
| 2026-04 | NVIDIA「很可能推出 CPO 版的 Rubin Ultra NVL144」[[semiengineering-optical-5yr-20260406]]；X 帳號貼文：Rubin Ultra scale-up 光學「CPO 優先，NPO 備選」[[wccftech-amd-mi500-20260420]] | 券商；匿名帳號 |
| 2026-06-04 | 「NVIDIA 官方路線圖顯示，2027 年下半年量產的 Rubin Ultra 平台及配套 Kyber 機架，雖然仍以銅纜為核心，但將同步搭載 CPO」[[threads-allen-rubinultra-20260604]] | KOL，稱引官方路線圖 |
| 2026-06-24／30 | 「面向 Rubin Ultra Kyber 平台的 2H27 CPO 方案，將於 2026 年下半年完成設計確認」[[wallstreetcn-glassbridge-20260624,cnyes-glassbridge-20260630]] | 券商（經媒體） |
| 2026-07-09 | 花旗與 NVIDIA 管理層溝通後：Kyber Rubin Ultra 的整體產品路線圖完全未受影響；展望 2028 年 Feynman，客戶可搭配 CPO 或銅纜使用 NVLink；沒有再提 Rubin Ultra scale-up 用 CPO[[threads-allen-citi-kyber-20260709]] | KOL 轉述券商 |

券商那句只有「Rubin Ultra Kyber 平台」幾個字，沒說是 scale-up 還是 scale-out、是 NVL144 還是 NVL576；兩家券商的報告原文都是付費報告，查不到。對照之下，GTC 2026 投影片 Rubin 欄列的是 scale-out 的 Spectrum6 CPO，「NVLink 8 CPO」在 2028 年 Feynman 欄[[glennklockwood-gtc2026-recap-20260323]]。

### 台灣報導裡的「Rubin Ultra 訂單」

把台灣和轉載台灣的報導裡，說 FAU 或 CPO 訂單和 Rubin Ultra 有關的 16 則逐條查過：

- 沒有一則是公司自己說「供貨 Rubin Ultra」。
- 最接近公司說的兩則：上詮董事長說 FAU 第 3 季起依客戶需求量產交貨，沒點平台；標題寫的是 Vera Rubin，法人另說雲端客戶態度保守、短期有出貨遞延的疑慮[[ctee-foci-csp-20260704]]。大立光「不評論市場傳聞」，只確認一位量產型客戶的 FA 規格 7 月送樣、試產線第三季底建好[[moneyweekly-largan-land-cpo-20260826]]。
- 「Rubin Ultra」多半出現在「法人指出」「市場臆測」「專家」這類句子裡。8 月 24 日經濟日報寫大立光、上詮、天孚「最快明年下半年量產，市場臆測，將供貨輝達 Rubin Ultra 平台」[[udn-largan-cpo-20260824]]；韓國網站的英文轉譯把「市場臆測」拿掉，改寫成「expected to begin mass production … for supply to the Rubin Ultra platform」[[stockhub-fau-20260824]]。
- 波若威的報導寫的是「打入 Vera Rubin 平台」，不是 Rubin Ultra[[udn-brillink-vera-rubin-20260427]]。
- 一篇媒體報導寫：輝達 Vera Rubin、Rubin Ultra 也被點名將陸續導入 COUPE，「不過這些多屬分析師預測、尚未經官方正式確認」[[bnext-sipho-stocks-20260612]]。

### Rubin Ultra 本身變小了嗎

另一條線是 Rubin Ultra 的實體規格：

| 日期 | 說法 | 誰 |
|---|---|---|
| 2026-04-01 | 晶圓代工端規劃「仍以雙晶片（2-die）架構為主」，四顆晶粒會把封裝放大到光罩極限的約 7.5–8 倍，影響良率和成本；台積電投片量不變[[ctee-rubinultra-2die-20260401]] | 媒體 |
| 2026-06-29 | 「原本四顆晶粒的 Rubin Ultra 因製造執行風險已取消；新的 Rubin Ultra 大小約一半、實際效能約一半」[[tomshardware-rubinultra-2die-202606]] | 研究機構（經媒體轉述）：兩顆運算晶粒、8 顆 HBM4E（原本 16 顆） |
| 2026-07-06 | 研究機構說 Kyber NVL144 延到 2028（延後超過 12 個月），原因是 78 層正交背板 PCB 製造困難；過渡方案 NVL72×2 因大客戶反對而取消；Rubin Ultra 2027 年「沒有經過驗證的方案可以把 scale-up 規模擴大」。NVIDIA 回應「路線圖不變」，沒給細節[[tomshardware-kyber-delay-20260706]]。財聯社轉述發言人說路線圖不變，「這意味著 Kyber 仍將在 2027 年下半年推出」，這句是財聯社自己的推論[[cls-nvidia-denies-kyber-delay-20260707]] | 研究機構；公司說 |
| 2026-08-10 | 日本專欄引「複數消息來源」：原版 Rubin Ultra 的 9.5 倍光罩 CoWoS-L 中介層（180 層配線）翹曲、剝離，第一版原型不動作、第二版也不行；他推測 GTC 才冒出的 NVL576 是用現有 Vera Rubin 湊出 576 顆的辦法（他自己標「おそらく」）。他說 6 月 Computex 的路線圖上 Rubin Ultra 消失了[[ascii-ohara-nvl576-20260810]] | KOL，引未具名來源 |

NVIDIA 對「四顆改兩顆」沒有任何正式說法，確認或否認都沒有；那句「Our roadmap is intact」回應的是 7 月 6 日的 Kyber 延期報導，不是晶粒數的報導。7 月 15 日報導寫黃仁勳否認延遲、說 Vera Rubin 出貨量大，但沒有回應 Rubin Ultra 機櫃的延期報導[[tomshardware-jensen-rubin-volume-202607]]。另外，Kyber 的 NVL144 用正交背板 PCB 取代銅纜匣，若改用銅纜，一個機櫃要兩萬多條線[[wallstreetcn-kyber-delay-20260706]]。

「Rubin Ultra 從路線圖消失」的證據比轉述的弱：那位專欄作家拿來當證據的 Computex 投影片，是 PC／工作站產品線的路線圖（年份標 Blackwell 2026、Rubin 2027–2028、Feynman 2029–2030），不是資料中心路線圖[[ascii-ohara-nvl576-20260810,youtube-nvidia-gtctaipei-20260601]]。但另一方面，NVIDIA 自己幾乎也不提它：GTC Taipei 主題演講字幕、Computex 論壇的 Deierling 演講、Hot Chips 2026 Rubin 演講（媒體轉貼的部分）、8 月 26 日的法說，都找不到 Rubin Ultra、NVL576 或 Kyber 的光學說明[[youtube-nvidia-gtctaipei-20260601,sth-hotchips2026-rubin-nvl72,nvidia-q2fy27-call-20260826]]。

這些對台廠的意思是：如果 Rubin Ultra 變小、NVL576 少量出貨，掛在「Rubin Ultra 平台」上的 FAU 量要重新對照；至少一家研究機構明說「2027 下半年起量」的時點不成立。

### NVIDIA 研究部門的 FAU 線索

VLSI 短課程的投影片裡，有幾頁和 FAU 直接有關（都是 NVIDIA 投影片，經日本媒體轉貼）：

- **兩種 CPO 封裝（第 19 頁）**：Quantum-X（Q3450）是 28.8T 封裝，「Socketed, External Laser, Pigtailed」（插槽式、外部雷射、光纖直接連在光引擎上）；Spectrum-X 是 102.4T 封裝，「Soldered, External Laser, Detachable」（焊死、外部雷射、光纖接頭可拆）。兩種的差別見[固定式和可拆式](fau.md#fau-types)。
- **DWDM 測試晶片（第 41 頁）**：7nm 的 EIC 和 65nm 的 PIC 用台積電 COUPE 3D 整合，8 個波長 × 32 Gb/s；剖面圖標「FAU with cover」，PIC 版圖上標「FAU attach area」（FAU 貼附區）。日本專欄作家認為這套 DWDM 訊號和現行乙太網路不相容，最可能用在 NVSwitch 8 之後（他的推測）[[ascii-ohara-nvl576-p3-20260810]]。
- **假想 200 Tb/s 交換器的 I/O 耗電（第 49 頁）**：插拔式約 4,000 W，CPO 約 1,200 W，2.5D 光學約 600 W；投影片註明是業界通用的示意數字。

<div class="pair">

![VLSI 2026 短課程投影片第 19 頁：左 Quantum-X photonics（28.8T，插槽式、外部雷射、光纖直接連在光引擎上），右 Spectrum-X photonics（102.4T，焊死、外部雷射、光纖接頭可拆）。（NVIDIA 投影片，經日本媒體轉貼）[[ascii-ohara-nvl576-p3-20260810]]](img/media/ASCII-VLSI2026-SCT8-NVIDIA-slide19-CPO兩種封裝-Pigtailed與Detachable-20260810.jpg)
![第 41 頁：NVIDIA Research 的 DWDM 測試晶片，剖面圖標「FAU with cover」，PIC 版圖上標「FAU attach area」。（NVIDIA 投影片，經日本媒體轉貼）[[ascii-ohara-nvl576-p3-20260810]]](img/media/ASCII-VLSI2026-SCT8-NVIDIA-slide41-DWDM測試晶片-FAU貼附區-COUPE-20260810.jpg)

</div>

這支持「FAU 在 COUPE 上」，但同一份投影片沒有把它連到哪一代 NVLink 產品。

## Google 的光路交換器（OCS） {#tm-ocs}

Google 的 TPU 是另一個做法：scale-up 很早就有一段是光，但不是 CPO，也不是 COUPE，而是**光路交換器**（OCS）。OCS 是一台用鏡子（MEMS 微鏡，也有用液晶的）把光直接從一根光纖反射到另一根光纖的機器，不把光轉成電，所以可以動態重新接線、繞過故障的晶片。

**TPU 怎麼用它。** Ironwood 一個 superpod 9,216 顆，晶片間互連 9.6 Tb/s，用 OCS 動態重組、繞過故障[[google-ironwood-blog-202511]]。TPU 8（2026 年 4 月）：8t 一個 superpod 9,600 顆；8i 改用 Boardfly 拓撲：4 顆一托盤、8 托盤用銅線組成一組（32 顆），36 組「經 OCS 連接」成最多 1,024 顆可用的 pod，最遠 7 跳，其中一跳是光[[google-tpu8-blog-20260422]]。

<div class="pair">

![TPU 8i 的 Boardfly 拓撲：銅線組加 OCS 的三層結構。（Google 技術部落格的圖）[[google-tpu8-blog-20260422]]](img/vendor/google-tpu8i-boardfly-topology-20260422-01.png)
![TPU 8i 最遠 7 跳的路徑，其中 1 跳經過 OCS。（Google 技術部落格的圖）[[google-tpu8-blog-20260422]]](img/vendor/google-tpu8i-boardfly-ocs-7hop-20260422-02.png)

</div>

**一個 pod 要幾台。** Google 的論文講 TPU v4：64 顆 TPU 的 cube 六面各 16 條、共 96 條光鏈路接 OCS；3D 環狀拓撲的環回要接同一台 OCS，所以每個 cube 接 6 × 16 ÷ 2 ＝ 48 台 OCS；v4 的 OCS 是 136 × 136（128 埠加 8 埠備用），48 台接 64 個 cube 共 4,096 顆[[arxiv-2606-15870-google-tpu]]。Ironwood 9,216 ÷ 64 ＝ 144 個 cube，若沿用同一拓撲，每台 OCS 要接 144 對、288 埠，仍在 300 埠的 OCS 內，仍是 48 台（計算；論文沒寫 Ironwood 的台數）。

![Google 論文的圖：64 顆 TPU 的 cube 六面出線，經 X、Y、Z 三組 OCS 接成 3D 環狀拓撲。[[arxiv-2606-15870-google-tpu]]](img/papers/arxiv-2606.15870-google-tpu-cube-ocs-fig4-202606.png){.s}

**一年出多少台、市場多大，各說法並排：**

| 誰 | 數字 |
|---|---|
| 一家投資研究（Convequity）[[substack-newdealinvest-ocs-20261002]] | Google 2026 年約 1.5 萬台（代工廠 Calient 約 9,000、Lumentum 約 4,000、Coherent 約 1,400） |
| 另一家投資研究（semifundamental）[[substack-semifundamental-ocs-20260326]] | 2026 年全市場超過 2 萬台，Google 約 1.8 萬台，其中外購約 5–6 千台；Coherent 約出 3,000 台給 Google |
| 一家研究機構（經上市公司半年報轉述）[[cninfo-tengjing-h1-20260829]] | 2029 年 OCS 出貨破 5 萬台，2025–2030 年出貨年複合成長 15% |
| 光學市場研究機構（2025-12）[[cignal-ocs-2029-20251205]] | 外部 OCS 市場 2029 年超過 25 億美元 |
| 同上（2026-06，經訊石）[[xunshi-cignal-20260622]] | 扣除 Google 自用，2026 年 OCS 可觸及市場超過 10 億美元 |
| 同上（2026-07）[[cignal-ocs-2030-20260730]] | 2030 年超過 80 億美元，2026–2030 年年複合成長 30% 以上；上修「幾乎全部」來自 GPU scale-up（NVL576，2028 年起量）；這家機構自己寫市場大小「高度取決於幾個變動很大的假設（每埠價格、XPU 出貨）」 |
| 另一份摘要[[semiengineering-optical-5yr-20260406]] | OCS 的 TAM 超過 30 億美元 |
| Lumentum[[investing-lumentum-q4fy26-20260811]] | 2026 下半年 OCS 4 億美元「照計畫」；2027 會計年度第一季是第一個破億美元的 OCS 季；有一個客戶「有內部供應來源」，預計 2027 年初成為第一大供應商；2028 年規劃托盤內（in-tray）OCS |
| Coherent[[zacks-coherent-q4fy26-20260812]] | OCS 機會超過 40 億美元 |

另外，Lumentum 年報寫 OCS 在 2026 會計年度（到 2026 年 6 月）貢獻超過 9,000 萬美元營收[[sec-lumentum-10k-20260817]]。

**Coherent 自己的序列。** 2025 年 11 月說已向 7 家客戶出貨 OCS 系統（64×64 和 320×320 兩種規格），問答中提到有客戶在談把 OCS 交換器放進 scale-up 網路裡；2026 年 2 月說接洽的客戶超過 10 家；2026 年 5 月把 OCS 的市場機會從超過 20 億美元上調到超過 40 億美元，理由是資料中心互連、scale-out、scale-up 網路的用途都在擴大[[fool-coherent-q1fy26-20251106,fool-coherent-q2fy26-20260204,fool-coherent-fy26q3-20260506]]。上面表裡 8 月那一列的「超過 40 億美元」，5 月就已經這樣說了。

**模組廠怎麼看外部 OCS 的需求時點。** 新易盛 2026-06-02 說公司在 OCS 已有布局，「预计市场明年下半年或者 2028 年将有批量供应需求」；2026-07-20 改成「预计 OCS 产品自 2028 年开始有批量级商业需求」。同一家公司，一個半月內往後挪了一格[[cninfo-eoptolink-irm-20260602,cninfo-eoptolink-irm-20260720]]。

**中國零件廠和設備廠各自說的（投資人記錄）：**

| 公司 | 日期 | 說法 |
|---|---|---|
| 炬光科技 | 2026-05-07 | OCS 相關業務推進相對較快，已進入產能爬坡並逐步實現批量生產[[sse-focuslight-irm-20260507]] |
| 炬光科技 | 2026-06-02 | 在 OCS 領域已切入 MEMS 技術路線，供應 N×N 大透鏡陣列，相關產品處於小批量供應階段[[sse-focuslight-irm-20260602]] |
| 炬光科技 | 2026-08-14 | OCS 用的微透鏡陣列（MLA）在大客戶處持續爬坡並進入量產階段[[sse-focuslight-irm-20260814]] |
| 羅博特科（ficonTEC 母公司） | 2026-03-01 | ficonTEC 與瑞士一家頭部客戶簽了兩條完整自動化產線的設備訂單，用來生產該客戶的 OCS 核心模組；第一條整線預計 2026 年第一季交付[[cninfo-ficontec-irm-20260301]] |
| 騰景科技 | 2026-04-02 | 大尺寸純 YVO4（釩酸釔）晶體已開始量產[[sse-tengjing-irm-20260402]] |
| 光迅科技 | 2026-05-14 | 有 OCS 相關技術和產品布局，目前在市場拓展及客戶驗證階段[[p5w-accelink-results-20260514]] |
| 光庫科技 | 2026-04-01 | 全資子公司武漢光庫有 OCS 代工業務，營收占比較低，對公司業績影響較小[[cninfo-oplink-irm-20260401]] |

炬光同一家公司三個月內有爬坡、小批量、量產三種說法，但 6 月那句指的是 MEMS 路線的 N×N 大透鏡陣列，5 月和 8 月講的是 OCS 整體或微透鏡陣列，可能不是同一個產品，不能當成進度單向往前走。

**每顆 TPU 的 OCS 是變多還是變少？兩種說法相反。** 光學市場研究機構的說法是下一代 TPU 架構每顆會用更少的 OCS 埠，並分析 Boardfly 的較低 OCS 埠對 TPU 比[[cignal-ocs-2q26-20260723]]；另一位 KOL 轉述的估計是 TPU7 每千顆約 5 台、TPU8 約 17–18 台，TPU8 生命週期 OCS 需求約 25.9 萬台[[fangezi-tpu8-ocs-20261010]]。TPU8 的 OCS 要更快切換，MEMS、液晶不夠快，會帶出矽光子 OCS 的需求（第三方的說法）[[substack-newdealinvest-ocs-20261002]]。「SPOCS」這個詞只有那位 KOL 用，Google 的部落格和 Hot Chips 轉述都沒有，查不到定義[[fangezi-tpu8-ocs-20261010,google-tpu8-blog-20260422]]。

**誰做零件：**

| 環節 | 查到的 |
|---|---|
| 整機 | Google 自己設計的 MEMS OCS 由 Calient 代工（Calient.AI，美國加州 Goleta；官網和聯絡頁都沒有台灣據點或台灣股東）[[calient-about-20261012]]；Lumentum（自稱「今天唯一的 OCS 商用供應商」）、Coherent（液晶）；瑞士的 Huber+Suhner 2025 年 7 月接到一家超大規模業者的 OCS 大單，2026 上半年首度貢獻營收，因前期投資通訊部門虧損[[hubersuhner-polatis-20250730,hubersuhner-h1-20260818]]；光學市場研究機構說 Google 已對 Lumentum、Coherent、Huber+Suhner 下了「種子訂單」，正從自製轉向外購[[cignal-ocs-2030-20260730]] |
| MEMS 鏡 | 瑞典 Silex 自稱「唯一生產 OCS 晶片的 MEMS 代工廠，做了十年」，Q2 營收年增 27.3%、受 OCS 需求帶動，並向 onsemi 買美國賓州晶圓廠改成 MEMS 廠[[silex-q2-2026-20260717,silex-pa-fab-20260707]]；中國賽微電子說自己的 MEMS-OCS 晶片「尚未量產」；民德電子參股的公司，SOI 矽片用在 OCS 微鏡陣列[[cninfo-irm-ocs-20261012]] |
| 二維準直器陣列（光纖陣列加透鏡陣列） | Coherent 2025 年推出 OCS 用二維準直器陣列[[coherent-2d-collimator-20250317]]；德國 Ingeneric 展示光交換用準直器陣列[[ingeneric-ofc2026-202603]]；中國騰景科技說「適配 MEMS、液晶、壓電陶瓷」，液晶方案部分產品已批量[[sse-tengjing-irm-20260930]]；中航光電子公司翔通的光纖陣列部分訂單排到 2027 年[[cninfo-irm-ocs-20261012]]；Molex 推 544×544 埠的 MEMS OCS 平台[[molex-ocs-2026]]。一篇第三方文章說 Google 的光纖陣列廠是 Coherent、Molex、Fiberguide，並估 176×176 平台的準直器系統約 2,000 美元[[substack-semifundamental-ocs-20260326]]。設備端，ficonTEC 為交換器廠提供 OCS 模組的雷射焊接、主動對位設備[[ficontec-ocs-202511]] |
| 台廠 | 只有一則專欄說波若威擅長光準直器、智邦投資液晶的 InLC 合作開發 OCS；台廠自己說供應 OCS 準直器陣列或 MEMS 的，查不到[[ctee-taiwan-ocs-20251206]] |

這是 FAU 以外的另一個光纖陣列市場。仕佳光子、中航光電、Coherent 都兩種都做，但用不用同一套設備、同一批廠，沒有資料。

**NVIDIA 也要 OCS 嗎？** 光學市場研究機構說 NVIDIA 會把 OCS 放進 NVL576（上節第 4 種說法）；專家調研說 NVIDIA 定製的小埠數 OCS 樣品用液晶方案，部署在 spine 交換器層[[eastmoney-dfau-survey-20260531]]；另一份說 Lumentum 的 64×64 OCS 樣品已送 Microsoft、NVIDIA 測試[[substack-semifundamental-ocs-20260326]]。OCP 白皮書提到插入損耗讓 OCS 實際只能走一到兩跳[[ocp-ocs-whitepaper-202604]]。

## 慢而寬：VCSEL、多模光纖、Micro LED {#tm-wide}

現在的 CPO 是「雷射加單模光纖」，每條通道跑得很快（例如 100G、200G），通道數少。**慢而寬**反過來：把同樣的頻寬切成很多條慢速通道並行。以 Microsoft 的 MOSAIC 為例，一般 800G 是 8 條 100G，MOSAIC 改成 400 條 2G，排成 20 × 20 的陣列，面積不到 1 平方毫米[[microsoft-mosaic-paper]]。每條通道慢，就不需要 DSP、類比數位轉換這類耗電的電路，約 1 到 2 pJ/bit（每傳 1 位元耗多少皮焦耳，越低越省）[[trendforce-microled-20260629]]。

慢而寬有三種光源：Micro LED（不用雷射）、VCSEL（從晶片表面垂直發光的小雷射，用砷化鎵做）、以及兩者的混合方案。它們共同的特點是：通道多、每條慢、光纖多；原料、代工、光纖都和現在的 CPO 不同。

### Micro LED

Micro LED 是一片很小的 LED 陣列（例如 20 × 20 個，每個 2 Gbps，合起來 800G），上面加微透鏡，接一根有很多纖芯的成像光纖；另一頭由像相機感光元件一樣的 CMOS 感測陣列接收。

<div class="pair">

![Micro LED 的做法：一片 CMOS 晶片上排一整片小 LED，上面加微透鏡，接一根有很多纖芯的成像光纖；另一頭由 CMOS 感測陣列接收。[[microsoft-mosaic-paper]]](img/papers/sigcomm25-mosaic-was-architecture-fig3.png)
![上半是今天：機櫃之間走雷射光纖、機櫃內走銅線，每條線 8 個快速通道（8 × 100G，紅線）。下半是 Micro LED：一樣插在原本的插拔式插槽，改成 400 個慢速通道（400 × 2G，紫線），交換器和電路板都不用改。[[microsoft-mosaic-paper]]](img/papers/sigcomm25-mosaic-today-vs-microled-links-fig4-5.png)

</div>

<div class="pair">

![原型實拍：發射板上的 Micro LED 晶片、微透鏡，多芯光纖另一頭看到的 100 個光點（每個點是一條通道），以及接收板上的 CMOS 感測晶片。原型是 100 條通道、每條 2 Gbps。[[microsoft-mosaic-paper]]](img/papers/sigcomm25-mosaic-prototype-fig9.png)
![做成產品時的構想：一樣是一支插拔式模組，裡面一片約 1 公分見方的晶片，上面同時有發光和收光的陣列。[[microsoft-mosaic-paper]]](img/papers/sigcomm25-mosaic-pluggable-module-fig10.png)

</div>

場景不一樣：友達和富采都說鎖定 10 公尺以內，也就是機櫃內，對應的是 scale-up[[auo-press-20260831,microledinfo-ennostar]]。友達說約 2 到 3 年後商品化，Micro LED 發射端來自集團的富采、收光端來自鼎元，光纖來自 Corning[[microledinfo-auo,auo-press-20260831]]；富采說可靠度驗證要 3,000 小時以上，生態系時程「放眼 2028」，已驗證每通道 1.25 Gbps[[youfenxi-ennostar-microled-20260902]]；錼創說最快 2 年內大規模爆發，和世芯集團的光循科技策略合作[[youfenxi-brillink-microled-20260406]]。一家研究機構預估出貨約 2028 下半年起量，2030 年 Micro LED CPO 光收發模組產值 8.48 億美元[[trendforce-microled-20260629,ltn-trendforce-microled-20260511]]。

美國這邊：Microsoft 和聯發科做 Micro LED 的主動光纜，說「預計 2027 年底前與產業夥伴商用化」[[eetasia-mediatek-microsoft-20260326]]。友達在 2026-04-30 法說被問到這件事，總經理說微軟這個用多顆矩陣取代高耗能、高成本單顆雷射的架構，與友達的定位一致，但沒有確認 2027 年底，只說「兩到三年內應該就可以快速進入到產品應用」[[allmind-auo-q1-20260430]]。Avicena 已經出貨 1 Tbps 的評估套件，最多 335 條通道、每條最高 3 Gbps，2026 年 9 月在 ECOC 展示第一款帶接頭的版本，接頭用業界標準的 MPO 外型、插芯是為多芯光纖特製的[[semitoday-avicena-20260917]]。Credo 收購了 Micro LED 晶片互連公司 Hyperlume，「給客戶 scale up AI 網路的新選項」，產品時程查不到[[nasdaq-credo-hyperlume-20250929]]；Credo 說它的 LED 光纜（ALC，30 公尺）10 月在 OCP 展示、FY28 開始有營收[[fool-credo-fy27q1-20260901]]。研究方面，法國 CEA-Leti 有三年期的 Micro LED 資料鏈路計畫，2026 年 4 月再和力積電合作把短距光鏈路放進 3D 堆疊和中介層平台[[microledinfo-cealeti-20251118]]；另有經濟日報傳 Intel 和友達合作 Micro LED 封裝，雙方都沒證實[[xenospectrum-intel-auo-20261010]]。

<div class="pair">

![Micro LED 光鏈路的原理：兩端晶片（GaN 發光層疊在 CMOS 上）各有一整片小 LED 和收光元件，中間一束成像光纖，一個芯負責一組 LED 和收光元件，也就是一條通道。[[optics-org-cealeti-20251119]]](img/media/optics.org-CEALeti微LED光鏈路原理-20251119-01.jpg)
![台廠的構想：GPU 旁邊放一組 Micro LED 陣列和收光陣列，加上驅動器（TX driver）和放大器（RX TIA），用一條多芯光纖接到另一片板子。[[bnext-ennostar-microled-20260701]]](img/media/數位時代-富采MicroLED光互連架構-20260701-01.jpg)

</div>

### 友達在法說會上說了什麼 {#tm-auo}

友達四場法說的說法依日期排（AllMind 的 AI 轉寫稿，說話者是 AI 指派的，下面標的職稱以原稿為準，可能有錯；2025Q4 是英文場，2026Q1、Q2 是簡體中文場）：

| 日期 | 說法 |
|---|---|
| 2025-10-30（2025Q3） | 去年起與富采（Ennostar）合作，把產能從 Micro LED 延伸到矽光子和光通訊，並加入矽光子產業聯盟。友達負責光學設計模擬和巨量轉移（轉錄寫成 mask transfer，應是 mass transfer），也在做光耦合、組裝，到模組和系統層級的開發[[allmind-auo-q3-20251030]] |
| 2026-02-10（2025Q4） | 友達投資的富采專攻 Micro LED，其子公司鼎元（Tyntek）專攻接收端；友達能整合整套光通訊模組；未來光通訊模組勢必轉向玻璃基板，友達在這方面累積 30 年經驗；「已經做出 demo 樣品，正在與客戶討論商品化」。同場另說：「CPO is still in the development stage. Currently, the industry expects CPO for optical communications to mature in 2 or 3 years. So it is not contributing to our revenue yet」[[allmind-auo-q4-20260210]] |
| 2026-04-30（2026Q1） | 董事長說已與 AI 供應鏈裡的光通訊大廠共同開發 Micro LED 光通訊模組，用在機櫃內的 scale-up；富采提供發射元件、旗下鼎元提供接收的光二極體，友達做系統整合；「我们有信心这个商品化，那应该在两到三年后就会成熟上市」[[allmind-auo-q1-20260430]] |
| 2026-07-30（2026Q2） | 說話者標為 Speaker #2（AI 指派，疑為友達管理層）：一個 CPO 光通訊模組可能價值「幾百塊美金」，卻要與幾萬甚至十萬美金的 GPU 或 HBM 封在一起，良率要求非常高；所以友達現在著重 scale-up 和 scale-out、「直接取代現在的銅線」，而不是和 GPU 封在一起，因為那條路時間可能長一點；目前跟國際知名的光通訊互連廠商談合作，已在設計和送樣過程中[[allmind-auo-q2-20260730]]。第三方整理的同日備忘錄寫法一致，但那不是原話[[fugle-auo-20260730]] |

「2 到 3 年後成熟」這句在 2026 年 2 月法說就出現了（當時的措辭是「業界預期」），4 月、7 月重複，口徑穩定，不是 8 月的新聞稿才說的。7 月的說法也等於回答了為什麼友達鎖定的是機櫃內、機櫃間取代銅線的連線，而不是和 GPU 封在一起：價值量和良率的理由是它自己給的。

**需不需要 FAU 那種對位？** 沒有任何來源說它用 V 型槽排單模光纖那種 FAU。友達 2026 年 2 月的法說（英文場，AI 轉寫稿）有主管在回答 Micro LED 與雷射的比較時提到 FAU，說加上 FAU 可以提高幾十公尺以內資料中心連線的頻寬、降低耗電；轉錄把 FAU 寫成 fiber assembly units（業界通用的全名是 fiber array unit，可能是聽錯，要核對影音），沒有說明友達指的 FAU 是什麼結構[[allmind-auo-q4-20260210]]。Microsoft 的論文用成像光纖，一顆 Micro LED 對到「多個」纖芯，不是一對一，「大幅放寬對位精度要求」，但還是要對位；Micro LED 的光發散角很大（約 180°，光纖只收約 20° 以內的光），標準微透鏡陣列收不到大部分光，Microsoft 自己設計了全反射透鏡，把光束收到 ±12°，耦合效率是標準微透鏡的 2 倍以上，可用奈米壓印做晶圓級生產[[microsoft-mosaic-paper,lfw-yole-microled-20261006]]。Yole 把「光耦合和連接」列為第二大瓶頸[[lfw-yole-microled-20261006]]。對位公差的數字，Avicena、MOSAIC、友達都查不到。

反對的聲音來自大立光執行長林恩平：「我個人是覺得 Micro LED 不太可能」，理由是耗電和尺寸，客戶持保留態度[[cna-largan-q3-20261008]]。查到的「客戶」只有 Microsoft 自己；沒有任何雲端業者或 GPU 廠公開說要採購 Micro LED 光連接。媒體轉述法人的說法：還有高頻調變、光耦合精度、巨量轉移的挑戰，目前只適合機櫃內、機櫃間短距[[ctee-microled-20260421]]。

### VCSEL 和多模光纖

- **Lumentum**：OFC 2026 展示多模 1060 nm VCSEL 陣列和主機 ASIC 共同封裝，鎖定 UCIe、PCIe 這類「慢而寬」的 scale-up 協定；用扇出型晶圓級封裝和多模光纖；背面透鏡做精準光學對位；可備用通道、耐 150°C 以上；自己說是矽光子和 InP 雷射之外的「獨立供應鏈選項」[[lumentum-pr-ofc2026-vcsel-20260317]]。10 Tbps 的 VCSEL 光引擎原型，分析師把它看成「InP 供應吃緊時」某些 scale-up 場景的替代[[lumentum-blog-nextphase-20260430]]。
- **Lumentum、高通、Corning（ECOC 2026）**：聯合展示 1060 nm VCSEL 的晶粒對晶粒光連接：高通的介面 IP、Lumentum 的 VCSEL、Corning 的多模光纖，每通道 32 Gb/s，鎖定未來的 CPO、NPO 和 UCIe[[lumentum-pr-qualcomm-corning-20260921]]。Lumentum 在 ECOC 的演講（經媒體整理）：第一代陣列 64 Gb/s × 256 通道 ＝ 8 Tb/s、2.0 mm 岸線、2.5 pJ/bit；1060 nm 在 115°C 烤箱 5,000 小時零失效，850 nm 1,600 小時後開始失效；講者承認每通道慢、光纖多是成本問題，「對 scale-up 可以接受」[[stt-ecoc2026-lumentum-1060-202609]]。
- **Broadcom**：論文用 200G VCSEL 做 scale-up NPO；3.2T 引擎 19 × 19 mm、4 組 8 通道陣列；50 公尺 OM4 跑 9 小時無錯，50 公尺那組用 Corning 的客製高頻寬光纖[[stt-broadcom-vcsel-npo-2026]]。
- **ams OSRAM 和貿聯（ECOC 2026）**：850 nm 薄膜 micro-VCSEL 陣列，25 μm 間距、32 Gb/s、約 0.25 pJ/bit；和貿聯合作展示「接頭化的多芯光纖方案」，貿聯負責光纖陣列整合和光連接[[semitoday-amsosram-bizlink-20260922]]。德國財經網站說沒有已宣布的終端客戶、沒有量產時程，「依媒體報導，這項合作的營收最早 2028 年」[[tradingtreff-amsosram-20260929]]。
- **Coherent**：每個發光點獨立驅動，適合「寬而慢」；背面出光的陣列可用 32 個發光點[[coherent-blog-wide-slow-20260625]]；ECOC 展示 GaAs VCSEL 的 NPO／CPO 1.2 pJ/bit、不用外部雷射（媒體整理）[[fundaai-ecoc2026-20260929]]。
- **PicoJool**：200G VCSEL，設計磊晶層、交給磊晶廠長晶；穩懋只做晶圓製程，切割後交封裝夥伴；4 × 16 光纖束接頭 64 通道、每通道 200G ＝ 12.8T；下季送樣，2027 年初量產[[chipstrat-picojool-20260716]]。
- **其他**：Applied Materials 的 Chris Cole（以個人身分）說慢而寬需要的封裝「還要 4 到 6 年」；OpenAI 的技術人員說慢而寬可以用在 GPU 對 GPU 直連[[fundaai-ecoc2026-20260929]]。

**台廠在哪裡？** 穩懋 7 月法說：光通訊營收佔比第一季 5–10%、第二季 10–15%，2027 年挑戰雙位數；EML、VCSEL 都已量產；法說沒有提 scale-up 或 PicoJool[[cnyes-winsemi-20260724]]。宏捷科：850、940 nm 短距光通訊產品年需求成長超過 50%，光通訊等非射頻產品「最快 2028 年前後」明顯成長[[youfenxi-aht-20260806]]。全新的法說簡報「未來驅動」列 VCSEL for 400G & 800G[[vpec-slides-20260902]]；英特磊預期 200G VCSEL 2026 年量產[[technews-iet-vcsel-20260428]]。穩懋、宏捷科、全新任何一家公開說自己的 VCSEL 用在 scale-up，查不到。

**貿聯是另一種位置。** 一手文件只確認貿聯是 Credo AEC（銅線）的長約代工[[sec-credo-10k-20260615]]；媒體和外資說它是 Credo LED 光纜的主要或獨家供應商（Credo、貿聯都沒說）[[moneydj-credo-alc-20260915]]；承接康寧和 Senko 的光纖接頭組裝、102.4T CPO 交換器內部連接線已送樣[[cnyes-bizlink-computex-20260602,udn-bizlink-corning-20260929]]。光通訊目前約占貿聯營收 2–4%（官股券商報告，經媒體轉述）[[ctee-bizlink-optics-share-20260723]]；貿聯自己的法說簡報沒有光通訊營收數字，也沒有提 Credo 或 CPO[[mops-bizlink-q2-20260821]]。

### NVIDIA 為什麼暫停

NVIDIA 的 Daniel Kuchta 在 ECOC 2026 做了一場 VCSEL 綜覽演講，開場聲明這是多家公司技術的綜覽，「不代表 NVIDIA 對任何一家的背書」。媒體整理的投影片內容：NVIDIA 研究部門的慢而寬概念設計，每條有效光纖 50 Gb/s、模擬約 3.0 pJ/bit、距離 10 公尺；一個引擎 4.8 Tb/s 單向（16 條光纖帶 × 6 芯 × 50 Gb/s），一顆 GPU 12 個引擎共 57.6 Tb/s 單向；算成一顆 GPU 單向 1,152 芯、雙向 2,304 芯（計算：57.6 Tb/s ÷ 50 Gb/s ＝ 1,152），整個機房約六萬芯。他說的原話中譯：「真正讓我們停下來的是光纖的高成本。我們真的需要重新思考光纖與連接器的成本，然後也許再回頭重新檢視這個方法。」[[stt-ecoc2026-kuchta-20260924]]另一份整理的說法是 NVIDIA 把它的 VCSEL 設計描述為「探索性概念，不是產品計畫」，並不預期 2027 下半年前會有具名的慢而寬部署[[fundaai-ecoc2026-20260929]]。兩份都是看演講寫的二手，原投影片沒有公開。

同一場演講提到一條新的多模光纖規格：26 µm 芯徑、80 µm 玻璃外徑、1060 nm，「在 IEEE 社群推」。這件事在 IEEE 802.3ds（每波長 200 Gb/s 的多模光纖實體層）的文件裡查得到：

- 2026 年 3 月 11 日，Panduit 提「為 1060 nm 優化的多模光纖」，選項 A 是 50 µm 芯、選項 B 約 26 µm 芯；支持者名單有兩位 NVIDIA 工程師，包括 Kuchta[[ieee8023ds-panduit-26um-20260311]]。
- 2026 年 3 月 12 日，IEEE 802.3 致函 IEC，請 IEC 考慮制定新的 1060 nm 多模光纖標準，芯徑選項包括 50 µm 和 24–32 µm[[ieee8023-liaison-iec-20260312]]；5 月 IEC TC86 回覆會成立聯合工作組[[iec-tc86-reply-202605]]。
- 2026 年 5 月 12 日，1060 nm 基線提案（三級光纖、三種實體層）通過，支持者有 NVIDIA 的 Kuchta[[ieee8023ds-1060nm-baseline-20260512]]。
- 2026 年 9 月 15 日，Corning 建議芯徑先訂 27 ± 2 µm；同日表決，芯徑寫成「25 到 29 µm 的範圍」24 票、寫成「27」8 票；目標 11 月出 D2.0[[ieee8023ds-vote-20260915]]。
- 「80 µm 玻璃外徑」，讀過的 9 份 802.3ds 文件都沒有；只有 Lightera 一句「小外徑多模光纖」。參與的廠商：光纖是 Lightera 和 Corning、佈線是 Panduit 和 CommScope/Amphenol、光源是 Lumentum、Coherent、Broadcom、華為；名單裡沒有台灣公司[[ieee8023ds-lightera-20260311]]。

這是多模光纖加二維陣列或多芯插芯，不是單模 V 型槽 FAU。

### OCP 上的多芯光纖

多芯光纖（一根光纖裡有多個纖芯）在 OCP 的議程上出現三次：住友電工講多芯光纖用在 scale-up、scale-out、scale-across；LightXcelerate 的背發光 micro-VCSEL 陣列配 19 芯多芯光纖，每根光纖 608 Gb/s；TeraHop 的 SDM4 四芯光纖 MSA[[ocp2026-agenda-20261012]]。一根光纖有 4 或 19 芯，光纖數和 FAU 的通道排法就和現在一根一芯的 V 型槽陣列不同；V 槽要不要改、誰做多芯的扇入扇出，沒查到。

### 兩條路並排

| 方案 | 每條通道速度 | 通道數 | 距離 | 耗電 | 進度 |
|---|---|---|---|---|---|
| 雷射加單模光纖的 CPO（NVIDIA Spectrum-X） | 200G | 每個 800G 埠 4 條 | 單模直連線最長 500 公尺 | 雷射式連結約 5 pJ/bit（研究機構估計） | 2026 年 8 月出貨[[nvidia-sn6000-manual-20260916,lfw-yole-microled-20261006,cnyes-spectrumx-20260817]] |
| NVIDIA 研究部門的 VCSEL 概念設計 | 50G | 一顆 GPU 單向 1,152 芯 | 10 公尺 | 模擬約 3.0 pJ/bit | 暫停[[stt-ecoc2026-kuchta-20260924]] |
| Lumentum 1060 nm VCSEL | 32G、64G | 256 通道 ＝ 8 Tb/s | — | 2.5 pJ/bit | 示範[[stt-ecoc2026-lumentum-1060-202609]] |
| Microsoft MOSAIC | 2G | 800G 用 400 條；原型 100 條 | 最遠 50 公尺 | 一端 3.1–5.3 W，比現在 800G 光纖連結（9.8–12 W）少 56–68% | 研究原型[[microsoft-mosaic-paper]] |
| Avicena LightBundle | 最高 3G | 最多 335 條 | 最遠約 5 公尺 | 1–2 pJ/bit | 評估套件已出貨[[semitoday-avicena-20260917,trendforce-microled-20260629]] |
| 富采、友達 | 1.25G（已展示） | | 10 公尺以內 | | 2026 年 9 月展出模組，說 2–3 年後商品化[[microledinfo-ennostar,auo-press-20260831,microledinfo-auo]] |

耗電的比較要小心：Micro LED 的 1 pJ/bit 是把 SerDes（把一路高速電訊號拆成多路慢速、或反過來的電路）也拿掉的情況；要接今天只會吐高速序列訊號的交換器晶片，還是得加 SerDes 和驅動器，耗電會回到約 3–6 pJ/bit[[lfw-yole-microled-20261006]]。一篇主推 VCSEL 的論文自己做的估計也顯示，每條通道慢的方案不見得都比較省：矽光子 CPO 約 6.7 pJ/bit（含 SerDes 約 8），Microsoft 的 Micro LED 模組 3.6 pJ/bit（總計 6.6–7），VCSEL 在 4 Gb/s 可到 0.5 pJ/bit；Avicena 背對背量測做到 1 pJ/bit，但 GaN LED 插座效率只有 1.2%、要 4.4 V 驅動[[arxiv-2601-14342]]。

![每傳 1 bit 要花多少電的估計（pJ/bit，越低越省），條件都是一塊 3.2 Tbit/s 的光引擎。綠色是 VCSEL，藍色是 Micro LED，紫色是現在 CPO 用的矽光子。這是一篇主推 VCSEL 的論文自己做的估計。[[arxiv-2601-14342]]](img/arxiv-2601.14342-vcsel-cpo-scaleup-fig3-energy-per-bit-bars.png){.s}

這一類方案目前離 scale-up 的主流還遠：NVIDIA 的版本暫停、Lumentum 的是示範、Micro LED 的商用時點是 2027 年底到 2028 年。一家研究機構把 VCSEL NPO、主動銅纜（AEC）、Micro LED 列為機櫃內三大短距方案[[ltn-trendforce-microled-20260511]]。

## CPO 現在卡在哪？接下來怎麼發展？ {#q27b}

公開講到的卡關點，可以整理成幾個。前五個是做 CPO 本身的難處，後面是整個光通訊都在缺的東西。

**一、良率和可維修。**光引擎焊上基板後沒有重工的路：要拆下一顆已經回焊、填膠的光引擎，得在離交換器晶片幾毫米的地方加熱到 220–260°C，光引擎裡次微米的光纖對位也撐不過第二次加熱，所以一顆光引擎壞掉，整顆交換器晶片、基板和其他光引擎一起報廢[[tomshardware-npo-20260813]]。華星光預計 2027 到 2029 年以 NPO 為主，理由就是 CPO 良率不足、壞了難修[[luxnet-slides-20260828,udn-luxnet-20260828]]。供應鏈還不成熟、缺乏可靠度數據，客戶對採用 CPO 有所遲疑，需要龍頭大廠帶頭出貨逼供應鏈成熟[[semianalysis-cpo-book]]。良率的數字：Morgan Stanley（經媒體轉述）說 SoIC 良率約 50–60%、下游組裝良率 20–50%[[udn-ms-cpo-yield-20260611]]。Microsoft 在 OCP 的摘要點出另一個問題：光學整合越深，一顆雷射或 PIC 壞掉會連帶多條通道（失效域變大），系統又偏好單一高密度接頭，很難把備援路徑實體分開[[ocp2026-agenda-20261012]]。可靠度數據的現況見[量產到哪一步](#q27)。

**二、對位。**單一 PIC 的通道數升到百條以上，光學介面從一維的晶片邊緣走向二維陣列，「超高通道數 FAU 與 PIC 晶片的精密對位組裝，已成為決定量產良率與成本的最大瓶頸」[[udn-gmt-fau-pic-20260827]]。怎麼對位見[怎麼對準、怎麼固定](fau.md#q14)。台積電的路線表把 2026 年的單排 FAU 換成 2028 年的雙排 FAU，大立光說量產專案都是單排、雙排在概念驗證，10 月法說說多排 FA 送樣，「會是 2028 年的案子」[[tomshardware-cpo-foundry-20260803,yahoo-largan-q2-20261010]]。

**三、測試。**CPO 把 EIC、PIC、FAU、光引擎和交換器晶片封在一起，測試要從晶圓一路做到整台機器，大致分四個節點：PIC 晶圓級光學測試、EIC 和 PIC 接合後的光電測試、光引擎測試、系統級最終測試。各家對「第幾段」的定義不一樣（有四段、有五段），每一段是誰的機台、各家說法並排，見[測試分幾段](equipment-test.md#eq-test)。測試介面廠給過一組數字：單模光纖纖芯 9 微米、累積機械公差常到 3.8 微米，天然產生高達 40% 的位置偏差，單次對準要 5 到 30 秒[[wallstreetcn-wins-forum]]。另有測試設備廠說，業界預測 FAU 廠產能跟不上，需要第二來源，第二來源若用不同接頭會「很亂」[[semieng-cpo-test-20261007]]。測試步驟本身也可能被精簡：封測廠研究員說 PIC 測試以後可能不需要做[[semieng-cpo-test-20261007]]。

**四、雷射產能。**Lumentum 執行長說，晶圓廠和材料的產出已經比客戶要的少 30%[[tomshardware-lumentum-20260731]]；誰說缺、缺多少，見[誰說缺](lasers.md#las-shortage)。

**五、後段封裝的人工和成本。**錢主要花在後段，不在晶片。Lightmatter 說，CPO 的前段晶圓代工和載板只佔成本約 40%，後段封裝和製程佔約 60%；後段貴的核心原因是光纖貼合的良率和效率不足，而且高度靠人工[[technews-trendforce-forum-20260529]]。保偏光纖 FAU 現在用人工組裝，人工佔總成本 50–80%[[utwente-phix]]。一篇綜述論文拆的矽光收發器成本也是同一個方向：封裝、測試、組裝佔 80%[[lsa-review-202601]]。

**六、上游原料一起缺。**做 PIC 的 SOI 晶圓、做雷射的 InP 基板、拉光纖的預製棒，三條線都在擴產，也都有人說需求超過預期：

| 原料 | 用在哪 | 查到的狀況 |
|---|---|---|
| SOI 晶圓（矽上面隔一層氧化物再一層矽） | PIC 的底材（[第 8 題](inside.md#q8)） | Soitec 和多家客戶簽了多年期產能保留協議，客戶付了現金訂金[[soitec-fy27q1-20260722]]；說「為 CPO 產業認證出貨的量在增加，準備接下來的量產」[[soitec-fy26-20260527]] |
| InP 基板 | 雷射晶片（[第 21 題](lasers.md#q21)） | JX 金屬未來四年最多投資 1,200 億日圓，產能要擴大約 7 到 10 倍[[jx-inp-20260616]]；住友電工把 2028 財年產能目標從 2024 財年的 2.4 倍拉到 3.1 倍（媒體報導）[[technews-sumitomo-inp-20260703]]。見 [InP 基板和銦](lasers.md#las-inp) |
| 光纖預製棒 | 拉成光纖 | 新產能要 18–24 個月才能蓋好（媒體報導）[[tomshardware-fiber-20260516]]；研究機構說預製棒已成光纖價值鏈的瓶頸，中國 G.652.D 裸光纖價格 2025 年 11 月到 2026 年 1 月漲了 80% 以上[[cru-preform-20260226]]。講的都是一般資料中心光纖，沒有一則專講 CPO 用的光纖。見[光纖和預製棒](passive.md#pas-fiber) |

**七、DSP 也在缺。**這是插拔式光模組的瓶頸，反過來也是 CPO 拿掉 DSP 的理由之一：1.6T 模組用的 DSP 要 3 奈米製程，一位產業專家估計 2026 年需求超過 2,000 萬顆、實際出貨只有 1,600 到 1,700 萬顆[[cnyes-hao-nomura-dsp-20260923]]。細節見[DSP 缺貨推向哪裡](alternatives.md#alt-dsp)。

**八、scale-up 的量要等。**CPO 要真正變大，靠的是從 scale-out 走進 GPU 之間，但這一步的時點和形式（CPO、NPO、插拔式、OCS、銅線）都還沒定，見 [scale-up 什麼時候用光](#tm-scaleup)。

**九、零件廠、材料廠、整機廠談時程，口徑不一。**

- 天孚通信 2026-08-19 說 CPO 相關配套產品已進入量產交付階段，「产品良率已满足规模量产需要」；炬光科技 2026-08-31 說「行业尚未形成统一标准，不同技术方案仍处于并行发展阶段」，並認為應理性看待商業化節奏[[cninfo-tfc-20260819,sse-focuslight-irm-20260831]]。兩句不互相反駁（一個講自己對某客戶的 FAU、外部光源，一個講整個產業路線），但同月的公開口徑不同；光庫科技 2026-04-01 則說 CPO 正從 800G／1.6T 埠場景開始導入，預計 2026–2027 年進入初步部署階段，後續逐步放量[[cninfo-oplink-irm-20260401]]。
- 住友電工（2026-06-10 決算說明會問答）：客戶把 CPO 和傳統插拔式並行評估，對 CPO 會不會立刻大幅起量，公司持「慎重」的看法[[sumitomo-qa-20260610]]。
- Soitec（SOI 晶圓廠，2026-07-23 法說會轉錄稿，說話者標示可能錯位）：scale-out 的 CPO 預期年底起量；scale-up 多半仍是插拔式，CPO 何時真正進來「是個問號」，CPO 的挑戰之一在組裝和測試，要確保整體組裝的良率[[investing-soitec-fy27q1-20260723]]。
- Fabrinet（2026-08-17 法說會轉錄稿，AI 轉寫）：NPO 往 6.4T、12.8T 走，製造複雜度和良率「變得關鍵」[[allmind-fabrinet-q4-20260817]]。2026-02 它說已有一些 CPO 營收但金額相對小，正與三家客戶做 CPO 專案[[fool-fabrinet-fy26q2-20260202]]；5 月被問三個專案是否都有營收，沒有回答是或否，只說營收「大部分還在前面」[[fool-fabrinet-q3-20260504]]。
- Lightmatter 的「後段封裝佔成本約六成」見上面的第五點；Fabrinet 把製造複雜度和良率當成自己的賣點，兩者可並列。

**接下來的方向**，各家的動作很一致：讓光纖和晶片可以分開測好再接上、減少主動對位的時間、把人工換成機台，以及擴產雷射和原料。

| 方向 | 誰在做什麼 | 進度 |
|---|---|---|
| 可拆式接頭：晶片這邊先固定一個接座，光纖做成插頭，最後一步才接上 | NVIDIA Spectrum-X 用垂直出光的可拆式光纖接頭，光纖在最後階段由精密機台全自動接上[[nvidia-blog-20260106]]；Lightmatter 和 Senko 的 vClick[[lightmatter-vclick-20260311,senko-lightmatter-20260311]]；Senko 的 SEAT 接座[[senko-wiwynn-computex2026]]；Corning 展示可拆式 FAU 接頭[[corning-ir-ofc2026-20260316]]，OCP 摘要講擴束的 VSFF 接頭[[ocp2026-agenda-20261012]]；Coherent 的可拆式 FlexConnect FAU 接頭[[futurum-coherent-photonlink-20260923]]；Credo 和 Senko 的盲插光學背板、Samtec 等六家的「可在現場更換」CPO[[credo-ocp-pr-20261009,ocp2026-agenda-20261012]]；NVIDIA 子公司 Mellanox 的 FAU 機械耦合件專利[[nvidia-mellanox-us20260063849a1]]；Intel、Marvell 的 ECTC 論文[[intel-ectc2026,marvell-ectc2026]]。詳見[可拆式接頭](detachable.md#det-why) | NVIDIA 的已隨交換器出貨；其他是產品發表、樣品、專利或論文 |
| 被動對位：靠擋塊、凸塊、對位記號放上去就對準 | Corning 的玻璃橋（[康寧玻璃橋](detachable.md#q29)）[[corning-gf-ectc2026,corning-glassbridge-brochure]]；台積電專利裡 FAU 底下的凸塊卡進基板溝槽[[us20260133379a1]]；Lightmatter 和 Flex 在 OCP 驗證被動對位的測試載具[[ocp2026-agenda-20261012]] | 型錄、論文、專利；沒有公開的量產時程 |
| 自動化設備：一次對更多通道 | 高明鐵和光循展示 120 通道 FAU 對 PIC 的自動對位平台，重複性優於 50 奈米[[udn-gmt-fau-pic-20260827]]；萬潤轉投資的光陽展出 160 通道 FAU 貼合機，定位 ±50 奈米[[udn-allring-160ch-20260907]]。見[對位貼合設備](equipment-test.md#eq-align) | 展會展示；光陽說已交付 1.6T、3.2T、6.4T 的 FAU 製造和檢測設備 |
| 測試往前移 | 上詮和晶圓測試廠合作開發光纖陣列探針卡[[ctee-cpo-test-20260914]]；測試介面廠開發測試用 Golden FAU 和自對準[[wallstreetcn-wins-forum]] | 開發中 |
| 雷射和原料擴產 | Coherent 的 InP 產能去年翻倍，計畫到 2027 年在 6 吋 InP 線上再翻一倍[[futurum-coherent-photonlink-20260923]]；JX 金屬、住友電工擴 InP 基板（見上表） | 擴產中 |

## 市場會長多大？取代的是誰？ {#q28}

各家估的數字差很大，主要是因為算的東西不一樣：有的只算 CPO，有的把 NPO、光模組一起算，有的算整個網路市場；假設的滲透率也不同。所以下面每一列只能自己跟自己比（從起點長到終點長了幾倍），不能拿不同列的數字互相比大小。

<table>
<tr><th>誰估</th><th>算的是什麼</th><th class="n">起點</th><th class="n">終點</th><th>前提、附帶數字</th></tr>
<tr><td>研究機構[[cna-trendforce-20260615,udn-trendforce-20260615]]</td><td>CPO＋NPO</td><td class="n">2025 年約 1 億美元</td><td class="n">2030 年 390 億美元以上</td><td>同一份估計：插拔式光模組到 2030 年仍有近 260 億美元</td></tr>
<tr><td>券商[[etenterprise-gs-20260520]]</td><td>scale-up 加 scale-out 的網路市場</td><td class="n">2026 年約 150 億美元</td><td class="n">2028 年 1,540 億美元</td><td>其中 CPO 約 910 億（59%），假設 scale-out 有 29% 改用 CPO</td></tr>
<tr><td>日本研究機構[[moneydj-fuji-20260121]]</td><td>CPO</td><td class="n">2025 年約 1,130 億日圓</td><td class="n">2030 年約 14.2 兆日圓</td><td>2030 年是 2024 年的約 166 倍；2029 年左右起大幅擴張</td></tr>
<tr><td>研究機構[[lightcounting-2026-202605]]</td><td>光模組、AOC、NPO、CPO 裡用的光晶片</td><td class="n">2025 年 40 億美元</td><td class="n">2031 年 150 億美元</td><td>假設 2030–31 年只有 10–15% 的 scale-up 連線改用 NPO／CPO；光模組、AOC、NPO、CPO 本身合計 2031 年近 800 億美元</td></tr>
<tr><td>中國諮詢公司，受一家雷射晶片公司委託[[technews-cic-20260820,tomshardware-cic-20260817]]</td><td>資料中心光互連全體</td><td class="n">2024 年 137 億美元</td><td class="n">2030 年 1,444 億美元</td><td>矽光子佔 63.7%</td></tr>
</table>

<div class="trio">
<figure><svg viewBox="0 0 300 230" width="100%" role="img" aria-label="CPO+NPO 2025 到 2030">
<text class="head" x="10" y="22">CPO＋NPO</text><text class="note" x="10" y="42">研究機構，億美元</text>
<line class="grid" x1="20" y1="200" x2="290" y2="200"/>
<rect class="bar2" x="60" y="199.5" width="70" height="0.5"/><text class="item" x="95" y="192" text-anchor="middle">約 1</text>
<rect class="bar" x="170" y="60" width="70" height="140"/><text class="item" x="205" y="54" text-anchor="middle">390 以上</text>
<text class="note" x="95" y="220" text-anchor="middle">2025</text><text class="note" x="205" y="220" text-anchor="middle">2030</text>
</svg><figcaption>[[cna-trendforce-20260615]]</figcaption></figure>
<figure><svg viewBox="0 0 300 230" width="100%" role="img" aria-label="網路市場 2026 到 2028">
<text class="head" x="10" y="22">scale-up＋scale-out 網路</text><text class="note" x="10" y="42">券商，億美元</text>
<line class="grid" x1="20" y1="200" x2="290" y2="200"/>
<rect class="bar2" x="60" y="186.4" width="70" height="13.6"/><text class="item" x="95" y="180" text-anchor="middle">約 150</text>
<rect class="bar" x="170" y="60" width="70" height="140"/><text class="item" x="205" y="54" text-anchor="middle">1,540</text>
<text class="note" x="95" y="220" text-anchor="middle">2026</text><text class="note" x="205" y="220" text-anchor="middle">2028</text>
</svg><figcaption>[[etenterprise-gs-20260520]]</figcaption></figure>
<figure><svg viewBox="0 0 300 230" width="100%" role="img" aria-label="CPO 日圓 2025 到 2030">
<text class="head" x="10" y="22">CPO</text><text class="note" x="10" y="42">日本研究機構，億日圓</text>
<line class="grid" x1="20" y1="200" x2="290" y2="200"/>
<rect class="bar2" x="60" y="198.9" width="70" height="1.1"/><text class="item" x="95" y="192" text-anchor="middle">約 1,130</text>
<rect class="bar" x="170" y="60" width="70" height="140"/><text class="item" x="205" y="54" text-anchor="middle">約 141,850</text>
<text class="note" x="95" y="220" text-anchor="middle">2025</text><text class="note" x="205" y="220" text-anchor="middle">2030</text>
</svg><figcaption>[[moneydj-fuji-20260121]]</figcaption></figure>
<figure><svg viewBox="0 0 300 230" width="100%" role="img" aria-label="光晶片 2025 到 2031">
<text class="head" x="10" y="22">光模組等用的光晶片</text><text class="note" x="10" y="42">研究機構，億美元</text>
<line class="grid" x1="20" y1="200" x2="290" y2="200"/>
<rect class="bar2" x="60" y="162.7" width="70" height="37.3"/><text class="item" x="95" y="156" text-anchor="middle">40</text>
<rect class="bar" x="170" y="60" width="70" height="140"/><text class="item" x="205" y="54" text-anchor="middle">150</text>
<text class="note" x="95" y="220" text-anchor="middle">2025</text><text class="note" x="205" y="220" text-anchor="middle">2031</text>
</svg><figcaption>[[lightcounting-2026-202605]]</figcaption></figure>
<figure><svg viewBox="0 0 300 230" width="100%" role="img" aria-label="光互連 2024 到 2030">
<text class="head" x="10" y="22">資料中心光互連全體</text><text class="note" x="10" y="42">受委託的估計，億美元</text>
<line class="grid" x1="20" y1="200" x2="290" y2="200"/>
<rect class="bar2" x="60" y="186.7" width="70" height="13.3"/><text class="item" x="95" y="180" text-anchor="middle">137</text>
<rect class="bar" x="170" y="60" width="70" height="140"/><text class="item" x="205" y="54" text-anchor="middle">1,444</text>
<text class="note" x="95" y="220" text-anchor="middle">2024</text><text class="note" x="205" y="220" text-anchor="middle">2030</text>
</svg><figcaption>[[technews-cic-20260820]]</figcaption></figure>
</div>
<p class="tag">五張圖各自的範圍、單位、年份都不同，每張的高度只表示自己的起點和終點，不能互相比較。</p>

公司自己也在估。Coherent 在 2026 年 9 月把它 2030 年可服務的市場從 600 億美元上調到 900 億美元，並說如果整套光學方案都由它供應，一顆 100 Tbps、每通道 200G 的交換器或運算晶片，它能賣進的內容最多約 1.5 萬美元；這是廠商自己的估計，還沒有採購數字驗證[[futurum-coherent-photonlink-20260923]]。Marvell 的投資人日簡報說 scale-up 光學的營收機會「遠大於 scale-up 交換」，scale-out 交換器 FY28 成長到超過 10 億美元[[marvell-investor-day-deck-20261006]]。

廠商自己也給了幾個數字。Lumentum（2026-05 法說會轉錄稿）說，已描述的數十億美元訂單多半來自 scale-out，scale-up 的營收機會預期明顯更大，大約超過 50 億美元的增量營收（「如果執行得好」）[[fool-lumentum-q3fy26-20260506]]。Credo 轉述預測機構：插拔式光模組的出貨量從 2026 年約 6,000 萬顆成長到 2030 年約 1.75 億顆，「再加上 scale-up 的成長」；CPO 取代的是這一塊的一部分，插拔式本身還在成長[[fool-credo-fy27q1-20260901]]。Credo 在 2026-03 還說，許多預測師給 CPO 在交換器市場未來三年低個位數的佔比（Credo 轉述，不是它自己的預測）[[fool-credo-q3fy26-20260302]]。

scale-up 這一塊，另有幾個數字：一家研究機構在 GTC 2026 之後把「NVLink 8 CPO」加進 scale-up 交換器預測，因為把 CPO 的價值算進交換器售價，2029 年以後的預測「大幅提高」，scale-up 交換晶片年複合成長 53%[[lightcounting-scaleup-20260427]]；研究機構說 scale-up 互連的市場規模「已經遠大於」scale-out 網路，CPO 市場會以 scale-up 為主[[semianalysis-cpo-book]]。OCS 的市場估計見 [Google 的 OCS](#tm-ocs)。FAU 這一個零件的市場，見[對營收的貢獻](fau-makers.md#fau-revenue)。

**取代的對象是插拔式光模組和裡面的 DSP。**DSP（數位訊號處理晶片）負責把跑了一段長銅線、變形的訊號整理回來。光引擎搬到晶片旁，電線短到不需要整理，模組和 DSP 就可以拿掉；CPO 的價值會算進交換器的售價裡[[lightcounting-scaleup-20260427]]。DSP 佔光模組多少耗電和成本、長期合約價，見[DSP 缺貨推向哪裡](alternatives.md#alt-dsp)。用整台機器比最直接：同一顆 Spectrum-6 交換器晶片，插拔式版本整台典型耗電 3.3 kW 或 2.79 kW，CPO 版本 1.96 kW，見[同一顆晶片整台耗電比較](alternatives.md#alt-power)和[CPO 怎麼解決這個問題](basics.md#q3)。

但各家都不認為會一刀切。研究機構說 CPO、NPO、插拔式會依耗電、距離、成本、成熟度在不同場景並行發展[[udn-trendforce-20260615]]，Meta、Microsoft 先做 NPO[[ctee-trendforce-20260616]]；券商把 CPO 和插拔式光模組並列算在市場裡[[etenterprise-gs-20260520]]；華星光預計 2027 到 2029 年 NPO 是主流[[luxnet-slides-20260828]]。OCP 的議程上，同一段距離有 CPO、NPO、XPO、共同封裝銅線、銅線五種方案在講：Arista 說 XPO 加開放式 CPO／NPO 讓每櫃頻寬從 OSFP 的 1.6 Pb/s 提高到 6.5 Pb/s[[arista-ocp-pr-20261007]]；Broadcom 說銅線可到 4 公尺；TE 說 448G 的 CPC 是通往 CPO 的過渡[[ocp2026-agenda-20261012]]。插拔式這一邊也在往中間靠，例如只在發射端放 DSP 的 TRO 模組，見[拿掉 DSP：LPO、TRO](alternatives.md#alt-lpo)。

## 還有哪些沒問到、但值得注意的？ {#q31b}

這些在別的筆記裡有主場，這裡只列出會影響「什麼時候、多大」的幾件：

- **誰訂規格。**台積電說 COUPE 以「標準化插座」為目標[[tianxia-coupe-20260818]]，但在台積電自己的新聞稿和法說裡，沒有找到「standardized socket」這個說法；找到的插座都是 Open CPX MSA 和 Oracle 主張的 socketed CPO[[stt-ofc2026-cpo-panel-2026]]。誰的規格變成標準，供應商名單就跟著誰。見[各種規格](alternatives.md#alt-specs)和[「NVIDIA 暫離 COUPE」傳聞](players.md#pl-coupe)。
- **保偏光纖可能被拿掉。**NVIDIA 在 ECTC 2025 提出用一般單模光纖加晶片上的偏振追蹤電路，封裝成本約降 2.7 倍；如果成真，雷射那一側的 FAU 規格會變。見[保偏光纖會不會被拿掉](detachable.md#det-pm)。
- **一根光纖跑幾路。**WDM 讓一根光纖跑多個波長，波長越多，需要的光纖和 FAU 通道就越少（[PIC 怎麼電光互換](inside.md#q7)）。台積電說的路線是 WDM 波長從 1 個增加到 4、8、16 個[[technews-tsmc-coupe-20260831]]；NVIDIA 的測試晶片已是 8 波長。
- **前面板接頭在換代：MPO → MMC。**Quantum-X800 前面板用 MPO，Spectrum-X 已改用更小的 MMC-16；Meta 的 102.4T 交換器摘要寫 16 個「四埠 MMC」介面，和 NVIDIA 同是 102.4T 但接頭數量級不同，所以用 NVIDIA 一台推算 MMC 或 FAU 用量，不一定適用 Meta 這種設計[[ocp2026-agenda-20261012]]。見[MPO、MMC 和授權](passive.md#pas-mmc)。
- **CPO 交換器一定要液冷。**NVIDIA 三台 CPO 交換器都是液冷；Meta 的 102.4T 也是 100% 液冷、無風扇。見[散熱](inside.md#q10b)。
- **插拔式和 CPO 之間的折衷。**TRO、LPO、XPO、NPO 並行多久，會影響 CPO 用的零件需求。見[插拔式的折衷](alternatives.md#alt-xpo)和[雲端大廠要買什麼](alternatives.md#alt-buyers)。
- **DSP 缺貨。**壓著插拔式，也是 CPO 拿掉 DSP 的賣點；但插拔式的 TRO、LPO 也在減 DSP。見[DSP 缺貨推向哪裡](alternatives.md#alt-dsp)。
- **中國供應鏈。**依公司自己的說法，中國 FAU 和零件廠進度比台廠前面，會影響價格和台廠的空間。見[中國的 FAU 和零件廠](china.md#cn-fau)。
- **可靠度數據。**客戶遲疑的原因之一是缺乏可靠度數據；大規模部署之後的故障率，是 CPO 能不能從交換器走到 GPU 旁邊的關鍵。見[可靠度數據](equipment-test.md#eq-reliability)。
- **台積電的人事。**COUPE 的開發者、先進封裝整合處長侯上勇 2026 年 6 月 30 日退休，報導說他是 COUPE 的命名者，傳將加入聯發科（聯發科「無法評論」）[[udn-tsmc-hou-20260711]]。只是人事事實，影響沒有資料。

## 還不知道的 {#tm-open}

日期都從 [calendar.md](calendar.md#cal-events) 的日曆抄來；「未公告」是查詢日（2026-10-12）官方還沒寫日期。

**NVL576、Rubin Ultra**

- **NVL576 櫃與櫃之間到底是插拔式、NPO、CPO 還是 OCS：**NVIDIA 書面只寫「銅線和直接光學連接」。OCP 10/12 17:45 Ian Buck 主題演講；GTC Washington, D.C.（11/30–12/3，主題演講 12/1）；GTC 2027（2027/3/14–18）。OEM 的規格書（鴻海、廣達、緯穎）查不到。
- **Ian Buck 說「spine 用插拔式」的原始場合：**只有一篇報導沒標出處；從其他 GTC 2026 記者會查起。
- **NVL576 的光學埠比例、光鏈路數、每櫃光引擎數：**Corning 說保密；Corning 第三季法說 10/27；專家調研的「每托盤 16 個 3.2T 光引擎」要等 OCP 展示和 GTC 路線圖對照；高盛「324／162／5,184」原句找不到。
- **Polyphe 每托盤幾條線、接頭型式：**NVIDIA 原圖最大 1296 × 629；要 NVIDIA 媒體資料庫的原圖或現場照。
- **NVIDIA VLSI 2026 短課程的完整投影片：**日本媒體只轉貼約 8 頁；Hot Chips 2026 NVIDIA 完整投影片要會員帳號。
- **Rubin Ultra 是不是改成兩顆晶粒、Kyber 是不是延到 2028：**NVIDIA 只說路線圖不變；NVIDIA 第三季財報（11 月中下旬，未公告）、台積電第三季法說（10/15 14:00）；專家說 Rubin Ultra 交換晶片「10 月才 tape-out 回來」，同樣等這兩場。
- **Cignal 說的「NVIDIA 會把 OCS 放進 NVL576」根據是什麼：**Lumentum FY27 第一季法說（11/05）的 OCS 客戶說法。

**scale-up 的其他玩家**

- **Coherent 2026 年 2 月那張「極大」CPO 採購單的客戶：**沒點名；Coherent 11 月初法說、2027 年 2 月初下一場。scale-up CPO「2027 下半年」的說法已連續四季不變，看有沒有改口。
- **Astera Labs 的 NPO（2027）、CPO（2028）時程有沒有再改：**2025-11 到 2026-08 已改過兩次；Astera Labs 第三季財報（去年 2025-11-04，今年未公告）、OCP 10/14 10:45 場次；Amazon 認股權解鎖後買的光引擎是什麼產品。
- **Arista 的 ESUN 規格何時出、2027 年的 CPO 實例和試用是誰：**Arista 下一場法說（日期未公告）、OCP 10/13 13:00 Bechtolsheim。
- **OCI MSA 第一代規格本身：**一個 scale-up 埠用幾根光纖、接頭、要不要 FAU、雷射放哪；第二代 400G 預計 2027 年公開；從 oci-msa.org 和 OIF 的提案查起，OCP 10/12–15（Broadcom Pancholy 10/14 15:15 〈CPO, OCI〉）。
- **Marvell「明年數億美元」的 scale-up 光學客戶，和下一次的數字：**3 月到 10 月數字改了四次（5 億美元年化、1.5 億、含 NPO 約 3 億、「比一季前想的大很多」），8 月之後沒有新的金額，也沒說 NPO 和 CPO 各佔多少。Marvell FY27 第三季財報（12 月初，未公告）、AWS re:Invent（11/30–12/4）。
- **Credo scale-up NPO 的客戶（9 月說「確定的設計導入」，沒點名）、Dust Photonics 的 PIC 誰代工、LED 光纜的光學次組件誰做、和 Senko 的盲插背板誰組裝：**Credo FY27 第二季財報（12 月初，未公告）、OCP 展示；貿聯第三季法說（11 月，未公告）。
- **AMD MI500 的光學是 CPO 還是 NPO、誰做：**只有媒體引未具名來源；日月光法說（去年同期 10/30，今年未公告）。
- **共同封裝銅線的出貨量：**Broadcom FY26 第四季財報（12 月中，未公告）、Amphenol、貿聯法說。
- **Broadcom 說的「新的寬型 CPO」是什麼：**只出現在 OCP 執行長的引言；10/12 Khamisy 主題演講、10/14 Pancholy 兩場。

**OCS**

- **Google TPU8 每顆 TPU 的 OCS 埠變多還是變少：**兩種說法相反；Google Hot Chips 2026 投影片要會員帳號。「SPOCS」是什麼：只有一位 KOL 用。
- **OCS 台數兩份估計差很多（1.5 萬 vs 1.8 萬）：**光學市場研究機構原始報告對齊；2030 年 80 億美元的假設。
- **Calient 現在的股東、Silex 的 OCS 客戶：**Calient 官網查不到；Silex 公開說明書。
- **台廠有沒有供應 OCS 準直器或 MEMS：**查不到公司說法；波若威、光聖、前鼎的下一場法說。
- **Lumentum 的托盤內 OCS（2028）：**11/05 法說；OFC 2027（2027/3/7–11）。

**慢而寬**

- **NVIDIA ECOC 2026 演講的原投影片：**ECOC 論文 IEEE Xplore 還沒收錄；Kuchta 的 IEEE 傑出講座投影片沒公開。
- **IEEE 802.3ds 11 月 D2.0 會不會定下芯徑：**802.3ds 11 月 plenary 文件；誰拉 1060 nm 小芯徑多模光纖、台灣有沒有拉絲廠；「80 µm 外徑」出處。
- **VCSEL 在 scale-up 的台灣曝險：**穩懋第三季法說（10/23 14:00）；穩懋、宏捷科、全新都沒說用在 scale-up。
- **Micro LED 的對位公差數字、雲端客戶：**查不到；Intel 和友達的傳聞雙方沒證實。友達 2026 年 2 月法說提到的 FAU 指什麼結構、友達說的「國際知名互連廠商」是誰：友達第三季法說（去年 2025-10-30，今年未公告）。
- **貿聯在慢而寬裡的角色：**貿聯第三季法說（去年同期 11/07，今年未公告）；ams OSRAM 後續新聞稿。

**時程、量和可靠度**

- **穎崴把基板上的光引擎叫 NPO、中介層上才叫 CPO，與台積電用法不同：**台積電第三季法說（10/15 14:00）會不會澄清口徑。
- **台積電的「量產」到底多大、中介層版年份：**台積電第三季法說（10/15 14:00）會不會被問；竹南還是嘉義、2028 年雙排 FAU 的原始投影片、陳明發 SEMICON 2026 投影片（lane 數寫 64 → 128 還是 16 → 128）都查不到。
- **2027 年 CPO 交換器台數差五倍（5.9 萬到 30 萬）：**鴻海和工業富聯 5 萬台、製造市佔 9 成的說法要對工業富聯半年報、法說；NVIDIA 第三季財報（11 月中下旬，未公告）。
- **Meta OFC 2026 的原始論文：**可靠度數字在二手整理間互相矛盾（1.47M 對 1.7M 小時、40°C 對 43°C）；Meta、Broadcom 的 OFC 2026 投影片、ECOC 2026 有沒有 Phase 2 更新；NVIDIA COUPE 交換器的任何可靠度數據都沒有。
- **NVIDIA 這週在 OCP 講什麼：**10/14 09:15 Shainer（含製造流程）；Meta 102.4T 的「四埠 MMC」是什麼外形：10/14 08:00 Meta 場次。
- **接下來還沒講完的 OCP 場次：**議程腳本 `data/ocp2026_agenda.py` 重跑，`media_uploads` 欄會出現大會上傳的投影片。
