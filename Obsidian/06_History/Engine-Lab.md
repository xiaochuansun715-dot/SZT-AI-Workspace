# Engine-Lab 历史证据资料

导入：2026-10-29。来源为既有会话摘要，不是全部原始聊天。仅按需检索；较新的纠错与项目现状优先。
历史交易确认仅对当次有效，不能继承为新操作授权。

## 2026-10-18T04-25-24-VNwa-engine_simulator_project_and_ipa_download.md

thread_id: 01a14d41-dd0c-71e2-8741-b1315e2de766
updated_at: 2026-10-18T04:58:21+00:00
rollout_path: C:\Users\Administrator\.codex\archived_sessions\rollout-2026-10-18T12-25-24-01a14d41-dd0c-71e2-8741-b1315e2de766.jsonl
cwd: \\?\D:\GPT\引擎模拟器

用户要求加载昨天的引擎模拟器、安装 majd/ipatool 并尝试下载 App Store 的“引擎模拟器”IPA，随后要求整理为 Codex 项目。工作目录最终为 `D:\GPT\引擎模拟器`，本地项目已创建，用户确认当前聊天也已在项目中，昨天的引擎制作聊天已归入。172 个文件从旧目录复制并逐个进行 SHA256 校验，源文件保留；模拟器已从新目录启动并验证 HTTP 200。ipatool 2.7.0 Windows x64 已安装，压缩包 SHA256 已核对。目标应用为 App Store ID `6818613440`、Bundle ID `com.madmax.enginesimulator`。下载过程中先后处理了 Apple 登录、本地 keychain 解锁和免费许可问题；加密凭据备份已保留且校验通过，未读取凭据内容。最终 IPA 下载成功，文件为 `D:\GPT\引擎模拟器\downloads\ipa\EngineSimulator-6818613440.ipa`，版本 1.0.7、构建 14、77,707,801 字节；ZIP 65 个条目通过 CRC，主程序和包标识验证通过，SHA256 为 `5443e3118b8161802f866fdda9b60f6a63ab4abc8913884046a1fdf99cb071da`。校验记录位于项目 `docs/ipa-verification.json`，说明位于 `outputs/IPA下载与校验.md`。尚未开展原应用代码分析或解密，电脑试玩版仍应视为独立实现而非官方 Windows 版或完整复刻。


---

## 2026-10-18T04-58-57-hYuY-ipad_wda_control_and_engine_simulator_rebuild_20261018.md

thread_id: 01a14d60-927c-73b3-99d1-9ab6408c9b78
updated_at: 2026-10-18T11:49:50+00:00
rollout_path: C:\Users\Administrator\.codex\archived_sessions\rollout-2026-10-18T12-58-57-01a14d60-927c-73b3-99d1-9ab6408c9b78.jsonl
cwd: \\?\D:\GPT\引擎模拟器

在 D:\GPT\引擎模拟器 中，用户先要求用 REA 基于已有 IPA 迭代引擎模拟器。IPA 被确认是加密 Unity 包；可解析资源包括 443 段发动机音频、13 段爆音、5 段启动素材及 24 个精确 profile。项目完成 1.3 版：长按启动/松手取消、启动参数、点火时序同步、排气门修复、真实音源接入；34 项测试和浏览器验收通过，但原生代码、动力公式和 DSP 仍是独立实现，不能称为完整复刻。随后用户指出实验室不能换挡。1.4 版重做传动，支持 N 和 1–8 挡、离合、手动/自动换挡；40 项测试及实测通过，N 挡轰油不驱动车辆，升降挡会改变转速。用户要求 IPA 解密；实测 iPad8,1/iPadOS 18.7、开发者模式和配对正常，但原 App debuggable=false，未越狱，REA/普通开发者模式无法导出明文。后来通过 GitHub 查找 iLoader 2.3.10 替代爱思；爱思 8.60 仍在 Apple token/plist 认证阶段失败。iLoader 初始包触发 XCTest 插件 Bundle ID 校验，生成兼容版后又被 AMFI 拒绝，原因是 MH_BUNDLE 测试插件被赋予主程序 entitlements。最终将完整 WebDriverAgentRunner.xctest 从 PlugIns 移到 Frameworks，保留原生文件字节，使用明确 XCTest 路径启动；用户完成 iPad 开发者信任，开发者镜像挂载，WDA ready=true。已实际读取并点击原 App，在“发动机工坊”“变速箱·车辆”“驾驶与仪表”之间切换，截图逐张检查，最终恢复驾驶页；WDA/XCTest 会话关闭且 8100 端口不可达。证据和报告位于 outputs/iPad真机控制验证.md、work/advance-20261018/wda-runtime/visual-verification.json；最终 WDA 包为 outputs/WDA准备签名/WebDriverAgent-v16.14.0-测试插件签名修正版.ipa，SHA256 1bbd31fbce9f31fc3b433888d09031e504447f59e6020b2058826bc2cf8e8966。原 IPA SHA256 5443e3118b8161802f866fdda9b60f6a63ab4abc8913884046a1fdf99cb071da，未修改；IPA 仍未解密，未取得原生方法体或原 DSP。


---

## 2026-10-18T11-50-40-7Tax-engine_simulator_structured_snapshot_replica_v1_5_github_upl.md

thread_id: 01a14ed9-8639-7881-bb01-881dbc970e91
updated_at: 2026-10-20T09:41:22+00:00
rollout_path: \\?\C:\Users\Administrator\.codex\sessions\2026\10\18\rollout-2026-10-18T19-50-40-01a14ed9-8639-7881-bb01-881dbc970e91.jsonl
cwd: \\?\D:\GPT\引擎模拟器

在 D:\GPT\引擎模拟器 中，用户明确选择“不越狱”，并授权继续使用已连接 iPad 研究原作。已确认原 IPA（com.madmax.enginesimulator，1.0.7/build 14）仍 cryptid=1、未解密；REA 6.7.0 在 Windows 解包成功但无法对该 Mach-O 做原生反编译。用户随后要求以真机行为和数据推进复刻，而非继续解密。

已通过 WDA/pymobiledevice3 采集原作三个主界面（驾驶与仪表、发动机工坊、变速箱·车辆）在熄火和怠速状态的向下页面，共核读 76 张、交付 75 张截图；记录了启动、仪表、气流、温度、电压、燃油、逐缸剖面、波形、诊断、齿比和道路设置。最终原机状态已确认熄火、N 挡、0 RPM、0 油门、0 车速、0.00 km。控制中心遮挡截图未作为证据。用户手动在“文件-App-我的 iPhone-引擎模拟器”导出两份 JSON；通过 HouseArrest/VendDocuments 只读取得，格式 noi-box-backup v1，当前 V8，170 组配置，两份除时间字段外一致。原始导出保存在本机，未上传 GitHub。

已生成结构化快照 `outputs/iPad结构化快照-20261019/`：75 个快照、207 个字段、460 条带截图来源的读数、10,213 个原生 JSON 叶节点、71 个界面/原生字段对应、SQLite 查询索引；校验包括文件摘要、SQLite 完整性、模式检查和查询，均通过。快照明确区分原厂生效双涡轮与开放表单单涡轮、原生自动换挡阈值 null 与界面显示 6984/3960，并保留不确定性边界。

用户随后要求“复刻迭代”。已在 app/ 完成 1.5 版，先备份至 `archives/app-v1.4-before-v1.5-20261020/`，接入最新 V8 参数，新增驾驶/工坊/车辆三页、24 个仪表（主转速+核心表+19 小表）、油压/油温/真空、燃油/电池/电压/油耗/气流、补给、速度诊断、可编辑齿比/终传/轮胎/效率/质量/阻力/路面等。补给需完全停机且不重置健康、温度或里程；动态公式、温度、油耗、损坏、传动、混音仍是独立近似实现。原机可见 V8 预测峰值 574 PS、700 N·m、511 wheel PS 被作为曲线锚点，但不代表恢复了原始 DSP 或完整公式。`node --test` 58/58 通过；Edge 16 组交互、3 页×5 种宽度、无脚本错误/外部请求通过；75 项参考字段对照和 169 个可玩模型有限性检查通过；本地 400 m 结果约 10.88 s，仅为本版模型结果。交付：`outputs/引擎工坊-1.5-原机数据迭代版.zip`、`outputs/复刻迭代-1.5-说明.md`及预览图；本地服务确认监听 `127.0.0.1:4328`，版本 1.5.0。

用户要求先上传 GitHub。已确认账号 `xiaochuansun715-dot`、既有私有仓库 `xiaochuansun715-dot/engine-lab`、默认分支 main 和写权限；用户此前要求保留历史、只新增文件，并排除原始备份/IPA/录屏/运行日志/验证记录。按此范围新增 `engine-lab-v1.5/` 目录 60 个文件：程序、处理后的 `phone-current-data.json`、必要音频/三维素材和许可文件；未上传原始手机 JSON。上传副本 50 项测试及 4 项浏览器检查通过。使用 expected SHA 的非强制更新，旧树全部保留；提交 `fcefe11a8297aeafedbfcaf80d5a515d3f9a0115`，父提交 `6bdc29c7111888aa214983862027de0940e3854d`，新树 `dabf65185e3d1f73179b4d0e40f4981915348a08`。已读回仓库可见性（private）、main HEAD、`package.json`、README 和 app.js；仓库链接为 `https://github.com/xiaochuansun715-dot/engine-lab/tree/main/engine-lab-v1.5`。


---

## 2026-10-19T12-10-28-mMLD-ipad_race_and_drag_results_project_record.md

thread_id: 01a15412-0270-7bd1-968f-577c2b7ad8a9
updated_at: 2026-10-19T17:22:11+00:00
rollout_path: C:\Users\Administrator\.codex\archived_sessions\rollout-2026-10-19T20-10-28-01a15412-0270-7bd1-968f-577c2b7ad8a9.jsonl
cwd: \\?\D:\GPT\引擎模拟器

项目目录 D:\GPT\引擎模拟器 中实际操作了 iPad 原作。综合赛道（1 圈、2.3 km）起步后最高约 92 km/h，进入首个左直角弯时冲出赛道，游戏判定该圈不计最佳，未完成有效圈。400 米直线加速赛完成并获胜：玩家 10.93 秒，AI 原厂车 11.27 秒。结果已写入 outputs\iPad原作赛道与直线加速赛实测记录-20261019.md，证据截图位于 work\race-play-20261019\runs\20261019T123711213247Z\；WDA 会话随后关闭，未修改调校或设备设置。用户随后询问项目内新对话能否读取该文件；已确认“引擎模拟器”为本地项目，项目内新对话可访问主文件夹中的文件，但各对话 transcript 独立；项目外对话不保证能访问本地文件。


---

## 2026-10-20T09-41-28-Oy2G-wechat_miniprogram_feasibility_engine_simulator.md

thread_id: 01a158af-f475-7b43-bd3d-9849222fa5fe
updated_at: 2026-10-20T09:43:16+00:00
rollout_path: C:\Users\Administrator\.codex\sessions\2026\10\20\rollout-2026-10-20T17-41-28-01a158af-f475-7b43-bd3d-9849222fa5fe.jsonl
cwd: \\?\D:\GPT\引擎模拟器

用户询问现有《引擎模拟器》是否能放入微信小程序。工作目录为 `D:\GPT\引擎模拟器`。检查显示当前项目是本地离线 Web 应用 `app/`（`package.json` 版本 1.5.0），入口由 Node 服务运行在 `127.0.0.1:4328`；使用 HTML/CSS/ES modules、Three.js/WebGL、Canvas、Web Audio/AudioWorklet、`localStorage` 和本地音频/JSON 参数数据。结论是可以接入，但本机地址不能直接被微信访问，且本轮没有修改源码或创建小程序工程。建议优先将 H5 部署到 HTTPS 域名，再以小程序 `web-view` 加载；上线需配置业务域名并验证 3D、实时音频、触屏交互和本地保存能力。原生小程序方案需要重写页面及部分浏览器能力，模拟逻辑和参数数据可复用。还提醒公开上线前需确认从 IPA 提取音源的授权范围。官方文档检索未成功直接打开，相关结论主要来自项目代码检查及搜索结果，因此具体 API 兼容性仍需真机验证。

