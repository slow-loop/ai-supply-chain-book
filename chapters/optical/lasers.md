# 雷射、外部光源、InP

CPO 交換器裡的光，是從機器前面板插著的雷射模組送進來的。這份筆記講這條供應鏈：從原料銦、InP（磷化銦）基板、磊晶、雷射晶片，一直到插在交換器上的外部光源模組，誰在做、做到哪、缺不缺、值多少錢。雷射為什麼不放在晶片上、光怎麼從模組走進光引擎，主場在 [inside.md 的第 10 題](inside.md#q10)，這裡只講供應鏈。

原本的看法是「FAU 是 CPO 的瓶頸，台廠（大立光、上詮）經由台積電 COUPE 吃到這塊」。後來幾輪查到的事，有幾件會改變這個看法，先列在這裡，細節在各節：

- **台積電點名的「大規模部署瓶頸」是雷射、光纖、光纖連接器和產品測試。** 每一個報導版本都沒有出現 FAU 這個字。（[誰說缺](#las-shortage)）
- **做雷射的公司自己在 2026 年 8–9 月的法說說 CPO 雷射做不夠。** Lumentum 說出貨「遠遠落後」，AAOI 說因為做不夠沒辦法參加客戶的第一代部署，Broadcom 說雷射需求遠超過供給；Coherent 在 2026 年 2 月就說 InP 的供需失衡可能是「很長一段時間」。（[誰說缺](#las-shortage)）
- **同一家公司的說法，每一季都在改。** Lumentum 的 InP 產能目標、Coherent 的擴產倍數、AAOI 的擴產時點、環宇的 100 mW 放量時間，都是一季一季往前或往後調；華工 2026 年 3 月預期 4 月起交付率到 8–9 成，8 月自己說上半年實際交付不到預期的一半。（[說法怎麼隨時間改變](#las-timeline)、[各家目標一季一季怎麼改](#las-capex-path)）
- **「CPO 少用 4 倍雷射」只有跟 EML 模組比才成立。** 跟每支 2 顆雷射的矽光模組比，顆數一樣，但 CPO 每顆雷射的功率約是 3 倍，晶片約大 6 倍、良率較低。（[用幾顆、值多少](#las-count)）
- **一份未具名的調研紀要裡，一台 CPO 交換器的雷射加外部光源模組比 FAU 值錢；Coherent 也說外部光源模組和 FAU 是 CPO 裡金額最大的兩塊。**（[用幾顆、值多少](#las-count)）
- **一位產業分析師說，CPO 雷射通過 NVIDIA 認證的只有 Lumentum，Coherent 是下一個，兩三年內不會有第三家。** 兩家都不是台廠。（[各國廠商](#q21)）
- **Lumentum 的外部光源模組第一張訂單是 2026 年 8 月才拿到的，2027 下半年交貨。** 舊版把 Lumentum 寫成「負責外部光源組裝」，要照它自己的說法改。（[各國廠商](#q21)）
- **日本雷射廠對 CPO 的時間點比較保守。** 三菱電機說市場 2028–29 年度起來、2030 年代才放大；住友電工說客戶在 CPO 和插拔式之間並行評估。（[各國廠商](#q21)）
- **上游有一個 FAU 沒有的單一國家管制。** 中國管制 InP 和兩種有機銦的出口，金屬銦不在清單上，但 2026 年 6 月起只有媒體報導說海關開始查銦錠的最終用途。（[InP 基板和銦](#las-inp)）
- **最常被引用的 InP 基板市佔（住友 42%、AXT 36%、JX 13%）是 2020 年的數字。**（[InP 基板和銦](#las-inp)）
- **公開資訊觀測站看得到的光通訊擴產，金額最大的在雷射這一層，不在 FAU。**（[公告看得到的擴產](#las-capex)）
- **台灣磊晶廠的原料看不到中國卡點，曝險在基板和客戶地區。**（[台廠在哪一層](#las-tw)）

## 從銦到外部光源模組，分幾層？ {#las-layers}

雷射這條線可以分五層。最上游是**銦**，是煉鋅時順帶回收的副產品，產量跟著鋅走，不跟著雷射的需求走[[usgs-indium-202601]]。銦和磷做成 **InP（磷化銦）基板**，一片圓形的晶圓；在基板上一層層長出會發光的晶體，叫**磊晶**，長法常見的有兩種：MOCVD（有機金屬化學氣相沉積，原料用三甲基銦這類含銦的有機化合物，業界叫 MO 源）和 MBE（分子束磊晶，原料直接用銦等元素）；把磊晶片做成一顆顆**雷射晶片**，CPO 用的是一直亮著的連續光雷射，叫 CW 雷射，訊號由光引擎裡的調變器加上去；最後把雷射晶片封裝成可插拔的**外部光源模組**（ELS，External Laser Source；做成插拔規格的叫 ELSFP），插在交換器面板上，光再經保偏光纖送進光引擎。

為什麼一定要 InP：矽本身幾乎不會發光，InP 會，所以矽光子晶片的光源要靠 InP 雷射[[etnews-oe-cto-20260825]]。

<div class="scroll">
<svg viewBox="0 0 1000 804" width="100%" style="min-width:760px" role="img" aria-label="雷射這條線的五層和各家做到哪一層">
<defs><marker id="las-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0,0 L10,5 L0,10 z" class="bar"/></marker></defs>
<rect class="box" x="180" y="10" width="156" height="96" rx="4"/>
<text class="head" x="188" y="36">1. 銦、有機銦</text>
<text class="note" x="188" y="62">鋅冶煉的副產品；</text>
<text class="note" x="188" y="82">磊晶用三甲基銦</text>
<path class="solid" d="M336,58 L344,58" marker-end="url(#las-a)"/>
<line class="grid" x1="340" y1="122" x2="340" y2="798"/>
<rect class="box" x="344" y="10" width="156" height="96" rx="4"/>
<text class="head" x="352" y="36">2. InP 基板</text>
<text class="note" x="352" y="62">磷化銦晶圓，</text>
<text class="note" x="352" y="82">雷射長在它上面</text>
<path class="solid" d="M500,58 L508,58" marker-end="url(#las-a)"/>
<line class="grid" x1="504" y1="122" x2="504" y2="798"/>
<rect class="box" x="508" y="10" width="156" height="96" rx="4"/>
<text class="head" x="516" y="36">3. 磊晶</text>
<text class="note" x="516" y="62">在基板上長出</text>
<text class="note" x="516" y="82">會發光的晶體層</text>
<path class="solid" d="M664,58 L672,58" marker-end="url(#las-a)"/>
<line class="grid" x1="668" y1="122" x2="668" y2="798"/>
<rect class="box" x="672" y="10" width="156" height="96" rx="4"/>
<text class="head" x="680" y="36">4. 雷射晶片</text>
<text class="note" x="680" y="62">切成一顆顆</text>
<text class="note" x="680" y="82">連續發光的 CW 雷射</text>
<path class="solid" d="M828,58 L836,58" marker-end="url(#las-a)"/>
<line class="grid" x1="832" y1="122" x2="832" y2="798"/>
<rect class="box" x="836" y="10" width="156" height="96" rx="4"/>
<text class="head" x="844" y="36">5. 外部光源模組</text>
<text class="note" x="844" y="62">封裝成插拔模組，</text>
<text class="note" x="844" y="82">插在交換器面板上</text>
<text class="item" x="172" y="157" text-anchor="end">中國冶煉廠</text>
<rect class="bar2" x="186" y="146" width="148" height="14" rx="2"/>
<text class="item" x="172" y="181" text-anchor="end">南大光電（中）</text>
<rect class="bar2" x="186" y="170" width="148" height="14" rx="2"/>
<text class="item" x="172" y="205" text-anchor="end">Nouryon</text>
<rect class="bar2" x="186" y="194" width="148" height="14" rx="2"/>
<text class="item" x="172" y="229" text-anchor="end">住友電工 ★</text>
<rect class="bar2" x="350" y="218" width="148" height="14" rx="2"/>
<rect class="bar2" x="678" y="218" width="312" height="14" rx="2"/>
<text class="item" x="172" y="253" text-anchor="end">JX 金屬</text>
<rect class="bar2" x="350" y="242" width="148" height="14" rx="2"/>
<text class="item" x="172" y="277" text-anchor="end">AXT／通美</text>
<rect class="bar2" x="350" y="266" width="148" height="14" rx="2"/>
<text class="item" x="172" y="301" text-anchor="end">雲南鍺業（中）</text>
<rect class="bar2" x="350" y="290" width="148" height="14" rx="2"/>
<text class="item" x="172" y="325" text-anchor="end">IQE（英）</text>
<rect class="bar2" x="514" y="314" width="148" height="14" rx="2"/>
<text class="item" x="172" y="349" text-anchor="end">英特磊</text>
<rect class="bar2" x="514" y="338" width="148" height="14" rx="2"/>
<text class="item" x="172" y="373" text-anchor="end">全新</text>
<rect class="bar2" x="514" y="362" width="148" height="14" rx="2"/>
<text class="item" x="172" y="397" text-anchor="end">聯亞</text>
<rect class="bar2" x="514" y="386" width="312" height="14" rx="2"/>
<text class="item" x="172" y="421" text-anchor="end">Coherent ★</text>
<rect class="bar2" x="514" y="410" width="476" height="14" rx="2"/>
<text class="item" x="172" y="445" text-anchor="end">AAOI</text>
<rect class="bar2" x="514" y="434" width="476" height="14" rx="2"/>
<text class="item" x="172" y="469" text-anchor="end">光迅（中）</text>
<rect class="bar2" x="514" y="458" width="476" height="14" rx="2"/>
<text class="item" x="172" y="493" text-anchor="end">Lumentum ★</text>
<rect class="bar2" x="678" y="482" width="312" height="14" rx="2"/>
<text class="item" x="172" y="517" text-anchor="end">Broadcom</text>
<rect class="bar2" x="678" y="506" width="148" height="14" rx="2"/>
<text class="item" x="172" y="541" text-anchor="end">三菱電機</text>
<rect class="bar2" x="678" y="530" width="148" height="14" rx="2"/>
<text class="item" x="172" y="565" text-anchor="end">古河電工</text>
<rect class="bar2" x="678" y="554" width="312" height="14" rx="2"/>
<text class="item" x="172" y="589" text-anchor="end">源杰（中）</text>
<rect class="bar2" x="678" y="578" width="148" height="14" rx="2"/>
<text class="item" x="172" y="613" text-anchor="end">Sivers（瑞典）</text>
<rect class="bar2" x="678" y="602" width="148" height="14" rx="2"/>
<text class="item" x="172" y="637" text-anchor="end">華星光</text>
<rect class="bar2" x="678" y="626" width="312" height="14" rx="2"/>
<text class="item" x="172" y="661" text-anchor="end">光環</text>
<rect class="bar2" x="678" y="650" width="148" height="14" rx="2"/>
<text class="item" x="172" y="685" text-anchor="end">OE Solutions（韓）</text>
<rect class="bar2" x="678" y="674" width="312" height="14" rx="2"/>
<text class="item" x="172" y="709" text-anchor="end">天孚（中）★</text>
<rect class="bar2" x="842" y="698" width="148" height="14" rx="2"/>
<text class="item" x="172" y="733" text-anchor="end">聯鈞</text>
<rect class="bar2" x="842" y="722" width="148" height="14" rx="2"/>
<text class="item" x="172" y="757" text-anchor="end">立碁</text>
<rect class="bar2" x="842" y="746" width="148" height="14" rx="2"/>
<text class="item" x="172" y="781" text-anchor="end">光創聯（中）</text>
<rect class="bar2" x="842" y="770" width="148" height="14" rx="2"/>
</svg>
</div>

<p class="tag">示意圖，非實際比例。橫條是各家自己說、或公開資料寫它做到的層；中間斷開代表那一層沒有資料。★ 是 NVIDIA 公布的合作夥伴：Lumentum、住友電工、Coherent 在 2025 年 3 月的名單上，「TFC」在 2026 年 6 月的名單上（見 <a href="players.md#q20">players.md 第 20 題</a>）。中國冶煉廠不是一家公司，代表中國佔全球原生銦約七成。</p>

![做雷射用的磷化銦（InP）晶圓，6 吋。6 吋晶圓的面積是 3 吋的 4 倍，同一片能切出更多雷射。廠商產品照。[[coherent-inp-blog-20241209]]](img/vendor/coherent-6inch-inp-wafers-20241209-01.jpg) ![一片小尺寸的 InP 光晶片晶圓，上面每一塊是一種晶片設計。這片是研究用、多家共用的晶圓。[[commons-inp-wafer]]](img/explain/commons-inp-multi-project-wafer.jpg)

最後一層的外部光源模組長得像一支光模組。拆開來，裡面是電路板上的雷射組件，一端是光纖接口，一端是拉環[[lightwave-eugenlight-elsfp-20260910]]。模組裡除了雷射，還有兩樣東西：**隔離器**，只讓光往外走，擋住反射回來的光，免得干擾雷射；**TEC**（熱電致冷器），一塊通電就能把熱搬走的小板子，讓雷射保持在固定溫度[[semieng-lasers-heartbeat-202605]]。雷射和 TEC 約佔模組耗電的七成，這是研究機構的估計[[semianalysis-cpo-book]]；從插座拿到的電，只有 10–15% 變成送出去的光[[semieng-lasers-heartbeat-202605]]。早期不帶 TEC 的 ELSFP 實際上難用，正轉向帶 TEC 的版本，這是一家韓國雷射廠技術長的說法[[etnews-oe-cto-20260825]]。

![一支外部光源模組拆開來：上蓋、外殼，綠色電路板上兩塊銅色的是雷射組件，左邊是光纖接口，右邊是拉環。原圖很小。[[lightwave-eugenlight-elsfp-20260910]]](img/media/Lightwave-光創聯ELSFP結構-20260910-01.jpg) ![Coherent 投影片：交換器面板上插著外部光源模組（中間那支），模組裡拆成三樣東西：InP CW 雷射、隔離器、熱電致冷器（TEC）。右邊文字是公司說法：德州 Sherman 廠 6 吋 InP 全量生產，拿到一家領先 AI 資料中心客戶的多年期 CPO 訂單。廠商投影片。[[semieng-lasers-heartbeat-202605]]](img/media/semieng-coherent-els-202605.png)

Coherent 說它的外部光源模組全部零件都自己做，包括雷射、隔離器、TEC 和保偏光纖[[semieng-lasers-heartbeat-202605]]。

### 這幾層會不會變？

有三個方向可能改變「雷射放在外面、一顆顆插在面板上」的做法，目前都還沒有時程：

- **台積電想把光源搬進 COUPE。** 一家媒體寫，台積電一位副處長在 2026 年 8 月 31 日的論壇上說，未來可望把調變器、SOA（半導體光放大器）和光源整合到 COUPE 平台背面[[technews-tsmc-coupe-20260831]]。同一場演講的另一個報導版本只寫「COUPE 未來可能成為連接運算晶片與光學元件的整合平台」，沒有寫光源和背面[[cna-tsmc-coupe-20260831]]。所有報導都沒有時程[[technews-tsmc-coupe-20260831,cna-tsmc-coupe-20260831,techorange-semicon-20260831]]。如果成真，外部光源模組和雷射到光引擎那一段保偏光纖的需求都會跟著改。
- **雷射和調變器可能拆開。** 三菱電機說，現在的 EML 晶片是 CW 雷射加上 InP 調變器做在一起，下一代 CPO 這兩樣可能分開用；市場上有人用 CW 雷射配 TFLN（薄膜鈮酸鋰）調變器，但 TFLN 尺寸大，三菱押的是做得小的 InP 調變器[[melco-irday-qa-20260608]]。
- **一片矽上放幾百顆雷射。** 新創 Lightmatter 的 GUIDE 把數百顆 InP 雷射整合在一片矽上，公司宣稱 2 個 GUIDE 能取代 Quantum-X 的 18 個外部光源模組，目前在送樣[[semianalysis-cpo-book]]。另一家新創 Scintil 宣稱它的整合法每顆雷射要用的 InP 面積可降到傳統做法的十分之一[[supercomputing-cpo-laser-202609]]。這兩個都是公司自己的說法。

## 誰說缺？缺多少？ {#las-shortage}

### 台積電點名的瓶頸

2026 年 8 月 31 日，台積電一位副總在 SEMICON Taiwan 的矽光子論壇上說：晶圓代工可以擴大光學引擎的規模，但真正的大規模部署瓶頸在供應鏈的其他環節，包括雷射、光纖、光纖連接器和產品測試[[cna-tsmc-bottleneck-20260831,technews-tsmc-bottleneck-20260831]]。說這句話的是 COUPE 的主人。

各家報導的寫法：

| 版本 | 列了什麼 |
|---|---|
| 通訊社原稿、另一家科技媒體、一家科技新創媒體 | 雷射、光纖、光纖連接器、產品測試[[cna-tsmc-bottleneck-20260831,technews-tsmc-bottleneck-20260831,techorange-semicon-20260831]] |
| 一家英文媒體（轉通訊社） | 雷射、光纖連接器、測試 |
| 一家財經媒體 | 這句是「整體供應鏈涵蓋」的範圍：雷射光源、光纖、光纖連接器、光偵測器、封裝、耦光與測試，不是瓶頸清單 |

沒有一個版本出現「FAU」或「光纖陣列」；台積電沒有公開這場演講的逐字稿或簡報。「光纖連接器」算不算包含 FAU，是讀者自己的解讀[[supercomputing-cpo-laser-202609]]。

研究機構對「卡在哪」說法也不一樣。舊版引過一家研究機構說「FAU 與 PIC 的精密對位是最大瓶頸」；同一家機構 2026 年 7 月列的 CPO 交換器量產三個限制是光引擎良率、矽光製造與封裝、先進封裝產能，沒有雷射[[trendforce-cpo-bottleneck-20260727]]。這幾個說法並列，不取哪一個。完整的卡點清單在 [timing.md 第 27b 題](timing.md#q27b)。

### 做雷射的公司自己怎麼說

| 誰 | 說了什麼 | 什麼時候 |
|---|---|---|
| Lumentum | 高功率雷射的出貨「遠遠落後」需求，而且比上次說的更落後；EML 到年底仍大幅落後需求；為了超高功率雷射，過去三個月又去找基板廠加量[[investing-lumentum-q4fy26-20260811]]。更早說出貨比客戶要的少 30% 以上，「我們兩家加起來都供應不了需求」[[tomshardware-lumentum-20260731]] | 2026-08-11 |
| Coherent | InP 是公司內部主要的限制，組裝測試不是瓶頸；6 月季 InP 雷射產量年增約 80%[[futurum-coherent-q4fy26-20261009,zacks-coherent-q4fy26-20260812]]。年報寫擴德州 InP 產能是為了「客戶需求增加和全產業短缺」[[sec-coherent-10k-20260814]]。2026 年 2 月的法說問答，執行長說：「I think we could be in a very sustained long period of supply-demand imbalance on indium phosphide」（InP 可能處在很長一段供需失衡裡），客戶要的量會把這些產能全部吃掉還不夠[[fool-coherent-q2fy26-20260204]]（法說會轉錄稿） | 2026-02、2026-08 |
| Broadcom | 執行長 Hock Tan：雷射需求，不管 EML 還是 CW，「is far surpassing supply out there in the industry」，公司在加倍擴產，「we have a fairly substantial share of this market」。光學部門主管 Charlie Kawwas：EML、CW、VCSEL 的磷化銦廠，美國和新加坡都在，「we're actually more than tripling them year-on-year」，今年的產能已經擴了，未來兩年還要大幅增加[[fool-broadcom-q3fy26-20260909,webull-broadcom-q3fy26-20260903]]（法說會轉錄稿） | 2026-09 |
| AAOI | 「主要 CPO 客戶很喜歡我們的雷射，但我們做不出足夠的量，所以沒辦法參與他們現在的第一代部署」，要先顧自家光模組；從今天訂設備，最少 21–24 個月才能高量生產[[investing-aaoi-q2-20260806]]。基板和庫存的部分，董事長說：「right now we have enough inventory, we have enough supply until end of next year」（夠用到 2027 年底），擔心的是 2028、2029 年需要的量[[investing-aaoi-q2-20260806]] | 2026-08-06 |
| AXT（基板） | 不論加產能多快，客戶需求都持續超過供給[[investing-axt-q2-20260730]] | 2026-07-30 |
| JX 金屬（基板） | 客戶持續要求大幅增量，需求超過原本預期[[jx-inp-20260616]] | 2026-06-16 |
| Sivers | 客戶需要大幅更多的雷射產能[[sivers-glasgow-20260903]] | 2026-09-03 |
| 天孚 | 1.6T 光引擎因個別物料缺料，產量未達預期[[eastmoney-tfc-20260422]]；2026 年 7 月的答覆說，受上半年 200G EML 芯片供應緊張影響，有源產品線只做小量生產[[cninfo-tfc-irm-20260709]]。後來改口說緩解，見[說法怎麼隨時間改變](#las-timeline) | 2026-04 起 |
| 華星光、聯亞 | 都說產能吃緊；華星光說 800G 光模組「瓶頸仍是在產能上」[[udn-luxnet-20260828,ttv-landmark-20260817]] | 2026-08 |

NVIDIA 執行長在 2026 年 3 月的 GTC 說：「我們需要更多銅的產能、更多光學的產能、更多 CPO 的產能。」這句話只有媒體報導[[theregister-nvidia-scaleup-20260405]]。

![Lumentum 投影片：橘色柱是 Lumentum 估的 InP 雷射通道需求（2026–2030 年每年約成長 85%），藍線是它自己的產能預測，兩條線的差距一路拉大。沒有絕對數字。廠商投影片。[[semieng-lasers-heartbeat-202605]]](img/media/semieng-lumentum-inp-capacity-202605.png) ![Lumentum 投影片引研究機構的數字：AI 資料中心的高速光通道裡，用 InP 雷射的比例從 2022 年 44%、2025 年 79%，到 2030 年預估 91%，其餘是 VCSEL（從晶片表面發光的小雷射）。廠商投影片。[[semieng-lasers-heartbeat-202605]]](img/media/semieng-lumentum-inp-lasers-202605.png)

### 研究機構怎麼說

- 一家研究機構說 NVIDIA 包下 EML 產能，EML 交期排到 2027 年以後；CW 雷射擴產受設備交期限制[[eettw-laser-shortage-20251231]]。同一家機構 2026 年 7、8 月說 InP 交期拉長、現貨價續漲，失衡會延續到 2027 年以後[[trendforce-sumitomo-inp-20260713,trendforce-inp-20260806]]。
- 另一家研究機構提醒：「InP 短缺」的說法要小心，真正缺的是**通過認證、高良率、高可靠度**的化合物半導體產能，不是原料[[yole-transceivers-20260506]]。
- 第三家研究機構的預估一直在變：2026 年 3 月說缺貨 2026 年中緩解，4 月說 2026 年底前消失[[lightwave-lightcounting-202603,tomshardware-lumentum-20260731]]；9 月它的分析師說，一般雷射晶片 2027 年中緩解，但 CPO 用的雷射可能缺到 2030 年[[supercomputing-cpo-laser-202609]]。

### 說法怎麼隨時間改變 {#las-timeline}

同一家公司在不同季度說的話，照時間放在一起看。引號裡是原話：Motley Fool、Investing.com 的是法說會轉錄稿，AllMind 的是 AI 轉寫稿（說話者標示未必正確）；中國公司的是它們在投資者關係活動記錄表或互動易上的答覆。

**Lumentum：InP 產能和 CW 雷射**

| 時間 | 說了什麼 |
|---|---|
| 2025-11-04 | InP 晶圓廠的良率和產出比預期好，「line of sight to add approximately 40% more unit capacity over the next few quarters」（未來幾季多加約 40% 的單位產能）[[allmind-lumentum-q1fy26-20251104]]。插拔式模組用的 CW 雷射：70 mW 這一季開始出貨，100 mW 當月送樣、預計 2026 年中全量產；70 mW 先賣給別的客戶，目的是之後裝進自己的模組[[allmind-lumentum-q1fy26-20251104]]（AI 轉寫稿） |
| 2026-02-03 | 「We have front-loaded our 40% expansion target, delivering on over half of that this past quarter.」（40% 的擴產目標前移，上一季就做完一半以上）；EML 產能「is spoken for in these LTAs」，長約「run through the balance of calendar 2027」（長約排到 2027 年底）；自家 CW 雷射裝進自家模組的時間，原本說 Q2 前後，現在說「pushed out to late Q2, early Q3」（轉錄稿沒標是日曆年還是會計年度）[[fool-lumentum-q2fy26-20260203]] |
| 2026-05-05 | 2027 年要出的雷射顆數「really a massive step-up」；基板長約「leave us in pretty good shape on substrates」；預估自家 CW 雷射會裝進約 20% 的模組；買下北卡第五座 InP 廠[[fool-lumentum-q3fy26-20260506]] |
| 2026-08-11 | 高功率雷射比上一季更落後；為了超高功率雷射，過去三個月又去找基板廠加量，簽了 AXT。對基板，執行長說現在「pretty comfortable」，但需求變得太快，這句話「may not be true a quarter or two from now either」[[investing-lumentum-q4fy26-20260811]] |

5 月說基板長約狀況不錯、8 月又和 AXT 簽 6 年的產能保留，是同一家公司三個月內的兩個說法。8 月的問答裡，是分析師把這個轉折問出來的，執行長的回答是超高功率雷射的需求超過原本預期。

**Coherent：InP 產能和需求**

| 時間 | 說了什麼 |
|---|---|
| 2025-11-05 | 「we expect to roughly double our total internal production capacity of indium phosphide over the next year」（一年內翻倍）；「we do not sell indium phosphide in the open market」（不對外賣）[[fool-coherent-q1fy26-20251106]] |
| 2026-02-04 | 「a very sustained long period of supply-demand imbalance」；12 月季的晶圓投片是 9 月季的 4 倍以上（「more than quadrupled the number of wafer starts」）；從投片到模組出貨「about six months」（約 6 個月，等於兩季，計算）[[fool-coherent-q2fy26-20260204]] |
| 2026-05-06 | 6 吋 InP 的產能擴充「executed ahead of plan」；明年再翻倍（見[各家目標一季一季怎麼改](#las-capex-path)）[[fool-coherent-fy26q3-20260506]] |
| 2026-08-12 | 「Indium Phosphide capacity continues to be our primary constraint」；「I do not see any time in the near future where we would be selling Indium Phosphide lasers externally. Our data center transceiver demand is absorbing every bit of capacity.」[[allmind-coherent-q4fy26-20260812]]（AI 轉寫稿） |

**說「缺料會緩解」的預測，和後來的說法**

| 時間 | 誰 | 說了什麼 |
|---|---|---|
| 2026-02-01 | 中際旭創 | EML 和 CW 等光芯片的生產週期長、相對更緊缺，「預計今年上半年供給還將緊張，要到下半年供給才將得到一定程度的緩解」[[cninfo-innolight-irm-20260201]] |
| 2026-03-26 | 華工科技 | 「公司 4 月起交付率將提升至 80%-90%以上」[[cninfo-hgtech-irm-20260326]] |
| 2026-07-09 | 天孚通信 | 上半年 200G EML 芯片緊張，有源產品線只做小量生產[[cninfo-tfc-irm-20260709]] |
| 2026-08-06 | 仕佳光子 | 「當前行業內高端光芯片供給整體仍處於相對緊缺的狀態」，行業需求和技術都在快速變，不敢對 2027 年全行業供需做確定的判斷[[sse-sourcephotonics-irm-20260806]] |
| 2026-08-21 答覆 | 天孚通信 | 臨時性短缺，已導入新供應商，「自 2026 年第三季度起，相關物料短缺狀況已逐步得到緩解」[[szse-irm-tfc-20260826]] |
| 2026-08-27 | 華工科技 | 上半年 800G、1.6T 光模組受核心物料到貨影響，「實際交付數量不及預期的 50%」；7–8 月齊套率（零件配齊的比率）回到 70%[[cninfo-hgtech-irm-20260827]] |
| 2026-10-09 | 天孚通信 | 「相關關鍵物料供應緊張狀況已較前期有明顯緩解」[[cninfo-tfc-irm-20261009]] |

華工 8 月那句講的缺料是 1.6T DSP 和 800G LPO 的驅動晶片，是電晶片，不是雷射（DSP 缺貨見 [DSP 缺貨推向哪裡](alternatives.md#alt-dsp)）[[cninfo-hgtech-irm-20260827]]；天孚 8 月、10 月的答覆都只說「相關物料」，沒有說是不是雷射晶片。這張表放的是不同公司對同一個問題的說法，不是同一種缺料。

### 要多久才補得上

| 環節 | 要多久 | 誰說的 |
|---|---|---|
| 新雷射產能：從訂設備到高量生產 | 21–24 個月 | AAOI（公司說）[[investing-aaoi-q2-20260806]] |
| Sivers 蘇格蘭新產能 | 2026 下半年開工、2027 第四季上線 | Sivers 新聞稿[[sivers-glasgow-20260903]] |
| Lumentum 北卡新廠 | 2028 年初第一筆營收，2028 年中到 2029 年滿載 | Lumentum（公司說）[[investing-lumentum-q4fy26-20260811]] |
| 新客戶認證 | 第一次導入雲端大廠，可能超過 18 個月 | 聯亞（公司說）[[moneydj-landmark-20260813]] |
| 基板新產線 | 建置 18–24 個月、MOCVD 設備交期 1–2 年、大尺寸良率爬坡 3–5 年 | 一家財經資訊網站，只當線索[[biggo-inp-price-20260425]] |

### 時間點：缺的是哪一年的雷射

「誰是瓶頸」要分時間看。Lumentum 說第一階段 scale-up（GPU 和 GPU 之間）的光連線是跨機櫃的，新一代 GPU、ASIC 的 SerDes（晶片對外收發訊號的電路）2027 年中到 2028 年初才夠快，所以 NPO、CPO 是「2028 年的事件」，不會回頭裝在現有晶片上；它的 scale-up CPO 雷射 2027 下半年高量出貨，客戶 2028 年部署[[investing-lumentum-q4fy26-20260811]]。AXT 也說 CPO 真正的成長在 2028–29 年[[investing-axt-q2-20260730]]。2026–27 年的雷射需求，主要來自現在的 scale-out 交換器（Quantum-X、Spectrum-X 這類）和插拔式模組。scale-up 什麼時候改用光，見 [timing.md](timing.md#tm-scaleup)。

**反方**。缺雷射可能是暫時的：研究機構年初的預估是 2026 年內緩解；Coherent 的 6 吋 InP 擴產超前原定計畫，6 吋晶圓的良率比 3 吋高[[tomshardware-lumentum-20260731,futurum-coherent-q4fy26-20261009,fool-coherent-fy26q3-20260506]]；天孚 8 月、10 月的答覆說物料短缺已緩解（沒說是哪種物料）[[szse-irm-tfc-20260826,cninfo-tfc-irm-20261009]]；而且真正缺的是「合格產能」，不是 InP 原料[[yole-transceivers-20260506]]。

**Coherent 不能只放在反方。** 同一家公司，2026 年 2 月說 InP 的供需失衡可能是「很長一段時間」，8 月仍說 InP 產能是主要的限制，並說近期看不到它會把 InP 雷射對外賣，因為資料中心模組的需求吃掉每一分產能[[fool-coherent-q2fy26-20260204,allmind-coherent-q4fy26-20260812]]。產能超前和需求仍追不上，是同一家公司同一年裡的兩句話。Lumentum 8 月說高功率雷射比上一季更落後，AAOI 說 CPO 要的產能是今天的 8–10 倍，Broadcom 說需求遠超過供給，各家說的是目前還沒追上[[investing-lumentum-q4fy26-20260811,investing-aaoi-q2-20260806,fool-broadcom-q3fy26-20260909]]。

## 一台 CPO 交換器用幾顆雷射？值多少？ {#las-count}

### 顆數

NVIDIA 公布的數字：每個外部光源模組裡有 8 顆雷射，一個模組供 Quantum-X 交換器 576 條發送通道中的 32 條；Spectrum-X 單顆交換器晶片配 16 個模組，四顆晶片的機種配 64 個[[nvidia-blog-20250826,nvidia-sn6000-manual-20260916]]。照這些數字算（計算）：

| 機種 | 外部光源模組 | 雷射 |
|---|---|---|
| Quantum-X（115.2T，576 條 200G） | 576 ÷ 32 ＝ 18 個 | 18 × 8 ＝ 144 顆 |
| Spectrum-X 單晶片（102.4T，512 條） | 16 個 | 16 × 8 ＝ 128 顆 |
| Spectrum-X SN6800-LD（四晶片，409.6T） | 64 個 | 64 × 8 ＝ 512 顆 |

<p class="tag">表的出處：[[nvidia-blog-20250826,nvidia-sn6000-manual-20260916]]。雷射顆數是計算。</p>

模組廠聯鈞也說「一個 CPO 約需要 18 個外部光源」[[udn-unitedopto-20260818,moneydj-unitedopto-20260819]]。一份未具名的調研紀要寫 3.2T CPO 交換機有 16 套外部光源模組、每套 8 顆 CW 雷射、共 128 顆，和 NVIDIA 公布的 Spectrum-X 單晶片配置一樣[[gewo168-cpo-passive-20260530]]。

### 「少用 4 倍」是跟什麼比

NVIDIA 說，把雷射集中在外部光源模組，資料中心裡的雷射總數比「舊設計」少四倍[[nvidia-blog-20250826,nvidia-pr-20250318]]，但沒說舊設計是哪一種。插拔式模組有兩種做法：EML 模組每條通道一顆雷射，一支 1.6T 模組用 8 顆；矽光模組只要 2 顆 CW 雷射，再用分光分給各通道[[naddod-1p6t-lasers-20250530]]；也有每支 2–8 顆的說法[[luxnet-slides-20260828]]。用同樣 576 條通道比（計算）：

<div class="scroll">
<svg viewBox="0 0 1000 240" width="100%" style="max-width:1000px" role="img" aria-label="同一台 115.2T 交換器用幾顆雷射">
<text class="item" x="320" y="38" text-anchor="end">CPO：Quantum-X（18 個 ELS × 8 顆）</text>
<rect class="bar" x="330" y="24" width="125.0" height="20"/>
<text class="item" x="463.0" y="39">144 顆</text>
<text class="item" x="320" y="78" text-anchor="end">插拔式 EML：一條通道一顆</text>
<rect class="bar2" x="330" y="64" width="500.0" height="20"/>
<text class="item" x="838.0" y="79">576 顆（4 倍）</text>
<text class="item" x="320" y="118" text-anchor="end">插拔式矽光：每支 2 顆 CW</text>
<rect class="bar2" x="330" y="104" width="125.0" height="20"/>
<text class="item" x="463.0" y="119">144 顆（1 倍）</text>
<text class="item" x="320" y="158" text-anchor="end">插拔式矽光：每支 4 顆 CW</text>
<rect class="bar2" x="330" y="144" width="250.0" height="20"/>
<text class="item" x="588.0" y="159">288 顆（2 倍）</text>
<text class="item" x="320" y="198" text-anchor="end">插拔式矽光：每支 8 顆 CW</text>
<rect class="bar2" x="330" y="184" width="500.0" height="20"/>
<text class="item" x="838.0" y="199">576 顆（4 倍）</text>
<text class="note" x="330" y="14">單位：顆雷射（同樣 576 條 200G 發送通道）</text>
</svg>
</div>

<p class="tag">計算。插拔式以 72 支 1.6T 模組湊滿同樣頻寬。出處：[[nvidia-blog-20250826,naddod-1p6t-lasers-20250530,luxnet-slides-20260828]]</p>

「4 倍」只有拿 EML 當基準才對得上；跟每支 2 顆的矽光模組比，顆數一樣。

矽光模組用的雷射比 EML 少一半，做模組和做矽光晶片的公司自己也這樣說：Tower（做矽光 PIC 的代工廠）2025 年 11 月的法說說，「SiPho typically requires half the number of lasers as an equivalent EML product」[[allmind-tower-q3-20251110]]；AAOI 董事長同月說，800G 模組用 EML 要 8 顆，用矽光「you only need two high-power CW lasers」，並說這是用矽光的一個好理由[[allmind-aaoi-q3-20251107]]。兩份都是 AI 轉寫稿，AAOI 那份把董事長的名字轉成 Chih-Hsiang Lin，Tower 那份把 III-V 調變器轉成「3.5」。

### 每顆比較大、比較難做

CPO 少的是顆數，不是 InP。每顆雷射要更亮，因為光從模組到光引擎、再出交換器，一路會損失：

| 用在哪 | 每顆雷射功率 | 出處 |
|---|---|---|
| 800G 插拔式模組 | 70 mW | AAOI（公司說）[[investing-aaoi-q2-20260806]] |
| 1.6T 插拔式模組 | 100 mW | 同上 |
| 插拔式用的 CW：Lumentum | 70 mW（2025 年 9 月季開始出貨）；100 mW（2025 年 11 月送樣，預計 2026 年中全量產）；都不是 CPO 用的超高功率 | Lumentum（公司說，轉寫稿）[[allmind-lumentum-q1fy26-20251104]] |
| 插拔式用的 CW：中國廠 | 仕佳光子 100 mW CW 2026 年 8 月已批量出貨，400 mW 等規格小批量（6 月時 70–100 mW 還是小批量）；長光華芯 100 mW CW DFB、70 mW CWDM4 DFB 2025 年 12 月已達量產出貨水平 | 公司說[[sse-sourcephotonics-irm-20260602,sse-sourcephotonics-irm-20260805,sse-everbright-irm-20251204]] |
| 華星光的計畫 | 2026 年主力 70、100 mW，後續開發 200、400 mW | 第三方整理，不是原話[[fugle-luxnet-20251222]] |
| 聯鈞的外部光源模組 | 至少輸出 20 dBm（計算：10^(20/10) ＝ 100 mW），對應雷射晶片約 300–400 mW；70、100 mW 對聯鈞是「中低功率」 | 第三方整理，不是原話[[fugle-unitedopto-20260818]] |
| 未來一兩年的主流 | 70–100 mW | 聯亞（公司說）[[moneydj-landmark-20260813]] |
| CPO | 300 mW 以上 | AAOI、聯亞（公司說）[[investing-aaoi-q2-20260806,moneydj-landmark-20260813]] |
| CPO 外部光源，每顆要 24.5 dBm 才補得回損耗 | 約 282 mW（計算：10^(24.5/10)） | 研究機構[[semianalysis-cpo-book]] |
| 外部光源的插拔規格上限 | 每個波長最高 26 dBm（約 400 mW）；為了眼睛安全，每根光纖上限 24.5 dBm | 規格組織 OIF 的 ELSFP 規格[[supercomputing-cpo-laser-202609]] |
| 住友電工的 CPO 雷射論文 | 外部光源要「數百 mW」、電轉光效率 20% 以上；45°C 下輸出超過 400 mW、效率 25% | 住友技術論文[[sei-tr205-cpo-laser-202407]] |
| Lumentum 的產品 | 120、150、400 mW 一系列；另有 1 W 以上的 | Lumentum（公司說）[[investing-lumentum-q4fy26-20260811,lumentum-pr-ofc2026-20260317]] |

AAOI 說，300 mW 的 CPO 雷射晶片大約是插拔式用的 6 倍大、良率較低；要滿足 CPO 市場，產能要比現在大 8–10 倍[[investing-aaoi-q2-20260806]]。更早的 2026 年 5 月法說，董事長講的數字不一樣：「the CPO laser is about 300 to 400 milliwatts, compared to 70 milliwatts for 800G transceivers and 100 milliwatts for 1.6T transceivers. The die size is much bigger—minimum maybe five or six times bigger.」（功率 300–400 mW，晶片面積至少大 5 到 6 倍）[[fool-aaoi-q1-20260507]]。5 月和 8 月的功率（300–400 對 300 mW）、倍數（至少 5–6 倍對約 6 倍）略有出入，兩個日期並列。

用 Quantum-X 算（計算，只算雷射輸出的光，不含效率和損耗）：CPO 144 顆 × 282 mW ≈ 40.6 W；同頻寬的矽光插拔式 144 顆 × 100 mW ＝ 14.4 W。顆數一樣，光的總量約是 2.8 倍。

光為什麼要這麼多：下圖是一個作者舉的例子，一條 CPO 鏈路從外部光源模組出發，經過接頭、發送端光引擎、再幾個接頭，到接收端光引擎時只剩約 1.2% 的光（總損耗 18.2 dB）[[semieng-cpo-link-budget-202606]]。外部光源模組本身內部也損失 1.5–3 dB[[semieng-cpo-link-budget-202606]]。

![一條 CPO 鏈路每一站還剩多少光：雷射出發 100%，過第一個接頭剩 71%，過發送端光引擎剩 11%，再經接頭、托盤之間、可拆接頭，到接收端光引擎只剩 1.2%。這是作者的示例，不是實測。[[semieng-cpo-link-budget-202606]]](img/media/semieng-cpo-link-budget-202606.jpg){.s}

### 可靠度要求更嚴

可靠度常用 FIT 表示：十億個元件小時裡壞幾次，數字越小越可靠。OIF 對 CPO 光源的目標，是餵一顆 3.2T 光引擎的整個光源只能 50 FIT；插拔式模組常見約 300 FIT，嚴了 5 倍以上[[lumentum-elsfp-wp-202606,supercomputing-cpo-laser-202609]]。Lumentum 說它的超高功率雷射在 400 mW 下是 20 FIT，依據是超過 1 億個加速測試元件小時零失效；但這種雷射還沒有實際裝在機房裡跑出來的資料[[lumentum-elsfp-wp-202606,supercomputing-cpo-laser-202609]]。這也是那位分析師說「兩三年內不會有第三家通過認證」的理由：這種雷射的可靠度很難證明[[supercomputing-cpo-laser-202609]]。

### 值多少錢

沒有任何公司或研究機構公開同一個口徑的「雷射 vs FAU」單價。手上有的：

| 說法 | 數字 | 可信度 |
|---|---|---|
| 一份未具名調研紀要（3.2T CPO 交換機，一位受訪者） | FAU 36 個 × 700 元人民幣 ＝ 2.5 萬元；外部光源模組 16 套「合計超過 4 萬元」；CW 雷射 128 顆 × 200 元 ＝ 2.7 萬元；隔離器約 2,300 個 × 20 元 ＝ 5 萬元；MPO 接頭 144 個 × 350 元 ＝ 5 萬元[[gewo168-cpo-passive-20260530]] | 未具名紀要 |
| 同一份紀要，假設一年出貨 100 萬台 | FAU 約 250 億元、CW 雷射接近 300 億元、隔離器和 MPO 各 500 億元（人民幣）[[gewo168-cpo-passive-20260530]] | 未具名紀要 |
| Coherent | 外部光源模組和 FAU 是 CPO 可服務市場裡最大的兩塊，沒拆到元件層級[[futurum-coherent-ofc2026-20260323]]；一顆 100T、200G 通道的交換器晶片，Coherent 能賣的內容「最多 1.5 萬美元」[[coherent-photonlink-deck-20260921]] | 公司說 |
| 研究機構 | 光引擎每顆約 1,000 美元，含 FAU；36 顆光引擎加外部光源合計 3.5–4 萬美元，外部光源沒有單獨列價[[semianalysis-cpo-book]] | 第三方 |
| 一位產業分析師 | CPO 雷射的價格約是插拔式雷射晶片的 10 倍，2030 年可能縮到 5 倍[[supercomputing-cpo-laser-202609]] | 第三方 |
| 券商的 BOM 拆解 | 一台 CPO 交換機 70,640 美元，沒有拆出外部光源和 FAU[[wallstreetcn-tianfeng-bom-20260418]] | 第三方 |

在那份紀要的口徑裡，FAU（2.5 萬元）和 CW 雷射晶片（2.7 萬元）同一個量級，外部光源模組（超過 4 萬元）比 FAU 高。紀要沒說 4 萬元有沒有包含 128 顆雷射；如果沒包含，雷射加模組約 6.7 萬元，是 FAU 的約 2.7 倍（計算）。FAU 這一側的數量和單價，主場在 [fau-makers.md](fau-makers.md#fau-value)。

價格和毛利，公司自己的說法：Lumentum 說「確實小幅重新定價」，多數長約的價格影響在後面，CW 雷射的漲價能力「讓我們驚訝」[[investing-lumentum-q4fy26-20260811]]；Coherent 的長約有最低採購量、約定整段合約的價格[[futurum-coherent-q4fy26-20261009]]；AAOI 說雷射毛利 55–65%，外部光源模組預期 50% 以上[[investing-aaoi-q2-20260806]]；中國雷射晶片廠源杰的資料中心產品毛利約 84%，這是媒體依半年報算的[[wallstreetcn-yuanjie-h1-202608]]。一份財經資訊網站說 70 mW CW 晶片從每顆 3.50 美元漲到 3.80 美元，只當線索[[biggo-inp-price-20260425]]。

### 規模感

計算，不推論：AAOI 的目標是 2028 年每月約 40 萬支外部光源模組[[investing-aaoi-q2-20260806]]，如果每支 8 顆，是每月 320 萬顆 CPO 雷射（8 顆是假設）。對照插拔式：華星光引研究機構估，2026 年用 CW 雷射的模組約 8,500 萬支、每支 2–8 顆，全年約 4 億顆 CW，約每月 3,300 萬顆；另有 EML 約 1.6 億顆[[luxnet-slides-20260828]]。

## 雷射是誰在做？ {#q21}

### NVIDIA 為什麼投資兩家雷射廠

這一塊最大的兩家是美國的 Lumentum 和 Coherent。NVIDIA 在 2026 年 3 月 2 日各投資兩家 20 億美元，還附上「數十億美元的採購承諾和未來產能使用權」[[nvidia-pr-coherent-20260302,nvidia-pr-lumentum-20260302]]：Coherent 以每股 256.80 美元發行 7,788,161 股普通股給 NVIDIA，Lumentum 發行 2,876,415 股可轉換特別股，每股 695.31 美元[[sec-coherent-8k-20260302,sec-lumentum-8k-20260302,sec-lumentum-10k-20260817]]。兩家的年報都沒有揭露採購承諾的金額。Coherent 在年報裡說，它和 NVIDIA 的協議是多年、非獨家的，另有一份到 2030 年的多年產能協議，可能需要追加設備、人力和營運資金[[sec-coherent-10k-20260814]]。只有一則媒體報導寫 Coherent 這份協議涵蓋「高功率 CW 雷射、外部光源模組和 FAU」；一手文件裡找不到 FAU 這個字[[tomshardware-lumentum-20260731,sec-coherent-10k-20260814]]。

### 產能排名

![研究機構 2026 年 6 月的雷射產能排名。上：EML 加 CW-DFB 合計，前三名 Broadcom、Lumentum、住友電工佔 55%。中：EML 前三名 Lumentum、Broadcom、三菱電機佔 72%。下：CW-DFB（CPO 用的連續光雷射屬於這種），Broadcom 和住友電工並列第一，其次 Coherent，第三是聯亞／華星光，合計 74%。[[semitoday-trendforce-laser-20260604]]](img/media/trendforce-eml-cwdfb-capacity-2026.jpg){.s}

同一份估計說，2026 年 EML 加 CW-DFB 的月產能會翻倍，到約 5,070 萬顆[[semitoday-trendforce-laser-20260604]]。

### 各家自己怎麼說

| 廠商 | 國 | 做哪層 | 公司自己說的（另有標註的除外） |
|---|---|---|---|
| Lumentum | 美 | 晶片、模組 | CPO 用超高功率雷射已在出貨給 scale-out；「主要 CPO 客戶」的 scale-up 高量出貨在 2027 下半年、客戶 2028 年部署；2026 年 8 月拿到**第一張**外部光源模組訂單，2027 下半年交貨[[investing-lumentum-q4fy26-20260811,sec-lumentum-8k-q4fy26-20260811]]；2026 年 2 月拿到一張數億美元的追加訂單，法說原話寫明品項是超高功率雷射、用在 scale-out、2027 年出貨：「an additional multi-$100 million purchase order for ultra-high-power lasers that support optical scale-out applications」[[fool-lumentum-q2fy26-20260203]]；5 月說這張單排在 2027 上半年交貨，超高功率雷射的 CPO 產線「proceeding according to plan」，2026 年 12 月季就會有明顯營收[[fool-lumentum-q3fy26-20260506]]（法說會轉錄稿；**改正**：舊稿寫「沒說是雷射還是模組」，原話是雷射）；超高功率雷射營收年底約每季 5,000 萬美元，2027 年第三季可能第一次破億[[investing-lumentum-q4fy26-20260811]]；給 scale-up 規格 OCI 用的 8 波長 ELSFP，2027 上半年初步供貨[[lumentum-pr-ecoc2026-20260921]]；北卡新廠做 6 吋 InP，NVIDIA 是客戶[[businesswire-lumentum-nc-20260326,opticsorg-lumentum-20260401]]；共有 5 座 InP 廠[[tomshardware-lumentum-20260731]] |
| Coherent | 美 | 磊晶、晶片、模組 | 德州已量產 CPO 用超高功率 CW 雷射，「包含和 NVIDIA 合作的那些」，CPO 營收從 2026 年 12 月季開始；scale-up CPO 在 2027 下半年；一個外部光源模組最多 8 顆雷射[[futurum-coherent-q4fy26-20261009,webull-coherent-q4fy26-20260812]]；2026 年 2 月第一次講這件事：剛拿到一家「market-leading AI data center customer」的「exceptionally large purchase order」，內容是含新高功率 CW 雷射的 CPO 方案，初期營收在 2026 年底、之後更明顯，客戶沒點名；執行長說客戶選 Coherent 的原因之一，是這顆高功率 CW 雷射做在德州 Sherman 的 6 吋 InP 線上（美國製造）[[fool-coherent-q2fy26-20260204]]；外部光源模組已送樣給客戶[[coherent-photonlink-deck-20260921]]；宣稱超過 10 個 CPO 客戶專案、超過 10 個 NPO 客戶專案，已出貨超過 3 億顆 InP 雷射[[futurum-coherent-photonlink-20260923]]；6 吋 InP 一片產出約 3 吋的 4 倍、成本不到一半，蘇黎世第三座 6 吋線 2027 上半年上線[[futurum-coherent-q4fy26-20261009]]；德州 Sherman 廠投資 6.5 億美元、晶圓產出 4 倍（只有媒體報導）[[theregister-coherent-4x-20260617]] |
| Broadcom | 美 | 晶片 | InP 晶圓的唯一來源是自己的賓州廠，III-V 晶圓大部分在美國和新加坡自己做[[sec-broadcom-10k-20251218,sec-broadcom-10q-20260910]]；EML、CW、VCSEL 的 InP 廠一年擴三倍以上[[webull-broadcom-q3fy26-20260903,fool-broadcom-q3fy26-20260909]]；CPO 交換器的雷射做成前面板可插拔、可更換的模組[[broadcom-pr-bailly-20240314,broadcom-ecoc2025-202509,broadcom-pr-20251008]]；模組幾顆雷射、幾 mW、用不用自家晶片，文件都沒寫 |
| 住友電工 | 日 | 基板、晶片、外部光源組裝 | CPO 用高功率 CW 雷射正在做最後的送樣和認證，和多家客戶討論，2026 年度末（2027 年 3 月）試量產出貨，2027 年度起量；客戶把 CPO 和插拔式並行評估，「對 CPO 是否馬上大幅起來看法謹慎」，日文原話：「顧客は CPO の使用と従来のプラカブルの使用を並列で検討されており、CPO がすぐに大きく立ち上がるかについては、慎重な見方をしている」[[sumitomo-qa-20260610]]；InP 基板產能 2024→2028 擴 3 倍[[sumitomo-results-briefing-20260522]]；NVIDIA 2025 年名單上負責外部光源組裝、對位、測試[[nvidia-blog-20250327]] |
| 三菱電機 | 日 | 晶片 | EML 產能 2029 年度是 2025 年度的 3 倍以上，2025 年度決定投資 400 億日圓；CPO 用 CW 光源和調變器是新商機[[melco-irday-semi-20260529,melco-irday-qa-20260608]]；CPO「現在是不成熟的技術」，市場 2028–29 年度起來、2030 年代才正式放大，主要用在機櫃內[[melco-irday-qa-20260608]] |
| 古河電工 | 日 | 晶片、模組 | 投資 380 億日圓在岩手蓋 DFB 雷射晶片新廠，2028 年 4 月量產，2028 年 DFB 產能是 2025 年度的 5 倍以上；100 mW DFB 預期會用在 ELSFP[[furukawa-dfb-plant-20251217]]；DFB、SOA 等雷射晶片的獲利上修，主因是增產不是漲價[[furukawa-q1fy26-qa-20260806]]；產能倍數：DFB 到 2025 年度上半年末已是 2023 年度的 5 倍，2026 年度再增產到 2025 年度的 1.5 倍[[furukawa-q1fy26-qa-20260806]]；MT 插芯（多芯光纖接頭的核心零件）的增產也已達 2023 年度的 5 倍，公司並說 CPO 市場用的光零件持續增產[[furukawa-q2fy25-speech-20251110]]；論文發表 16 通道 ELSFP 模組（兩顆 8 通道發射元件）[[furukawa-ofc2026-elsfp-202603]] |
| JX 金屬 | 日 | 基板 | 四年最多 1,200 億日圓擴產，產能約擴 7–10 倍[[jx-inp-20260616]] |
| AXT | 美（中國生產） | 基板 | 見[下一節](#las-inp)[[sec-axt-8k-20260730]] |
| AAOI | 美 | 磊晶到模組 | 雷射晶片全在德州自產；CPO 雷射 300 mW；ELSFP 2028 年目標每月約 40 萬支；約 5 家客戶[[investing-aaoi-q2-20260806,cw-en-aoi-20260818]]；2026 年 5 月說正和約 3 家客戶談 3 年長約，含雷射和 ELSFP[[fool-aaoi-q1-20260507]] |
| Sivers | 瑞典 | 晶片 | 蘇格蘭格拉斯哥 InP 廠投資 3,000 萬美元，2027 年第四季上線後年產超過 1 億顆 CW DFB[[sivers-glasgow-20260903]]；新創 Ayar Labs 的 16 波長光源用 Sivers 的雷射陣列（只有媒體報導）[[supercomputing-cpo-laser-202609]] |
| OE Solutions | 韓 | 晶片、模組 | 自製 InP 的 100G EML 雷射晶片；ELSFP 今年推出，2027 年起進入 CPO 市場（媒體引公司）[[etnews-oesolutions-20260506,mt-oesolutions-20260508]] |
| 天孚 | 中 | 模組 | CPO 配套的 FAU、外部光源模組「穩定量產交付」，沒寫客戶[[jrj-tfc-20261009,cninfo-irm-search]]；見下方「誰在供 NVIDIA」。另一句要並排：2025 年 11 月被問「主要供應商在 CW 光源方面的擴產進度」，公司答「公司產品不包括 CW 光源產品」，擴產請去問上游[[cninfo-tfc-irm-20251127]]。兩句都是公司答覆：外部光源模組是它的產品，CW 光源（雷射晶片）不是；晶片從誰買，答覆沒寫 |
| 源杰 | 中 | 晶片 | 2026 上半年營收 9.25 億人民幣、年增 351%，資料中心約佔 84%，主力是 70／100 mW CW 批量出貨，研發 300 mW（媒體報導）[[wallstreetcn-yuanjie-h1-202608]]；陝西新園區投資約 42.68 億人民幣[[cbn21-yuanjie-20260812]]。公司自己的說法：2025 年 11 月 CPO 光源「研發進展順利，目前已與客戶進行技術規格的對接交流」[[sse-yuanjie-irm-20251103]]；2026 年 8 月「NPO 對 CW 光源需求可能更高，不同客戶方案對光源功率要求存在差異，市場處於動態快速發展階段，方案將持續迭代優化」，也就是光源規格還沒定案[[sse-yuanjie-irm-20260831]] |
| 光迅 | 中 | 磊晶到模組 | 3.2T NPO 模組含外部光源[[c114-accelink-ofc2026-20260320]] |
| 仕佳光子、長光華芯、三安光電 | 中 | 晶片 | 2026 年 10 月中國光博會展出 200–500 mW 的 CW 雷射；仕佳同一個攤位也賣 FAU[[ledinside-cioe-20261008]] |
| 仕佳光子 | 中 | 晶片 | 公司自己的進度：2026 年 6 月「70-100mW 產品已實現小批量出貨」；8 月「100mW CW 產品已實現批量出貨，400mW 等規格產品實現小批量出貨」[[sse-sourcephotonics-irm-20260602,sse-sourcephotonics-irm-20260805]] |
| 長光華芯 | 中 | 晶片 | 2025 年 12 月：100G EML 已量產、200G EML 在客戶驗證，「100G VCSEL、100mW CW DFB 和 70mW CWDM4 DFB 芯片已達到量產出貨水平」[[sse-everbright-irm-20251204]] |
| 華工科技（雲嶺光電） | 中 | 模組；晶片靠發起設立的雲嶺光電 | 2025 年 10 月說雲嶺光電的光芯片、CW 光源「驗證情況都很不錯，可做備份方案」；2026 年 8 月說這些已「實現量產並批量交付」，一年內從備案變成實際供貨；外置光源模組（ELSP）已備好，正在拉小批試製線[[cninfo-hgtech-irm-20251026,cninfo-hgtech-irm-20260827]] |
| 光創聯（環旭旗下）、銘普光磁 | 中 | 模組 | 光創聯超高功率 ELSFP 2026 下半年試產、最快 2027 年第一季量產；銘普光磁 ELSFP 樣品交付（只有媒體轉述）[[uanalyze-elsfp-20260924]] |
| 聯亞、全新、英特磊、華星光、光環、聯鈞、立碁 | 台 | 見[台廠在哪一層](#las-tw) | |

中國廠的 400 mW 雷射已送樣、小批量驗證，缺的是「百萬級量產的長期可靠度數據」，這是一篇作者文章的說法[[eetchina-400mw-cw-20261009]]。中國自己的路線見 [china.md](china.md#cn-npo)。

### 舊版要改的地方：Lumentum 做的是雷射晶片，模組才剛接單

舊版的表把 Lumentum 寫成「NVIDIA 2025 年名單上負責外部光源組裝、對位、測試」。NVIDIA 2025 年 3 月的原句是：Lumentum、住友、Coherent「提供外部光源組裝、光學對位，以及和矽光子引擎一起測試」[[nvidia-blog-20250327]]。但 Lumentum 自己 2026 年 8 月的財報新聞稿寫的是「拿到外部光源模組的第一張訂單」，交貨在 2027 下半年[[sec-lumentum-8k-q4fy26-20260811,investing-lumentum-q4fy26-20260811]]。照 Lumentum 自己的文件，它到目前在 CPO 賣的是雷射晶片；NVIDIA 2025 那句是開發合作期間的分工，不能讀成「Lumentum 現在出貨外部光源模組給 NVIDIA」。Lumentum 也沒有任何關於保偏光纖、FAU、接頭的公開說法[[sec-lumentum-10k-20260817]]。

### 誰在供 NVIDIA 的雷射

完整的表在 [players.md](players.md#pl-nv)，這裡只列雷射：

- 一位產業分析師說，Lumentum 的 CPO 雷射已通過 NVIDIA 認證，Coherent 是下一個，「未來 2–3 年不會有其他供應商通過，因為這種雷射的可靠度很難證明」。這是分析師的說法，不是 NVIDIA 或兩家公司說的[[supercomputing-cpo-laser-202609]]。
- Coherent 說它量產的 CPO 雷射「包含和 NVIDIA 合作的那些」[[futurum-coherent-q4fy26-20261009,webull-coherent-q4fy26-20260812]]；Lumentum 說它「主要的 CPO 客戶」需求上調，沒點名[[investing-lumentum-q4fy26-20260811]]。
- NVIDIA 2026 年 6 月寫：「TFC」的雷射晶粒被封裝成雷射模組，並驗證了 AI 工作負載要的可靠度[[nvidia-blog-20260601]]。那段放在台灣生態系的段落，但天孚（TFC Communication）總部在蘇州、廠在中國和泰國，NVIDIA 沒有說明。
- 一份未具名紀要說，Lumentum 把 CW 雷射賣給天孚、中際旭創、新易盛去封裝 ELSFP；住友的份額「非常小」[[eastmoney-dfau-survey-20260531]]。
- NVIDIA 2025 年和 2026 年公布的夥伴名單不一樣：2025 年有 Lumentum、住友、Coherent，2026 年 6 月那篇只列台積電、矽品、TFC、鴻海[[nvidia-blog-20250327,nvidia-blog-20260601]]。2026 年那篇只寫台灣段落，不能從這裡推誰退出。

### 雷射廠也在打包光纖和 FAU

Coherent 說它在 CPO 一個插座上能賣的東西包括雷射、外部光源模組、隔離器、保偏光纖、整套光纖貼合組件和 PIC[[futurum-coherent-q4fy26-20261009]]；2026 年 9 月它把 FAU、可拆式 FAU 接頭、光纖整線都列進產品線，FAU 2026 年第四季、可拆接頭 2027 年第一季可以量產[[coherent-photonlink-deck-20260921,coherent-ecoc2026-20260920]]。中國的仕佳光子在同一個攤位賣 500 mW CW 雷射和 FAU[[ledinside-cioe-20261008]]。FAU 不一定只經過台廠和 COUPE，雷射供應商也在同一個插座上賣光纖組件。這條路的細節在 [fau-makers.md](fau-makers.md#fau-routes)。

### 兩種做大功率雷射的方法

一篇作者文章說，Lumentum 走「DFB 雷射加 SOA 放大」，晶片面積大，一片晶圓切出來的顆數少近 10 倍；Coherent 走單顆大功率 DFB[[eetchina-400mw-cw-20261009]]。這只有作者的說法。如果是真的，CPO 對 InP 晶圓面積的需求會比顆數看起來大得多。住友的論文也是 DFB 加寬條 SOA 的做法[[sei-tr205-cpo-laser-202407]]；古河的 16 通道模組用的是 SOA 整合 DFB[[furukawa-ofc2026-elsfp-202603]]。

## InP 基板和銦 {#las-inp}

### 銦：中國佔約七成，管制的是化合物

2025 年全球原生精煉銦約 1,100 公噸，中國 760 公噸，其次韓國 180、日本 65、加拿大 40[[usgs-indium-202601]]。760 ÷ 1,100 ≈ 69%（計算）。回收銦沒有資料。美國倉庫的銦均價 2025 年約每公斤 390 美元（2024 年 351 美元）[[usgs-indium-202601]]。全球銦的消費大部分在 ITO（顯示器的透明導電膜），不在雷射[[usgs-indium-202601]]。

中國 2025 年 2 月 4 日起的出口管制，和銦有關的是三項：磷化銦（InP）、三甲基銦、三乙基銦。**金屬銦本身不在清單上**[[xinhua-mofcom-indium-20250204]]。美國政府的礦產報告寫成「銦被納入出口限制」，和公告原文有出入[[usgs-indium-202601]]。管制之後一年，中國未鍛軋銦的出口年減 72%[[usgs-indium-202601]]。

2026 年 6 月，只有媒體報導說：銦錠雖然沒有正式管制，中國海關開始要買方揭露最終用途，審件從當天變成數天，目前沒有出貨被擋的案例；同時美國國防後勤局提出三年內最多收儲 403 公噸銦的標案[[businesskorea-indium-20260619,idnfinancials-indium-202606]]。中國 2025 年底修改對外貿易法，2026 年 3 月起擴大限制進出口的授權，理由包括「國內供應短缺」「建立或加速建立特定國內產業」[[sec-axt-10q-20260813]]。一家媒體說日美企業申請中國產 InP 基板的拒絕率超過 80%，沒有出處[[tmtpost-inp-indium-20260508]]。出口管制整體見 [china.md](china.md#cn-export)。

### InP 用掉多少銦

沒有一手機構公布這個數字。手上的：

| 項目 | 數字 | 出處 |
|---|---|---|
| 4 吋 InP 晶圓（625 µm 厚）含銦 | 約 19.2 g（計算：InP 裡銦佔質量 78.75%）；一家化學品商估約 19 g，高速應用有效良率 30–50%，實際要翻倍 | 計算；[[tmtpost-inp-indium-20260508]] |
| 券商估 2027 年全球 InP 晶圓銷量 | 341.5 萬片，用銦約 163 公噸 | 券商的估計（媒體轉述）[[tmtpost-inp-indium-20260508]] |
| 同一位券商估 2026 年全球銦總需求 | 約 2,407 公噸，InP 佔 6.77% | 同上 |
| 中國一家 InP 晶體專案 | 年產 40 噸 InP，含銦約 31.5 公噸（計算） | 媒體報導[[mexicobusiness-inp-202609]] |

163 ÷ 341.5 萬片 ＝ 每片 47.7 g，是 4 吋理論值的約 2.5 倍，比「良率翻倍」的約 38 g 還高；轉述沒寫晶圓尺寸，也沒寫含不含長晶損耗（計算）。分母換成 USGS 的原生產量，163 ÷ 1,100 ＝ 14.8%（計算）。兩個分母口徑不同：USGS 只算原生精煉，2,407 公噸含回收。結論只到這裡：InP 用的銦佔全球產量個位數到十幾 %，看用哪個口徑。

### 有機銦（MO 源）會不會卡住台灣磊晶廠

三家台灣磊晶廠的 2025 年報都寫了原料來源：

| 公司 | 磊晶方法 | 基板供應商 | 有機金屬或銦原料供應商 | 年報寫的供應狀況 |
|---|---|---|---|---|
| 全新 | MOCVD | AXT、Freiberger、住友電工香港 | 台灣日酸、林德台灣、凱信；主要原料由日本、美國、德國、台灣供應 | 「目前供應情形良好」[[mops-vpec-ar2025-20260529]] |
| 聯亞 | MOCVD | 三家用代號 | MO 源：兩家用代號、凱信 AKZO | 「正常」[[mops-landmark-ar2025-20260527]] |
| 英特磊 | MBE | 住友、Freiberger、JX | 銦等元素材料：UMC、5N Plus、Indium Corp.、Yamanaka | 「良好」[[mops-iet-ar2025-20260623]] |

英特磊用 MBE，原料是銦本身，不是三甲基銦；它年報寫 2025 年 III-V 族材料「價格大幅上漲，本公司大量買進以確保原料貨源」，基板佔直接材料九成以上[[mops-iet-ar2025-20260623]]。全新、聯亞的 MO 源名單裡沒有寫出中國公司的名字，兩份年報都沒提三甲基銦管制[[mops-vpec-ar2025-20260529,mops-landmark-ar2025-20260527]]。

聯亞寫的「凱信 AKZO」，AKZO 是 Nouryon 的前身（前 AkzoNobel 特用化學品）。Nouryon 的型錄寫它的 MO 源工廠在美國德州 La Porte，產品表裡的銦只有三甲基銦[[nouryon-hpmo-202603]]；它在中國嘉興的廠做的是聚合物用的金屬烷基，不是半導體用的 MO 源[[nouryon-alkyls-20261012]]。型錄沒有排除其他產地，各地區另有分裝站，沒寫在哪[[nouryon-hpmo-202603]]。

中國這邊，南大光電說三甲基銦年產能共 5 噸，其中能用在 InP 的高純品約 2 噸，通過商務部審批後對外銷售；客戶驗證通常要一年半左右[[cninfo-irm-tmin-20261012]]。2 噸三甲基銦約含 1.4 公噸銦（計算，銦佔三甲基銦質量 71.8%）。

台灣在這一層的曝險，目前看到的不在三甲基銦，而在基板（下面的 AXT 出口許可）和客戶地區（[台廠在哪一層](#las-tw)）。

### 基板誰在做：市佔有四個版本

| 版本 | 能追到的最早出處 | 可信度 |
|---|---|---|
| 住友 42%、AXT 36%、JX 13%，三家合計九成以上 | 一家研究機構 **2020 年**的統計，2026 年 5 月一份券商報告轉述[[dwzq-inp-20260513]]；之後很多文章沒寫年份照抄[[sina-axt-inp-20260615]]；也有寫成 43／35／13 的[[biggo-inp-price-20260425]] | 第三方（2020 年數字） |
| 住友 60%、AXT 35%、JX 5% | 2026 年 1 月一份未具名會議紀要、一篇產業媒體文章，都沒寫來源[[fxbaogao-inp-20260105,sina-semiinsights-inp-20260123]]；另一篇作者文章寫「住友近半到六成」[[huxiu-indium-20260622]] | KOL、媒體報 |
| AXT 加住友近 80%、JX 約 10% | 國際通訊社 2026 年 6 月 11 日的報導，句子沒標出處[[reuters-inp-20260611]] | 媒體報 |
| 住友、JX 各約四成 | 兩家媒體，都沒寫出處[[technews-sumitomo-inp-20260703,toyokeizai-inp-20260904]]；其中一家同一篇又說 AXT 是全球最大[[technews-sumitomo-inp-20260703]] | 媒體報 |

四個版本裡只有第一個追得到研究機構，而且是 2020 年的數字。第二和第四個版本對 JX 的估計差 8 倍（5% 對 40%）。2020 年之後，AXT 受中國出口許可影響、JX 宣布擴產 7–10 倍、住友擴 3 倍，所以這裡不採用任何一個市佔。同一則通訊社報導還說，住友的基板大量自用，外賣不多[[mexicobusiness-inp-202609]]。

另外兩個說法也放在這裡，都沒有基準：AXT 自己在 2025 年 10 月的法說說「we are 40% of the indium phosphide supply chain」（我們佔 InP 供應鏈的 40%），沒說是數量還是金額、哪一年（AI 轉寫稿）[[allmind-axt-q3-20251030]]；英特磊 2026 年 3 月的法說（第三方整理，不是原話）列出基板主要供應商：日本的住友、美國上市但在中國生產的 AXT、德國的 Freiburger、法國的 InPact、日本的 JX，比上面的版本多了兩家歐洲廠[[fugle-iet-20260312]]。不採用任何一個市佔的理由不變。

### 擴產

| 廠商 | 擴產 | 可信度 |
|---|---|---|
| JX 金屬 | 四年最多 1,200 億日圓，在茨城常陸那珂新設產能，約擴 7–10 倍，是這項產品史上最大的一筆；同時「和客戶討論價格調整」[[jx-inp-20260616]] | 一手 |
| 住友電工 | 自己的說明會資料：InP 基板產能 2024→2026 年 1.8 倍、2026→2028 年 1.7 倍，合計 3 倍（以面積換算，含資料中心以外的用途）[[sumitomo-results-briefing-20260522]]；媒體引日本報導寫投資約 180 億日圓、2028 財年是 2024 財年的 3.1 倍（2025 年 11 月的目標是 2.4 倍）[[trendforce-sumitomo-inp-20260713,technews-sumitomo-inp-20260703]]；住友說依客戶給的 2030 年展望，2028 年度起產能還要再倍增[[sumitomo-qa-20260610]] | 公司說；媒體報 |
| AXT（北京通美） | 2026 年 InP 產能翻倍以上（法說另一處說「實際上是三倍」），年底季營收約 6,000 萬美元；2027 年在鄰近地點再翻倍，2027 年底季營收約 1.3 億美元[[investing-axt-q2-20260730]] | 公司說 |
| 雲南鍺業 | 2026 年 4 月宣布投資 1.89 億人民幣，年產能擴到 45 萬片[[mexicobusiness-inp-202609]] | 媒體報 |
| 廣東先導 | 子公司啟動年產 40 噸 InP 晶體專案[[mexicobusiness-inp-202609]] | 媒體報 |

![住友電工的說明會投影片：資料中心相關產品的產能，2024 年到 2028 年光連接器 13 倍、光纖 2 倍、資料中心內用光元件 4 倍、InP 基板 3 倍（以面積換算，含資料中心以外的用途）。廠商投影片。[[sumitomo-results-briefing-20260522]]](img/media/sei-2026-capex-dc-capacity-202605.png){.s}

舊版寫「住友擴到 3.1 倍只有媒體引日本報導，住友自己的公告沒找到」。現在找到住友自己的說明會資料寫 3 倍，媒體的 3.1 倍並列。

**4 吋換 6 吋。** Coherent 說 6 吋一片的產出約是 3 吋的 4 倍、成本不到一半，德州、瑞典的 6 吋線良率比 3 吋高[[futurum-coherent-q4fy26-20261009]]。這句話最早的原話是 2025 年 11 月的法說：「a six-inch wafer compared to a three-inch wafer will produce more than four times as many chips at less than half the cost」；德州 Sherman 的線是「the world's first six-inch indium phosphide production line」，前一季（2025 年 9 月季）開始生產，早期良率「actually higher than our current three-inch indium phosphide yields」[[fool-coherent-q1fy26-20251106]]。2026 年 5 月又宣布蘇黎世第三座 6 吋 InP 廠，「We expect to see production from that third site at the beginning of calendar 2027」[[fool-coherent-fy26q3-20260506]]（都是法說會轉錄稿）。AXT 說客戶從 2 吋、3 吋往 4 吋移，現在大力推 6 吋，6 吋「比 3、4 吋難量產好幾個等級」[[investing-axt-q2-20260730]]。聯亞說雷射功率提高、晶片變大，用大尺寸基板比較合適，但「全球 InP 基板 4 吋以上的產能比重仍非常低」[[moneydj-landmark-20260813]]。AAOI 說它「剛進入 4 吋量產」，基板供應商有歐洲兩家、日本兩家、中國三家，庫存夠用到 2027 年底[[investing-aaoi-q2-20260806]]。AAOI 自己的尺寸時程：2025 年 11 月說現在做 3 吋、之後轉 4 吋[[allmind-aaoi-q3-20251107]]；2026 年 5 月說過去 18 個月從 2 吋、3 吋走到 4 吋，目標「to go to six-inch by end of next year」（2027 年底前轉 6 吋）[[fool-aaoi-q1-20260507]]。歐洲另有一座 6 吋 InP 光晶片廠動土，投資逾 1.5 億歐元，2028 年全產；這是晶片廠，不是基板廠[[trendforce-6inch-inp-fab-20260318]]。

### 外面買得到 Coherent 的 InP 雷射嗎

買不到，而且連續三季這樣說。2025 年 11 月：「we do not sell indium phosphide in the open market」，產能全被自家光模組用掉[[fool-coherent-q1fy26-20251106]]；2026 年 8 月：「I do not see any time in the near future where we would be selling Indium Phosphide lasers externally」，資料中心光模組的需求吃掉每一分產能[[allmind-coherent-q4fy26-20260812]]。要找 Coherent 以外的 InP 雷射來源（例如台廠想找替代），這是一條界線。

### 磊晶層和下游廠：誰被基板卡到

基板缺貨的說法多半來自基板廠和研究機構。下面是磊晶廠、模組廠自己講受到的影響。

| 公司 | 說了什麼 | 時間 |
|---|---|---|
| Tower（矽光 PIC 代工，整合雷射要用 III-V 磊晶片） | 「indium phosphide right now is constrained. In our case, not necessarily the end laser product is the constraint, the starting material is the constraint」（卡的是起始材料，不一定是雷射成品）[[allmind-tower-q1-20260513]]；8 月：「We were under somewhat of a crunch for indium phosphide starting material. And we believe that we have addressed that very nicely with the contract with IQE」，也就是和磊晶廠 IQE 簽了合約後已處理[[fool-tower-q2-20260804]] | 2026-05、2026-08 |
| 英特磊 | 「磷化銦基板短缺仍是未來幾年的主要瓶頸」；第二季營收下滑，歸因於日本主要供應商住友在 4 月黃金週長假停工約兩週、基板供應中斷；如果能取得無限量的 InP 基板，以現有客戶需求，InP 營收可以輕易翻倍（第三方整理，不是原話）[[fugle-iet-20260312,fugle-iet-20260827]] | 2026-03、2026-08 |
| 環宇-KY | 因為 InP 基板供應受限，高毛利的自有品牌光電元件（AOC）產量減少，營收占比從 2026 年第一季的 74% 降到第二季的 23%；影響第二季產能的基板問題「已於 6 月解決」；計畫 2027 年提高非中系供應商的比例，特別是 200G 產品（第三方整理，不是原話）[[fugle-ufo-20260805]] | 2026-08 |

英特磊的備忘錄還寫，公司對這種基板採「即產即用（hand-to-mouth）」的做法、沒有庫存緩衝[[fugle-iet-20260827]]。

### 價格：說法差很多

| 說法 | 可信度 |
|---|---|
| 4 吋光通訊用 InP 基板每片約 650 → 900 美元，連三季漲，第四季可能再漲一成以上；部分磊晶廠要現金提貨[[technews-inp-price-20260817]] | 只有媒體報導（業界消息） |
| 2 吋光通訊級從 2025 年初 800 美元漲到 2026 年 4 月 2,300–2,500 美元；6 吋 1,400 → 5,000 美元[[biggo-inp-price-20260425]] | 一家財經資訊網站，沒寫出處 |
| 6 吋 InP 晶圓自管制以來漲 250%，到 5,000 美元[[mexicobusiness-inp-202609]] | 媒體報（轉述通訊社） |
| InP 基板漲約 3–5%[[bnext-inp-20260803]] | 媒體報 |
| JX：和客戶討論價格調整，沒給幅度[[jx-inp-20260616]] | 一手 |
| AXT：大尺寸、高價值產品帶來「有利的價格趨勢」[[investing-axt-q2-20260730]] | 公司說 |
| AXT 2025 年 10 月：多數產品價格很穩，但高階低 EPD（缺陷密度低）InP 基板的 ASP「is increasing」（在漲）[[allmind-axt-q3-20251030]]；2026 年 4 月：「We are raising some of our prices」，原因是原料，特別是銦，最近漲價[[fool-axt-q1-20260430]] | 公司說（轉錄稿） |

### 長約和預付款

| 買方 ← 賣方 | 內容 | 可信度 |
|---|---|---|
| Coherent ← AXT | 2026-06-26 簽，3 年，6 吋 InP 基板；AXT 2026–2028 年在北京擴產並承諾產能；Coherent 預付 22,288,500 美元[[sec-axt-8k-coherent-20260702]] | 一手 |
| 南京 Casela ← 通美 | 2026-06-11 簽，2027 全年固定量，總價 1.73 億人民幣（約 2,540 萬美元），簽約後付 50%；買不到 80% 要付取消費[[sec-axt-8k-casela-20260617]] | 一手 |
| Lumentum ← AXT | 2026-07-26 簽，產能保留 6 年；第一筆押金 4,350 萬美元，第二筆 4,350 萬美元 2028 年再議；年採購低於承諾要補差額；這份約 2027 年才開始[[sec-axt-8k-lumentum-20260729,investing-axt-q2-20260730]] | 一手 |
| 聯亞 ← 住友電工 | 2026–2030 五年期 InP 基板長約[[bnext-inp-20260803,mexicobusiness-inp-202609]] | 媒體報 |

舊版寫「Coherent 預付 AXT 約 2,229 萬美元，只有媒體報導」，現在 AXT 的 8-K 證實是 22,288,500 美元。AXT 財務長在法說把 Casela 和 Coherent 的預付金額講反了，以 8-K 為準[[investing-axt-q2-20260730,sec-axt-8k-coherent-20260702,sec-axt-8k-casela-20260617]]。一家媒體寫 Lumentum「同意支付 8,700 萬美元預付款」，那是兩筆 4,350 萬相加，但第二筆 2028 年才定[[ctee-inp-20260812]]。

### AXT 的出口許可

AXT 是美國公司，但 InP 基板在中國子公司北京通美生產。2025 年 2 月 4 日起，通美的三大產品（砷化鎵、鍺、InP）出口都要中國商務部許可；2025 年 6 月 11 日拿到第一批，先出給歐洲和日本客戶；公司說「InP 出口許可是我們目前最大的挑戰」[[sec-axt-10q-20260813]]。2026 年第二季營收 4,759 萬美元，其中 InP 3,070 萬美元創新高；未出貨訂單「遠超過 1 億美元，超過兩季」，很多在等許可；第三季約 6,600 萬美元的營收「已有許可或不需要許可」；許可「越來越規律，特別在某些地區」；「沒有訂單就不能申請許可」；中國境內出貨不需許可，第二季中國佔營收過半[[investing-axt-q2-20260730]]。

AXT 的未出貨訂單一季一季往上，許可也是公司說過的瓶頸：

| 時間 | AXT 說了什麼 |
|---|---|
| 2025-10-30 | InP 未出貨訂單「more than $49 million and growing」（超過 4,900 萬美元）；中國商務部審一件 InP 許可約 60 個工作天、約 3 個月[[allmind-axt-q3-20251030]] |
| 2026-02-20 | 「backlog for indium phosphide wafers have reached a new high of over $60 million」[[allmind-axt-q4-20260220]] |
| 2026-04-30 | 「an indium phosphide backlog that has now reached a new high of over $100 million」[[fool-axt-q1-20260430]] |
| 2026-07-30 | 未出貨訂單遠超過 1 億美元、超過兩季（上面一段）[[investing-axt-q2-20260730]] |

CPO 對基板需求的說法：2025 年 10 月，執行長說客戶的客戶形容有「tsunami」（海嘯）要來；分析師說他聽到的是 5 到 10 倍，業務副總回答「a lot of that is coming from CPO for scale up」（很大一部分來自 scale-up 的 CPO），同一場他也說目前的成長在插拔式、未來幾年還會是插拔式[[allmind-axt-q3-20251030]]。5 到 10 倍是分析師提的數字，不是 AXT 的預測。2026 年 4 月，公司說基板市場未來 3 到 5 年「a four to six times increase」（成長 4 到 6 倍），scale-out 和 scale-up 都推，並說這可能是公司業務從 2027 年底起的另一個轉折點[[fool-axt-q1-20260430]]（公司說這是它聽業界和客戶的預期，不是自己的預測）。這和 AAOI 的說法並排：AAOI 說庫存夠用到 2027 年底，擔心的是 2028、2029 年的量[[investing-aaoi-q2-20260806]]。

<figure class="s">
<svg viewBox="0 0 560 240" width="100%" style="max-width:560px" role="img" aria-label="AXT 季營收">
<line class="grid" x1="40" y1="200" x2="540" y2="200"/>
<rect class="bar" x="70" y="146.1" width="100" height="53.9"/>
<text class="item" x="120" y="138.1" text-anchor="middle">1,797 萬</text>
<text class="note" x="120" y="220" text-anchor="middle">2025 Q2</text>
<rect class="bar" x="230" y="119.3" width="100" height="80.7"/>
<text class="item" x="280" y="111.3" text-anchor="middle">2,690 萬</text>
<text class="note" x="280" y="220" text-anchor="middle">2026 Q1</text>
<rect class="bar" x="390" y="57.2" width="100" height="142.8"/>
<text class="item" x="440" y="49.2" text-anchor="middle">4,759 萬</text>
<text class="note" x="440" y="220" text-anchor="middle">2026 Q2</text>
<text class="note" x="40" y="18">單位：美元（季營收）</text>
</svg>
<figcaption>InP 基板廠 AXT 的季營收。2026 年第二季是去年同期的 2.6 倍（計算：4,759 ÷ 1,797）[[sec-axt-8k-20260730]]。</figcaption></figure>

只有媒體報導說：全新、聯亞曾因 AXT 許可延遲遇到基板中斷；Coherent 執行長 5 月隨美國總統訪中，部分目的是反映 InP 出口許可延遲[[mexicobusiness-inp-202609]]；2026 年 5 月底起部分中國供應商取得出口許可，6 月起分批交付全新[[bnext-inp-20260803,digitimes-inp-export-20260615]]。通美撤回上海科創板上市申請，改申請香港上市[[investing-axt-q2-20260730]]。

## 台廠在哪一層？ {#las-tw}

常和 FAU 一起被提到的「聯亞」「聯鈞」做的是雷射（磊晶片、外部光源模組），不是 FAU。台廠在雷射這條線的位置：

| 公司 | 做哪層 | 和 CPO 有關的說法 |
|---|---|---|
| 聯亞 3081 | 磊晶、晶片 | CW-DFB 產能和華星光並列研究機構排名第三[[semitoday-trendforce-laser-20260604]]；2027 年產能比 2026 年增加約 1.5 倍，資料中心佔 80–85%，以矽光用的 CW 為大宗，產能吃緊[[ttv-landmark-20260817]]；70／100 mW 未來一兩年仍是主流，CPO 雷射可能要 300 mW 以上，第一次導入雲端大廠驗證可能超過 18 個月[[moneydj-landmark-20260813]] |
| 全新 2455 | 磊晶 | 砷化鎵磊晶起家，法說簡報列 CW 雷射、2–4 吋 InP 基板、InP 磊晶片[[vpec-slides-20260902]] |
| 英特磊 4971 | 磊晶（MBE） | 公司估 InP 佔 2026 年營收 55–60%，全年 InP 基板可能偏緊（媒體報導）[[bnext-inp-20260803]]；德州新廠 2026 年底到 2027 年初完工[[moneydj-iet-20260727]]；第二季營收下滑，公司歸因於 InP 基板供應中斷；也在做不用 InP 基板的量子點 CW 雷射（見下）[[fugle-iet-20260827,fugle-iet-20260312]] |
| 華星光 4979 | 晶片到模組 | 有 CW、EML 晶片代工；產品線列出外部光源；2027–2029 年以 NPO 為主，CPO 2030 年成為主流[[luxnet-slides-20260828]]；CW 雷射月產能預計 2026 年第四季從 150 萬顆擴到 300–400 萬顆（第三方整理，見下）[[fugle-luxnet-20251222]] |
| 光環 3234 | 晶片、封裝 | 建 300 毫瓦雷射產能卡位 CPO（法人說法）[[udn-applied-optoelectronics-20260823]]；傳拿到 InP 後段製程訂單，間接打入 Lumentum、AAOI（只有媒體報導）[[udn-applied-optoelectronics-20260823]]。公司自己的說法比較保守：只做光源和整合服務，不做整機（見下）[[fugle-applied-opto-20251222]] |
| 聯鈞 3450 | 封裝、模組 | ELSFP 和雷射晶片大廠合作，工程試產，明年可能小量；晶片規格涵蓋 70／100／300／400 mW[[moneydj-unitedopto-20260819,udn-unitedopto-20260818]]；公司說現在是 design-in 階段，不自己做雷射晶片，晶片由客戶供應（第三方整理，見下）[[fugle-unitedopto-20260818]] |
| 立碁 8111 | 模組 | 1310 nm CW 雷射的外部光源，單模組輸出 20 dBm，明年目標 26 dBm；ELSFP 開發中；鎖定 CPO、NPO[[ctee-ligitek-20260904]] |
| 環宇-KY 4991 | 晶片、模組 | 70 mW CW 小量出貨，100 mW 認證中，放量時間一場一場往後（見下）；新竹新廠負責 CW 雷射後段晶片製程；最大客戶在中國，也供貨給 Lumentum、Coherent[[fugle-ufo-20260304,fugle-ufo-20260505,fugle-ufo-20260805]] |

和「台廠經由 COUPE 吃到 FAU」比，這是另一種曝險：聯亞、華星光在 CW 雷射產能排名前段，但 CPO 要的 300 mW 以上雷射，聯亞自己說第一次認證可能超過 18 個月；聯鈞、立碁的外部光源模組在試產或開發中；而那位分析師說的兩家 NVIDIA CPO 雷射供應商都是美國公司[[supercomputing-cpo-laser-202609]]。

### 台廠公司自己怎麼說

下面是富果研究的法說會備忘錄，是第三方整理，不是公司原話，也不是逐字稿；有簡報的標明簡報。

**華星光**（2025 年 12 月場）。CW 雷射 2025 年出貨量約為前一年的 4 倍；月產能預計從當時的 150 萬顆，到 2026 年第四季擴到 300–400 萬顆，2027 年 600 萬顆以上。晶圓尺寸：2026 年第二季 3 吋產能超過 2 吋成為主力，2026 年第四季完成 4 吋建置，2027 年量產。功率：2026 年主力 70 mW 和 100 mW，後續開發 200 mW 和 400 mW。現有場地可滿足 InP 晶片每月 400–500 萬顆的需求；CW 雷射和 DCI 產品線各有 3 家以上雲端服務商客戶[[fugle-luxnet-20251222]]。同一份備忘錄引的 CPO 市場數字：從 2024 年 4,600 萬美元到 2030 年 81 億美元，年複合成長率 137%，華星光佈局外置光源；備忘錄沒寫這個數字是哪家研究機構的[[fugle-luxnet-20251222]]。對照 2026 年 8 月的簡報說 CPO 2030 年才成為主流（上表）。上面功率表裡 CPO 要 300 mW 以上，華星光這一場說的是 70、100 mW 為主、200 mW 和 400 mW 是後續開發。

**光環**（2025 年 12 月國票場）。簡報只寫「佈局 CPO( 共同封裝光學 )與矽光子技術，開發晶片級封裝與高速零組件」[[mops-applied-opto-20251222]]。備忘錄的問答：在 CPO 裡專注提供關鍵的雷射光源，並透過設計與整合服務協助客戶做先進封裝和光引擎開發，「不會自行生產整機 CPO 產品」；產能瓶頸主要在後段的切割（Die Fab），不是前段晶圓製造[[fugle-applied-opto-20251222]]。這和上表的媒體說法（建 300 毫瓦雷射產能卡位 CPO）並列，兩者不衝突，但公司講的範圍比媒體窄。

**聯鈞**（2026 年 8 月 18 日場）。外部光源是 CPO、NPO 商品化的必要條件；已和雷射晶片大廠合作共同開發，產品進入工程試產與小量生產階段，簡報寫 ELSFP 正式進入試產[[fugle-unitedopto-20260818,mops-unitedopto-slides-20260818]]。問答：和終端用戶、系統設計商都有合作，目前是 design-in 階段，客戶名稱因保密協議不能說；至少用輸出 20 dBm 的規格，對應的雷射晶片約 300–400 mW，70 或 100 mW 對聯鈞是中低功率；出貨「沒那麼快」，2027 年下半年可能小量出貨，數量無法預估[[fugle-unitedopto-20260818]]。COSA（雷射晶片裝在載板上的半成品）產能從 2024 年起預計每年翻倍；AI 相關光學產品（COSA、光模組）占營收比重從 32.7% 升到 45.5%；計畫發行 30 億元可轉換公司債支應擴產；聯鈞不自己生產晶片，由客戶以客供（consign）方式提供，2025 年 11 月 19 日場也是同樣的說法[[fugle-unitedopto-20260818,fugle-unitedopto-20251119]]。

**環宇-KY**。100 mW CW 的放量時間，一場一場往後：

| 場次 | 70 mW | 100 mW |
|---|---|---|
| 2026-03-04 | 已獲客戶驗證、開始出貨 | 最終認證階段；目標 2026 年第三到第四季開始放量，期望到百萬顆等級[[fugle-ufo-20260304]] |
| 2026-05-05 | 已完成 5,000 小時可靠度測試，具備量產能力、小量出貨，會謹慎逐步放量 | 最終認證中，保守預估 2027 年第一季可放量[[fugle-ufo-20260505]] |
| 2026-08-05 | — | 仍在可靠性測試，期望 2026 年第四季或 2027 年初有進展；新竹新廠負責 CW 雷射的後段晶片製程（鍍膜、切割、測試），無塵室建置中[[fugle-ufo-20260805]] |

**英特磊的量子點雷射**。這是一條不用 InP 基板的路線：在砷化鎵基板上做量子點（QD）CW 雷射，不是直接長在矽上。2026 年 3 月場說，這是 2026 年的研發重點之一，已投入專用機台，進度優於預期，正與大型客戶合作開發矽光子用的 CW 光源；能不能用，要看元件表現能否和現有的 InP DFB 雷射匹配。5 月場說，已找到願意合作的下游代工廠（一般砷化鎵雷射廠），但還沒送片，年底能否量產要看客戶端的可靠度測試[[fugle-iet-20260312,fugle-iet-20260507]]。沒有客戶名稱和量產日期。

**聯亞賣給誰**。聯亞 2025 年營收 22.03 億元，中國佔 71.40%（2024 年 73.40%），美國從 9.43% 升到 21.46%，金額是 4.1 倍（計算）[[mops-landmark-ar2025-20260527]]。年報用的詞是「中國」，沒有拆中國公司和在中國設廠的外商。主要客戶只有代號：C06 佔 25.76%、C09 21.01%、C03 13.33%、C10 10.40%；C09 從 2024 年的 418 萬元跳到 2025 年 4.63 億元，C10 從 24 萬元跳到 2.29 億元，年報說增加的原因是「數據中心相關產品出貨成長」[[mops-landmark-ar2025-20260527]]。只有媒體說聯亞 2026 年「新增美系雲端客戶」，沒點名。

**月營收**。這些公司的營收大多來自插拔式光模組，沒有一家拆出 CPO：

| 公司 | 2026 年 9 月營收（百萬元） | 年增 |
|---|---|---|
| 聯亞 3081 | 540 | +190.2% |
| 全新 2455 | 449 | +29.5% |
| 英特磊 4971 | 108 | +11.4% |
| 光環 3234 | 121 | +140.3% |
| 華星光 4979 | 575 | +97.8% |
| 聯鈞 3450 | 1,289 | +99.8% |
| 立碁 8111 | 73 | +0.6% |
| 環宇-KY 4991 | 435 | +112.9% |

<p class="tag">出處：[[finmind-laser-tw-20261012]]</p>

## 公告看得到的擴產 {#las-capex}

公開資訊觀測站的「取得機器設備」公告能看到「誰向誰買了多少錢的機台」，但所有公告的用途都只寫「供生產用」之類，看不出是不是 CPO 機台[[mops-capex-20261012]]。而且資本額未達 100 億元的公司，一年內向同一家設備商累積買到 5 億元才要公告[[moj-asset-rule31-20261012]]。FAU 廠的公告情形見 [equipment-test.md](equipment-test.md#eq-mops)。

雷射這條線的台廠公告：

| 買方 | 公告日 | 賣方或內容 | 金額 |
|---|---|---|---|
| 聯亞 | 2026-06-17 | AIXTRON（德國，MOCVD 磊晶設備） | 約 8.37 億元 |
| 聯亞 | 2026-08-26 | AIXTRON | 約 9.9 億元 |
| 聯亞 | 2026-09-15 | 台灣艾司摩爾（ASML，曝光設備） | 約 5.35 億元 |
| 聯亞 | 2026-08-13、08-20 | 漢科系統、帆宣系統（廠務） | 12.26 億、5.57 億元 |
| 聯亞 | 2026-01-28／04-22／06-17／08-26 | 董事會購置機器設備投資案，「因應客戶訂單需求」 | 上限 7.07／13.15／30.09／22.7 億元，合計 73.01 億元（計算） |
| 全新 | 2026-07-30 | AIXTRON | 6.53 億元，平均每台 9,335 萬元，即 7 台（計算） |
| 聯鈞 | 2026-02-05 | Four Technos | 日幣 26.4 億（約 5.40 億元） |
| 聯鈞 | 2026-07-16 | Soliware Storage Technology | 美金 2,240 萬（約 7.02 億元） |
| 聯鈞 | 2026-10-08 | 2026、2027 年資本支出預算，全數買新增產能的機器設備 | 合計 32.4 億元 |
| 光環 | 2026-08-07 | 董事會：擴充產能的設備採購 | 上限 11.01 億元 |
| 華星光 | 2026-05-12 | 向亞帝歐光電買土地廠房 | 土地 6,280 m²、建物 12,022 m² |

<p class="tag">出處：[[mops-capex-20261012]]。聯鈞向 Four Technos、Soliware 買的是什麼，查不到。</p>

聯鈞 2026 年 8 月法說（第三方整理，不是原話）另說：計畫發行 30 億元可轉換公司債支應擴產；COSA 產能從 2024 年起預計每年翻倍[[fugle-unitedopto-20260818]]。

擺在一起比（各家口徑不同：聯亞是董事會核准的上限，聯鈞是預算，全新是實際交易，上詮是年報寫的現增資金用途）：

<div class="scroll">
<svg viewBox="0 0 1000 240" width="100%" style="max-width:1000px" role="img" aria-label="台廠公告的擴產金額">
<text class="item" x="390" y="38" text-anchor="end">聯亞：2026 年四次董事會購置設備上限合計</text>
<rect class="bar" x="400" y="24" width="460.0" height="20"/>
<text class="item" x="868.0" y="39">73.01 億元</text>
<text class="item" x="390" y="78" text-anchor="end">聯鈞：2026、2027 年資本支出預算</text>
<rect class="bar" x="400" y="64" width="204.1" height="20"/>
<text class="item" x="612.1" y="79">32.4 億元</text>
<text class="item" x="390" y="118" text-anchor="end">上詮：現增資金指定買 FAU 生產線</text>
<rect class="bar2" x="400" y="104" width="96.9" height="20"/>
<text class="item" x="504.9" y="119">15.38 億元</text>
<text class="item" x="390" y="158" text-anchor="end">光環：董事會設備採購上限</text>
<rect class="bar" x="400" y="144" width="69.4" height="20"/>
<text class="item" x="477.4" y="159">11.01 億元</text>
<text class="item" x="390" y="198" text-anchor="end">全新：向 AIXTRON 買 7 台磊晶機</text>
<rect class="bar" x="400" y="184" width="41.1" height="20"/>
<text class="item" x="449.1" y="199">6.53 億元</text>
<text class="note" x="400" y="14">單位：新台幣億元；深色＝雷射這條線，淺色＝FAU（對照）</text>
</svg>
</div>

<p class="tag">出處：[[mops-capex-20261012,foci-ar2025]]</p>

公告裡金額最大的光通訊資本支出在雷射這一層。上詮把現金增資的 15.38 億元指定買 FAU 高精密自動化生產線，是 FAU 這一側唯一有金額、有用途的一手數字[[foci-ar2025]]。

國外雷射和基板廠的擴產（前面各節已列，這裡彙整）：

| 公司 | 擴產 | 可信度 |
|---|---|---|
| JX 金屬 | InP 基板，四年最多 1,200 億日圓[[jx-inp-20260616]] | 一手 |
| 三菱電機 | EML，2025 年度決定 400 億日圓，2029 年度產能 3 倍以上[[melco-irday-semi-20260529]] | 公司說 |
| 古河電工 | DFB 雷射晶片新廠 380 億日圓，2028 年 4 月量產[[furukawa-dfb-plant-20251217]]；現有產能：DFB 2025 年度上半年末是 2023 年度的 5 倍，2026 年度再增到 2025 年度的 1.5 倍[[furukawa-q1fy26-qa-20260806]] | 一手 |
| 住友電工 | InP 基板約 180 億日圓（媒體引日經）[[trendforce-sumitomo-inp-20260713]] | 第三方 |
| Coherent | 德州 Sherman 6.5 億美元，晶圓產出 4 倍[[theregister-coherent-4x-20260617]]；InP 總產能目標一季一季往前拉（見下） | 媒體報；公司說 |
| Lumentum | 北卡新廠，2028 年初第一筆營收[[investing-lumentum-q4fy26-20260811]]；這是第五座 InP 廠，2026 年 3 月中買下，原本是砷化鎵廠，要改成 InP，既有機台大多沿用[[fool-lumentum-q3fy26-20260506]] | 公司說 |
| Broadcom | 美國、新加坡的 InP 廠（做 EML、CW、VCSEL）一年擴三倍以上，今年的產能已擴，未來兩年再大幅增加（Charlie Kawwas：「we're actually more than tripling them year-on-year」）[[webull-broadcom-q3fy26-20260903,fool-broadcom-q3fy26-20260909]] | 公司說 |
| AAOI | 2027 年中產能三倍；2027 年前雷射產能再擴約 350%；2027 年底前轉 6 吋（見下） | 公司說 |
| Sivers | 格拉斯哥 3,000 萬美元，年產超過 1 億顆[[sivers-glasgow-20260903]] | 一手 |
| 源杰 | 陝西新園區約 42.68 億人民幣[[cbn21-yuanjie-20260812]] | 媒體報 |
| IQE（英國磊晶廠） | 下半年把既有機台改做 InP；2026 上半年營收年增 43%，全年成長指引從 20% 以上調到 30% 以上[[semitoday-iqe-20260909]] | 媒體報（公司公告） |

### 各家目標一季一季怎麼改 {#las-capex-path}

擴產目標和時程不是一次講完，是每一季法說改一次。Motley Fool、Investing.com 的是法說會轉錄稿，AllMind 是 AI 轉寫稿。

**Coherent：InP 產能**

| 時間 | 目標 |
|---|---|
| 2025-11-05 | 「we expect to roughly double our total internal production capacity of indium phosphide over the next year」（一年內約翻倍）[[fool-coherent-q1fy26-20251106]] |
| 2026-02-04 | 近期目標是 2026 年底前產能翻倍，之後的目標「very aggressive」[[fool-coherent-q2fy26-20260204]] |
| 2026-05-06 | 「Looking into next calendar year, we expect to more than double indium phosphide capacity again—a quadrupling over a two-year period.」（明年再翻倍以上，兩年四倍）；宣布蘇黎世第三座 6 吋 InP 廠，2027 年初生產[[fool-coherent-fy26q3-20260506]] |
| 2026-08-12 | 6 月季的 InP 雷射比去年同期多約 80%（「about 80% more Indium Phosphide lasers」；轉錄稿有口誤重複「about 80」）[[allmind-coherent-q4fy26-20260812]] |

**Lumentum：超高功率雷射和 InP 廠**

| 時間 | 說了什麼 |
|---|---|
| 2026-02-03 | 追加訂單是「ultra-high-power lasers」，2027 年出貨；40% 擴產目標已前移完成一半以上[[fool-lumentum-q2fy26-20260203]] |
| 2026-05-05 | 「Our ultra-high-power laser chip manufacturing ramp for CPO applications is also proceeding according to plan」，上一季連續成長，2026 年 12 月季開始「meaningful revenue」，並如期履行排在 2027 年上半年的數億美元訂單；北卡 Greensboro 的 InP 廠「plans to convert the facility from gallium arsenide to indium phosphide are well underway」[[fool-lumentum-q3fy26-20260506]] |
| 2026-08-11 | 北卡首筆營收 2028 年初；分析師問能不能把 Greensboro 剩下的產能簽長約，執行長說在找，Greensboro 還有空間，也在和客戶談協助他們的雷射需求，「過幾季」會有新安排可談[[investing-lumentum-q4fy26-20260811]] |

**AAOI：雷射產能**

| 時間 | 目標 |
|---|---|
| 2025-11-07 | 現在做 3 吋，之後轉 4 吋[[allmind-aaoi-q3-20251107]] |
| 2026-02-26 | 「triple our production of indium phosphide related devices」，在 2027 年中以前（原話 by the middle part of next year）[[fool-aaoi-q4-20260226]] |
| 2026-05-07 | 「We expect to further expand our laser fabrication capacity by around 350% by 2027」；目標 2027 年底前轉 6 吋[[fool-aaoi-q1-20260507]] |
| 2026-08-06 | CPO 市場要的產能要比今天大 8–10 倍；從訂設備到高量生產至少 21–24 個月[[investing-aaoi-q2-20260806]] |

AAOI 2 月說三倍、5 月說再擴約 350%，兩次的基準沒有說明，轉錄稿也沒有說 350% 是增加還是變成。

**古河電工：DFB 雷射晶片的三個基準年**。2025 年 12 月的新廠公告是 2028 年 DFB 產能為 2025 年度的 5 倍以上[[furukawa-dfb-plant-20251217]]；2026 年 8 月說明會的說法是 2025 年度上半年末已是 2023 年度的 5 倍，2026 年度再增產到 2025 年度的 1.5 倍[[furukawa-q1fy26-qa-20260806]]。三個基準年（2023、2025 年度、2025 年度上半年末）不同，古河沒有給絕對數字，不能直接相乘或相加。

## 還不知道的 {#las-open}

日期都從 [calendar.md](calendar.md#cal-events) 的日曆抄來；「未公告」是查詢日（2026-10-12）官方還沒寫日期。

- **NVIDIA 的 CPO 雷射到底誰在供、Lumentum 第一張外部光源模組訂單的客戶是誰**：等 Lumentum FY27 第一季財報（11/05）和它的 10-Q 客戶集中度；NVIDIA 第三季財報（11 月中下旬，未公告）。
- **Lumentum 的泵浦雷射和 CPO 雷射搶不搶同一條產線**：Lumentum 11/05 法說。
- **Lumentum 北卡 Greensboro 的「新安排」是什麼**：8 月執行長說過幾季會有可談的新安排（和客戶談協助他們的雷射需求，是不是對外代工沒有講）；Lumentum 11/05 法說。
- **Coherent 2 月說的那張「超大 CPO 採購單」客戶是誰**：當時只說是一家領先的 AI 資料中心客戶，沒點名，也沒說和 3 月 NVIDIA 的投資是不是同一件事；Coherent 11 月初法說（未公告）。
- **AAOI 擔心的 2028、2029 年基板量有沒有長約**：AAOI 說庫存夠用到 2027 年底，後面的量沒有講；AAOI 下一場法說（日期沒查到）。
- **環宇-KY 的 100 mW CW 認證結果**：3 月、5 月、8 月三場的放量時間一路往後；環宇下一場法說（日期沒查到，今年是 3/4、5/5、8/5）。
- **華星光有沒有 300 mW 以上的 CPO 規格量產**：2025 年 12 月場說 70、100 mW 為主，200、400 mW 是後續開發；華星光下一場法說（最近一場是 2026-08-28，下一場日期沒查到）。
- **天孚說緩解的「相關物料」是哪些**：8 月、10 月的答覆沒點名；天孚下一份投資者關係活動記錄。
- **源杰、仕佳光子的 NPO 用 CW 光源規格什麼時候定案**：源杰 8 月說各家客戶功率要求不同、方案持續迭代；源杰三季報（10/31）之後的投資者關係活動記錄。
- **一台交換器裡雷射和 FAU 各值多少**：沒有同口徑的公開數字；Coherent 下一場法說（11 月初，未公告）看它「每顆 100T 晶片 1.5 萬美元」怎麼拆。
- **台積電說的「光纖連接器」包不包括 FAU、COUPE 背面整合光源有沒有時程**：台積電第三季法說（10/15）；之後 11 月的券商論壇簡報會上傳公開資訊觀測站。
- **AXT 的出口許可和北美營收**：AXT 第三季財報（10/29）。一篇作者文章說 AXT 6 月季北美營收只有 16.1 萬美元，10-Q 裡找不到這行。
- **中國國產 InP 基板能不能出口**：雲南鍺業三季報（10/21）。
- **中國 CW 雷射廠的出貨**：源杰三季報（10/31）。
- **住友電工「CPO 向け製品」是什麼、CPO 雷射的功率和客戶**：住友下一份決算說明會質疑應答（日期沒查到，從住友 IR 資料庫追）。
- **古河電工 16 通道 ELSFP 的客戶和時程**：古河下一場決算說明會（日期沒查到）；2026 年 6 月光事業說明會簡報。
- **古河電工 DFB 產能的絕對數字**：2026 年 8 月的原話把基準講清楚了（2025 年度上半年末是 2023 年度的 5 倍，2026 年度再 1.5 倍），但三個基準年（含新廠的 2028 年對 2025 年度）的實際顆數古河沒給；等古河下一場決算說明會。
- **聯亞的 C09、C10 是誰**：聯亞法說（去年同期是 10/29、11/25，今年還沒申報）；10、11、12 月營收（11/10、12/10、2027/1/10）。
- **三甲基銦管制對台灣磊晶廠有沒有影響**：三家年報和法說都沒提；聯亞、全新的下一場法說。
- **Nouryon 的亞洲分裝站在哪、凱信是不是它的代理**：查商工登記、三甲基銦的安全資料表。
- **InP 基板一年用掉多少銦**：沒有一手數字；那份券商報告原文找不到，晶圓尺寸和每片克數不明。
- **InP 基板 2024–2026 年的市佔**：目前所有說法都是 2020 年數字或沒出處；等研究機構的新版。
- **NVIDIA「少用 4 倍」的基準是哪種模組**：NVIDIA 原始投影片的註腳；GTC DC（11/30–12/3）、GTC 2027（2027/3/14–18）。
- **Broadcom 雷射模組的規格（幾顆、幾 mW、誰的晶片）、前五大材料供應商是不是基板廠**：Broadcom FY26 第四季財報和之後的 10-K（12 月中，未公告）。
- **Sivers 會不會成為第三家 CPO 雷射來源**：Sivers 第三季財報（11/26，日期未確認）。
- **Lumentum「DFB 加 SOA」是不是真的比 Coherent 多用近 10 倍晶圓面積**：只有作者文章；Lumentum 白皮書、OFC 論文。
- **不帶 TEC 的外部光源模組做不做得出來**：OIF ELSFP 規格、Lumentum 和 Coherent 產品頁。
- **scale-up 每顆 GPU 要幾個外部光源模組**：OCI 規格；OFC 2027（2027/3/7–11）。
- **Coherent 的 CPO 營收和客戶、FAU 說不說**：Coherent 12 月季法說（2027 年 2 月初）。
- **聯鈞向 Four Technos、Soliware 買了什麼**：聯鈞法說（去年同期 11/19，今年還沒申報）。
- **「中國拒絕日美企業八成 InP 基板申請」**：只有一家媒體，沒有出處；查中國商務部 2026 年 1 月公告原文。
