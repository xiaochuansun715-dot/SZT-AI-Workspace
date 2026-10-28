# 记忆维护与同步

时区：Asia/Shanghai。用户授权本库跨项目长期维护，面向所有获授权Agent。
已创建并回读自动化卡片：每日22:00整理（ID：22，ACTIVE）；每周日22:30增量复盘（ID：automation，ACTIVE）。周日22:30为本次默认安排，可由用户调整。时区按Asia/Shanghai，实际执行结果以每轮回执为准。

## 每日

1. 读取START_HERE、质量规则、最新更新记录与本地同步状态。
2. 运行 python tools/memory_ops.py scan；首次可用--since限定UTC起点。脚本只读取用户发言和助手最终答复，不读取推理/工具输出；队列只在.memory_state/pending。
3. 按需读取队列片段，审阅材料默认≤18000字符。先提取明确偏好、决定、项目成果、纠错、待办；不要把原文直接上传。若一批未读完，保留队列，不ack。
4. 用list_threads识别活跃/外部会话，必要时read_thread补读有变化的用户消息及最终答复；不要记录推理、工具参数或凭据。其他Agent来源不可读时记录缺口。
5. 合并到现行项目和偏好，形成当日日志；相同事实不新增副本。保留source_date与本次recorded的区别。
6. 完整审阅一批后才运行 python tools/memory_ops.py ack <batch.json>。ack只表示本地语义整理完成，不代表GitHub同步。
7. 运行 python tools/build_context.py 和 python tools/memory_ops.py audit。失败则修复，不能上传错误或疑似凭据。
8. 使用已授权GitHub连接增量同步。读取远端现有文件后与.memory_state/sync.json的基线比对；远端有并发变更则合并，不能覆盖。顺序写入，回读内容一致后记录sha256/blob_sha/commit。失败保留本地pending_sync，不把旧数据覆盖新远端。
9. 有新结论、失败或需要用户处理时才通知。无有用变化不刷状态。不得因本计划对外发信/发群消息。

## 每周日

先看近7天日志和变更清单，仅检查改动条目及标记的冲突/过期项。
材料默认≤12000字符；不扫描历史全文。无变更直接结束。
合并重复项、更新取代关系，把细节移至按项目历史，保留必要证据与用户原意。
更新07_Operations/Weekly/的周报、重建精简上下文并质量检查，按同样冲突规则同步。
多余待办下一次继续，不能静默遗漏。不要另起多个Agent或调用收费API重复检查。

## 本地运行边界

调度在Codex桌面应用本机执行，电脑、应用和网络需可用；这不是已部署在InstaBox的云端守护程序。
其他Agent有权限即可按08_Agents/Protocol.md读取/交接，不代表已为它们安装读取入口。
不在GitHub保存日志原文、模型认证或本地游标。
