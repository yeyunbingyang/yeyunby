---
title: Hermes Agent 技能与工具完全手册
domain: Core_Ability
tags: [Hermes, Agent, AI工具, 参考手册]
status: 稳定
created: 2026-07-04
updated: 2026-07-04
source: "https://hermes-agent.nousresearch.com/docs"
related:
  - "[[03-Resources(资源层)/00 Github优质项目/01-Agent引擎/hermes-agent.md|Hermes Agent 项目]]"
  - "[[02-Knowledge(知识层)/20-核心能力-Core_Ability/10 AI应用-AI_Application/01 AI工具/02 Agent/00 基础设施/skills/Claude-Skills/Obsidian-Skills-索引.md|Obsidian Skills 索引]]"
summary: "Hermes Agent (Nous Research) 的 21 个内置工具、25 个工具集、73 个技能、20+ Provider 支持、15+ 消息平台的完整使用手册，含 CLI 命令速查和故障排查指南"
---

# Hermes Agent — 技能与工具完全手册

> 编译日期：2026-07-04 | 基于当前会话的技能列表 + 内置 hermes-agent 技能文档
> 项目笔记见：[[03-Resources(资源层)/00 Github优质项目/01-Agent引擎/hermes-agent.md|Hermes Agent GitHub 项目]]

---

## 一、什么是 Hermes Agent

Hermes Agent 是 **Nous Research** 开发的开源 AI Agent 框架，与 Claude Code、OpenAI Codex、OpenCode 同类。它运行在终端、消息平台（Telegram/Discord/微信等）和 IDE 中，通过工具调用与你的系统交互。

**核心特性：**
- ✅ **自学习技能体系** — 解决复杂问题后自动保存为可复用的技能（Skill）
- ✅ **跨会话持久记忆** — 记住你的偏好、环境、约定
- ✅ **多平台网关** — 同一个 Agent 运行在 Telegram、Discord、Slack、微信等 15+ 平台
- ✅ **模型无关** — 支持 20+ 模型提供商，随时切换
- ✅ **多 Profile** — 隔离的配置、会话、技能、记忆
- ✅ **可扩展** — 插件、MCP 服务器、自定义工具、Webhook、Cron 调度

---

## 二、内置工具（Tools）

Hermes Agent 每次会话加载一套**工具集**，每个工具是一个可调用的函数。以下是当前可用工具的完整清单：

### 2.1 核心工具

| 工具 | 用途 | 说明 |
|------|------|------|
| **`terminal`** | 执行 Shell 命令 | Linux(本地/Docker/SSH/Modal)，支持前后台运行、PTY 模式 |
| **`read_file`** | 读取文件 | 带行号分页，自动解压 .ipynb/.docx/.xlsx |
| **`write_file`** | 写入文件 | 覆盖写入，自动创建父目录，支持语法检查 |
| **`patch`** | 找替换编辑 | 模糊匹配，9 种策略，支持单文件/多文件 V4A 补丁 |
| **`search_files`** | 搜索文件内容/名称 | Ripgrep 内核，支持正则、文件类型过滤 |
| **`web_search`** | 网页搜索 | 返回标题/URL/摘要，支持 `site:` 等高级语法 |
| **`web_extract`** | 网页内容提取 | 返回 Markdown，支持 PDF，超长页面自动截断+存盘 |
| **`execute_code`** | Python 沙盒执行 | 可以调用 Hermes 工具，适合复杂逻辑/循环/条件分支 |
| **`delegate_task`** | 子任务委派 | 生成独立子 Agent，支持并行批量（最多 3 个） |

### 2.2 人机交互工具

| 工具 | 用途 | 说明 |
|------|------|------|
| **`clarify`** | 向用户提问 | 支持选择题（4 个选项）和开放题两种模式 |
| **`text_to_speech`** | 文字转语音 | 返回音频文件，支持 Edge/OpenAI/ElevenLabs 等 |

### 2.3 浏览器工具

| 工具 | 用途 | 说明 |
|------|------|------|
| **`browser_navigate`** | 导航到 URL | 返回页面交互式摘要（含 ref ID） |
| **`browser_snapshot`** | 页面快照 | 获取当前页面可访问性树 / 完整内容 |
| **`browser_click`** | 点击元素 | 通过 ref ID（如 `@e5`）定位 |
| **`browser_type`** | 输入文本 | 清空字段后输入 |
| **`browser_scroll`** | 滚动页面 | 上/下方向 |
| **`browser_press`** | 按键 | Enter/Tab/Escape/方向键等 |
| **`browser_back`** | 后退 | 返回上一页 |
| **`browser_console`** | 浏览器控制台 | 获取 console 输出 / 执行 JS |
| **`browser_get_images`** | 获取页面图片列表 | 含 URL 和 alt 文本 |

### 2.4 任务管理工具

| 工具 | 用途 | 说明 |
|------|------|------|
| **`todo`** | 任务列表 | 当前会话内的多步骤任务追踪 |
| **`cronjob`** | 定时任务 | 创建/管理持久化 Cron 作业 |
| **`process`** | 后台进程管理 | list/poll/wait/kill/write/submit/close |

### 2.5 记忆与知识工具

| 工具 | 用途 | 说明 |
|------|------|------|
| **`memory`** | 持久记忆 | 保存用户偏好/环境事实到 `memory` 或 `user` |
| **`session_search`** | 跨会话搜索 | FTS5 搜索引擎，支持发现/滚动/读取/浏览四种模式 |
| **`skill_view`** | 加载技能 | 读取技能全部内容，含链接文件 |
| **`skill_manage`** | 管理技能 | 创建/更新/删除/打补丁 |
| **`skills_list`** | 技能列表 | 列出所有可用技能及分类 |

### 2.6 项目管理工具

| 工具 | 用途 | 说明 |
|------|------|------|
| **`project_create`** | 创建项目 | 绑定文件夹，切换工作区 |
| **`project_switch`** | 切换项目 | 按名称/slug/ID 切换 |
| **`project_list`** | 项目列表 | 查看所有项目和当前活跃项目 |

### 2.7 其他

| 工具 | 用途 | 说明 |
|------|------|------|
| **`read_terminal`** | 读取 TUI 终端面板 | 获取 GUI 内嵌终端的可见内容 |
| **`close_terminal`** | 关闭后台终端标签 | 仅关闭视图，不杀进程 |

---

## 三、工具集（Toolsets）体系

工具按**工具集**分组，可以按需启用/禁用：

| 工具集                           | 包含的工具         | 说明                          |
| ----------------------------- | ------------- | --------------------------- |
| `web`                         | 网页搜索+内容提取     |                             |
| `search`                      | 网页搜索（子集）      |                             |
| `browser`                     | 浏览器自动化全套      | 基于本地 Chromium / Browserbase |
| `terminal`                    | shell 命令+进程管理 |                             |
| `file`                        | 文件读写搜索编辑      |                             |
| `code_execution`              | 沙盒 Python 执行  |                             |
| `vision`                      | 图片分析          |                             |
| `image_gen`                   | AI 图片生成       |                             |
| `video`                       | 视频分析/生成       |                             |
| `tts`                         | 文字转语音         |                             |
| `skills`                      | 技能浏览/管理       |                             |
| `memory`                      | 持久记忆          |                             |
| `session_search`              | 跨会话搜索         |                             |
| `delegation`                  | 子 Agent 委派    |                             |
| `cronjob`                     | 定时任务管理        |                             |
| `clarify`                     | 向用户提问         |                             |
| `messaging`                   | 跨平台消息发送       |                             |
| `todo`                        | 任务规划          |                             |
| `kanban`                      | 多 Agent 看板    |                             |
| `debugging`                   | 调试工具（默认关）     |                             |
| `safe`                        | 最小安全工具集       |                             |
| `spotify`                     | Spotify 音乐控制  |                             |
| `homeassistant`               | 智能家居（默认关）     |                             |
| `discord`                     | Discord 集成    |                             |
| `discord_admin`               | Discord 管理    |                             |
| `feishu_doc` / `feishu_drive` | 飞书文档/云盘       |                             |
| `yuanbao`                     | 元宝集成          |                             |

> 操作命令：`hermes tools`（交互式），`hermes tools enable/disable NAME`
> 切换工具集需要 `/reset` 新会话生效

---

## 四、技能体系（Skills）— 73 个技能完全清单

技能是 Hermes Agent 的**程序化记忆** — 可复用的工作流模板，分为 15 个类别：

### 4.1 自主 AI Agent（autonomous-ai-agents）— 4 个

| 技能 | 用途 | 说明 |
|------|------|------|
| **`hermes-agent`** | 配置/扩展/贡献 Hermes Agent 本身 | 内含完整 CLI 参考、Provider 清单、工具集定义、故障排查 |
| **`claude-code`** | 委派编码任务给 Claude Code CLI | 特性开发、PR |
| **`codex`** | 委派编码任务给 OpenAI Codex CLI | 特性开发、PR |
| **`opencode`** | 委派编码任务给 OpenCode CLI | 特性开发、PR 审查 |

### 4.2 创意（creative）— 15 个

| 技能                             | 用途                        | 说明                                 |
| ------------------------------ | ------------------------- | ---------------------------------- |
| **`architecture-diagram`**     | 深色主题 SVG 架构图              | 云/基础设施拓扑 HTML                      |
| **`ascii-art`**                | 生成 ASCII 艺术               | pyfiglet, cowsay, boxes, 图片转 ASCII |
| **`ascii-video`**              | 生成 ASCII 视频               | 视频/音频转彩色 ASCII MP4/GIF             |
| **`baoyu-infographic`**        | 信息图生成                     | 21 种布局 x 21 种风格                    |
| **`claude-design`**            | 一次性 HTML 设计               | 落地页/演示/原型                          |
| **`comfyui`**                  | ComfyUI 图像/视频/音频生成        | 安装/启动/管理节点模型/运行工作流                 |
| **`design-md`**                | Google DESIGN.md token 规范 | 编写/验证/导出                           |
| **`excalidraw`**               | 手绘风格 Excalidraw 图表        | 架构图/流程图/时序图 JSON                   |
| **`humanizer`**                | 文本人性化                     | 去除 AI 腔调，增加真实感                     |
| **`manim-video`**              | Manim CE 动画视频             | 3Blue1Brown 风格数学/算法视频              |
| **`p5js`**                     | p5.js 创意编程                | 生成艺术、着色器、交互、3D                     |
| **`popular-web-designs`**      | 54 个真实设计系统                | Stripe/Linear/Vercel 等 HTML/CSS    |
| **`pretext`**                  | @chenglou/pretext 浏览器演示   | 无 DOM 文字排版、字符艺术游戏                  |
| **`sketch`**                   | 一次性 HTML 原型               | 2-3 个设计变体比较                        |
| **`songwriting-and-ai-music`** | 作词+ Suno AI 音乐生成          | 歌词创作技巧 + AI 音乐提示词                  |
| **`touchdesigner-mcp`**        | TouchDesigner MCP 控制      | 创建算子、设参数、连线、执行 Python，36 个原生工具     |

### 4.3 数据科学（data-science）— 1 个

| 技能 | 用途 |
|------|------|
| **`jupyter-live-kernel`** | 通过 Jupyter 内核迭代执行 Python |

### 4.4 DevOps — 1 个

| 技能 | 用途 |
|------|------|
| **`hermes-gateway-wechat-qq`** | Windows 上安装 Hermes Gateway 并连接微信/QQ |

### 4.5 邮件（email）— 1 个

| 技能 | 用途 |
|------|------|
| **`himalaya`** | Himalaya CLI 终端邮件收发 |

### 4.6 GitHub — 5 个

| 技能 | 用途 |
|------|------|
| **`github-auth`** | GitHub 认证（HTTPS Token/SSH/gh CLI） |
| **`github-code-review`** | PR 审查（diff + 行内评论） |
| **`github-issues`** | 创建/分类/标注/分配 Issue |
| **`github-pr-workflow`** | PR 全流程（分支→提交→创建→CI→合入） |
| **`github-repo-management`** | 克隆/创建/Fork 仓库，管理远程/Release |

### 4.7 媒体（media）— 5 个

| 技能 | 用途 |
|------|------|
| **`gif-search`** | 搜索/下载 GIF（Tenor API） |
| **`heartmula`** | HeartMuLa 歌曲生成（歌词+标签） |
| **`songsee`** | 音频频谱图/特征可视化 |
| **`streaming-video-download`** | 下载 HLS/m3u8 流媒体视频 |
| **`youtube-content`** | YouTube 字幕转摘要/文章/推文 |

### 4.8 MLOps — 4 个

| 技能 | 用途 |
|------|------|
| **`huggingface-hub`** | HuggingFace CLI 搜索/下载/上传模型和数据集 |
| **`llama-cpp`** | 本地 GGUF 推理 + HF Hub 模型发现 |
| **`segment-anything-model`** | SAM 零样本图像分割 |
| **`weights-and-biases`** | W&B 实验追踪/超参搜索/模型注册表 |

### 4.9 笔记（note-taking）— 2 个

| 技能 | 用途 |
|------|------|
| **`obsidian`** | Obsidian 知识库读写搜索（通用） |
| **`vault-crossref-audit`** | 审计 Obsidian 笔记库的交叉引用、断链、Dataview → 重组 |

### 4.10 Obsidian 专项（obsidian-*）— 4 个

| 技能 | 用途 |
|------|------|
| **`obsidian-bases`** | 创建/编辑 .base 文件（数据库视图） |
| **`obsidian-cli`** | Obsidian CLI 全交互（CRUD / 插件开发 / DOM 检查） |
| **`obsidian-markdown`** | Obsidian 风味 Markdown（wikilink / callout / 属性） |
| **`obsidian-vault`** | 笔记库搜索/创建/管理 |

### 4.11 导入技能（openclaw-imports）— 2 个

| 技能 | 用途 |
|------|------|
| **`find-skills`** | 帮助发现和安装外部技能（npx skills 生态） |
| **`opencli-browser`** | 通过 opencli 驱动真实 Chrome 浏览器 |

### 4.12 生产力（productivity）— 8 个

| 技能 | 用途 |
|------|------|
| **`airtable`** | Airtable REST API（记录 CRUD/过滤/upsert） |
| **`google-workspace`** | Gmail/Calendar/Drive/Docs/Sheets |
| **`maps`** | 地理编码/POI/路线/时区（OSM/OSRM） |
| **`notion`** | Notion API + ntn CLI（页面/数据库/Markdown） |
| **`ocr-and-documents`** | PDF/扫描件文字提取 + PDF 文本编辑 |
| **`petdex`** | 安装和选择 Hermes 桌面宠物 |
| **`powerpoint`** | PPTX 创建/读取/编辑/模板 |
| **`teams-meeting-pipeline`** | Teams 会议摘要流水线操作 |

### 4.13 红队（red-teaming）— 1 个

| 技能 | 用途 |
|------|------|
| **`godmode`** | 破解 LLM 安全限制（Parseltongue/GODMODE） |

### 4.14 研究（research）— 4 个

| 技能 | 用途 |
|------|------|
| **`arxiv`** | 搜索 arXiv 论文 |
| **`blogwatcher`** | 监控博客和 RSS 更新 |
| **`llm-wiki`** | Karpathy 风格 LLM Wiki 知识库 |
| **`polymarket`** | 查询 Polymarket（市场/价格/订单簿/历史） |

### 4.15 智能家居（smart-home）— 1 个

| 技能 | 用途 |
|------|------|
| **`openhue`** | 控制 Philips Hue 灯光/场景/房间 |

### 4.16 软件工程（software-development）— 7 个

| 技能 | 用途 |
|------|------|
| **`node-inspect-debugger`** | Node.js --inspect + Chrome DevTools 调试 |
| **`plan`** | 规划模式：编写 Markdown 计划到 .hermes/plans/ |
| **`requesting-code-review`** | 提交前审查（安全扫描/质量门禁/自动修复） |
| **`simplify-code`** | 3 Agent 并行清理近期代码变更 |
| **`spike`** | 一次性实验验证想法 |
| **`systematic-debugging`** | 4 阶段根因调试 |
| **`test-driven-development`** | TDD 测试驱动开发 |

---

## 五、CLI 命令速查

```
hermes                         启动交互式聊天
hermes chat -q "问题"          单次查询（非交互）
hermes setup                   设置向导
hermes model                   切换模型/Provider
hermes doctor                  检查依赖和配置
hermes config                  查看配置
hermes config set KEY VAL      设置配置项
hermes config edit             编辑 config.yaml
hermes tools                   交互式工具管理
hermes skills list             列出已安装技能
hermes skills search QUERY     搜索技能市场
hermes skills install ID       安装技能
hermes sessions list           列出近期会话
hermes sessions export OUT     导出会话
hermes gateway run             启动消息网关
hermes gateway setup           配置消息平台
hermes cron list               列出定时任务
hermes cron create SCHED       创建定时任务
hermes mcp add NAME            添加 MCP 服务器
hermes mcp list                列出 MCP 服务器
hermes profile list            列出所有 Profile
hermes profile create NAME     创建 Profile
hermes auth                    交互式凭据管理
hermes update                  更新到最新版
hermes --yolo                  跳过危险命令确认
hermes -s skill_name           预加载技能
hermes -p profile_name         指定 Profile
hermes -w                      工作树模式（并行 Agent）
hermes --continue              恢复最近的会话
hermes --resume SESSION_ID     恢复指定会话
```

---

## 六、Slash 命令（会话内）

在交互式 CLI 中键入 `/` 即可使用：

### 会话控制
| 命令 | 用途 |
|------|------|
| `/new` 或 `/reset` | 开始新会话 |
| `/retry` | 重发上条消息 |
| `/undo` | 撤销上轮对话 |
| `/title [name]` | 命名当前会话 |
| `/compress` | 手动压缩上下文 |
| `/stop` | 杀死后台进程 |
| `/rollback [N]` | 回滚文件系统检查点 |
| `/background <prompt>` | 后台执行提示 |
| `/queue <prompt>` | 排队到下一轮 |
| `/steer <prompt>` | 在下次工具调用后注入消息 |
| `/goal [text]` | 设定持续目标 |

### 配置
| 命令 | 用途 |
|------|------|
| `/model [name]` | 查看或切换模型 |
| `/personality [name]` | 设置人格 |
| `/reasoning [level]` | 设置推理级别 |
| `/voice [on/off/tts]` | 语音模式 |
| `/yolo` | 切换审批绕过 |
| `/skin [name]` | 更换主题（CLI） |

### 工具与技能
| 命令 | 用途 |
|------|------|
| `/skills` | 搜索/安装技能 |
| `/skill <name>` | 加载技能到会话 |
| `/reload-skills` | 扫描新增/删除的技能 |
| `/reload-mcp` | 重载 MCP 服务器 |
| `/cron` | 管理定时任务 |
| `/plugins` | 查看插件列表 |

### 信息
| 命令 | 用途 |
|------|------|
| `/help` | 显示所有命令 |
| `/usage` | Token 用量 |
| `/insights [days]` | 使用分析 |
| `/profile` | 查看当前 Profile |
| `/debug` | 上传调试报告 |

### 网关
| 命令 | 用途 |
|------|------|
| `/approve` / `/deny` | 批准/拒绝待决命令 |
| `/restart` | 重启网关 |
| `/sethome` | 设当前频道为家频道 |
| `/platforms` | 显示平台连接状态 |

---

## 七、Provider 支持（20+）

| Provider | 认证方式 | 环境变量 |
|----------|---------|----------|
| OpenRouter | API Key | `OPENROUTER_API_KEY` |
| Anthropic | API Key | `ANTHROPIC_API_KEY` |
| Nous Portal | OAuth | `hermes auth` |
| OpenAI Codex | OAuth | `hermes auth` |
| GitHub Copilot | Token | `COPILOT_GITHUB_TOKEN` |
| Google Gemini | API Key | `GOOGLE_API_KEY` 或 `GEMINI_API_KEY` |
| DeepSeek | API Key | `DEEPSEEK_API_KEY` |
| xAI / Grok | API Key | `XAI_API_KEY` |
| Hugging Face | Token | `HF_TOKEN` |
| Z.AI / GLM | API Key | `GLM_API_KEY` |
| MiniMax | API Key | `MINIMAX_API_KEY` |
| Kimi / Moonshot | API Key | `KIMI_API_KEY` |
| Alibaba DashScope | API Key | `DASHSCOPE_API_KEY` |
| Xiaomi MiMo | API Key | `XIAOMI_API_KEY` |
| Qwen OAuth | OAuth | `hermes auth add qwen-oauth` |
| 自定义端点 | 配置设置 | `model.base_url` + `model.api_key` |

---

## 八、消息平台（Gateway）

Hermes Gateway 支持 15+ 消息平台：

| 平台 | 说明 |
|------|------|
| Telegram | 完整交互 + 话题线程 |
| Discord | Bot + 消息意图 |
| Slack | DM + 频道 |
| WhatsApp | 消息收发 |
| Signal | 加密消息 |
| Email (IMAP/SMTP) | 邮件收发 |
| SMS | 短信 |
| Matrix | 去中心化聊天 |
| Mattermost | 企业聊天 |
| Home Assistant | 智能家居 |
| 钉钉 / 飞书 / 企微 | 国内平台 |
| 微信 (WeChat) | 微信个人号 |
| BlueBubbles (iMessage) | Apple iMessage |
| API Server | HTTP API |
| Webhooks | HTTP 回调 |

---

## 九、快速参考：常用工作流

### 日常开发
```
hermes -s github-pr-workflow    # 加载 PR 工作流技能，进入开发
```

### 研究论文
```
hermes -s arxiv                 # 加载 arXiv 技能
```

### 笔记管理（Obsidian）
```
hermes -s obsidian-vault        # 进入 Obsidian 知识库工作模式
```

### 定时监控
```
hermes cron create "0 9 * * *"  # 每天 9 点执行
```

### 多 Agent 协作
```
hermes -w                       # 工作树模式（并行 Agent 不冲突）
```

---

## 十、故障排查速查

| 症状 | 检查 |
|------|------|
| 工具不可用 | `hermes tools` 检查是否启用 → `/reset` |
| 模型报错 | `hermes doctor` → 检查 `.env` API Key |
| 技能不显示 | `hermes skills list` → `hermes skills config` 检查平台启用 |
| 技能不加载 | `/skill name` 显式加载 |
| 配置不生效 | 网关：`/restart`，CLI：退出重开 |
| 语音不工作 | 检查 `stt.enabled: true` → 安装 `faster-whisper` |
| Gateway 挂掉 | `grep error ~/.hermes/logs/gateway.log` |
| Copilot 403 | 必须用 OAuth 设备码流程（`gh auth login` token 不适用） |

---

*本文档由当前会话的技能列表和 hermes-agent 技能文档自动编译。官方最新文档见 https://hermes-agent.nousresearch.com/docs*
