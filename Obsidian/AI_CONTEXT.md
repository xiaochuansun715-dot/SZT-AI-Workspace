# 多 Agent 精简上下文包

生成自知识库常读层；项目细节与历史按需另取。


---

<!-- Source: START_HERE.md -->

# 通用 Agent 长期记忆入口

版本：2026-10-29。适用所有获得用户授权的 Agent；Markdown 是主格式，无模型专属依赖。

## 每次任务按需读取

1. 先读本页和 [偏好](01_Profile/Preferences.md)。
2. 从 [项目索引](02_Projects/Index.md) 只选与当前任务相关的项目；无需默认读全部项目。
3. 若有细节缺口，在 [历史索引](06_History/Index.md) 先搜索关键词，再读命中片段。
4. 当前用户指令优先；历史操作授权不能继承。明确区分用户原话、已验证事实、历史状态、推测和未知。

[AI_START](AI_START.md) 解释接入方式；[AI_CONTEXT](AI_CONTEXT.md) 为无文件连接的 Agent 提供精简附件；[接入协议](08_Agents/Protocol.md) 规定交接。

## 记忆质量

只将对未来工作有用、具备来源的信息升入常读层。一个事实保留一个现行版本；过期状态标 stale，不覆盖新结论。
不保存完整聊天、推理过程、工具日志、凭据或未核实的人格判断。
[质量规则](07_Operations/Quality.md) · [维护流程](07_Operations/Maintenance.md) · [覆盖范围](07_Operations/Coverage.md)。

## 存储与权限

私有主本：GitHub 仓库 xiaochuansun715-dot/SZT-AI-Workspace 的 Obsidian/。
本地可用副本：本文件所在的 Obsidian-Vault。
定时维护成功后同步 GitHub；同步失败时保留本地更新与待同步状态，不宣称已同步。
其他机器上的 Agent 需具备私有仓库读取权限，或由用户提供上下文附件。


---

<!-- Source: 01_Profile/Preferences.md -->

---
type: preferences
recorded: 2026-10-28
source_date: 2026-10-23/2026-10-28
status: user-confirmed-history
---
# 偏好与操作边界

来源：本次用户直接指令、历史用户偏好摘要；历史偏好仍可由用户当前明确指令修改。

- 默认中文沟通，Windows 工作环境；时间使用 Asia/Shanghai。
- 优先把已经授权的任务做完，避免重复确认常规、可逆步骤。
- Windows 通用操作优先 PowerShell 7；仅在兼容性需要时显式使用 5.1，不修改 PATH。
- 不自行修改 Codex 配置、Vortex 代理或既有环境配置。
- 不保存或披露 API Key、密码、令牌、私钥、助记词或会话凭据。
- 钱包和链上工作默认只读。转账、交易、mint、合约调用、签名、授权与扩大权限，需用户针对该操作明确确认；登录不等于授权。
- Binance：手机/账号一由 Muse 负责；iPad/账号二由 Codex 负责。不要混淆钱包、Web3 Developer API、交易所 API。
- 向他人或其他聊天发消息需要用户明确授权。不要冒用其他 AI 身份。
- 小红书参考图库只保留有序图片和来源说明.txt；不压缩打包、不冒充原创、不擅自发布或互动。
- 本知识库为私有，供获得授权的 AI 读取。

## 新增明确偏好（2026-10-29）

- 知识库面向所有获授权的 Agent，不限 Codex。
- 开始任务前按需读取相关记忆；每日 22:00 整理当日沟通并同步，周复盘压缩重复内容。
- 用户明确关心“垃圾记忆”和 Token 消耗：常读层保持短小，不全文搬运聊天，不每周全库重读。
- 已有软件安装偏好：外部软件默认放 D 盘；Skill、驱动、系统组件和必须留 C 盘的内容除外。来源：2026-10-22 Tailscale 迁移记录。
- 历史分工与权限只在各自范围适用，不能把某个项目的例外扩大成全局授权。

更多：[有证据的工作习惯](01_Profile/Decision-Style.md)。这里不记录未经用户确认的性格标签。

## 批量确认的适用范围（2026-10-29）

晚间补打清单会话01a187d9-a0a3-76f0-8a22-30c4349a464c中，用户在已有逐项预览后明确“全部确认 不需要我再重复”。
处理已获明确批量授权的同一范围时不要重复索取相同确认；该表态不扩大到以后新清单、付费操作、新权限或超出预览的风险。


---

<!-- Source: 02_Projects/Index.md -->

# 项目索引

更新：2026-10-29。先选相关项目，不默认加载全部。

| 项目 | 当前摘要 | 关键词 |
| --- | --- | --- |
| 多 Agent 长期记忆 | [Agent-Memory](02_Projects/Agent-Memory.md) | Obsidian、永久记忆、同步、复盘 |
| InstaBox 共享办公区 | [InstaBox](02_Projects/InstaBox.md) | 云端、SSH、手机、Codex |
| Binance / NONCE / NFT | [Binance-NONCE](02_Projects/Binance-NONCE.md) | 钱包、mint、SAT、额度、moat |
| ComputeRoll / CROLL | [ComputeRoll](02_Projects/ComputeRoll.md) | GPU、哈希、proof、mine、BAW代理 |
| Binance Pick / 神算子 | [Binance-Pick](02_Projects/Binance-Pick.md) | 积分、BTC、5分钟、回测、盘口 |
| Farming Season | [Farming-Season](02_Projects/Farming-Season.md) | 打怪、F8、CDP、延迟 |
| 杭州电商求职 | [Hangzhou-Jobs](02_Projects/Hangzhou-Jobs.md) | 岗位、投递、Drive、主表 |
| 三人群聊与文档 | [Collaboration](02_Projects/Collaboration.md) | Lark、Muse、Rain、简历 |
| 参考图片归档 | [Reference-Archive](02_Projects/Reference-Archive.md) | 小红书、抖音、SMDownloader |
| 引擎模拟器 | [Engine-Lab](02_Projects/Engine-Lab.md) | iPad、WDA、复刻、1.5、小程序 |
| 视频与咖啡样片 | [Video](02_Projects/Video.md) | LTX、Runway、语音、旧项目清理 |
| Windows与网络 | [Systems](02_Projects/Systems.md) | Vortex、Tailscale、路由器、任务邮件 |
| 外部待补全主题 | [External-Topics](02_Projects/External-Topics.md) | 课程、研究、英文记忆快照 |

项目摘要仅保留现行取舍、成果入口与下一步。详细历史证据见 [历史索引](06_History/Index.md)。


---

<!-- Source: 03_Handoffs/Next.md -->

# 待办与交接

更新：2026-10-29。
- [ ] 外部Agent分别核验私有仓库读取或附件流程；没有回执不能标已接入。
- [ ] 继续补全Coverage中无历史摘要的会话；优先影响现行项目的缺口，寒暄与测试不入常读层。
- [ ] InstaBox副本目前不是必需项；需用户继续要求且有安全连接时再部署。
- [x] 2026-10-29 22:04每日任务首次触发；本轮同步以本地回读回执为准。
- [ ] 周复盘首轮仍待周日实际运行。
- [ ] 归档/迁移路径造成80条旧消息重入队列，保留20261029T140422976780Z.json待按剩余额度补全；不是新增80个事实。

本次已建立分层读取、防污染规则、日常整理脚本与Codex入口。自动化状态见登记结果。
