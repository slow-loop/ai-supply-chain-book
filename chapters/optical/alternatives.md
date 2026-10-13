# 插拔式的折衷：LPO、TRO、XPO、NPO

<p class="src">2026-10-12。CPO 筆記的一份：CPO 以外，插拔式光模組這一邊也在變。這份把中間的幾種做法一次講清楚：拿掉 DSP 的 LPO、只拿掉一半的 TRO、Arista 的 XPO、光引擎插在晶片旁插座上的 NPO，以及各種規格組織、DSP 缺貨、雲端大廠的態度。CPO 本身是什麼、為什麼要搬到晶片旁，見 <a href="basics.md#q3">CPO 怎麼解決</a>。句尾小數字是出處，文末每條標了可信度。</p>

## 先看全貌：幾種做法差在哪 {#alt-overview}

光模組要做的事只有一件：把交換器晶片送出來的電訊號變成光，送進光纖。各種做法的差別在三件事：**光引擎離晶片多遠**（也就是電要走的銅線多長）、**模組裡還有沒有 DSP**（數位訊號處理晶片，負責把跑長銅線跑髒的訊號整理乾淨，見 [光怎麼接到晶片](basics.md#q2)）、**壞了能不能拔下來換**。越靠近晶片越省電，但越難做、越難修。光引擎一步步靠近晶片的剖面圖在 [從插拔式到 CPO 的階段](basics.md#q4)；這裡把每一種做法的狀態並排。

| 做法 | 光引擎在哪 | 晶片到光引擎的電路 | DSP | 壞了怎麼換 | 現況 | 誰在推 |
|---|---|---|---|---|---|---|
| 插拔式（FRO，收發兩端都有 DSP） | 前面板的光模組裡 | 15–30 公分電路板[[semianalysis-cpo-book]] | 收、發都有[[nvidia-sn6000-manual-20260916]] | 整支拔[[tomshardware-npo-20260813]] | 800G 產品約 95% 是這種[[fundaai-cioe-20260916]] | 所有模組廠 |
| TRO／LRO（只留發射端 DSP） | 同上 | 同上 | 只有發射端[[nvidia-sn6000-manual-20260916,ieee-eps-lpo-202603]] | 整支拔 | NVIDIA SN6600-LD 可選用[[nvidia-sn6000-manual-20260916]]；1.6T 這代被認為比 LPO 可行[[ieee-eps-lpo-202603]] | NVIDIA（TRO）、Marvell（Ara T）、Credo（LRO）[[marvell-blog-arat-2026,fundaai-cioe-20260916]] |
| LPO（整顆 DSP 拿掉） | 同上 | 同上，由晶片的 SerDes 直接驅動[[synopsys-224g-lpo-2025q1]] | 沒有 | 整支拔 | 800G 約 5%[[fundaai-cioe-20260916]]；部署仍有限[[gazettabyte-ofc2026-lpo-20260409]] | Arista、Cisco、Juniper（交換器）；MACOM、Semtech、MaxLinear（晶片）[[ieee-eps-lpo-202603]] |
| XPO | **還是前面板的模組裡**，一個模組 12.8T，中間夾液冷板[[arista-xpo-whitepaper-202603]] | 同上 | 線性、半 retimed、全 retimed 都支援[[arista-pr-xpo-20260311]] | 整支拔，熱插拔[[arista-xpo-whitepaper-202603]] | 預計 2027 年量產[[nextplatform-xpo-20260417,cninfo-innolight-irm-20260823]] | Arista 主導；Microsoft、Marvell、Broadcom、Ciena 創始[[nextplatform-xpo-20260417]] |
| OBO（板上光學） | 機殼內主機板上[[semianalysis-cpo-book]] | 比插拔式短 | — | — | 停在概念驗證（製圖者註）[[technews-sipho-20260317]] | — |
| NPO（近封裝） | 晶片旁另一片基板，插在插座上[[semianalysis-cpo-book]] | 一段短銅線[[semianalysis-cpo-book]] | 可以拿掉[[tomshardware-npo-20260813]] | 光引擎可以拔換[[semianalysis-cpo-book]] | 多家模組廠說 2027 年開始交、2028 年放量[[cninfo-innolight-irm-20260728,cninfo-eoptolink-irm-20260912]]；華工科技說 2026 年已有訂單、小批交付（「批量」的定義不同，見 [各家的口風](#alt-npo-wording)）[[cninfo-hgtech-irm-20260827]] | Broadcom、Marvell、中際旭創、新易盛、光迅、Coherent、Ranovus、華為、阿里、騰訊 |
| CPO（同一片封裝基板） | 和交換晶片同一片封裝基板[[bnext-coupe-20260521]] | 幾毫米[[nvidia-qx800-datasheet-20260911]] | 不需要[[semianalysis-cpo-book]] | 光引擎焊死；光纖接頭、雷射模組可拔[[nvidia-blog-20260106,tomshardware-npo-20260813]] | NVIDIA、Broadcom 的 CPO 交換器已出貨[[tomshardware-npo-20260813]] | NVIDIA、Broadcom |
| CPO（中介層上） | 和運算晶片同一片中介層[[semianalysis-cpo-book]] | 更短 | 不需要 | 不能單獨換光引擎 | 台積電「探索中」[[semianalysis-cpo-book]]；供應鏈預估 2028 年以後[[tianxia-coupe-20260818]] | 台積電 |

表上看不到、但這幾輪查到之後要改的看法，在下面各節展開：

- **XPO 不是 CPO。** 原本的筆記把它寫成「可插拔式 CPO 構想」、結構查不到；Arista 的白皮書寫得很清楚，它是插在前面板的大號光模組，光引擎還在模組裡（[XPO](#alt-xpo)）。
- **「CPO 比插拔式省 70%」是只算光學那一段的說法。** 同一顆晶片的整台機器，CPO 比兩端都有 DSP 的插拔式少約 41%，比只留發射端 DSP 的插拔式少約 30%（[整台耗電](#alt-power)）。
- **雲端大廠近期被描述為先上 NPO。** Meta、Microsoft、Oracle、阿里、騰訊都有人這樣說；Google 被描述為最不願意上 CPO（[雲端大廠](#alt-buyers)）。
- **NPO 的規格都沒有規定 FAU。** 兩份最主要的開放規格（Open CPX、OCI）都沒寫光纖怎麼貼到光晶片，也就是沒有規定 FAU（光纖陣列單元），光纖貼合留給模組廠自己做，不經過台積電 COUPE 那條供應鏈（[規格](#alt-specs)）。
- **DSP 缺貨推的是 TRO、LPO 和第二供應商，沒查到有人說因此改買 CPO**；而且拿掉 DSP 之後，TIA、驅動 IC 也在缺（[DSP 缺貨](#alt-dsp)）。

## 同一顆晶片，CPO 整台比插拔式省多少電？ {#alt-power}

**最好懂的比法是同一顆晶片、同樣散熱、整台機器。**目前查到的這種數字只有 NVIDIA 一家。它的 Spectrum-6 交換晶片（102.4 Tb/s）同時有插拔式和 CPO 兩種機器，都是液冷：插拔式 SN6600-LD 裝 FRO 模組（收發兩端都有 DSP）時典型功耗 3.3 kW，裝 TRO 模組（只有發射端有 DSP）時 2.79 kW；CPO 版 SN6810-LD 典型 1.96 kW、最大 2.2 kW[[nvidia-sn6000-manual-20260916]]。計算：（3.3 − 1.96）÷ 3.3 ≈ 41%，（2.79 − 1.96）÷ 2.79 ≈ 30%。手冊沒寫插拔式是裝了幾支、哪一家的模組。氣冷的插拔式 SN6600 更高：3.94 kW（FRO）、3.2 kW（TRO）[[nvidia-sn6000-manual-20260916]]。

<figure>
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
<figcaption>整台交換器的典型功耗，單位 kW。數據來自手冊，圖自己畫。[[nvidia-sn6000-manual-20260916]]</figcaption>
</figure>

**為什麼會看到「省 70%」和「省 40%」兩種數字？**因為量的範圍不一樣。「70%」是只算光學那一段：Broadcom 說它第三代 CPO（Tomahawk 6 搭 Davisson 光引擎）每個 800G 埠約 3.5 W，比插拔式少 70% 以上[[nextplatform-broadcom-cpo-20251017,broadcom-davisson-briefing-202510]]。整台機器還有交換晶片、風扇、電源，這些不會因為換成 CPO 就變少，所以百分比會往下掉。唯一給出整台百分比的是一家用 Broadcom 上一代 CPO（Bailly）做 51.2T 交換器的公司：比插拔式交換器省 40% 以上；同一篇報導列了 Broadcom 說 Bailly 的光互連省 70%，兩個數字並列在一起[[convergedigest-micas-cpo-2025]]。Cisco、Celestica、Arista 的 CPO 整機功耗查不到。

Broadcom 三代 CPO 的每埠數字可以看出光學那一段降了多少：

| 世代 | 每個 800G 埠 | 對照 |
|---|---|---|
| Tomahawk 4 CPO | 約 6.4 W | 同一台用插拔式約 16–18 W[[nextplatform-broadcom-cpo-20251017]] |
| Tomahawk 5 Bailly | 5.5 W | Meta 量測：光引擎加雷射約 5.4 W，800G 2xFR4 插拔式約 15 W，省 65%[[nextplatform-broadcom-cpo-20251017,semianalysis-cpo-book]] |
| Tomahawk 6 Davisson | 約 3.5 W | 比上一代 CPO 少 36.4%，比插拔式少 70% 以上[[nextplatform-broadcom-cpo-20251017]] |

各家自己公布的效果，比較基準都不一樣，下面並排列出，不能直接互相比：

| 誰 | 比的是什麼 | 數字 |
|---|---|---|
| NVIDIA（手冊） | 同一顆 Spectrum-6，整台 CPO 對插拔式 | 1.96 kW 對 3.3 kW（FRO）／2.79 kW（TRO）[[nvidia-sn6000-manual-20260916]] |
| NVIDIA | Spectrum-X 光子交換器，每個 1.6T 埠對插拔式 | 少到五分之一[[nvidia-blog-20260106]] |
| NVIDIA | 光子交換器對傳統做法：能效、訊號品質、雷射數 | 能效 3.5 倍、訊號品質 63 倍、雷射少 4 倍[[nvidia-pr-20250318,nvidia-blog-20250826]] |
| NVIDIA | 光網路耗電、雷射數、MTBI（平均中斷間隔） | 耗電最多降 5 倍、雷射少 4 倍、MTBI 高 10 倍[[convergedigest-shainer-hoti-202608]] |
| NVIDIA | Q3450-LD 晶片到光的電訊號損耗 | 約 4 dB 對插拔式 22 dB[[nvidia-qx800-datasheet-20260911]] |
| 台積電 | COUPE 放在封裝基板上對電路板上的插拔式 | 能效 2 倍、延遲少 10 倍[[tsmc-pr-20260422]] |
| Broadcom | Davisson 每個 800G 埠 | 約 3.5 W，比插拔式少 70% 以上[[nextplatform-broadcom-cpo-20251017,broadcom-pr-20251008]] |
| 一家交換器廠 | Bailly 51.2T 整台對插拔式整台 | 省 40% 以上[[convergedigest-micas-cpo-2025]] |
| 研究機構估計 | 每 800G：Q3450 光引擎加外部雷射對 800G DR4 模組 | 約 4–5 W 對 16–17 W（少 73%）[[semianalysis-cpo-book]] |
| 媒體報導 | NVIDIA 給的 1.6T 一條連線 | 約 30 W 降到 9 W[[tomshardware-npo-20260813]] |

**拿 LPO 來比，差距又更小。**LPO（下一節）自己就宣稱模組耗電比有 DSP 的模組少 50–60%[[cisco-pr-g300-lpo-20260210,arista-pr-7060xe7-20260609]]。一篇報導寫 LPO 每 800G 約 10 W，CPO 每 100G 通道再比 LPO 少 35%[[nextplatform-broadcom-cpo-20251017]]；另一篇報導寫 800G LPO 約 7 到 8.5 W[[tomshardware-npo-20260813]]，兩個數字對不上，並列。Arista 創辦人 Bechtolsheim 在 2024 年算過一座 10 萬顆 XPU（每顆 4 kW）的叢集，光模組要多少電：

<figure>
<svg viewBox="0 0 820 230" width="100%" role="img" aria-label="十萬顆 XPU 叢集的光模組耗電，三種做法">
<line class="grid" x1="250" y1="8" x2="250" y2="190"/>
<text class="item" x="10" y="38">XPU 本身（對照）</text>
<rect class="box" x="250" y="18" width="460" height="30"/>
<text class="item" x="720" y="38">400 MW</text>
<text class="item" x="10" y="88">插拔式光模組（640 萬支）</text>
<rect class="bar2" x="250" y="68" width="221" height="30"/>
<text class="item" x="481" y="88">192 MW</text>
<text class="item" x="10" y="138">LPO</text>
<rect class="bar2" x="250" y="118" width="74" height="30"/>
<text class="item" x="334" y="138">64 MW</text>
<text class="item" x="10" y="188">CPO</text>
<rect class="bar" x="250" y="168" width="48" height="30"/>
<text class="item" x="308" y="188">42 MW（XPU 的 10.5%）</text>
<text class="note" x="10" y="220">2024 年的試算：10 萬顆 XPU、每顆 4 kW。只算把 XPU 連起來的光學，不含交換晶片。</text>
</svg>
<figcaption>十萬顆 XPU 叢集裡光學的耗電，三種做法。數字來自報導轉述的試算，圖自己畫，長度照數字比例。[[nextplatform-broadcom-cpo-20251017]]</figcaption>
</figure>

**放到整座叢集，比例更小。**網路只佔一座 AI 叢集總耗電的約 9%（三層網路），所以一家研究機構估計，scale-out 網路全面改用 CPO，網路耗電少 23% 到 48%（看能不能從三層減成兩層），整座叢集只少 2% 到 4%[[semianalysis-cpo-book]]。XPO 這種新外形則是另一個方向：它不省電，省的是機櫃空間，見 [XPO](#alt-xpo)。

## 拿掉 DSP：LPO、TRO {#alt-lpo}

**先看圖。**下面三張是同一個畫法：上半是剖面（左邊是插在前面板的光模組，右邊是交換器晶片 ASIC），下半是方塊圖。第一張是一般模組，中間夾一顆收發兩用的 DSP；第二張是 LPO，DSP 整顆拿掉，模組裡只剩驅動器（Driver）和線性的 TIA（轉阻放大器，把光偵測器的微弱電流放大成電壓），訊號由交換晶片自己的 SerDes 直接推；第三張是 LRO，只在發射那條路上留 DSP，接收那條路拿掉。

![一般插拔式模組：收發兩端都有 DSP（圖中 DSP (Tx/Rx)）。紅線是光纖，藍色虛線是從模組到交換晶片的電路。[[ieee-eps-lpo-202603]]](img/explain/ieee-eps-lpo-overview-fig1-pluggable-dsp-202603.png) ![LPO：DSP 拿掉，模組裡換成驅動器加 CTLE（一種簡單的類比等化）和線性 TIA，等化工作交給交換晶片的 SerDes。[[ieee-eps-lpo-202603]]](img/explain/ieee-eps-lpo-overview-fig2-lpo-202603.png) ![LRO（NVIDIA、Marvell 叫 TRO）：只在發射路徑留 DSP（DSP (TX Path Only)），接收端直接把 TIA 的輸出送回交換晶片。[[ieee-eps-lpo-202603]]](img/explain/ieee-eps-lpo-overview-fig3-lro-202603.png)

### LPO 是什麼

**LPO**（Linear Pluggable Optics，線性驅動插拔式模組）把模組裡的 DSP 整顆拿掉，由交換器晶片自己的 SerDes 直接驅動模組裡的雷射驅動器和接收端[[semianalysis-cpo-book,synopsys-224g-lpo-2025q1]]。訊號整理的工作被拆給交換晶片、驅動 IC 和 TIA[[ieee-eps-lpo-202603]]。光引擎還是在前面板的模組裡，所以晶片到模組那 15–30 公分的銅線還在，CPO 縮短銅線的好處它拿不到；它省的是 DSP 本身那一份電。

![上：一般光模組，交換器晶片和雷射之間夾一顆 PAM-4 DSP 重新整理訊號；下：線性直驅（LPO 的做法），DSP 拿掉，交換器晶片的 SerDes 直接把訊號推到模組裡的驅動器（DRV）和雷射。TIA 是接收端放大器，PD 是光偵測器。廠商技術文章的圖。[[synopsys-224g-lpo-2025q1]]](img/vendor/synopsys-retimed-vs-linear-drive-2025Q1-02.png){.s}

省多少：Cisco 說它的 800G LPO 模組比有 DSP 的模組少 50%[[cisco-pr-g300-lpo-20260210]]；Arista 說它的 Tomahawk 6 交換器（7060XE7，102.4T）用 LPO 讓互連耗電少約 60%[[arista-pr-7060xe7-20260609]]；Bechtolsheim 說 LPO、LRO 比有 DSP 的設計省 30–65%[[convergedigest-bechtolsheim-20251104]]。一家研究機構估計，叢集的後端網路從 DSP 模組換成 LPO，光模組耗電少 36%、網路總耗電少 16%[[semianalysis-cpo-book]]。

### LPO 普及了嗎

**沒有。**Marvell 說它目前 800G 產品約 95% 是兩端都有 DSP 的 FRO，LPO 約 5%[[fundaai-cioe-20260916]]。研究機構在 OFC 2026（2026 年 3 月的光通訊大會）後說 LPO 部署仍有限[[gazettabyte-ofc2026-lpo-20260409]]。一篇 2026 年 3 月的業界綜述說，一般看法是 LPO 在 800G 只會佔一小塊，因為資料中心已經照有 DSP 的模組設計好了；Juniper、Arista 的交換器支援 LPO，但部署「仍在起步」[[ieee-eps-lpo-202603]]。Bechtolsheim 在 2025 年 11 月說，當時出貨的光學 99.9% 還是插拔式[[convergedigest-bechtolsheim-20251104]]。

做 DSP 的 MaxLinear 在 2026 年 1 月的法說（法說會轉錄稿）上對 LPO 的評價更直接：整個市場「仍是插拔式市場」，LPO 的部署目前「很小眾」（very nichey），他把 LPO 看成市場裡很小的一部分，而且不是長期的[[fool-maxlinear-q4-20260130]]。

有在推的：交換器端是 Arista、Cisco、Juniper，晶片端是 MACOM、Semtech、MaxLinear[[ieee-eps-lpo-202603]]；模組廠新易盛說 LPO 與客戶合作進展順利[[cninfo-eoptolink-irm-20260912,fundaai-cioe-20260916]]。Arista 的 1.6T 新平台新聞稿裡，Meta、Microsoft、Oracle 的主管都有背書，但引言講的是 1.6T 平台和液冷，沒有提 LPO 本身[[arista-pr-7060xe7-20260609]]。

### LPO 卡在哪

- **互通。**早期 LPO 要在模組和交換器埠之間手動調參數，抵掉了效率的好處；很多早期產品過不了模組輸入端（TP2）的光功率和消光比規格；損耗高的埠還要在 TIA 端再做等化[[lightwave-lpo-20250722]]。不過 LPO 的多源協議（MSA）已有超過 49 家公司，2025 年初約 90 人參加的互通測試，「幾乎所有連線一接上就通」[[lightwave-lpo-20250722]]。
- **看不到狀況。**沒有 DSP 之後，雲端業者能拿到的診斷資訊比有 DSP 的模組少[[lightwave-lpo-20250722]]。
- **速度越高越難。**距離較短、標準還不完整、對交換晶片的 SerDes 要求更高，和 200G SerDes 相容「很難」[[ieee-eps-lpo-202603]]。1.6T 的 LPO 在 Arista 實驗室表現乾淨，但晶片封裝的反射需要更好的跨接線（flyover）或直接接封裝[[convergedigest-bechtolsheim-20251104]]。
- **DSP 市場被切開，不是消失。**短距、受控的機櫃內連線可以用 LPO；長距、環境複雜、相干光（長途用的那種）仍要 DSP[[yole-transceivers-20260506]]。

一位研究者認為 CPO 和 LPO 會依應用並存，比例大約 60/40 偏 CPO，她自己說這是猜的[[tomshardware-optical-battle-20260723]]。

### TRO／LRO：只拿掉一半

**只在發射端留 DSP，接收端拿掉。**NVIDIA、Marvell 叫它 TRO（Transmit Retimed Optics），Credo 和業界綜述叫它 LRO（Linear Receive Optics），兩端都有 DSP 的叫 FRO[[nvidia-sn6000-manual-20260916,marvell-blog-arat-2026,ieee-eps-lpo-202603]]。發射端還是照 IEEE 802.3 的標準送訊號，所以距離比 LPO 長、互通比較好，代價是比 LPO 耗電[[ieee-eps-lpo-202603]]。

| | 說法 |
|---|---|
| 為什麼 1.6T 這代改推 TRO | 1.6T 的初期 LPO 方案要 30 W 以上，散熱很難；LRO 有機會壓到 20 W 以下。OFC 上每一家展示 1.6T LPO 的公司也都有 LRO[[ieee-eps-lpo-202603]] |
| 整台差多少 | 同一台 SN6600-LD，裝 TRO 比裝 FRO 少約 0.5 kW（3.3 → 2.79 kW）[[nvidia-sn6000-manual-20260916]] |
| 模組差多少 | Marvell 說它的 Ara T（「第一顆 1.6T 只做發射的 DSP」，5–500 公尺）讓模組耗電少 35% 以上；Lumentum 展示 1.6T TRO 模組約 16 W[[marvell-blog-arat-2026]] |
| 什麼時候 | Marvell 的 Ara T 等 1.6T DSP 2026 年第一季開始送樣[[marvell-pr-16t-dsp-202603]]；研究機構說 1.6T LRO 今年可能部署較多[[gazettabyte-ofc2026-lpo-20260409]] |
| 誰做 | NVIDIA（TRO 模組）、Marvell（Ara T）、Credo（1.6T LRO 仍用自家 3 奈米 DSP）[[nvidia-sn6000-manual-20260916,marvell-blog-arat-2026,fundaai-cioe-20260916]] |

## XPO：插拔式的大號版 {#alt-xpo}

**XPO 是插在前面板的光模組，不是 CPO。**原本的筆記照一篇論壇報導寫成「可插拔式 CPO 構想」、結構查不到[[technews-trendforce-forum-20260529]]；後來找到 Arista 的白皮書，結構寫得很清楚：一個 XPO 模組 12.8 Tb/s、64 條 200G 電通道，外型 60.8 × 111.8 × 21.3 mm，大約是現在 OSFP 模組的 2.7 倍寬、頻寬 8 倍。模組裡是兩片各 32 通道的電路板（paddle card，模組裡插進交換器的那片板子），腹對腹夾住中間一塊液冷冷板，發熱元件朝內貼著冷板；冷板可以帶走 400 W 以上[[arista-xpo-whitepaper-202603]]。光纖接頭在前端，用 MPO-16[[arista-xpo-whitepaper-202603]]。

![XPO 的爆炸圖：上下兩片電路板（Paddle Card-1、-2）中間夾冷板（Cold Plate），後面接液冷進出口（Liquid Inlet/Outlet）和 48V 電源卡，前端是光纖接頭（Optical Connectors）。廠商白皮書的渲染圖。[[arista-xpo-whitepaper-202603]]](img/vendor/arista-xpo-whitepaper-exploded-view-p4-202603.png) ![左：一個 XPO 模組；右：八個 OSFP 模組。一個 XPO 的頻寬等於八個 OSFP。廠商白皮書的渲染圖。[[arista-xpo-whitepaper-202603]]](img/vendor/arista-xpo-vs-8x-osfp-whitepaper-p3-202603.png)

| 項目 | XPO | 對照 |
|---|---|---|
| 每個模組頻寬 | 12.8 Tb/s，64 × 200G[[arista-xpo-whitepaper-202603]] | 1.6T OSFP 的 8 倍 |
| 前面板密度 | 一個機架單位（1OU）可放 204.8 Tb/s[[arista-xpo-whitepaper-202603]] | OSFP 的 4 倍 |
| 散熱 | 液冷冷板，400 W 以上；液冷快接頭可插拔 500 次[[arista-xpo-whitepaper-202603]] | 液冷的 12.8T ZR 模組約 45°C，氣冷 1.6T OSFP-ZR 約 65–70°C[[nextplatform-xpo-20260417]] |
| 供電 | 直接吃機櫃匯流排 46–53 V，模組內自己降到 3.3 V[[arista-xpo-whitepaper-202603]] | |
| DSP | 線性、半 retimed、全 retimed 三種都支援[[arista-pr-xpo-20260311,marvell-blog-xpo-20260316]] | |
| 電通道速度 | 目前 200G；400G（25.6T）在路線圖上[[arista-xpo-whitepaper-202603]] | 研究機構希望看到 400G[[gazettabyte-ofc2026-lpo-20260409]] |
| 光纖接頭 | MPO-16[[arista-xpo-whitepaper-202603]] | |

**裡面有幾個光引擎、用不用 DSP？**中文媒體寫一個 XPO 裡整合 8 個 1.6T 光引擎，配高頻寬的 EML（一種雷射）可以做到不用 DSP[[stockstar-xpo-20260414]]；中際旭創的 XPO 型號寫「12.8T 8×DR8」[[hkex-innolight-prospectus-20260722]]。Arista 白皮書說它的電通道乾淨，適合 LPO，可以少用 DSP[[arista-xpo-whitepaper-202603]]。Bechtolsheim 說 XPO 用的是現有晶片和電路板設計：兩個 OSFP 的電路板並排、再上下對疊，就是 8 倍通道[[nextplatform-xpo-20260417]]。**模組裡的光引擎用不用 FAU、誰供，查不到**；XPO 官網只有一頁標題，沒有公開規格書[[nextplatform-xpo-20260417]]。如果裡面是矽光子引擎，就要光纖貼合，那這塊 FAU 的需求會落在模組廠手上，見 [不經過 COUPE 的路](fau-makers.md#fau-routes)。

**省電嗎？大致打平，省的是空間。**Bechtolsheim 舉例：512 顆 XPU 用 1.6T OSFP 交換器，要 4 櫃運算加 8 櫃網路；換成 XPO，網路只要 2 櫃，12 櫃變 6 櫃。網路櫃更熱、但數量更少，電「大致打平」[[nextplatform-xpo-20260417]]。白皮書的機櫃表：OSFP 交換器櫃 1.6 Pb/s、32 kW，XPO 交換器櫃 6.5 Pb/s、128 kW[[arista-xpo-whitepaper-202603]]。計算：32,000 W ÷ 1,600 Tb/s = 20 W／Tb/s；128,000 W ÷ 6,500 Tb/s ≈ 19.7 W／Tb/s，每單位頻寬的耗電幾乎一樣。

**Arista 為什麼不做 CPO。**白皮書說 CPO 和板上光學在現場維修、擴充、製造上有重大挑戰，難以在雲端大規模部署[[arista-xpo-whitepaper-202603]]；一篇分析轉述 Arista 的說法，CPO 模組「因為每個模組裡光纖對位很精細」而極難製造[[futuriom-arista-xpo-202603]]。換句話說，Arista 的理由正好落在 FAU 這一段；它的解法是把光引擎和光纖貼合留在前面板模組裡。Bechtolsheim 說他們對任何技術「都不是宗教信仰」，唯一堅持的是能大量出貨；超過 20 家廠商會做 XPO 模組，預計 2027 年量產；這件事是「一家大客戶推動的」，沒點名[[nextplatform-xpo-20260417]]。

**誰加入。**

| | 名單 |
|---|---|
| 創始 | Arista、Microsoft、Marvell、Broadcom、Ciena；一個月內超過 100 家；Google 不在名單上[[nextplatform-xpo-20260417]] |
| Microsoft | 主管在新聞稿說相信這個規格能成為被廣泛採用的外形，把插拔式的好處延伸到 scale-out 和 scale-up[[arista-pr-xpo-20260311]] |
| 也做 CPO 的 | Coherent（創始成員，OFC 展示 12.8T XPO）[[coherent-pr-ofc2026-20260317]]；Lightmatter（創始成員）[[networkworld-arista-xpo-202603]] |
| 中國模組廠 | 中際旭創（經新加坡子公司 TeraHop）、新易盛、華工正源、光迅、聯特都是創始成員；華工正源 OFC 首日發表 12.8T XPO[[stockstar-xpo-20260414]]；光迅 OFC 展示 12.8T XPO[[c114-accelink-ofc2026-20260320]] |
| 台灣 | 只看到鴻海系：Foxconn 是公開確認的成員[[sixrackunits-xpo-20260401]]；鴻騰精密說聯盟成員包括鴻騰、中際旭創、Coherent[[technews-trendforce-forum-20260529]] |
| 時程 | 中際旭創說 2.4T、NPO、XPO 依大客戶要求在開發或送樣，2027 下半年量產、2028 更大規模[[cninfo-innolight-irm-20260823]]；新易盛說它的 XPO 突破了「雙 PCB 加液冷整合」的封裝，「為未來 CPO/NPO 奠定基礎」[[cninfo-eoptolink-ar2025-20260424]] |

一篇中文報導說，XPO 用的 EML 雷射、CPC 線纜連接器、液冷件中國都能量產[[stockstar-xpo-20260414]]。官方成員名單抓不到。

## NPO 是什麼、誰在推 {#alt-npo}

**NPO**（Near-Packaged Optics，近封裝光學）把光引擎從前面板搬到交換晶片或運算晶片旁邊的另一片基板上，插在插座（socket）裡；晶片和光引擎之間還有一段短銅線[[semianalysis-cpo-book]]。因為夠近，模組裡的 DSP 可以拿掉；因為是插座式，光引擎壞了能在現場換，焊在 CPO 封裝基板上的光引擎就不行[[tomshardware-npo-20260813]]。比它更早的一種叫 OBO（板上光學），光引擎放在機殼內的主機板上，一家研究機構說它「兩邊的缺點都有」：有 CPO 的複雜，又留著插拔式的限制[[semianalysis-cpo-book]]。

界線不總是很清楚。NVIDIA 的 Quantum-X 交換器把光引擎裝在可拆的光學子模組上，雷射模組可以從面板抽出來，一家研究機構說嚴格一點的人會把它算成 NPO；NVIDIA 自己稱它為 CPO[[semianalysis-cpo-book,tomshardware-npo-20260813]]。下一節的 Open CPX 規格也一樣：同一種插座式模組，插座焊在交換晶片的封裝基板上就算 CPO，焊在主機板上就算 NPO[[opencpx-spec-v1-20260916]]。

### 誰有產品

| 誰 | 產品、說法 |
|---|---|
| Broadcom | OFC 2026 列出 3.2T、用 VCSEL（從晶片表面發光的小雷射，配多模光纖）的 NPO，和它的 CPO 交換器並行[[broadcom-pr-ofc2026-20260312,tomshardware-npo-20260813]] |
| Marvell | 「除了 CPO，我們的 NPO 方案也在多家客戶強勁採用」；參與方式有兩種：賣 NPO 用的 TIA／驅動 IC（市佔高），和自家開發多年的 NPO 光引擎；沒點名客戶[[bullfincher-marvell-fy27q2-20260827]]。第三代 6.4T 光引擎「與多家 tier 1 客戶深度接洽」，NPO 和 CPO 兩種做法都做[[fool-marvell-q1-20260527]]。scale-up 光學的數字一路上調，見 [Marvell 說的數字](players.md#pl-marvell)。8 月的法說上，Marvell 把步調講成：CPO 是重要的一塊，但「現在步調快得多的是 NPO」；10 月投資人日（YouTube 自動字幕）說 NPO「會上量」、CPO 仍在進行，不是一個起來另一個就掉下去，NPO 是替多數客戶最終走向 CPO 鋪路的一列火車；客戶選 NPO 的理由是光學可現場更換、故障影響範圍小、可重新配置，Marvell 對兩種都開放[[allmind-marvell-q2-20260827,youtube-marvell-investor-day-20261006]] |
| 中際旭創 | OFC 2026 展示「6.4T-4xDR8 可插拔 NPO 模組」[[hkex-innolight-prospectus-20260722]]；2027 下半年「行業內兩個有影響力的重點客戶」開始批量採購 NPO，更大上量在 2028 年[[cninfo-innolight-irm-20260728]]；預計是第一批交付 NPO 的供應商[[cninfo-innolight-irm-20260712]]；NPO 新產能更多放海外[[cninfo-innolight-irm-20260823]]；2025 年 10 月到 2026 年 7 月的說法怎麼變，見 [各家的口風](#alt-npo-wording) |
| 新易盛 | OFC 2026 發表 6.4T NPO（32 × 200G，矽光子），新聞稿沒有功耗數字[[eoptolink-pr-npo-20260313]]；2027 年開始交付、2028 年規模化，「預計將成為公司主要產品之一」[[cninfo-eoptolink-irm-20260912,p5w-eoptolink-collective-20260911]]；7 月的版本限定「2027 年下半年」，見 [各家的口風](#alt-npo-wording) |
| 光迅 | OFC 2026 展示 3.2T NPO、6.4T 矽光 NPO、3.2T VCSEL NPO[[c114-accelink-ofc2026-20260320]]；2026-05-14 業績說明會上公司說，這款 3.2T 矽光單模 NPO 模組「已在國內頭部 CSP 廠商完成全系列驗證」，同一場後面另一則答覆寫成「完成系統驗證」；兩個說法並排，沒說客戶是誰[[p5w-accelink-results-20260514]] |
| 華工科技 | 2026-03：「3.2T NPO 產品 2026 年已有在手訂單，目前正進行交付，與頭部廠商及交換機芯片廠商合作，今年將實現批量，明年爭取更大規模訂單交付」[[cninfo-hgtech-irm-20260326]]。2026-08：NPO「目前與國內外多家頭部 AI 廠商小批交付和細化確定最終方案」；3.2T／6.4T NPO 在國內外頭部 AI 廠商測試中；光引擎（OE）用自研矽光，OE 加外置光源模組（ELSP）「已準備就緒，正在拉動小批量試製線」，2.5D／3D 先進封裝向外部封裝廠找合作、同步啟動產能擴充[[cninfo-hgtech-irm-20260827]]。兩次說法的差別見 [各家的口風](#alt-npo-wording) |
| 天孚通信 | 2026-07-09：「具備 NPO 各相關產品的技術和能力，目前正在配合多個客戶進行配套產品研發」；沒說是哪些產品、哪些客戶[[cninfo-tfc-irm-20260709]] |
| 意法半導體 | 2026-04-23 法說問答，執行長講到光纜與近封裝／共封裝光學這一塊：「主要推手之一會是 AWS」，但意法要提供產品和方案的對象「遠不只 AWS」；沒說是 NPO 還是 CPO、沒說數量（AI 轉寫稿，句子不順）[[allmind-st-q1-20260423]]。同一場他也說意法是「唯一能在 12 吋晶圓上提供矽光技術」的公司，近封裝和共封裝光學「可能比預期更快」[[allmind-st-q1-20260423]]。7 月第二季法說上，光連接的內容是 800G／1.6T 插拔式，沒有再提 AWS 或近封裝[[webull-st-q2-202607]] |
| Astera Labs | scale-up 交換器晶片廠。2025 年 10 月宣布收購光纖與晶片耦合公司（見 [新創](players.md#q19)）。時程說法三次：2025-11 財務長說 scale-up 光學連接「最早在 2028、2029 年」；2026-02 執行長說 scale-up 的 CPO 首批部署「在 2028 年前後」，光學會先以插拔式出現、接著是近封裝（轉錄稿寫 a new package optics，應是 near-packaged）、最後才是共封裝；2026-08 說「2027 年是 NPO 部署的一年，2028 年以後是 CPO」，這一代和下一代機櫃內的 scale-up 仍是銅[[allmind-astera-q3-20251104,fool-astera-q4-20260210,fool-astera-2026q2-20260811]] |
| Coherent | 展示 6.4T 矽光 NPO 模組（32 × 200G）和 2D VCSEL NPO 模組；NPO 客戶互動超過 10 個，營收時間 2027 下半年[[coherent-photonlink-deck-20260921]] |
| Ranovus | 說已出貨 NPO 模組給數家美國雲端，公開要等 OFC 2027[[lightcounting-npo-202605]] |
| NewPhotonics | 2026 年 1 月推 1.6T NPO 發射晶片，標榜「可維修的 NPO」[[newphotonics-pr-npo-20260113]] |
| Lightmatter | Passage L20：雙向（BiDi）每方向 6.4 Tb/s、資料光纖 32 根、焊在板上（1,827 球 BGA、可回焊）；規格欄寫光纖件「Corning CPO Flexconnect」[[lightmatter-l20-20261012]]；OFC 2026 說 L20 讓光纖數少 50%[[lightmatter-ofc2026-20260319]] |
| 華為 | Hi-ONE：7.2T、36 通道、內置光源，華為說是「業界首個量產的 NPO 產品」，用在昇騰 960 超節點[[huawei-hi-one-20260917]]。詳見 [華為、阿里、騰訊的 NPO](china.md#cn-npo) |
| 華星光 | 預計 2027 到 2029 年 NPO 是主要出貨架構，理由是 CPO 良率不足、壞了難維修[[luxnet-slides-20260828,udn-luxnet-20260828]] |
| NVIDIA | 網路部門主管說 CPO 和 NPO 會並存；研究機構說如果 NVIDIA 也提供 NPO 選項，明年可能就有首批部署[[lightcounting-cpo-npo-20260723]] |

![Lightmatter Passage L20 的渲染圖：模組下緣拖出兩條光纖帶。廠商渲染圖，只作參考。[[lightmatter-l20-20261012]]](img/vendor/lightmatter-passage-l20-npo-render-two-fiber-ribbons-202603.png){.xs}

### 什麼時候、多少

各方說的時間大致落在 2027 年開始、2028 年放量，但出處的可信度差很多：

| 說法 | 誰說 |
|---|---|
| 2027 下半年兩個重點客戶批量採購，2028 更大上量 | 中際旭創自己[[cninfo-innolight-irm-20260728]] |
| 2027 年開始交付、2028 年規模化 | 新易盛自己[[cninfo-eoptolink-irm-20260912]] |
| 首批 NPO 應用 2027 年初，規模化 2027 下半年 | 一份未具名的專家紀要[[cnyes-hao-expert-shuffle-20260819]] |
| 國內頭部雲最早今年底小批量；單波 200G NPO 2027 放量、2028 大規模；海外略晚於國內 | 只有媒體報導[[eeo-huawei-npo-20260918]] |
| NPO 光引擎 2027 年 1,100 萬顆、2028 年 4,000 萬顆；其中 AWS Trainium 4 用 6.4T NPO（2027 下半年 500 萬、2028 年 1,200 萬），NVIDIA 3.2T NPO（600 萬、1,900 萬） | 券商的估計，經媒體轉述[[cnyeshao-gf-npo-oe-20260818]] |
| 亞馬遜下一代機櫃全面改用 3.2T NPO，中際旭創、新易盛、Coherent 送樣；3.2T NPO 模組裡驅動加 TIA 佔材料成本 30%，2028 年單價 2,000–3,000 美元 | 一份未具名的專家紀要[[cnyeshao-expert-npo-aws-20260816]] |
| 騰訊 2026 年第四季部署 NPO 超節點、2028 規模化；阿里 2026 年底小批量、2027 規模化 | 媒體轉述公司主管[[c114-cioe2026-npo-20260920,c114-alibaba-chenqin-20260530]]，詳見 [中國的 NPO](china.md#cn-npo) |
| 2026 年已有 3.2T NPO 在手訂單、正在交付，今年批量；8 月改說「小批交付」 | 華工科技自己[[cninfo-hgtech-irm-20260326,cninfo-hgtech-irm-20260827]] |
| 2027 年 NPO 部署、2028 年以後 CPO | Astera Labs 自己（法說會轉錄稿）[[fool-astera-2026q2-20260811]] |

「Trainium 4 用 NPO」只有券商估計和未具名紀要兩個說法；Marvell 給 Amazon 的認股權條件寫的是 Amazon 買多少 Celestial AI 的光學互連產品（photonic fabric），文件沒寫 Trainium、也沒寫 NPO[[sec-marvell-8k-amazon-20251202]]。

### 各家的口風是怎麼變的 {#alt-npo-wording}

同一家公司對 NPO 的說法，隨時間在變。下面照時間排，都是公司對投資人的答覆。

**中際旭創**

| 日期 | 說法 |
|---|---|
| 2025-10-31 | scale-up 需要的光連接，「相對可行的方案包括 LPO、XPO 和 NPO 等」，預計 2027 年有望看到應用和部署[[cninfo-innolight-irm-20251031]] |
| 2026-02-01 | NPO 比 CPO 多了彈性和性價比：光引擎可插拔、PCB 封裝技術成熟、能大量生產、供應鏈更開放、成本更低；「目前 NPO 是 CSP 客戶比較青睞和重視的方案，並有可能成為一個較為長期的技術選擇」[[cninfo-innolight-irm-20260201]] |
| 2026-04-17 | OFC 展出 NPO、XPO、OCS；「NPO 有望率先在 scale-up 場景應用，已經有 CSP 客戶給了明確的需求指引，預計將在 2027 年量產」[[cninfo-innolight-irm-20260417]] |
| 2026-07-12 | 「NPO 今年 3 月開始呈現明顯加速的趨勢」；「部分客戶已經明確提出 27-28 年的需求指引」；已進入開發、送測到認證的全流程[[cninfo-innolight-irm-20260712]] |
| 2026-07-28 | 2027 年下半年起，行業內兩個有影響力的重點客戶開始批量採購，更大上量在 2028 年[[cninfo-innolight-irm-20260728]] |

從「可行方案之一」，到「雲端客戶青睞」，到「客戶已給需求指引」；公司自己在 7 月說，轉折在 2026 年 3 月（OFC 前後）。

**新易盛**

| 日期 | 說法 |
|---|---|
| 2026-07-20 | 「預計 2027 年下半年有訂單交付需求，2028 年出貨量級將逐步提升」；「預計 2027 年下半年開始商業起量」[[cninfo-eoptolink-irm-20260720]] |
| 2026-09-11 | 「預計 2027 年有批量訂單交付需求，2028 年出貨的規模化量級將進一步提升」；被問 2027 年下半年交付是小批驗證還是大規模商用的開始，答「預計 2027 年開始實現產品交付，2028 年 NPO 產品交付的規模化量級將進一步提升」，不再限定下半年[[p5w-eoptolink-collective-20260911]] |
| 2026-09-20（互動易回覆） | 「預計 2027 年逐步有訂單交付需求，2028 年出貨量級將逐步提升」[[szse-irm-eoptolink-cpo-20260907]] |

7 月限定「下半年」，9 月起寫「2027 年」。時間點是不是真的變了，公司沒有說明；可能只是說得更寬。

**華工科技**

| 日期 | 說法 |
|---|---|
| 2026-03-26 | 3.2T NPO「2026 年已有在手訂單，目前正進行交付」，今年批量；同一場說 4 月起 800G／1.6T 的交付率將提升到 80% 至 90% 以上[[cninfo-hgtech-irm-20260326]] |
| 2026-08-27 | NPO「與國內外多家頭部 AI 廠商小批交付和細化確定最終方案」；「1.6T NPO 頭部客戶需求指引 500 萬只」；預計明年「海外市場將有幾百萬套的需求，國內市場需求亦將達到百萬套以上」。同一場承認上半年 800G、1.6T 光模組受核心物料到貨影響，「實際交付數量不及預期的 50%」[[cninfo-hgtech-irm-20260827]] |

**「批量」「交付」在各家不是同一個意思。**華工說的「交付」是小批量，2026 年已經開始，8 月自己也寫成「小批交付」；中際旭創、新易盛說的「批量」是大客戶批量採購，從 2027 年（下半年）起。定義不同，並排時要標明。另外兩個數字別讀錯：「500 萬只」是華工轉述的「頭部客戶需求指引」，不是華工的訂單；「明年幾百萬套」是華工對市場的預估，原文沒有說是 3.2T 還是 1.6T。3 月預測 4 月起交付率回到八九成，8 月自述上半年實際交付不到預期的一半，所以廠商說「緩解」的預測，要和之後的自述一起看。

### 省多少電

廠商沒有公布 NPO 的實測功耗。一家光模組通路商的部落格估算：一顆 6.4T NPO（模組 26 W 加外部雷射 13 W）約每 bit 6 pJ（皮焦耳），1.6T 插拔式模組（約 24 W）約每 bit 15 pJ[[fibermall-upo-npo-20260918]]。計算驗算：39 W ÷ 6.4 Tb/s ≈ 6.1 pJ/bit；24 W ÷ 1.6 Tb/s = 15 pJ/bit。

### NPO 也要 FAU

光引擎搬到晶片旁之後，光纖還是要貼到光晶片上，NPO 一樣需要 FAU（光纖陣列單元，把一排光纖對準光晶片出光口的零件，見 [FAU 是什麼](fau.md#q11)）。查到的：一家研究機構說 Lightmatter 的 NPO 光引擎最多接 3 個 FAU、每個 40 芯，光引擎本身用台積電 COUPE 或格芯的製程[[semianalysis-cpo-book]]；中國 ODCC 的 UPO 框架把 FAU 做成可插拔（下一節）[[fibermall-upo-npo-20260918]]；Coherent 說它的 FAU 2026 年第四季量產、可拆 FAU 接頭 2027 年第一季量產，賣給 CPO 和 NPO 客戶[[coherent-photonlink-deck-20260921]]。中際旭創自己做「光纖陣列及透鏡組件的自動對準與黏接」，但光纖陣列本身自製還是外購，招股章程沒寫[[hkex-innolight-prospectus-20260722]]；它說「FAU 等供應商交付正常」，表示有外部供應商[[cninfo-innolight-irm-20260712]]。**NPO 的 FAU 由誰供、有沒有台廠，查不到**，見 [不經過 COUPE 的路](fau-makers.md#fau-routes)。

## 各種規格：Open CPX、OCI、EBO、UPO、OPEN NPO {#alt-specs}

2026 年 3 月前後同時冒出好幾個光互連的規格組織（MSA，多源協議：幾家公司約好同一種外形和介面，讓買方可以向多家買）[[technews-trendforce-forum-20260529]]。它們管的段落不一樣：有的管晶片和光引擎之間的電插座，有的只管光的訊號格式，有的只管前面板的接頭。**共同點是：沒有一份公開的規格寫了光纖怎麼貼到光晶片（FAU）。**

<figure>
<div class="scroll">
<svg viewBox="0 0 980 470" width="100%" role="img" aria-label="各規格管的是哪一段">
<text class="note" x="10" y="22">從晶片到前面板，每份規格管哪一段</text>
<text class="item" x="232" y="52" font-weight="600" text-anchor="middle">電的介面</text><text class="note" x="232" y="70" text-anchor="middle">（插座、電連接器）</text>
<text class="item" x="362" y="52" font-weight="600" text-anchor="middle">光引擎</text><text class="note" x="362" y="70" text-anchor="middle">（光的訊號格式）</text>
<text class="item" x="492" y="52" font-weight="600" text-anchor="middle">光纖貼到晶片</text><text class="note" x="492" y="70" text-anchor="middle">（FAU）</text>
<text class="item" x="622" y="52" font-weight="600" text-anchor="middle">光纖束、尾纖</text>
<text class="item" x="752" y="52" font-weight="600" text-anchor="middle">前面板、跳線</text><text class="note" x="752" y="70" text-anchor="middle">接頭</text>
<text class="item" x="890" y="52" font-weight="600" text-anchor="middle">外部雷射</text><text class="note" x="890" y="70" text-anchor="middle">接頭、保偏光纖</text>
<rect class="hl" x="430" y="34" width="124" height="400"/>
<line class="grid" x1="10" y1="82" x2="970" y2="82"/>
<text class="item" x="10" y="108">Open CPX</text>
<rect class="box" x="174" y="92" width="116" height="24"/><text class="note" x="232" y="109" text-anchor="middle">插座、模組外形</text>
<rect class="box" x="304" y="92" width="116" height="24"/><text class="note" x="362" y="109" text-anchor="middle">照 802.3dj DR</text>
<rect class="box" x="564" y="92" width="116" height="24"/><text class="note" x="622" y="109" text-anchor="middle">光纖束、應力</text>
<rect class="dash" x="694" y="92" width="116" height="24"/><text class="note" x="752" y="109" text-anchor="middle">留給應用</text>
<rect class="dash" x="832" y="92" width="116" height="24"/><text class="note" x="890" y="109" text-anchor="middle">列可用接頭</text>
<line class="grid" x1="10" y1="126" x2="970" y2="126"/>
<text class="item" x="10" y="152">OCI MSA</text>
<rect class="box" x="304" y="136" width="116" height="24"/><text class="note" x="362" y="153" text-anchor="middle">一根光纖雙向</text>
<rect class="box" x="832" y="136" width="116" height="24"/><text class="note" x="890" y="153" text-anchor="middle">ELSFP＋保偏</text>
<line class="grid" x1="10" y1="170" x2="970" y2="170"/>
<text class="item" x="10" y="196">EBO MSA</text>
<rect class="box" x="694" y="180" width="116" height="24"/><text class="note" x="752" y="197" text-anchor="middle">擴束接頭</text>
<rect class="dash" x="832" y="180" width="116" height="24"/><text class="note" x="890" y="197" text-anchor="middle">計畫中</text>
<line class="grid" x1="10" y1="214" x2="970" y2="214"/>
<text class="item" x="10" y="240">UPO（ODCC）</text>
<rect class="box" x="174" y="224" width="116" height="24"/><text class="note" x="232" y="241" text-anchor="middle">三種插座</text>
<rect class="dash" x="434" y="224" width="116" height="24"/><text class="note" x="492" y="241" text-anchor="middle">可插拔 FAU</text>
<line class="grid" x1="10" y1="258" x2="970" y2="258"/>
<text class="item" x="10" y="284">OPEN NPO</text>
<rect class="box" x="174" y="268" width="116" height="24"/><text class="note" x="232" y="285" text-anchor="middle">電連接器圖紙</text>
<text class="note" x="564" y="285">首版規範預定 2026 年第三季，查不到發布</text>
<line class="grid" x1="10" y1="302" x2="970" y2="302"/>
<text class="item" x="10" y="328">OIF 12.8T NPO</text>
<rect class="dash" x="694" y="312" width="116" height="24"/><text class="note" x="752" y="329" text-anchor="middle">接頭考量</text>
<rect class="dash" x="832" y="312" width="116" height="24"/><text class="note" x="890" y="329" text-anchor="middle">雷射配置</text>
<text class="note" x="174" y="329">2026 年第二季立項</text>
<line class="grid" x1="10" y1="346" x2="970" y2="346"/>
<text class="item" x="10" y="372">騰訊 3.2T NPO</text>
<rect class="box" x="174" y="356" width="116" height="24"/><text class="note" x="232" y="373" text-anchor="middle">沿用 OIF 結構</text>
<rect class="box" x="564" y="356" width="116" height="24"/><text class="note" x="622" y="373" text-anchor="middle">補定義尾纖</text>
<rect class="box" x="694" y="356" width="116" height="24"/><text class="note" x="752" y="373" text-anchor="middle">最多 4 個接頭</text>
<rect class="box" x="832" y="356" width="116" height="24"/><text class="note" x="890" y="373" text-anchor="middle">外置光源協同</text>
<line class="grid" x1="10" y1="390" x2="970" y2="390"/>
<text class="item" x="10" y="416">XPO MSA</text>
<text class="note" x="174" y="416">沒有公開規格書</text><text class="note" x="564" y="416">光引擎在前面板模組裡</text>
<line class="grid" x1="10" y1="434" x2="970" y2="434"/>
<rect class="box" x="10" y="446" width="30" height="14"/><text class="note" x="48" y="458">規格裡有寫</text>
<rect class="dash" x="160" y="446" width="30" height="14"/><text class="note" x="198" y="458">只提到、留給應用、計畫中，或只有第三方描述</text>
<rect class="hl" x="560" y="446" width="30" height="14"/><text class="note" x="598" y="458">FAU 那一欄：只有 UPO 被第三方描述過</text>
</svg>
</div>
<figcaption>每份規格管的是哪一段。空白表示查到的規格文字沒有寫。依各規格書、官網和報導整理。示意圖，非實際比例。[[opencpx-spec-v1-20260916,oci-msa-spec-v1-20260311,ebo-msa-ecoc2026-20260923,fibermall-upo-npo-20260918,odcc-spring2026-network-20260401,ithome-open-npo-20260709,oif-q2-2026-npo-20260604,iccsz-tencent-npo-spec-20260127]]</figcaption>
</figure>

### Open CPX：插座式的模組，CPO 和 NPO 共用

由 Ciena、Coherent、Marvell、Molex、Samtec、TeraHop 創始，規格主編來自 Ciena；2026 年 9 月 16 日發布 1.0 版[[opencpx-spec-v1-20260916,opencpx-pr-spec-202609]]。TeraHop 是中際旭創持股 66.31% 的新加坡子公司，也是規格聯席主席之一[[hkex-innolight-prospectus-20260722,opencpx-spec-v1-20260916]]；中際旭創自己說它「參與發起設立 XPO MSA 和 Open CPX MSA」[[hkex-innolight-interim-20260911]]。

它定義的是一種插在插座上的光模組：插座焊在交換晶片的封裝基板上就是 CPO，焊在主機板上就是 NPO；模組插進插座不需要壓合的硬體[[opencpx-spec-v1-20260916,opencpx-pr-spec-202609]]。有兩種尺寸：Type-1 是 32 通道、Type-2 是 36 通道，每通道 200G；光學規格照 IEEE 802.3dj 的 DR（每通道收發各一根光纖的平行單模）[[opencpx-spec-v1-20260916]]。雷射有「外部雷射（ELM）」和「模組內建雷射（ILM）」兩種；外部雷射時 32 通道最多 8 根雷射光纖、36 通道最多 12 根，一根雷射光纖分給 3 到 4 個發射通道[[opencpx-spec-v1-20260916]]。

**光纖怎麼出來：一束光纖直接從模組拖出去。**規格第 8 章說，光學介面是「一束或多束光纖」，可以從模組指定區域的任何位置拖出；光纖束長度留給應用自定；模組裡要做光纖應力消除（例如每束直拉 2.2 N）；光纖可以是緊包、鬆包或裸光纖帶。訊號光纖的接頭型式也留給應用自定，建議照 OSFP、OSFP-XD、QSFP-DD 的埠對應，一般做成公頭，插進跟其他插拔模組相同的母頭跳線；外部雷射光纖可以用 MPO、MMC、SN-MT、MXC 或 ELSFP 的盲插接頭[[opencpx-spec-v1-20260916]]。**全文沒有 FAU 這個詞，也沒寫光纖怎麼接到光晶片**；光纖既然從模組拖出來，晶片那一端的光纖貼合就是在模組裡面完成，由模組廠自己決定[[opencpx-spec-v1-20260916]]。

![Open CPX 規格書第 14 頁。上：交換晶片（Host ASIC）四邊插 Type-1 模組，右邊兩組模組各拖出一條光纖束（Fiber bundle），左邊兩組是銅線版；下：xPU 兩側各插 4 個 Type-2 模組，同樣拖出光纖束。[[opencpx-spec-v1-20260916]]](img/explain/opencpx-spec-v1.0-fig3-1-3-2-system-examples-p14-20260916.png){.s}

每顆光引擎要接幾根光纖，各規格不一樣。下表訊號光纖數多數是照規格推算的：

| 光引擎或模組 | 頻寬 | 訊號光纖 | 外部雷射光纖 | 怎麼來的 |
|---|---|---|---|---|
| Open CPX Type-1（外部雷射） | 32 × 200G | 64 | 最多 8 | 32 發＋32 收（計算）；雷射光纖照規格[[opencpx-spec-v1-20260916]] |
| Open CPX Type-2（外部雷射） | 36 × 200G | 72 | 最多 12 | 36 發＋36 收（計算），合計最多 84 根[[opencpx-spec-v1-20260916]] |
| Open CPX（內建雷射） | 32／36 × 200G | 64／72 | 0 | 雷射在模組內[[opencpx-spec-v1-20260916]] |
| OCI 光引擎（以 6.4T 為例） | 6.4T | 32 | 規格未定 | 一根光纖雙向，6.4T ÷ 200G = 32（計算）[[oci-msa-spec-v1-20260311]] |
| Lightmatter Passage L20 | 每方向 6.4T | 32 | 規格表沒列 | 產品頁規格[[lightmatter-l20-20261012]] |
| 外部雷射的典型 3.2T 光引擎 | 3.2T | 32（16 收 16 發） | 4 根保偏光纖 | 康寧主管的描述，經媒體報導[[eeo-huawei-npo-20260918]] |
| 中際旭創 6.4T-4xDR8 NPO 模組 | 4 × 1.6T | 64 | 沒寫 | DR8 是 8 發 8 收，4 組 × 16（計算）[[hkex-innolight-prospectus-20260722]] |

一根光纖雙向（OCI、L20）的做法，讓同樣頻寬需要的光纖數減半，FAU 的通道數不一定跟著頻寬等比增加。一台交換器、一個光引擎用幾個 FAU，見 [FAU 的數量](fau.md#fau-count)。

**成員裡的台廠。**Open CPX 官網 10 月 12 日的成員名單比 9 月的新聞稿多出字節跳動、新易盛新加坡、光迅、聯特、英業達、貿聯、村田、Nokia、Micas 等[[opencpx-members-20261012]]。名單上的台灣公司是智邦、明泰、嘉澤、貿聯、英業達、鴻騰；大立光、上詮、波若威不在名單。中國的光纖件廠有天孚、昂納、成都安捷訊、上海 Lightepoch[[opencpx-members-20261012]]。Coherent 在自己的投資人簡報把自己列為 Open CPX 創始成員[[coherent-photonlink-deck-20260921]]。一場研討會上 Ciena 說 Intel、TE、智邦也加入，並預測 CPO／NPO 和插拔式的市佔在 2030 到 2031 年交叉[[simpletechtrend-ipec-npo-20260508]]。

### 廠商怎麼說這幾種形態的關係

規格文件之外，幾家廠商在法說會上（法說會轉錄稿）也講了自己怎麼看 XPO、CPX、NPO、CPO 的先後和分工。

- **Credo**（2026-09-01）：執行長說 scale-out 和前端網路「沒有真正的理由」離開插拔式；scale-up 網路則「根本需要更高密度的外形」，業界一直在談 XPO、CPX 怎麼和 NPO 搭，最後到 CPO，「這些方案都在解決密度提高 10 倍的需求」；Credo 的做法是對形態「不預設立場」，並已加入 CPX 聯盟[[fool-credo-fy27q1-20260901]]。
- **Lumentum**（2026-08-11）：「NPO 把光引擎放在板子上緊鄰 XPU，用功耗和成本換簡單，上市比較快」；客戶在評估 NPO 用的兩種雷射晶片：直接整合在光引擎裡的中功率雷射，和用在外部光源模組的高功率雷射；其餘客戶「目前把近封裝當成走向 CPO 之前的中間一步」；Lumentum 認為 NPO 最晚在 2027 年底到 2028 年進入市場。這份轉錄稿的說話者標示有錯位（把執行長標成 Operator），以內容為準[[investing-lumentum-q4fy26-20260811]]。
- **Ciena**：2026-03 宣布 Vesta，說它是「業界第一個高密度、低功耗、開放生態的插拔式 CPO 方案」，206.4T 光引擎（來自收購的 Nubis），樣品 2026 年第二季；2026-09 說已從生態系裡幾家「錨定客戶」拿到樣品訂單，並說 CPX 業務「營收預計 2027 年開始、2028 年爬升」[[fool-ciena-q1-20260305,fool-ciena-q3-20260909]]。

### OCI：只管光的訊號格式

OCI MSA 的成員是 AMD、Broadcom、Meta、Microsoft、NVIDIA、OpenAI，規格由 Meta、Broadcom、AMD 編，1.0 版 2026 年 3 月 11 日發布[[oci-msa-spec-v1-20260311]]。它定義的是光學 PHY（光的訊號格式）：**一根光纖收發同時跑**，發和收用兩組不同的波段對向傳，每個方向 4 個波長、每個波長 53.125G，合計每方向 212.5G；規格說這樣做是「為了減少 scale-up 網域的光纖連接和密度問題」[[oci-msa-spec-v1-20260311]]。外部光源要符合 OIF 的 ELSFP 規格，光要先耦合進保偏光纖（PMF，維持光的偏振方向的光纖）再接到光引擎[[oci-msa-spec-v1-20260311]]。參考鏈路是 500 公尺單模光纖、總損耗 2.5 dB，損耗「主要來自接頭」[[oci-msa-spec-v1-20260311]]。

光引擎可以放三種位置：主機板上（OBO）、晶片的封裝基板上、或緊貼晶片的中介層上[[oci-msa-spec-v1-20260311]]。**規格不管接頭、不管光纖、沒寫 FAU**；報導也說 OCI 刻意不規定封裝、外型和光纖線束[[convergedigest-oci-hoti-202608]]。

![OCI 規格書的三種實作：(a) 光引擎焊在主機板上（OBO），紅線是電要走的路，最長；(b) 光引擎放在晶片的封裝基板上；(c) 光引擎放在高密度中介層上，緊貼 ASIC，紅線最短。三種都從光引擎拖出訊號光纖（黃）和接到外部光源 ELS 的光纖（藍）。[[oci-msa-spec-v1-20260311]]](img/explain/oci-msa-spec-v1.0-fig1-three-implementations-p5-20260311.png){.s}

### EBO：管的是前面板的接頭，不是晶片端

EBO MSA 由 Oracle 任主席，3M／Xscape 共同主席，Amphenol、住友、Senko 任編輯[[ebo-msa-ecoc2026-20260923]]；成員 60 家，含 NVIDIA、Microsoft、Meta、Senko、住友、Molex、TE、天孚、昂納、立訊、嘉澤、鴻海[[ebo-msa-site-20261012]]。它要統一的是**擴束（expanded beam）光學接頭**：把單模光纖約 9 微米的光斑放大到約 80 微米，跨過一段空氣間隙再接到另一頭，讓接頭比較不怕髒、比較好清潔，也讓多家接頭廠可以供同一規格[[ebo-msa-ecoc2026-20260923]]。路線圖上 128 芯（8 × 16 芯）的設計規格「進行中」、16 芯 MPO「討論中」、16 芯的超小型接頭（VSFF）和 ELSFP 接頭「計畫中」[[ebo-msa-ecoc2026-20260923]]。

它公布的數據：隨機插拔 552 對、8,832 個點，平均插入損耗 0.32 dB，99.2% 小於 0.7 dB；約 80% 的網路問題和清潔有關，用 EBO 安裝加清潔的時間少約 85%[[ebo-msa-ecoc2026-20260923]]。規格 1.0 還沒發布，官網的規格連結只有一行佔位字[[ebo-msa-site-20261012]]。EBO 管的是面板、跳線、雷射模組這一段的接頭，和晶片端的 FAU 是兩回事；前面板接頭的換代見 [MPO、MMC](passive.md#pas-mmc)。

### UPO：中國 ODCC 的 NPO 框架，寫了「可插拔 FAU」

ODCC（開放數據中心委員會，中國的資料中心產業組織）2026 年春季全會上，騰訊的網路硬體專家講了 UPO 的 XD、HD、SD 三類規格和電介面、光引擎進展；同一場有設備商說 6.4T NPO「標準缺失」、外置光源有互通問題[[odcc-spring2026-network-20260401]]。一家通路商的部落格描述 UPO 1.0 框架（2026 年 9 月提出）：三種插座尺寸、四種整合方式（電路板上、封裝基板上、跨封裝基板、CoWoP 上），可現場更換光引擎、免焊插座，**光纖組件用可插拔 FAU（D-FAU），和光引擎分開處理**；6.4T 等級模組 2026 年內送樣驗證[[fibermall-upo-npo-20260918]]。這是目前查到唯一提到 FAU 的 NPO 規格，但只有第三方描述；UPO 文件本身、D-FAU 的介面和對位方式，在 ODCC 官網查不到。阿里在一場研討會上說 UPO 相容 NPO 和中介層式光學，6.4T UPO 已在 ODCC 立案[[simpletechtrend-ipec-npo-20260508]]。可拆式 FAU 的其他規格見 [可拆式接頭有沒有標準](detachable.md#det-standards)。

### OPEN NPO：華為牽頭，重點是電連接器

華為在 2026 年 7 月聯合中國移動、京東雲、百度等 20 餘家發起 OPEN NPO 多源協議，重點是 NPO 的機械、電氣、環境可靠性、管理運維，尤其電連接器要給到 2D／3D 圖紙級的定義；目標裡寫了「內置光源設計」；首版技術規範預定 2026 年第三季[[ithome-open-npo-20260709,cbj-open-npo-20260716]]。發起名單裡有光模組、矽光晶片、SerDes、電連接器廠，**沒有 FAU 或光纖連接器廠**[[cbj-open-npo-20260716]]。到 10 月 12 日查不到首版規範發布。

### 其他：OIF、騰訊、阿里

- **OIF 12.8T／6.4T NPO**：OIF（光互連論壇）2026 年第二季立項，預計包含「光學接頭考量」和雷射配置[[oif-q2-2026-npo-20260604]]。立項由中國信通院聯合華為、騰訊、阿里雲等提交[[c114-npo-oif-20260727]]。
- **騰訊 3.2T NPO 引擎規格**：機械結構沿用 OIF 的 3.2T CPO，補定義尾纖；鏈路最多 4 個附加接頭、最長 30 公尺、單模光損 3.0 dB；外部光源，新增和光源協同、進光檢查的流程[[iccsz-tencent-npo-spec-20260127]]。這是查到唯一有具體光學數字的中國 NPO 規格。
- **阿里 SNPO**：阿里雲和 ODCC 牽頭、8 家發起，光那一側用 4 個高密連接器；單模版用外置光源[[c114-alibaba-al64-snpo-20260922]]。
- 一家中國模組廠的技術長說，做 NPO 最難定的是插座，每家客戶給的都不一樣[[c114-cioe2026-npo-20260920]]。

中國這幾套規格的細節、接頭（UCM、UTU16）和光源路線，見 [中國的規格](china.md#cn-specs) 和 [中國自己的接頭](china.md#cn-connectors)。

## DSP 缺貨推向哪裡 {#alt-dsp}

**DSP 是插拔式光模組裡最貴、最耗電的零件之一。**光引擎搬到晶片旁之後，電線短到不需要整理，模組和 DSP 就可以拿掉，CPO 的價值改算進交換器的售價裡[[lightcounting-scaleup-20260427]]。DSP 在做什麼，見 [光怎麼接到晶片](basics.md#q2)。它的份量：

| 項目 | 數字 | 誰說的 |
|---|---|---|
| DSP 佔光模組耗電 | 約一半；800G 用的 DSP 約 6–7 W，1.6T 用的約 12–14 W | 研究機構[[semianalysis-cpo-book]] |
| DSP 佔光模組材料成本 | 20–30% | 研究機構[[semianalysis-cpo-book]] |
| 1.6T 插拔式模組材料成本 | 約 450–550 美元，其中 DSP 約 130–180 美元 | 券商的說法[[stockfeel-dsp-20260930]] |
| DSP 長期合約價 | 800G 每顆 45–70 美元；1.6T 每顆 120–150 美元；零售價再高 10–20% | 產業專家，經券商電話會轉述[[cnyes-hao-nomura-dsp-20260923]] |

### 缺多少

**1.6T 用的 DSP 要 3 奈米製程，產能不夠、良率低。**一份券商專家會議的紀要給的數字如下[[allweather-nomura-dsp-202609,cnyes-hao-nomura-dsp-20260923]]：

<figure>
<svg viewBox="0 0 820 290" width="100%" role="img" aria-label="1.6T DSP 需求和供給，2025 到 2027 年">
<line class="grid" x1="200" y1="10" x2="200" y2="250"/>
<text class="item" x="10" y="36">2025 出貨</text>
<rect class="bar2" x="200" y="18" width="18" height="26"/>
<text class="item" x="228" y="36">約 300 萬顆</text>
<text class="item" x="10" y="86">2026 需求</text>
<rect class="bar" x="200" y="68" width="120" height="26"/>
<text class="item" x="330" y="86">超過 2,000 萬</text>
<text class="item" x="10" y="126">2026 出貨</text>
<rect class="bar2" x="200" y="108" width="96" height="26"/><rect class="dash" x="296" y="108" width="6" height="26"/>
<text class="item" x="312" y="126">1,600–1,700 萬</text>
<text class="item" x="10" y="176">2027 需求</text>
<rect class="bar" x="200" y="158" width="360" height="26"/><rect class="dash" x="560" y="158" width="60" height="26"/>
<text class="item" x="630" y="176">6,000–7,000 萬</text>
<text class="item" x="10" y="216">2027 供給</text>
<rect class="bar2" x="200" y="198" width="240" height="26"/><rect class="dash" x="440" y="198" width="60" height="26"/>
<text class="item" x="510" y="216">4,000–5,000 萬</text>
<text class="note" x="10" y="270">深色是需求，淺色是出貨或供給；虛線框是區間的上下限。2026 年缺 300–400 萬顆，2027 年缺 2,000 萬顆以上。</text>
</svg>
<figcaption>1.6T DSP 的需求和供給，單位顆。數字來自一份券商專家會議紀要，圖自己畫。[[allweather-nomura-dsp-202609]]</figcaption>
</figure>

同一份紀要說，產能要到 2027 下半年才明顯開出；800G 用的 DSP 是 7、5 奈米，供給相對寬鬆，2026 年接近 5,000 萬顆；1.6T DSP 本身也有問題，部分錯誤更正（FEC）演算法有漏洞待修，高速 DSP 和交換器之間也有相容性問題[[allweather-nomura-dsp-202609]]。紀要也列了「缺口要往下修」的條件，其中一條是 NPO／CPO 加速取代，提前壓縮 DSP 需求[[allweather-nomura-dsp-202609]]——這是條件，不是預測。

### 誰在做 DSP

| 公司 | 說法 |
|---|---|
| Marvell | 自估光 DSP 市佔 60–65%[[stockfeel-dsp-20260930]]；800G 需求仍強，1.6T「快速爬坡」；整個產業供給受限，但它拿到更多供給；本財年預計付約 10 億美元產能預付款給供應商[[bullfincher-marvell-fy27q2-20260827]] |
| Broadcom | 市佔第二[[stockfeel-dsp-20260930]]；「我們現在是領先製程光 DSP 的領導者，並快速擴充產能」[[webull-broadcom-q3fy26-20260903]] |
| MaxLinear | 市佔 5–7%，目標 1.6T 拿 20–25%[[stockfeel-dsp-20260930]]；1.6T 的 Rushmore 在送樣和認證，2027 年開始有營收；現在靠 5 奈米的 800G 產品；「供給緊」；另有 200G TIA 可用在不需要 DSP 的 LPO 和 NPO[[marketbeat-maxlinear-q2-20260723]]。Rushmore 由三星代工只有媒體和第三方這樣寫，法說裡沒看到[[stockfeel-dsp-20260930,fundaai-cioe-20260916]] |
| NVIDIA | 有自研 1.6T DSP，只有一家研究機構這樣寫，找不到第二個來源[[fundaai-cioe-20260916]] |

Broadcom 的 Sian3、Marvell 的 Ara 都是 3 奈米[[stockfeel-dsp-20260930]]。

### 模組廠說有沒有卡住

- 中際旭創（8 月 23 日）被問 1.6T DSP 供應是否更緊：核心是 3 奈米 DSP 產能偏緊，但整體還好，仍能保持供應；大客戶對重要物料的分配有較強主導權，公司在大客戶佔比高，預計仍拿得到足夠物料；DSP、光晶片、電路板今年都偏緊，有望逐季好轉[[cninfo-innolight-irm-20260823]]。上半年用長期合約、預付款、導入新供應商鎖產能[[10jqka-innolight-16t-20260824]]；2027 年 1.6T 需求和之前預期一樣，只是客戶結構變了[[thepaper-innolight-h1-20260821]]。
- AAOI：近期銷售受產能和關鍵零件限制，不是需求；DSP 和 TIA 的取得「仍是高速模組生產的主要挑戰」；手上 1.6T 訂單超過 2 億美元[[marketbeat-aaoi-q2-20260806]]。
- 新易盛：第一季供應鏈緊張影響交付，第二季起逐步緩解[[cninfo-eoptolink-irm-20260720]]。
- 一家研究機構在 9 月的光博會（CIOE）後說，1.6T 的交付速度和市佔由 DSP、雷射、電路板拿不拿得到決定[[fundaai-cioe-20260916]]。

沒有任何一家模組廠給出「因為 DSP 少出了多少 1.6T」的數字。

### 缺貨把需求推向哪裡

查到的是各方的說法和動作，沒有誰贏的結論：

- **列出來的緩解辦法裡沒有 CPO。**一家研究機構列的路是：台積電 3 奈米擴產、MaxLinear 找三星代工、Credo 的 1.6T LRO（仍用 DSP 但少做一半）、800G LPO、NVIDIA 自研 DSP[[fundaai-cioe-20260916]]。
- **券商的看法**：1.6T 這代仍以插拔式搭 LPO 為主，3.2T 才開始驗證 CPO；DSP 拿掉之後，SerDes 的價值移到交換晶片[[stockfeel-dsp-20260930]]。
- **拿掉 DSP，工作移到 TIA 和驅動 IC，它們也在缺。**NPO／CPO 拿掉 DSP 之後，等化和糾錯改由 TIA、驅動 IC 和交換晶片承擔，對 TIA 和驅動的線性度要求更高；龍頭廠 200G 已量產、400G 開發中[[allweather-nomura-dsp-202609]]。Marvell 說 TIA 和驅動的需求超過公司預期[[bullfincher-marvell-fy27q2-20260827]]；AAOI 說缺的是 DSP 和 TIA 兩樣[[marketbeat-aaoi-q2-20260806]]。所以拿掉 DSP 的做法不一定躲得開零件吃緊。
- **模組廠全部都押。**中際旭創、新易盛都把 NPO、XPO、LPO、CPO 全列在產品線上[[cninfo-innolight-irm-20260823,cninfo-eoptolink-irm-20260912]]。
- **中國的角度**：中國媒體寫 NPO 拿掉 DSP，「繞開了國產電晶片最大短板」，見 [出口管制](china.md#cn-export)。

原本的筆記寫「DSP 缺貨壓著插拔式，也是 CPO 拿掉 DSP 的賣點」。查到的是：缺貨這件事目前帶動的是 TRO／LRO、LPO 和更多 DSP 供應商；把 NPO、CPO 當成解法的說法，只出現在專家紀要「缺口可能被高估」的條件裡。市場規模的估計見 [市場多大](timing.md#q28)。

## 雲端大廠要買什麼 {#alt-buyers}

買方怎麼選，比廠商怎麼說更直接。下表把查到的說法依公司並排；「自己說的」和「別人轉述的」分開看。

| 誰 | 自己說的 | 別人說的 |
|---|---|---|
| Meta | 「能不能做出來」大致答完了，現在的問題是「該不該」，因為每一點省電都要拿可靠度、可用性、可維修性去換；CPO 第二階段系統測了超過 5,000 萬裝置小時，初步看可靠度比插拔式高，但還要更長的資料；在研究可現場維修的設計[[convergedigest-meta-ofc2026]]。光學要「可靠、效能好，而且成本和耗電要和電的方案相當」[[photoncap-ofc2026-cpo]]。OCI 創始成員[[lightcounting-ofc2026-20260326]] | 研究機構：Meta、Oracle 暗示先上 NPO，CPO 是最終方案[[gazettabyte-ofc2026-lpo-20260409]]；另一家研究機構：Meta、Microsoft 傾向先布局 NPO[[cna-trendforce-20260615,ctee-trendforce-20260616]] |
| Microsoft | XPO 創始成員，主管說 XPO 把插拔式的好處延伸到 scale-out 和 scale-up[[arista-pr-xpo-20260311,nextplatform-xpo-20260417]]；Azure 硬體主管說和 Arista 合作 1.6T 介面，用在自家 AI 晶片和資料中心[[arista-pr-7060xe7-20260609]]。OCI 成員[[oci-msa-spec-v1-20260311]] | 傾向先布局 NPO（同上）；研究機構問「Microsoft 這次會部署 NPO 嗎？當初為什麼放棄 COBO（更早的板上光學聯盟）？」[[gazettabyte-ofc2026-lpo-20260409]] |
| Google | 沒找到 2026 年自己的公開說法；不在 XPO 名單[[nextplatform-xpo-20260417]] | 研究機構：Google 是最不願部署 CPO 的雲端大廠，可靠度對它是「deal breaker」，短期不預期採用[[semianalysis-cpo-book]]；另一家研究機構（2025 年 4 月）：Google 評估過 CPO，結論是問題比解決的多，它的策略是少用光、搭光路交換器（OCS）、提高插拔式頻寬[[lightcounting-ofc2025-202504]]；券商紀要：Google 在 TPU 和 OCS 網路用 2.4T 的 coherent-lite 模組[[allweather-nomura-dsp-202609]] |
| AWS／Amazon | 沒找到自己的說法；AWS 副總在 Marvell 收購 Celestial AI 的新聞稿說光互連會在 AI 基礎設施扮演重要角色[[marvell-celestial-20251202]] | Marvell 給 Amazon 的認股權，依 Amazon 買 Celestial 光學互連產品的量解鎖[[sec-marvell-8k-amazon-20251202]]；研究機構：Amazon 和 ST 合作布局 NPO[[cna-trendforce-20260615]]。意法自己的說法分兩場：2026-04-23 法說問答，執行長講到光纜與近封裝光學，「主要推手之一會是 AWS」，但意法要服務的對象遠不只 AWS，沒說是 NPO 還是 CPO、沒說數量（AI 轉寫稿）[[allmind-st-q1-20260423]]；2026-07-23 第二季法說講的是 800G／1.6T 插拔式的晶片，沒有提 AWS 或近封裝[[webull-st-q2-202607]]。Trainium 4 用 NPO 只有券商和未具名紀要的說法（見 [NPO](#alt-npo)） |
| Oracle | EBO 接頭聯盟的主席[[ebo-msa-ecoc2026-20260923]]；在 Arista 1.6T 新聞稿背書[[arista-pr-7060xe7-20260609]] | 暗示先上 NPO（同上）；部署 LPO 查不到 |
| 阿里、騰訊 | 騰訊 2026 年第四季部署 NPO 超節點，認為 NPO 是走向 CPO 途中的中間路線；阿里 2026 年底小批量[[c114-cioe2026-npo-20260920,c114-npo-oif-20260727,c114-alibaba-chenqin-20260530]] | CPO 效能最好，但擔心沒有開放的生態；NPO 是現在最實際、最划算的大規模方案[[lightcounting-npo-202605]] |

幾件事放在一起看：

- **近期被描述為先上 NPO 的**：Meta、Oracle、Microsoft、阿里、騰訊。多數是研究機構轉述，Meta 自己公開講的是「該不該」，不是「選哪個」。
- **交換器廠 Arista 自己的立場，兩次法說（法說會轉錄稿）有變化。**2026-05：「業界談了很多共封裝光學，這些仍是科學實驗，而且很私有，各家做各家的」；Arista 擁抱幾年後的開放 CPO，但認為 XPO 有十年的路，尤其在需要液冷的 1.6T、3.2T；而且「今天和我們連接的光學市場，99% 是插拔式」[[fool-arista-q1-20260505]]。2026-08：CPO「大概明年進入範例和試用」，但供應鏈短缺下，世界上多數仍是插拔式光學和銅，「2028、2029 年會有一定數量的共封裝光學」；Arista 「不喜歡五種不同的私有實作」，要的開放 CPO 是插座式光引擎、尾纖、模組可以完整預先測試，「這類開放 CPO 常被叫做 NPO」[[fool-arista-q2-20260811]]。
- **Google 可能完全不走 CPO**，但這只有第三方說法，Google 沒公開表態；它的光路交換器路線見 [Google 的 OCS](timing.md#tm-ocs)。
- **Marvell 法說提到的「一家關鍵雲端大廠擴大合作」**，對應的 8-K 是 Google 的客製晶片（推論加速器、網卡等），文件沒提光學或 NPO[[sec-marvell-8k-google-20260819]]。
- **Meta 公開的 CPO 失效主因是外部雷射模組，不是光纖。**一份整理 Meta 演講的部落格寫：Bailly CPO 累計 9,000 萬裝置小時（400G 埠等效）；平均故障間隔（MTBF）插拔式 2×400G FR4 約 71 萬小時，CPO 第一階段全部失效算約 147 萬小時，扣掉一個外部雷射模組驅動電路上的零件劣化問題後約 820 萬小時；失效的主要來源是那顆零件，「髒光纖和接頭」則是插拔式和 CPO 共同的問題[[simpletechtrend-meta-cpo-2026]]。沒有 FAU 失效的分項數字。可靠度資料的細節見 [可靠度數據](equipment-test.md#eq-reliability)。

CPO 這一邊誰在主導，見 [誰主導](players.md#q17)。

## 還不知道的 {#alt-open}

- **XPO 模組裡有沒有 FAU、誰供**：沒有公開規格書；從 OFC 2027（2027-03-07～11，洛杉磯）的展場照片、中際旭創和新易盛的 XPO 產品頁、Arista 的 XPO 網路研討會查。
- **XPO 官方成員名單**：官網只有標題頁；等 xpomsa.com 更新，或從各家加入 XPO 的新聞稿拼出來。
- **XPO 到 400G 通道還能不能不用 DSP**：媒體說可以，研究機構說目前只有 200G；等 Arista 的 400G 路線圖或 OIF 高密度外形的進度。
- **中際旭創、新易盛 NPO 的 FAU 自製還是外購、跟誰買**：招股章程和年報都沒寫；等兩家 10/30 的三季報，以及互動易上沒回的 FAU 提問。
- **中際旭創招股章程裡的兩家中國無源光器件供應商（供應商 E、I）是誰**：從愛德泰招股書、蘅東光問詢回覆的客戶名單反查；蘅東光 10/28 三季報。
- **Marvell 的 NPO「多家客戶」是誰**：法說沒點名、8-K 沒有；等 Marvell FY27Q3 財報（12 月初，日期未公告）。另外，Marvell 說的 scale-up 光學金額（見 [Marvell 說的數字](players.md#pl-marvell)）裡 NPO 和 CPO 各占多少，沒有拆開。
- **意法說的「AWS 是近封裝光學主要推手之一」是 NPO 還是 CPO、用什麼產品、多少量**：2026-04-23 法說只有一句，沒有細節（原本這裡寫「ST 法說沒提」，對照逐字稿後更正）；從意法下一場法說（2026 年第三季，日期未公告）、矽光平台新聞稿、AWS re:Invent（11/30–12/4）查。
- **AWS、Google、Oracle 自己對 CPO／LPO／NPO 的公開說法**：都沒找到；AWS re:Invent（11/30–12/4）、OFC 2027（3 月）的講者名單。
- **Broadcom 3.2T VCSEL NPO 用什麼光纖介面**：多模，耦合方式可能和單模 FAU 不同；從 Broadcom 在 IFOC 2026 的演講報導、Broadcom FY26Q4 財報（12 月中，日期未公告）查。
- **Coherent PhotonLink 每顆 100T 晶片最多 1.5 萬美元的內容怎麼拆、FAU 佔多少、賣不賣 NPO 用 FAU**：等 Coherent FY27Q1 法說（11 月初，日期未公告）。
- **Lightmatter L20 的「Corning CPO Flexconnect」是光纖還是整組 FAU**：康寧的 FlexConnect 原本是一款耐彎光纖的名字，Coherent 也有同名的可拆 FAU 接頭；看 Corning 2026Q3 法說（10/27）和 L20 的規格書（要向 Lightmatter 索取）。
- **6.4T、3.2T NPO 的廠商實測功耗**：目前只有通路商的估算；等 OFC 2027 的論文和展示。
- **Broadcom、Cisco、Arista、Celestica 同一顆晶片插拔式對 CPO 的整台功耗**：只有 NVIDIA 有；從各家 CPO 交換器的硬體手冊查。
- **UPO 1.0 文件和 D-FAU 規格**：只有一篇第三方描述；ODCC 官網沒放；可以試 OpenCLI 走騰訊「鵝廠網事」公眾號和 ODCC 秋季會議稿。
- **OPEN NPO 首版規範出了沒、有沒有光口定義**：原訂 2026 年第三季，到 10/12 查不到；從 OAII 社區、華為計算公眾號查。
- **OIF 12.8T NPO 的光學接頭章節**：等 OIF 下一次季會的新聞稿（日期沒查）。
- **EBO 規格 1.0 什麼時候發布**：官網只有佔位字；盯 ebomsa.org。
- **Meta 在 OFC 2026 的可靠度論文原文**：想知道失效裡有沒有光纖端面、FAU 脫膠這類項目；目前只有二手整理；從 Optica 的 OFC 2026 論文集查。
- **NVIDIA 是不是自研 1.6T DSP**：只有一家研究機構一句；從 NVIDIA 1.6T 模組的文件查 DSP 型號。
- **MaxLinear Rushmore 是不是三星代工**：法說沒提；從 MaxLinear 10-Q 和 Rushmore 發表新聞稿查。
- **Credo 1.6T LRO 的實際採用**：等 Credo FY27Q2 財報（12 月初，日期未公告）。
- **DSP 缺貨讓 1.6T 少出了多少**：模組廠都只說物料緊；等中際旭創、新易盛 10/30 三季報，AAOI 下一季法說。
- **台廠在 XPO 供應鏈的位置**（液冷快接頭、冷板、CPC 線纜、MPO-16 接頭）：從台灣媒體和奇鋐、雙鴻、嘉澤、貿聯的法說查；貿聯去年同期 11/7 開法說（今年還沒申報）。
- **華工科技的 3.2T NPO 交付給誰、多少**：公司只說「與頭部廠商及交換機芯片廠商合作」「國內外多家頭部 AI 廠商小批交付」，沒點名；看華工三季報與下一場投資者關係活動記錄（日期未公告）。「1.6T NPO 頭部客戶需求指引 500 萬只」是哪一家客戶的指引，也沒說。
- **光迅 3.2T NPO 的「全系列驗證」與「系統驗證」差在哪、客戶是誰**：公司沒有說明；看光迅三季報（日期未公告）。
- **新易盛 NPO 的交付時間是 2027 年還是 2027 年下半年**：7 月限定下半年，9 月起寫 2027 年；等 10/30 三季報與下一場投資者關係活動記錄。
- **天孚說的 NPO「配套產品」是哪些、多個客戶是誰**：7 月 9 日只有一句；看天孚三季報（10/29）。
- **Ciena Vesta 的「錨定客戶」是誰、2027 年營收多大**：Ciena 沒說；看 Ciena FY26Q4 法說（日期未公告）。
