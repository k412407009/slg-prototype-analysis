# 轻量化 SLG 赛道 Steam 原型数据分析 · 网站信息维护指南

> 这是 `steam原型数据分析.html` 的**可维护性文档**。
> 任何人（包括未来的你自己、新来的协作者、交接 agent）拿到这份文档，都能在 15 分钟内回答三件事：
> **① 网站在讲什么** · **② 信息是从哪儿查到的** · **③ 下次要更新哪里怎么改**。

---

## 0. 文档元数据

| 字段 | 值 |
|---|---|
| 关联页面 | `steam原型数据分析.html`（同目录） |
| 页面版本 | v4.2（2026-04-20 · 评审框架 9 维 → 7 维精简 + 决策一览 Summary 表 + 6 项目 PPT 工程链接） |
| 页面上一版 | v4.1 评委会 9×6 矩阵版（同日上午）· v4 评审同步版（同日）· v3 真实数据版（2026-04-16 DREDGE 日语幻觉修正） |
| 本文档版本 | 2026-04-20（v2）· 增补"§3.6 评审框架 v4.2 精简说明（9→7）"和"§4.7 PPT 工程超链接规范" |
| 部署方式 | RUN Platform 静态托管，`bash start.sh` 起 Python http.server |
| 外部依赖 | 仅 Chart.js（`cdn.jsdelivr.net`），零后端 |

---

## 1. 网站在讲什么（一句话 + 三段话）

**一句话**：用 Steam 官方评论页的真实语言分布，筛选 8 款原型，推导出 8 个"轻量化 SLG + 海外发行"的候选题材方向，并给出立项建议（S+ / S / A+ / A / B+ / B / D）。

**三段话展开**：

1. **原型层（Prototype Tier）** — 8 款 Steam 真实热度原型（Schedule I / TCG Card Shop Simulator / DREDGE / Storage Hunter Simulator / Beholder / Empire of Sin / Undisputed / To The Rescue!），每款都给出评论总数、峰值在线、好评率、Steam 语言分布饼图、核心洞察、交叉验证来源。
2. **方向层（Direction Tier）** — 基于 8 个原型的交叉分析，归纳出 8 个可能做成"轻量化 SLG"的题材方向 A-I，每个方向标注买量合规性、海外盘大小、SLG 改造空间三个维度，按 S+/S/A+/A/B+/B/D 打档。
3. **洞察层（Insight Tier）** — 6 条跨原型的通用结论（如"拆包是跨文化通用爽点"、"日本 Steam 几乎不存在必须走 App Store"、"买量合规决定生死而不是题材好坏"），指导后续新方向立项时的思考框架。

---

## 2. 数据来源（References）· 逐原型登记

**数据真实性原则**：所有语言分布都来自 Steam 官方评论页过滤器的**真实计数**，不做估算；如某字段不可得，写 `unknown` 或 `数据未公开`，**不伪造**。

### 2.1 主数据源（按重要性排序）

| 数据源 | 用途 | URL |
|---|---|---|
| **Steam 评论过滤器（主）** | 语言分布、评论总数、好评率 | `https://store.steampowered.com/app/<ID>/` → 社区评论 → 语言筛选 |
| SteamDB | 峰值在线交叉验证 | `https://steamdb.info/app/<ID>/charts/` |
| SteamSpy | 销量区间估算 | `https://steamspy.com/app/<ID>` |
| Steam Charts | 历史玩家趋势 | `https://steamcharts.com/app/<ID>` |
| Steambase | 玩家趋势可视化 | `https://steambase.io/games/<slug>/steam-charts` |
| PlayTracker | 实际触达人数估算 | `https://playtracker.net/insight/game/<ID>` |
| Apple App Store | 移动端发行状态 + 评分 | `https://apps.apple.com/us/app/<name>/id<ID>` |
| Google Play | 安卓端发行状态 + 下载区间 | `https://play.google.com/store/apps/details?id=<pkg>` |

### 2.2 按原型登记（维护这张表即可）

| 原型（对应方向） | Steam AppID | 主要引用数据 | 交叉验证 |
|---|---|---|---|
| Schedule I（→ G 禁酒令 / D 毒枭） | 3164500 | 峰值 459,075 · 评论 292,471 · 好评 97% · 英语 186,574 条 · 德语 20,386 条 | Steambase + SteamSpy |
| TCG Card Shop Simulator（→ E 卡店帝国） | 3070070 | 峰值 53,255 · 评论 47,061 · 好评 97% · 东亚合计约 19% | Steam Charts + G2A News |
| DREDGE（→ H 深海守望者） | 1562430 | 销量 100 万+ · 评论 53,246 · 英语 30,641 (57.5%) · **日语真实 282 条 = 0.53%** | GameDeveloper 文章 + PlayTracker 290 万触达 |
| Storage Hunter Simulator（→ A 港口开箱） | 1442430 | 峰值约 3,500 · 评论 3,829 · 好评 79% · 英语 1,684 条 + 德语 358 条 | A&E 电视剧《Storage Wars》IP 血缘 |
| Beholder（→ B 极权公寓） | 475550 | 评论 30,255 · 俄语 38.8% > 英语 13.4% · 土耳其 1,337 条 | Alawar 发行商俄语区数据 |
| Empire of Sin（→ G 失败案例） | 604540 | 峰值 7,728 → 当前 ~70 · 评论 6,218 · 好评 48% | Steam Charts 跌幅 + Paradox 论坛停更 |
| Undisputed（→ C 地下拳馆） | 1451190 | 评论 21,961 · 好评 60% · 英语 84.3%（13,528 条） | 与 UFC 5 / Fight Night 对标 |
| To The Rescue!（→ I 动物联盟） | 946720 | 评论 2,123 · 好评 67% · 售价 $9.99 · 20% 捐 PetFinder | 同期 Cat Cafe Manager 参照 |

### 2.3 非 Steam 数据源（关键参考 IP / 题材 / 合规）

| 来源类型 | 用途 | 具体引用 |
|---|---|---|
| HBO / Netflix 剧集 | 题材情感锚点 | 《大西洋帝国 Boardwalk Empire》（禁酒令） · 《Peaky Blinders》（英式黑帮） · 《Narcos》（毒枭，题材可参考但禁买量） · 《Zootopia》（动物叙事） |
| 电视真人秀 / YouTube | 爽点血缘 | A&E《Storage Wars》13 季（仓储拍卖） · MrBeast 港口开箱（YouTube 单集 1-3 亿播放） |
| 广告合规政策 | 方向 D 封杀依据 | Meta Audience Network Policy · Google Ads Recreational Drugs Policy · AppLovin illegal-illicit-products · Unity Ads content policy |
| Apple 官方奖项 | DREDGE 移动端背书 | 2025 Apple Design Award · App Store 2025 iPad Game of the Year |

---

## 3. 思考过程（How We Got Here）

网站不是凭空写出来的，而是经过三轮迭代。记录这条决策链，是为了让后续任何人加新原型、新方向时，能沿用同一套筛选逻辑。

### 3.0 最初的分析框架（Why these 8 prototypes? Why these 8 directions?）

这一节专门回答"你最开始是基于什么分析的"。后续要新加方向 / 新加原型时，照这个框架走一遍即可。

#### 3.0.1 问题 Prompt（研究起点）

任务是："公司有一套 MyPerfectHotel-like 的放置经营骨架要复用，要找**海外能打**且**SLG 改造空间大**的轻度题材候选方向。"

从这一句 prompt 推出三个硬约束：

| 约束 | 含义 | 对原型筛选的影响 |
|---|---|---|
| **海外能打** | 首发市场不是国内，必须有英语区受众基础 | 原型的 Steam 英语评论 ≥ 1,000 条门槛 |
| **SLG 改造空间大** | 原作不能已经是重度 TBS/4X（那就没得改了） | 原作玩法重心≤单人经营 / 线性叙事 / 放置等轻度骨架 |
| **轻度题材** | 与 MPH 骨架能拼得上，不能是 AAA 剧情大作 | 原型售价 ≤ $25 或是 F2P，开发体量 1-3 年独立/中型工作室 |

#### 3.0.2 原型候选池（怎么选出这 8 款的）

从 Steam 2023-2026 年"经营模拟 + 叙事模拟 + 放置模拟"品类里筛出 30+ 款候选，依据以下 5 个信号**逐层漏下**来：

| 漏斗层 | 筛选信号 | 为什么用这个信号 |
|---|---|---|
| **L1 热度** | 峰值在线 ≥ 3,000 或 总评论 ≥ 2,000 | 热度过低证明题材天花板太矮，SLG 规模化没意义 |
| **L2 可迁移** | 原作是单人骨架 / 没有 PVP / 没有联盟 | 原作越"单薄"，SLG 改造空间越大 |
| **L3 跨文化** | 有至少 1 种非英语评论 ≥ 原作总评的 2%；或有电视剧/YouTube/电影 IP 跨文化背书 | 否则海外盘窄 |
| **L4 合规预筛** | 不是赌博 / 毒品 / 色情 / 极端暴力直出 | 否则 Meta/Google/Apple 一票否决，SLG 买量模型不成立 |
| **L5 数据可验证** | Steam 评论页能拉到真实语言过滤数据 | 这是本网站的立身之本，不可验证不收录 |

**最终过漏斗的 8 个原型**（连同漏掉的典型反例）：

| 过漏斗 8 款 | 为什么过 | 漏掉的典型反例 | 为什么漏 |
|---|---|---|---|
| Schedule I | L1 爆款级 · L2 单人骨架 · L3 全球通吃 | Schedule I 原味手游 | L4 毒品触合规（走方向 G 的"题材蒸馏"版本进） |
| TCG Card Shop Simulator | L1-L5 全过 · 东亚占比最高 | Hearthstone / MTG | L2 已是重度 TBS，改造空间 < 3 星 |
| DREDGE | L1 百万销量 · L3 克苏鲁跨文化 · Apple 奖项 | Dave the Diver | L5 虽热但 SLG 骨架已偏重，改造空间差一档 |
| Storage Hunter Simulator | L1 勉强过 · 电视剧 IP 血缘极强 | Bitlife | L3 纯文字缺视觉钩 |
| Beholder | L1 过 · 题材独特 | Papers Please | L3 俄语极度偏斜，反向验证"区域化陷阱" |
| Empire of Sin | 反面教材（重度 TBS 的翻车案例） | 直接剔除 | L2 重度 TBS · L1 从 7,728 跌到 70 = 最好"别这么做"范本 |
| Undisputed | L1 刚过门槛 · 验证垂直题材 | UFC 5 | L2 AAA 不可对标 |
| To The Rescue! | L1 勉强过 · 公益题材独家 | Animal Shelter | 实际 Animal Shelter 也过了漏斗，To The Rescue 承担"善意变现案例"角色，两者在方向 I 分析里都有引用 |

> **关键选择逻辑**：Empire of Sin 不是候选而是"反面教材"，专门用来证明"重度 TBS × 题材好感度 ≠ 成功"——这个反例对方向 G/D 的讨论很关键，不能删。

#### 3.0.3 原型 → 方向的映射逻辑

8 个方向 A-I 不是凭空列出来的，每个方向都来自"某个原型的某个子爽点 + MPH 骨架 + 某个跨文化 IP 情感"三合一推演。映射关系如下：

| 方向 | 核心爽点来源 | 情感 IP 来源 | 经营骨架 | 为什么合并到一起 |
|---|---|---|---|---|
| **A 港口开箱** | Storage Hunter Simulator 的"拆箱爽点" + MrBeast 港口开箱视频级爽感 | A&E《Storage Wars》13 季 | MPH | 拆包是跨文化通用爽点 + 港口叙事比家庭仓储更具 SLG 扩张性（多港争夺） |
| **B 极权公寓** | Beholder 的"窥视 + 抉择" | 《1984》《黑镜》 | MPH | 俄语基本盘证明独特题材能活，适合小众做区域化 |
| **C 地下拳馆** | Undisputed 的"垂直品类 + 上升故事" | Rocky / Fight Club | MPH | 垂直品类 + 上升故事结构极好承载 SLG |
| **D 毒枭原味** | Schedule I 的"生产-分销-体验"闭环 | Breaking Bad / Narcos | MPH | 爽点最强但合规死路，作为"反面对照"留住 |
| **E TCG 卡店帝国** | TCG Card Shop 的"开包 + 集换 + 市场博弈" | 游戏王 / 宝可梦 / MTG 20 年文化积累 | MPH | 开包爽点与"经营店主"视角天然绕开 lootbox 法律风险 |
| **G 禁酒令私酒帝国** | Schedule I 骨架（蒸馏） | HBO《大西洋帝国》+ Peaky Blinders | MPH | 把 D 的爽感移到合规题材，是 D 的合规替代解 |
| **H 深海守望者** | DREDGE 的"日常出海 + 恐怖节律" | 克苏鲁 / 灯塔 / Lovecraftian | MPH | DREDGE+ 移动端验证成功，SLG 层完全空白 |
| **I 动物联盟** | To The Rescue / Animal Shelter | Zootopia / Stray | MPH | 纯善 + 偷救叛逆=情感+策略+叛逆三重钩 |

> **为什么没有方向 F**：F 在早期稿是"殖民地管理"（Frostpunk 灵感），L4 合规 + L2 骨架重，被剔除到"候选池备忘"里，但编号保留跳过，防止后面重排 ID 把所有文档索引搞乱。

#### 3.0.4 为什么只有 8 个方向，不是 5 或 15？

- **下限**：少于 5 个方向 = "可选面太窄，高管会怀疑分析深度"。
- **上限**：超过 10 个方向 = "没法聚焦，且每个方向的数据支撑都薄"。
- **实际收敛**：8 个方向正好覆盖"S+/S/A+/A/B+/B/D"七档（C 档空缺，是故意留出的"下次迭代可补位"空间）。

### 3.1 v1 · 幻觉版（已淘汰）

**背景**：最早一版用"语言常识 + 品类经验"猜测语言分布，写了"DREDGE 日语占 12%"、"Empire of Sin 英语 70%"等估算值。

**教训**：
- 常识推断和真实数据可以差 20 倍（DREDGE 日语 12% → 实际 0.53%）
- 一个错误数据会带偏整个方向建议（最初因此错误判断"DREDGE 强日本，适合做日本市场"）

### 3.2 v2 · 补交叉源，但仍混估算（已淘汰）

**修正**：增加 SteamDB / SteamSpy / PlayTracker 三个来源交叉。
**遗留问题**：部分原型语言分布仍用"其他语种合并估算"填充（比如 Storage Hunter 因评论少而语言分段不完整）。

### 3.3 v3 · 真实数据版（2026-04-16，上一次稳定版）

**核心修正**：
1. 全部 8 个原型重新拉 Steam 评论页的语言过滤器，记录真实计数。
2. 把"DREDGE 日语 12%"更正为 "0.53%（282/53246）"，并据此重写方向 H 的「打日本一定要走 App Store 不能看 Steam」结论。
3. 对于评论过少（如 To The Rescue 只有 2,123 条）导致语言分布不可得的原型，明示 `unknown` 而非编数字。
4. 对于方向 D（毒枭原味）做**致命级合规判决**：用 Meta / Google / AppLovin 的官方政策条款直接否决，而不是模糊写"可能有风险"。

### 3.4 v4 · 立项评审同步版（2026-04-20，本次更新）

**触发原因**：6 个立项方向（A / E / G / H / I / D）已经出了 PPT 设计稿，并经过 5 人评委会评审，结果沉淀为 `ppt-master/projects/review-summary.md`。

**更新动作**：
1. 在第三部分"最终推荐方向"总览表格新增**「立项评审」列**，显示加权总分 + 裁决（CONDITIONAL PASS / REJECT）。
2. 每个推荐方向的卡片底部新增 **review ribbon**，列出 P0 待改条数 + 最紧迫的 1-2 条。
3. 新增**第四部分「立项评审进展」**章节，包括：
   - 6 项目加权总分横向对比
   - 5 位评委共性问题汇总（题材合规 / 团队预算 / 阶段过渡 / 付费模型）
   - 推进顺序建议
4. footer 版本号改为"v4 · 2026-04-20 评审同步版"。

### 3.5 方向打档规则（档位怎么定）

每个方向的最终档位（S+ / S / A+ / A / B+ / B / D）由三个维度推导：

| 维度 | 打分原则 |
|---|---|
| **买量合规** | 完美（所有主渠道可投）= 满分；需区域裁剪 = 中等；Meta/Google 明确禁投 = 致命降级（方向 D 即因此从 S 级直接落到 D） |
| **海外盘大小** | 英语区评论 ≥ 10 万 + 多语言分布均衡 = 5 星；只在某一语种强势（如 Beholder 只俄语 38%）= 2-3 星 |
| **SLG 改造空间** | 原作已有的是单人经营骨架，且未做 PVP / 联盟 / 多城扩张 = 5 星；原作已经是重度 TBS/SLG = 3 星以下 |

**档位映射**（从高到低）：
- **S+**：三维全 5 星 + 有电视剧 / YouTube 级别跨文化爆款背书
- **S**：三维全 5 星但某一维有边界条件（如方向 G 需题材蒸馏才合规）
- **A+**：两维 5 星 + 一维 4 星
- **A**：三维都 4 星
- **B+**：某一维降到 3 星（比如暴力内容）
- **B**：两维都在 3 星以下（如 Beholder 仅俄语区）
- **D**：合规维被直接一票否决

#### 3.5.1 每个方向档位的实际推导（Scorecard Traceback）

下面这张表是**实际填过的 scorecard**，任何人要质疑某个档位、或要往上/往下调档，都可以直接对着这张表追溯依据。新加方向时，按同样的结构填一张即可。

| 方向 | 买量合规 | 海外盘 | SLG 改造 | 档位 | 关键拐点（决定档位的那一条） |
|---|---|---|---|---|---|
| **A 港口开箱** | ⭐⭐⭐⭐⭐（拆包爽点 0 合规风险，电视剧 IP 加持） | ⭐⭐⭐⭐⭐（英语区 Storage Wars 13 季观众 + MrBeast 3 亿级播放） | ⭐⭐⭐⭐⭐（Storage Hunter 是单人骨架，多港争夺/海关博弈/帮派 PVP 层级全空白） | **S+** | 三维全 5 + 电视剧 IP 背书 |
| **G 禁酒令私酒帝国** | ⭐⭐⭐⭐⭐（酒精属合法成人商品，Meta/Google 允许投；部分伊斯兰区需区域屏蔽） | ⭐⭐⭐⭐⭐（《大西洋帝国》+《盖茨比》+ 英国 Peaky Blinders = 英语区+东亚"上海滩"共鸣） | ⭐⭐⭐⭐⭐（Schedule I 骨架可 100% 迁移到禁酒令） | **S**（不上 S+） | 差在"伊斯兰区需裁剪"的边界条件，比 A 少一层"所有区通吃"的底气 |
| **E TCG 卡店帝国** | ⭐⭐⭐⭐（店主视角规避 lootbox 主要风险，沙特仍需改名规避斋月） | ⭐⭐⭐⭐（英语区 + 东亚 10% 是所有原型最高，但基本盘绝对值不如 A/G） | ⭐⭐⭐⭐⭐（原作纯单店闭环，多店连锁/城市竞争/工会 PVP 全空白） | **A+** | 买量/海外盘各 4 星，SLG 改造满星，三维合计 = A+ |
| **H 深海守望者** | ⭐⭐⭐⭐（克苏鲁氛围 Meta/Google 可投，国内版号需叙事本地化） | ⭐⭐⭐⭐（DREDGE 全球均匀渗透，日本走 App Store 强势） | ⭐⭐⭐⭐⭐（DREDGE 是单机叙事 RPG，多港/联盟/深海争夺全空白） | **A+** | 买量 + 海外盘各降 0.5 星（国内本地化工作量 + DREDGE IP 识别度 5% 而非 Pokémon 70%） |
| **I 动物联盟** | ⭐⭐⭐⭐（公益叙事全合规，WWF 合作真捐绑定） | ⭐⭐⭐⭐（欧美 + 港澳台 + 东南亚全覆盖，女性玩家加分） | ⭐⭐⭐⭐（从"纯救助"加"偷救叛逆"后 SLG 空间打开，但仍弱于 E/H） | **A** | 三维都是 4，但缺乏"必杀亮点"没法冲 A+ |
| **C 地下拳馆** | ⭐⭐⭐（暴力内容需软化 TikTok 可投 / Meta 限投） | ⭐⭐⭐⭐（英语区 Undisputed 13K 条证明有盘，但 60% 好评说明硬核路线风险） | ⭐⭐⭐⭐（拳馆经营+签约+出赛 SLG 化空间 OK） | **B+** | 暴力合规拉到 3 星触发降档 |
| **B 极权公寓** | ⭐⭐⭐⭐（Beholder 主题西方可投，国内严管） | ⭐⭐（俄语 38.8% > 英语 13.4%，彻底区域化陷阱） | ⭐⭐⭐⭐（Beholder 是单人抉择游戏，SLG 空间大） | **B** | 海外盘只有俄语区，打不了欧美日韩，两维 3 星以下 |
| **D 毒枭原味** | ⭐（Meta/Google/AppLovin/Unity Ads 四大渠道全部禁投 + iOS/Google Play 100% 拒审） | ⭐⭐⭐⭐⭐（Schedule I 45.9 万峰值是数据最强的原型） | ⭐⭐⭐⭐⭐（Schedule I 骨架可迁移） | **D** | 海外盘+SLG空间都是 S 级，但合规一票否决直接拉到最低档 |

> **维护要点**：这张 scorecard 的三维分数**来源必须写在网站上的"为什么降级/为什么升档"句子里**，不是内部黑箱。否则下次评审或老板问"为什么是 A+ 不是 A"时没依据。

#### 3.5.2 打档的"硬边界"清单（什么时候必须降档）

下面列出的条件，命中任何一条就**自动触发降档**，与三维打分无关：

| 硬边界 | 触发条件 | 自动降档到 |
|---|---|---|
| **主渠道禁投** | Meta / Google Ads / AppLovin / Unity Ads 中任何 2 家政策全面禁投 | 直接 D 档（方向 D 的依据） |
| **iOS/Android 100% 拒审** | Apple App Review Guideline 或 Google Play Content Policy 有明确对标禁止条款 | 直接 D 档（方向 D 的依据） |
| **区域完全偏斜** | 英语区评论 < 20% 或 某一非英语语种 > 30%（Beholder 俄语 38.8%） | 至少降到 B 档 |
| **原作已是重度 SLG/TBS** | 原作已有联盟/PVP/多城扩张 | SLG 改造维降到 ≤3，连带整体档位降 |
| **IP 识别度过低** | Newzoo / Google Trends 上原 IP 识别度 < 10%（DREDGE 5%） | CPI 溢价 30%-50%，档位降 0.5（H 从"应该 S 级"降到"A+"） |

### 3.6 评审框架 v4.2 精简说明（9 维 → 7 维，为什么、怎么重算）

**触发原因**：业主在 2026-04-20 下午提出「第 8、9 两维不应决定立项 PASS/REJECT」，原因如下：

- 第 8 维「落地-团队/排期/预算」属于**执行阶段**判断，立项阶段团队与预算可能还在谈判，不应在立项评审里决定 PASS/REJECT；
- 第 9 维「演讲-PPT 表达力」属于**演示层**，与内容质量无关，同一份内容可以不断迭代表达。

**保留的 7 维核心**（按 §II 矩阵列顺序）：
1. 战略-题材匹配度
2. 玩法-核心循环
3. 玩法-时间节点
4. 玩法-阶段过渡
5. 商业化-付费/留存
6. 风险-题材/合规
7. 美术/配色/素材

**重算规则**：
- 旧 9 维是**加权平均**（权重未公开，但各项目已有 4.16 / 4.09 / … 这些锚点）。
- 新 7 维改为**简单均值**（透明、可复算），即 `sum(7 项得分) / 7`。
- 降级的「落地-团队/排期/预算」和「演讲-PPT 表达力」不丢弃，降级到每个项目的 P0 清单中作为执行项跟踪。

**本次重算结果（旧 → 新）**：

| 方向 | 旧 9 维加权 | 新 7 维均值 | 排名变化 | 原因 |
|---|---|---|---|---|
| A 港口开箱 | 4.16 | **4.26** | 1 → 1 | — |
| G 禁酒令 | 4.09 | **4.17** | 2 → 2 | — |
| **I 动物联盟** | 3.89 | **3.94** | 4 → **3 ⬆** | I 的落地（3.0）拖分，7 维版本抹掉这个短板后上浮 |
| **E TCG 卡店** | 4.05 | **3.91** | 3 → **4 ⬇** | E 的「演讲 4.6 ⭐」是原 9 维的亮点，7 维版本失去加分 |
| H 深海守望者 | 3.53 | **3.46** | 5 → 5 | — |
| D 毒枭原味 | 2.78 | **2.69** | 6 → 6 | — |

**维护要点（下次评审前必读）**：
- 如果下次评审新增维度（比如"用户获取成本模型"），**要先确认这一维是不是立项阶段可判断的**。如果是执行阶段才能谈的，就不应该进加权总分，只应进 P0 清单。
- 如果业主/评委会决定「恢复 9 维」或「新增第 10 维」，按同样规则回填 §II 矩阵与 §I Summary 表，并在 footer + disclaimer 上写明版本号递进（v4.2 → v4.3）。
- 每次维度变更都要同步改三个文件：
  1. `ppt-master/projects/review-summary.md` §II 的矩阵与 §I Summary
  2. `steam原型数据分析.html` 第四部分的 `.dim-matrix-table` 与 `.summary-table` 与 `.verdict-grid`
  3. 本文档 §3.6（加一条「v4.3 变更」记录）

---

## 4. 页面结构（Which Section Does What）

打开 `steam原型数据分析.html`，从上到下分为以下区块，每块说明其"信息需求"和"维护时该改哪里"：

| 序号 | 区块名 | 信息需求（UX 目的） | 维护时要改的地方 |
|---|---|---|---|
| H1 | 标题 + disclaimer bar | 第一眼告诉读者"这是真实数据不是拍脑袋" | `<h1>` + `.data-disclaimer` 文案 |
| S1 | 顶部 summary-bar（4 张统计卡） | 3 秒内传达：8 款原型 / 44.5 万评论 / 峰值 45.9 万 / 5 推荐 2 谨慎 1 不推荐 | `.summary-bar .stat-card .value` 数字 |
| S2 | legend-bar 图例 | 说明颜色语义（绿推荐 / 黄谨慎 / 红不推荐），对应 UI 原则"渐进式展示 + 反馈引导" | `.legend-bar` |
| **§一** | 8 款原型卡片 + 饼图 | 每款给出元数据 + Steam 语言分布 + 核心洞察 + 交叉验证链接 | 每张 `.proto-card`；对应 Chart.js `new Chart(...)` 初始化数据 |
| **§二** | 地区汇总大饼图 | 把 8 款原型的语言数据聚合，给出"英语永远是主盘"的总体结论 | `overall` JS 对象 + `.proto-card` 下的 `.proto-analysis ul` |
| **§三** | 方向总览表格 + 8 个方向详细卡片 | 决策用：按档位给出每个方向的"参考原型 / 合规 / 海外盘 / SLG 空间" | `<table>` 行；`.direction-block` 块；v4 起新增「立项评审」列 |
| **§四** | 立项评审进展（v4 新增） | 把 PPT 评审结果同步到原型分析页，形成 "Research → Proposal → Review" 全链路可见 | 新章节，维护时同步内部评审汇总 |
| 结尾 | 核心洞察 6 条 + 数据来源 + footer | 沉淀复用到新方向立项 | `.insight-card ul`；`.data-source-box .cite-list` |

---

## 5. 与 PPT Master Projects 的对照（全链路索引）

网站讲的是"原型 → 方向"的判断；PPT Master 工程则是"方向 → 立项 PPT → 评委会评审"的落地。两边必须互相对齐。

**v4.2 列顺序按 7 维均分排名 A > G > I > E > H > D**。

| 网站方向 | 对应 PPT 工程目录 / 链接 | 7 维均分 | 旧 9 维 | 评审裁决 | P0 待改数 |
|---|---|---|---|---|---|
| S+ 方向 A 港口开箱 | [`ppt-master/projects/A_港口开箱_...`](https://docs.google.com/presentation/d/1TAKXJiJcD-EuYpHrij9HnDZSRET3OxmS/edit?usp=sharing&ouid=110387310515616113298&rtpof=true&sd=true) · 文档名 `A_港口开箱_v4_含评审优化` | **4.26** | 4.16 | ⚠️ CONDITIONAL PASS | 4 |
| S 方向 G 禁酒令 | [`ppt-master/projects/G_禁酒令私酒帝国_...`](https://docs.google.com/presentation/d/1yzqprKv5d_heJeEEVsix4qnOjpc6jWov/edit?usp=sharing&ouid=110387310515616113298&rtpof=true&sd=true) | **4.17** | 4.09 | ⚠️ CONDITIONAL PASS | 5 |
| A 方向 I 动物联盟 ⬆ | [`ppt-master/projects/I_动物联盟_...`](https://docs.google.com/presentation/d/1NyFhmzUPGHLTeZWM3C_JsQiA8l7SqBEP/edit?usp=sharing&ouid=110387310515616113298&rtpof=true&sd=true) | **3.94** | 3.89 | ⚠️ CONDITIONAL PASS | 5 |
| A+ 方向 E TCG 卡店 ⬇ | [`ppt-master/projects/E_TCG卡店帝国_...`](https://docs.google.com/presentation/d/1-zja9e5Ad8v6vztUYACPL-b0yFAgYa3v/edit?usp=sharing&ouid=110387310515616113298&rtpof=true&sd=true) | **3.91** | 4.05 | ⚠️ CONDITIONAL PASS | 5 |
| A+ 方向 H 深海守望者 | [`ppt-master/projects/H_深海守望者_...`](https://docs.google.com/presentation/d/1wyVGT_4AHho2nLCSxKxdV1pX1w-gfes4/edit?usp=sharing&ouid=110387310515616113298&rtpof=true&sd=true) | **3.46** | 3.53 | ⚠️ CONDITIONAL PASS | 6 |
| B+ 方向 C 地下拳馆 | *（暂未立项）* | — | — | — | — |
| B 方向 B 极权公寓 | *（暂未立项）* | — | — | — | — |
| **D 方向 D 毒枭原味** | [`ppt-master/projects/d_nightking_empire_...`](https://docs.google.com/presentation/d/1KzZhURtjFFSqMVJm5bS9W74G4z4TEV_M/edit?usp=sharing&ouid=110387310515616113298&rtpof=true&sd=true) · 文档名 `d_nightking_empire` | **2.69** | 2.78 | ❌ **REJECT** | 8（结构性否决） |

> **注**：档位（S+ / S / A+ / A / B+ / B / D）由 §3.5 三维规则决定，与加权总分是两套体系。档位 A+ 的 E 不因 7 维均分降到 3.91 而改档（档位看的是"买量合规 / 海外盘 / SLG 改造"），只是**推进优先级**顺序在 7 维均分上 I 排到 E 前面。

**关键共性问题**（≥2 项目都被评委点名，需要 skill 层面强化的 · v4.2 已删除"落地"一行）：

| 共性问题 | 命中项目 |
|---|---|
| 风险-题材/合规 | A / D / G / H |
| 战略-题材匹配度 | D / H |
| 玩法-阶段过渡 | D / H |
| 商业化-付费/留存 | D / E / H |

> v4.2 说明：「落地-团队/排期/预算」（原 6/6 全中）已从评审框架移除，相关问题降级到各项目的 P0 清单中作为执行项跟踪，不再作为**立项阶段**的共性问题展示。

评审复审节点统一是 **2026-05-04**，届时原型数据可能还要对齐新的评审结论再做一次修订。

---

## 6. 维护 Checklist（每次更新按这个单走）

### 6.1 添加新原型

1. 确定目标 Steam AppID，找到其 store 页面。
2. 用 Steam 评论过滤器逐语言抓取真实计数（需要耐心一个一个切语言筛选）。
3. 记录峰值在线（SteamDB）+ 销量区间（SteamSpy）+ 好评率 + 发售日期 + 发行商。
4. 在 §2.2 登记表新增一行。
5. 在 HTML 里拷贝已有的 `.proto-card` 结构，修改以下字段：
   - `.proto-icon` 的 `src` → `https://cdn.cloudflare.steamstatic.com/steam/apps/<AppID>/capsule_184x69.jpg`
   - `.proto-title a` → 跳转到 Steam store 页
   - `.proto-subtitle`、`.proto-scheme-tag`、`.proto-metrics`、`.proto-analysis`
   - `.cross-ref` 的交叉验证链接
   - 底部对应的 `new Chart(...)` 初始化（复制一份 + 换 canvas id + 换数据）
6. 更新顶部 `summary-bar` 的「核心原型」计数。

### 6.2 添加新方向

1. 确保该方向已经有至少 1 款对应 Steam 原型（否则数据支撑不足，先补原型再写方向）。
2. 按三维打档规则（§3.5）给出档位 + 档位颜色。
3. **同步填 §3.5.1 scorecard**：把新方向的「买量合规 / 海外盘 / SLG 改造」三维分数与"关键拐点"一句话理由落盘。跳过此步等于把结论黑箱化，下次评审必然被追问。
4. **过一遍 §3.5.2 硬边界**：命中任一条就自动降档，不要"因为项目好感硬撑档位"。
5. 在 §0.3.3 的"原型 → 方向映射表"加一行，说明新方向的爽点/IP/骨架来源。
6. 在 §3 总览表格 `<table>` 里新增一行。
7. 在详细卡片区新增一个 `.direction-block`，填：
   - title / subtitle / 数据支撑 / 为什么选它 / SLG 改造方向 / 目标市场 / 风险点
8. 如果该方向已有对应 PPT 工程，加上 ribbon 指向 `ppt-master/projects/<目录>` 并附评审分。

### 6.3 更新评审结果（v4 后每次）

1. 读 `ppt-master/projects/review-summary.md` 的最新版（加权分、裁决、P0 清单都在里面）。
2. 更新 §3 总览表格的「立项评审」列。
3. 更新每个方向卡片底部的 review ribbon（P0 条数、最紧迫问题）。
4. 更新 §四「立项评审进展」章节的总分排序和共性问题汇总。
5. **如有维度变更**（如 9 维 → 7 维 / 新增维度），按 §3.6 的规则同步三个文件（review-summary.md / HTML / 本文档）。
6. **同步 PPT 工程链接**（v4.2 起）：如果 PPT 文件新建或重命名，更新 §5 对照表的 Google Slides URL，并同步到 HTML 的以下三个位置：
   - 方向总览表（§三）每行方向名的 `<a href>`
   - 每个 `.direction-block` 底部 review-ribbon 的 "PPT 工程" 名链接
   - §四 Summary 表格 + verdict-grid + dim-matrix-table 表头的 6 个链接
7. footer 版本号 +1（如 v4.1 → v4.2），写清本次变更要点。

### 6.4 数据年度巡检（每 6 个月做一次）

Steam 评论数是持续增长的，数据有半年以上就会明显过期。巡检时：

1. 重拉每款原型的 Steam 评论总数、峰值在线、好评率，对比 §2.2 登记表。
2. 若某款原型的评论数增长 ≥ 30%，重新拉一次完整语言分布（因为语言占比会随玩家盘扩张而漂移）。
3. 检查 DREDGE+ / Schedule I 等移动端状态是否有新动作（新区域上架、新奖项）。
4. 检查 Meta / Google / AppLovin / Unity Ads 的广告政策有无更新（方向 D 的"致命级合规判决"依赖这些政策条款）。
5. footer 版本号 +1。

### 6.5 发布流程

```bash
# 1. 本地修改完 HTML
open steam原型数据分析.html    # 肉眼先扫一遍是否有结构破损

# 2. UTF-8 校验
python3 -c "open('steam原型数据分析.html','rb').read().decode('utf-8')"

# 3. 推到 RUN Platform（见同目录 README.md 的 SOP）
#    通常是 ssh 进容器，然后 bash start.sh 拉起（端口 8000 → 外部）
```

---

## 7. 常见陷阱与规避

| 陷阱 | 规避 |
|---|---|
| **Steam 语言分布数据被按"评论主语言"而非"玩家地域"统计** | 所有文案都写"语言分布"而不是"地区分布"；地区推断需要在 insight 里写清楚（如英语 = 北美 + 欧洲 + 澳新） |
| **把 Steam 数据当移动端数据用** | 方向 H（DREDGE）一次踩坑：Steam 日语 0.53% 但 DREDGE+ 在日本 App Store 是王炸。凡涉及"打日本"或"打东南亚"结论，必须去对应 App Store / Google Play 国别榜交叉 |
| **用 Chart.js 展示占比时只显示百分比不显示绝对值** | 本页已经在 `makeTooltip(total)` 里强制同时显示"占比 + 具体评论数"，后续添加新图表时必须复用这个函数 |
| **对方向 D 的判决用"软话术"** | 方向 D 必须用"致命"、"不推荐直接对标"、"坚决不碰"这种强表态，否则评委 / 策划会误以为"加一点处理就能上"。Meta / Google Ads 的政策条款必须用原话引用 |
| **中文 .md 文件用 Cursor Write 工具落盘导致 latin-1 乱码** | 参见 `docs/lessons/Cursor写中文乱码_CURSOR_WRITE_LATIN1_BUG.md`。本文档、未来新增文档都用 Python heredoc + `write_bytes(s.encode('utf-8'))` |

---

## 8. 下一步（Roadmap）

### 近期（2 周内，配合 2026-05-04 评审复审）
- [ ] 评审复审后，再同步一次 review-summary.md 到本页 §四
- [ ] A / G / E / H / I 的 P0 改完后，ribbon 里的"待改条数"应同步降为 0
- [ ] 如果 D 方向彻底出局（REJECT 无复审），从总览表把它挪到「已否决」区块，但保留合规判决那段作为反面教材

### 中期（3 个月内）
- [ ] 补 §五「跨原型机制矩阵」：把 8 个原型的"拆包 / 经营 / 叙事 / PVP / 放置"5 种机制做成矩阵表
- [ ] 每个方向补「替代原型 Plan B」列，防止 A/B/C 级原型下架或凉透之后无替补
- [ ] 加上「女性玩家占比」维度（依据广告 ID 审计或 Newzoo 报告）

### 长期（半年+）
- [ ] 本页数据抽出成单独的 `data.json`，HTML 变成纯渲染层，方便接入 dashboard 做趋势图
- [ ] 增加 A/B 测试字段：对每个方向标注"已上线参考 vs 预测"，回归迭代数据决策模型

---

## 9. 相关文件索引

- 页面本体：`steam原型数据分析.html`（同目录）
- 部署脚本：`start.sh` · `.runplatform.json`
- 部署说明：`README.md`（RUN Platform SOP）
- 下游 PPT 工程：`~/Desktop/Git/ppt-master/projects/`（6 个项目目录 + `review-summary.md`）
- 上游立项方案：`~/Desktop/Git/personal-assistant/丁开心的游戏观察/drafts/SLG专题/立项方案/`
- 跨设备同步踩坑：`~/Desktop/Git/docs/lessons/工作区跨设备同步_WORKSPACE_CROSS_DEVICE_SYNC.md`
- 中文 .md 写盘陷阱：`~/Desktop/Git/docs/lessons/Cursor写中文乱码_CURSOR_WRITE_LATIN1_BUG.md`

---

_最后更新：2026-04-20（v4 · 同步 PPT 评审结果）_
