---
type: project
recorded: 2026-10-28
source_date: 2026-10-28
status: connection-unavailable
---
# InstaBox 共享办公区

来源：历史聊天“记录 INSTABOX 服务器申请通过”，聊天 ID 01a18073-d086-7432-896a-2bbc396d0352；本次读取本机办公区说明与 remote.py。
本机项目：D:\INSTABOX。历史云端工作台：/data/home/shared-office；共享目录：/data/workspace/team-office。

## 已有结论

历史记录显示 Codex 与 Muse 均实际读写过共享目录并生成验收回执；Hark、GPT 未有实际接入证据。
聊天上下文不会自动同步，项目结论应写入交接。成员署名不是安全隔离。
云端目录分为 projects、workspaces、artifacts、receipts。修改前应先领取自己的任务并读服务器 AGENTS.md。
本机入口 http://127.0.0.1:8765 依赖本机工作台与连接；免费服务器可能暂停，不能当全天在线服务。

## 本次核验与限制

2026-10-28：本机工作台健康检查不可达；已有 remote.py 无法复用 SSH 隧道。
因此本次未在服务器创建或核验知识库，未登记其他 AI 已接入。
未部署 VPN、未开放公网管理端口、未绕过暂停限制。

## 下一步

恢复既有安全连接后，读取服务器与 team-office 的 AGENTS.md；核验目标目录不存在冲突后部署知识库到 projects/ai-memory/Obsidian。
将 GitHub 作为主本，服务器仅作授权读取/协作副本，避免独立改动而形成两个主本。
不把 SSH 登录信息写入知识库或聊天；不向其他助手自动发消息。
