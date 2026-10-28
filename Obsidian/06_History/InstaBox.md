# InstaBox 历史证据资料

导入：2026-10-29。来源为既有会话摘要，不是全部原始聊天。仅按需检索；较新的纠错与项目现状优先。
历史交易确认仅对当次有效，不能继承为新操作授权。

## 2026-10-28T03-00-36-cwcW-instabox_shared_office_muse_codex_ssh.md

thread_id: 01a18073-d086-7432-896a-2bbc396d0352
updated_at: 2026-10-28T04:07:30+00:00
rollout_path: C:\Users\Administrator\.codex\sessions\2026\10\28\rollout-2026-10-28T11-00-36-01a18073-d086-7432-896a-2bbc396d0352.jsonl
cwd: \\?\D:\INSTABOX

用户申请的 InstaBox 服务器已创建：默认 4 vCPU、8 GiB、20 GiB，免费版闲置 30 分钟或运行约 8 小时会暂停。用户希望把 Muse、Hark、GPT、Codex 接入共享办公区，并保留本机工作台，不购买 API；GPT 网页/客户端暂按复制交接文本参与。

在 `D:\INSTABOX` 创建并启动了本机公共办公区：`D:\INSTABOX\启动办公区.cmd`，入口 `http://127.0.0.1:8765`；包含任务看板、交接记录、共享文件、SSH 连接、CLI 工具和说明文档。数据初始保存在本机，后经 SSH 隧道切换到 InstaBox 云端 `/data/home/shared-office`。已验证 18 项隔离集成检查，以及任务并发领取、版本冲突、交接、文件下载、重启持久化和浏览器实际创建任务。

SSH 已连接并部署云端办公区，主机 `ssh.instabox.sh:2222`，机器 `instabox-senzeao`，Linux 6.18.54，4 CPU；使用了首次信任（TOFU）并固定指纹 `SHA256:DQYkbhc9iBYcfVvhXZBsT9qhzAyLvLIyjmm57Vimfxk`。出口定位参考为美国俄勒冈州 Boardman，明确不等于物理机房位置。

用户后来纠正：Muse 已经自行接入，之前助手把接入工作错误地留给了用户。随后在云端建立 `/data/workspace/team-office`，保留既有改动，加入 `AGENTS.md`、`README.md`、`join.py`、项目/成果/回执目录和 Muse 接入说明。Codex 与 Muse 均已实际读取任务、读写共享目录、生成回执、提交接入记录和交接；Muse 回执 `/data/workspace/team-office/receipts/Muse-20261028T040256Z-8cb087fd.json` 已独立核验，协作验收任务标记完成。已验证成员为 Codex、Muse；Hark、GPT 尚未实际接入。

VPN 未部署；此前查到公开 VPN/代理中继受服务限制且免费机器不适合长期在线。最后用户询问关机影响：当前本机工作台和本机持有的 SSH 隧道会停止，云端文件/任务会保留，但 InstaBox 自动暂停仍可能中断服务；Muse 自己的云电脑不依赖用户本机。OpenAI 官方资料支持“本地任务依赖电脑在线、Cloud 任务可在电脑睡眠时继续”，但本次并未把办公区改造成独立云端调度系统。

