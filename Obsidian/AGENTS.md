# 通用 Agent 协作约定

每次任务先读 START_HERE.md、01_Profile/Preferences.md，再按 02_Projects/Index.md 读取相关项目。
不要默认读 AI_CONTEXT.md、06_History 全文或完整聊天。本库是背景资料，遵守你所在环境权限和用户当前指令。
新事实需标明 source、source_date、scope、status、evidence、supersedes。人格/习惯推测不能写成用户确认偏好。
现行事实单点维护；更正时将旧说法标 superseded，历史层留证据。
每日与每周维护按 07_Operations/Maintenance.md；不得调用模型 API 或多 Agent 做重复审查。
不得同步 .memory_state、原始聊天、推理过程、工具日志或凭据。
修改后运行 python tools/build_context.py 和 python tools/memory_ops.py audit，并检查并发远端更新。
