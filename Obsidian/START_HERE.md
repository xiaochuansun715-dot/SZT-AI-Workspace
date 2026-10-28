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
