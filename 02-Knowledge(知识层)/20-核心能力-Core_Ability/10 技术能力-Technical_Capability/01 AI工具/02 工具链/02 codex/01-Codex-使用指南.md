---
title: Codex 使用指南（完整版）
domain: Core_Ability
tags: [AI, Agent, Codex, 指南, 工具]
status: 稳定
created: 2026-06-16
updated: 2026-07-21
source: "微信原文《40分钟学会Codex》; 本地配置"
summary: "Codex 从零到一的完整教程 + 个人使用指南。基于微信原文《40分钟学会Codex》整理，包含安装配置、核心概念、插件Skills、MCP、自动化等全部能力。"
---

# Codex 使用指南（完整版）

> 基于微信原文《40分钟学会Codex》整理，融合个人配置和使用经验。

## 简介

这是一篇 Codex 奶妈级的零基础系统教程。以下内容从安装开始，覆盖基础能力到高级功能组合的 10 个实战场景。

📺 **视频教程**：40 分钟学会 Codex（与本文配套）
📎 **配套文档**：[飞书文档（含命令/工具/Skill/prompt）](https://my.feishu.cn/wiki/OCY5wzbGhiLDr8kMulkcLLuSnQd)

> 📷 **配图说明**：所有飞书截图已下载到本地 `images-wx/` 目录下（51 张）。

---

## ⚙️ 我的配置

### 模型配置

`config.toml` 完整配置：

```toml
model_provider = "custom"
model = "deepseek-v4-flash"
model_reasoning_effort = "medium"
sandbox_mode = "workspace-write"

[model_providers.custom]
name = "deepseek"
base_url = "http://127.0.0.1:15721/v1"  # 9router
wire_api = "responses"
requires_openai_auth = true

[windows]
sandbox = "elevated"

[desktop]
followUpQueueMode = "queue"
```

- **模型**：deepseek-v4-flash（日常）/ GPT-5.5（复杂任务时通过 cc-switch 切换）
- **9router**：http://127.0.0.1:15721/v1，负责模型路由 + RTK 压缩（节省 20-40% Token）
- **沙箱模式**：`workspace-write`（自动审查级别，AI 判断安全后自动执行命令和联网）
- **引导模式**：queue（排队执行，不打断当前任务）
- **当前信任项目**：`x:\kms\yeyunby` 等

### 已安装 Skills（8 个）

| Skill | 用途 |
|-------|------|
| agent-reach | 全网调研（小红书/B站/知乎等 13 平台）|
| agent-browser | 浏览器自动化 CLI |
| skill-creator | 创建新 Skill |
| cli-creator | 从 API 文档生成 CLI |
| find-skills | 搜索社区 Skills |
| imagegen | AI 图片生成 |
| check | 代码审查 |
| playwright | 浏览器自动化 |

### 已安装 Plugins（16 个）

详见 [[02-插件与技能系统]]。核心：browser、browser-use、chrome、computer-use、documents、spreadsheets、presentations、github、visualize。

### 核心 MCP

```toml
[mcp_servers.node_repl]
command = "...node_repl.exe"
env.BROWSER_USE_AVAILABLE_BACKENDS = "chrome,iab"
```

`node_repl` 是核心 MCP——持久化 Node.js 运行时，驱动浏览器自动化和脚本执行。

---

## 一、准备工作

### 1. 安装下载（需魔法）

**步骤 1**：官网（[点此处前往](https://openai.com/zh-Hans-CN/codex/)）下载

**步骤 2**：登陆Codex（可以用GPT账号或者API key登录）

- 用**ChatGPT**账号登录（有账号就行）

![1|800](images-wx/img01.png)

- 或者用**API key**登录（需要额外购买）

![2|800](images-wx/img02.png)![3|800](images-wx/img03.png)

> 如有需求/有条件，也可选择购买OpenAI API 密钥（[点击前往ChatGPT官网购买](https://platform.openai.com/api-keys)）进行登陆

### 2. 界面介绍

![4|800](images-wx/img04.png)

---

## 二、基础操作

### 1. 上下文管理

**步骤 1**：查看上下文情况

![5|800](images-wx/img05.png)

**步骤 2**：压缩上下文

- 可通过输入中文指令`/压缩`进行手动压缩

![6|800](images-wx/img06.png)

### 2. 额度状态

#### 方式 1：系统设置查看

![7|800](images-wx/img07.png)

#### 方式 2：斜杠命令查看

![8|800](images-wx/img08.png)![9|800](images-wx/img09.png)

### 3. 模型选择

![10|800](images-wx/img10.png)

> - 速度有两种模式：
>     - **标准**。默认速度，常规用量。
>     - **快速**。整体效率提高1.5倍，但额度用量的消耗也会提升。
> - 模型可直接选最新的**5.5模型**，也可按需选择其他的次级模型
> - 智能程度视任务难度而定，一般任务"**中**"就够了

---

## 三、本地文件读写

**步骤 1**：新建项目

- 如图，两者都可新建项目/选择本地文件夹

![11|800](images-wx/img11.png)

**步骤 2**：权限设置

- **默认权限**：仅能读写所选文件夹内全部文件，若需访问文件夹外内容，codex要单独申请权限。
- **自动审查**：相比默认，权限更高。AI 自动检查操作是否存在风险，判定有风险就请示，无风险则直接执行操作
- **完全访问权限：**codex能在你的电脑上执行任意操作，不做请示

![12|800](images-wx/img12.png)

**步骤 3**：项目内任务多开

- 支持在现有项目任务中，额外开启并行的对话任务

![13|800](images-wx/img13.png)

---

## 四、命令行使用

开启「**自动审查**」模式后，Codex 可直接用命令行开展工作。我们只需用日常沟通文字，就能让 Codex 帮我们安装各类工具。

![14|800](images-wx/img14.png)

> **Codex的一个缺点：**目前「**聊天任务框**」里显示的文件，可在右侧「**结果框**」内打开，但**无法编辑**
>
> ![15|800](images-wx/img15.png)
>
> **解决方案**：下载一个「**Agent IDE（有AI的编辑器）**」，Codex会自动识别并添加到右上角。以Cursor为例。
>
> - **步骤 1**：用日常沟通文字，让Codex在软件里部署好Cursor
>     ```Plain
>     请检查我是否已安装Cursor；若未安装，请先为我安装。
>     若已安装，把 Codex桌面端右上角"打开编辑器"的默认目标设置为 Cursor，并验证是否生效。
>     ```
> - **步骤 2**：部署好以后，Cursor会常驻右上角；之后，文件可直接在Cursor内打开进行编辑
>
> ![16|800](images-wx/img16.png)![17|800](images-wx/img17.png)

---

## 五、持久记忆

### 方式 1：全局级长期记忆

- 「**全局生效 Agents.md**」不管在哪个项目和 Codex 对话，都会第一时间把已记录的记忆，当作上下文传给大模型。
- 「**全局生效 Agents.md**」适合记录所有任务都通用的规则，比如你的使用习惯、工作偏好等。

**步骤 1**：在「**设置**」中找到「**个性化**」

![18|800](images-wx/img18.png)![19|800](images-wx/img19.png)

**步骤 2：**直接在「**自定义指令**」里添加想要的规则和约束，比如个人使用习惯、工作偏好等。

![20|800](images-wx/img20.png)

**步骤 3：**也可直接在聊天任务中使用日常语言交代自己的规则，并最终要求添加到「**全局agents.md**」

![21|800](images-wx/img21.png)

### 方式 2：项目级持久记忆

- 「**项目级agents.md**」只在固定项目持久生效

**步骤 1**：在具体项目中打开编辑器（如：Cursor）

![22|800](images-wx/img22.png)

**步骤 2**：在编辑器中新建文件，并命名为：**AGENTS.md**。（**注意**：AGENTS必须大写）

![23|800](images-wx/img23.png)

**步骤 3**：直接在AGENTS.md里，用自然语言，新增你想要的规则。

**步骤 4**：也可直接在聊天任务中使用日常语言交代自己的规则，并最终要求添加到"项目AGENTS.md"

### 方式 3：自动记忆

- 自动记忆的机制是，codex会在我们结束对话或任务，闲置一段时间之后，帮我们把之前对话总结成记忆，并在之后的对话与项目中复用。

**步骤 1**：在「**设置**」下的「**个性化**」中找到「**启用记忆**」

![24|800](images-wx/img24.png)

**步骤 2**：自动记忆的文件一般是在`/Users/xxxx/.codex/memories` 文件夹下面的

---

## 六、大型项目规划与落地

针对有一定复杂度的项目，或者我们自己都还没想清楚的项目，可开启「**计划模式**」，在codex的引导下完善项目想法与思路，并最终执行。

**步骤 1**：新建项目

**步骤 2**：打开「**计划模式**」

![20|800](images-wx/img25.png)

**步骤 3**：（以"**从0开始做个人网页**"为例）根据Codex的引导，通过引导选择，或自主输入提示词，最终完善计划

![26|800](images-wx/img26.png)

**步骤 4**：计划生成后，还可自行给出建议，调整计划

![27|800](images-wx/img27.png)

**步骤 5**：计划开始执行后，如果不满意，还可临时提交建议，并在合适的时机点击「**引导**」进行提交。执行过程不会被中止。

![28|800](images-wx/img28.png)![29|800](images-wx/img29.png)

**步骤 6**：如果执行中有些想法不确定，还可以通过「**fork（分叉）**」开个副本测试，这样不会弄乱主线任务

![30|800](images-wx/img30.png)

**步骤 7**：等待时，可在「**设置**」下的「**外观**」选择或定制桌面宠物。唤醒后，宠物会提示你，当前Codex正在做什么。

![31|800](images-wx/img31.png)

**步骤 8**：可以在结果预览界面右上角，选择「**注释**」对生成内容进行批注，批注好以后，发送给codex进行修改

![32|800](images-wx/img32.png)![33|800](images-wx/img33.png)![34|800](images-wx/img34.png)

**步骤 9**：项目完结后，可让codex帮我们基于刚才的项目，生成一份「**项目级AGENT.md**」

![35|800](images-wx/img35.png)![36|800](images-wx/img36.png)

---

## 七、插件

### 1. 插件位置&情况

![37|800](images-wx/img37.png)

### 2. 插件（中文）大全

| **必装插件** | **板块** | **可以做什么** |
|---|---|---|
| **Chrome** | **Featured / 精选** | 用你的浏览器登录态处理网页任务，适合查资料、测试页面、整理网页信息。|
| **GitHub** | **Featured / 精选** | 查看仓库、PR、Issue 和 CI 状态，适合代码协作、审查和发布流程。|
| **OpenAI Developers** | **Featured / 精选** | 查询 OpenAI API、Agents、ChatGPT Apps、Codex 等官方开发资料。|
| **Vercel** | **Featured / 精选** | 构建和部署 Web 应用、Agent、预览环境。|
| **Netlify** | **Coding / 编程与工程** | 部署前端项目、管理预览环境、配置站点和函数。|
| **Sentry** | **Coding / 编程与工程** | 查看线上错误和事件，帮助定位 bug、复现问题和评估影响范围。|
| **Remotion** | **Design / 设计** | 根据提示创建 动态图像 / 程序化视频。|
| **HyperFrames by HeyGen** | **Design / 设计** | 编写 HTML 并渲染视频，适合生成动态视觉内容。|

Codex收录的所有插件，相关中文信息，已全部整理到了文档里。

- 可在文档查看有安装需求的插件：[Codex插件大全](https://my.feishu.cn/wiki/NATtwZKgmiS4JSk1I74c78lYnRb)

### 3. 重点插件介绍

| 插件名称 | 功能作用 | 适用场景 | 场景案例 | 备注 |
|---|---|---|---|---|
| Browser | 让Codex操作**内置浏览器** | 一般用于前端的自动化测试 | 1. 自动登录网站 2. 点击按钮 3. 填写表单 4. 翻页截图 5. 确认页面功能和样式是否正常 | 处理公开网页、本地预览、无需登录的页面，优先使用 Codex 自带 Browser |
| Computer Use | 让codex多一双"眼睛"和"鼠标"，**能操控所有电脑软件** | 1. 命令行或插件不够用的场景 2. 完全依靠图形界面交互的场景 | 1. 测试桌面 App 2. 复现界面 Bug 3. 检查导入导出流程 4. 打开音乐软件搜歌 5. 使用微信界面发消息 | 目前仅限mac系统 |
| Chrome | codex控制**真实的谷歌浏览器**，并在后台执行浏览器操作 | 适合处理"必须登录真实网站才能完成"的浏览器任务 | 1. 打开 Gmail 查邮件 2. 进公司后台改资料 3. 跨多个网页整理资料 | 不会直接接管你正在用的窗口 |

---

## 八、Skills&CLI

可直接将Skill和CLI的下载链接丢给Codex进行自动下载，并在Codex引导下完成部署。

### 1. 推荐下载的skill

| skill名称 | 功能 | 下载链接 |
|---|---|---|
| Find-Skill | 根据用户需求，查找和安装来自agent skill开放生态的元技能 | [GitHub](https://github.com/vercel-labs/skills/tree/main/skills/find-skills) |
| Frontend-Design | 创建具有独特风格、生产级品质且设计精良的前端界面 | [GitHub](https://github.com/anthropics/skills/tree/main/skills/frontend-design) |
| humanizer-zh | Humanizer 的汉化版本，消除文本内容的 AI 生成痕迹。 | [GitHub](https://github.com/op7418/humanizer-zh) |

### 2. skill合集网站：[lobehub](https://lobehub.com/zh/skills)

大家既可以根据分类去寻找自己需要的skill，也可以直接在精选合集查看推荐的优质skill

![20|800](images-wx/img38.png)

### 3. 创建自己的skill

以最终创建一项「**自动撰写《本周 GitHub 热门项目推荐》文章**」的skill为例

**步骤 1**：要求codex整理出本周热门GitHub项目，并解释项目作用。
```Plain
本周最新的github流行项目、热门项目有哪些？并清晰解释这些项目的作用
```

**步骤 2**：筛选5个符合写作目标，且star数量最多的项目，写一篇《本周GitHub热门项目推荐》
```Plain
从整理名单中，在AI编程、研究、学习三个领域，选出5个star数量最多的项目，写一篇《本周GitHub热门项目推荐》
```

**步骤 3**：通过斜杠指令调出已下载好的humanizer-zh技能，去掉文章的AI味儿

![39|800](images-wx/img39.png)

**步骤 4**：对文章的内容与形式进行打磨
```Plain
加一个固定的开头和结尾，用image2生成一些配图，最后以飞书文档的形式写出来
```

**步骤 5**：让codex将整个过程整合为一个skill
```Plain
将以上过程的一整套动作、步骤和标准，整合优化为一个skill
```

![40|800](images-wx/img40.png)

**步骤 6**：可通过斜杠命令进行调出并使用这个skill

![41|800](images-wx/img41.png)

### 4. 推荐下载的CLI

| **CLI名称** | **功能** | **下载链接** |
|---|---|---|
| 飞书CLI | 飞书官方CLI工具，覆盖消息、文档、多维表格等 | [GitHub](https://github.com/larksuite/cli/blob/main/README.zh.md) |
| OpenCLI | 万能命令行工具箱，能将任何网站/桌面应用/本地程序变成统一命令行操作界面 | [GitHub](https://github.com/jackwener/opencli) |
| gh CLI | GitHub 官方命令行工具 | [GitHub](https://github.com/cli/cli) |
| gemini CLI | Gemini 模型终端访问 | [GitHub](https://github.com/google-gemini/gemini-cli) |

> 推荐GitHub上的CLI主题：[Command-line interface](https://github.com/topics/cli)

---

## 九、MCP

### 1. MCP位置

![42|800](images-wx/img42.png)![43|800](images-wx/img43.png)

### 2. MCP安装

对于小白用户，可以直接将mcp链接拷贝给codex，让codex自行操作，并最终引导我们授权完成。

- 以notebooklm mcp为例：

**步骤 1**：自然语言输入指令
```Plain
帮我安装好notebooklm的mcp：https://github.com/PleasePrompto/notebooklm-mcp
```

**步骤 2**：根据引导进行重启并授权

![44|800](images-wx/img44.png)![45|800](images-wx/img45.png)

**步骤 3**：在「**设置**」下的「**MCP服务器**」确认下载成功

![46|800](images-wx/img46.png)

### 3. MCP扩展

关于MCP，可结合以下教程内的MCP部分学习与实践：

**学习资源**

📺 **视频教程：**[用神器Claude Code！打造贴身AI秘书团【小白教程】](https://www.bilibili.com/video/BV1zqeMzfEiQ/)
📄 **文档教程：**[Claude Code教程](https://my.feishu.cn/wiki/BxLTwlkvkiQhJkkJ7vgc95aZnMe)

---

## 十、自动化任务

### 方式 1：自动化面板

**步骤 1**：打开「**自动化**」面板

![47|800](images-wx/img47.png)

**步骤 2**：新建自动化功能 / 选择需求相近的官方样例

![48|800](images-wx/img48.png)

**步骤 3**：完成自动化任务设置

![49|800](images-wx/img49.png)

### 方式 2：日常语言交互设置

通过在对话框与Codex进行日常语言交互，设置自动化任务，例如：

```Plain
帮我创建一个自动化任务，每周一早上9点。任务内容是：自动执行热门项目推荐的skill，产出一篇图文发到飞书群里
```

---

## 参考

- [[02-插件与技能系统]] — 插件和 Skills 详解
- [[Vibe Coding 视频创作场景]] — 视频创作场景
- images-wechat/ — 微信教程配图（85 张截图）
