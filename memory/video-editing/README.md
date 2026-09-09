# SZT AI Video Editing Memory

这是 SZT 的长期 AI 视频剪辑学习档案，用于跨电脑、跨 Codex 会话恢复已经通过用户反馈确认的剪辑判断方法。

## 档案结构

- `EDITING_STYLE_SZT.md`：长期规则主档，保存判断方法和可执行默认原则。
- `CASES/`：具体项目复盘。案例记录当次 AI 初版与用户人工最终版之间的变化，不把每个项目选择直接升级成永久规则。
- 根目录 `AGENTS.md`：视频任务的启动路由。

主档案和案例档案分开维护。新的人工成片出现后，先比较 AI 初版与人工最终版，记录改变、原因和证据；判断哪些只是本项目选择，哪些是重复出现的长期偏好。只有用户明确确认或多个案例持续支持的规律，才更新 `EDITING_STYLE_SZT.md`。

## 每次开始视频项目

1. 先读取 `memory/video-editing/EDITING_STYLE_SZT.md`。
2. 再读取本次项目需求、素材说明和项目／领导硬约束。
3. 按以下优先级执行：

   ```text
   本次用户明确要求
   >
   本次项目／领导硬约束
   >
   EDITING_STYLE_SZT.md
   >
   通用剪辑习惯
   ```

Style Guide 不是模板。不能机械复刻其中的时长、字体、片尾、人物长度、动画、镜头顺序或某个案例的具体布局；它保存的是面对新素材时的判断方法。本次用户明确的新要求始终可以覆盖历史规则。

## 本地同步原则

本地工作副本目前位于：

`D:\SZT\EDITING_STYLE_SZT.md`

它对应本仓库的：

`memory/video-editing/EDITING_STYLE_SZT.md`

本地和云端不一致时，不要静默覆盖。先比较差异，保留最新且经过用户人工反馈产生的有效规则；如果无法判断，报告差异并请求选择。案例文件只新增到 `CASES/`，不要为了方便把完整 Style Guide 复制进案例。

## New Computer Setup

换电脑或重装 Codex 后：

1. 登录自己的 GitHub 账号，并确认可以访问这个 Private Repository。
2. 在终端执行：

   ```powershell
   git clone https://github.com/xiaochuansun715-dot/SZT-AI-Workspace.git
   cd SZT-AI-Workspace
   ```

3. 在 Codex 中打开仓库目录，让 Codex 读取根目录 `AGENTS.md`。
4. 开始任何视频项目前，读取 `memory/video-editing/EDITING_STYLE_SZT.md`，再读取当前项目需求。
5. 如需要 SZT 工作区本地副本，再将主档案复制或链接到新的工作目录；复制前先比较差异，不要覆盖用户已经人工更新的版本。

如果新电脑尚未配置 Git 身份，先按 GitHub 的登录／凭据提示完成认证，再执行 clone、commit 和 push。不要把密码、Token 或 Cookie 写入仓库、脚本或 Markdown。

## 更新与版本管理

真正形成长期规律后，单独修改主档案并使用说明清楚的提交，例如：

```text
Update editing style from 2026-09-09 Teachers Day review
```

具体项目复盘使用日期和项目名进入 `CASES/`，例如：

`CASES/2026-09-09_TEACHERS_DAY_REVIEW.md`

每次更新后先检查本地与云端差异，再 commit 和 push。不要无说明地覆盖历史；Git 历史用于查看剪辑偏好是如何逐步学习出来的。

## 隐私边界

本档案只同步 Markdown、README、AGENTS.md 和必要的纯文本配置。禁止上传原始商业视频、未授权素材、大型媒体文件、客户敏感数据、账号信息、API Key、Cookie、Token 或密码。除非用户以后明确要求，否则不把视频素材同步进本仓库。
