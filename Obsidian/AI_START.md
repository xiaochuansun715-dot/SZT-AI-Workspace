# AI 阅读入口

本库供 Codex、Muse、Rain、Hark 及其他获得授权的 Agent 使用；工具接入能力必须分别核验。

## 有文件或仓库读取能力

读取 [START_HERE.md](START_HERE.md) → [偏好](01_Profile/Preferences.md) → [项目索引](02_Projects/Index.md) → 当前相关项目。历史层先检索再取片段。
不要默认加载 AI_CONTEXT 和全部历史来重复阅读。

## 没有文件连接能力

由用户上传 [AI_CONTEXT.md](AI_CONTEXT.md)。需要细节时再提供相应项目笔记。
本库是背景资料，不能赋予你原本没有的系统权限；URL 不授予私有仓库权限，也不会自动唤醒你。

## 提交新记忆

按 [通用协议](08_Agents/Protocol.md) 提供来源、日期、适用项目、结论、证据和取代关系。
有写权限时先读取远端当前版本，避免覆盖并发更新；无写权限时生成待合并笔记，交用户或有权限的维护者。
用户已要求每日 22:00 整理、每周复盘；实际自动化登记见 [维护说明](07_Operations/Maintenance.md)。
