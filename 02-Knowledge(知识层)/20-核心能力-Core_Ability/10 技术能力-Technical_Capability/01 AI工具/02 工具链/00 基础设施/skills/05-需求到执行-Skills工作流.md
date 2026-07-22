---
title: 需求到执行 Skills 工作流
domain: Core_Ability
tags: [AI, Agent, Skills, 工作流, 需求对齐, 最佳实践]
status: 稳定
created: 2026-07-06
updated: 2026-07-06
related:
  - "03-通用skills最佳实践"
  - "04-Skills生态全景"
  - "01-快速说明"
summary: "用户给需求后，Agent 如何用 Skills 对齐需求、完善完整度、高效执行的标准工作流——需求对齐→方案设计→执行→验证四阶段"
---

# 需求到执行 Skills 工作流

> 核心原则：**先对齐，再执行**。用户给一个需求时，Agent 的第一件事不是直接开干，而是通过追问把模糊需求变成可执行的清晰规格。

## 一、为什么需要需求对齐

用户给的需求往往是这样的：

| 用户说的 | 实际可能缺的 |
|---------|------------|
| "帮我整理一下 Docker 笔记" | 范围？格式？哪些笔记？输出什么？ |
| "调研一下 Serverless 趋势" | 深度？时间范围？关注哪些维度？ |
| "把这个页面改好看点" | 好看的标准？目标用户？品牌色？ |

**不经过对齐就直接执行，是 Agent 最常见的翻车原因。** 这对应了 Skills 生态中多个仓库都在解决的核心问题——mattpocock 的 `/grill-me`、agent-skills 的 `interview-me`、Waza 的 `/think`，本质上都在做同一件事：**把模糊需求变成可执行规格**。

## 二、四阶段工作流

```
用户给需求
    │
    ▼
┌─────────────────────────────────────┐
│ 阶段一：需求对齐（需求完整度检查）           │
│  ├─ 问清楚范围（Scope）               │
│  ├─ 问清楚标准（Acceptance Criteria）  │
│  ├─ 问清楚约束（Constraints）          │
│  └─ 问清楚优先级（Priority）           │
│                                      │
│  产出：对齐后的需求规格（几句话到一段话）      │
└─────────────────────────────────────┘
    │
    ▼
┌─────────────────────────────────────┐
│ 阶段二：方案设计（选择 Skills + 规划步骤）   │
│  ├─ 拆解为子任务                        │
│  ├─ 为每个子任务匹配最佳 Skill            │
│  └─ 确定执行顺序（串行/并行）              │
│                                      │
│  产出：执行计划（步骤 + 使用的 Skill）      │
└─────────────────────────────────────┘
    │
    ▼
┌─────────────────────────────────────┐
│ 阶段三：执行（按计划调用 Skills）          │
│  ├─ 按步骤执行                          │
│  ├─ 每步产出可验证的结果                  │
│  └─ 遇到问题及时反馈调整                  │
│                                      │
│  产出：各步骤的交付物                     │
└─────────────────────────────────────┘
    │
    ▼
┌─────────────────────────────────────┐
│ 阶段四：验证与收尾                       │
│  ├─ 检查是否满足对齐时定的标准             │
│  ├─ 输出总结报告                        │
│  └─ 如有必要，固化为新的 Skill            │
│                                      │
│  产出：最终交付 + 总结                   │
└─────────────────────────────────────┘
```

## 三、阶段一详解：需求对齐（我的做法）

当你给我一个需求时，我会自动做以下检查。**不需要你主动说"先对齐一下"**——这是我内置的工作方式。

### 3.1 我会问什么

| 检查维度 | 典型问题 | 为什么重要 |
|---------|---------|-----------|
| **目标（Goal）** | "最终想要什么效果？" | 避免做出来不是你想要的 |
| **范围（Scope）** | "包含什么？不包含什么？" | 避免范围蔓延 |
| **验收标准（Acceptance）** | "怎么算做完？" | 有明确的完成标志 |
| **约束（Constraints）** | "有什么限制？技术栈？时间？" | 避免方案不可行 |
| **优先级（Priority）** | "哪些是必须的？哪些可以砍？" | 时间不够时知道砍什么 |
| **上下文（Context）** | "之前做过类似的吗？有什么可以参考？" | 避免重复造轮子 |
| **受众（Audience）** | "给谁看的？" | 决定输出风格和深度 |

### 3.2 追问的节奏

```
你：帮我整理一下 Docker 笔记
    │
    ▼
我：好的，我先确认几个问题——
    ├─ 范围：是所有 Docker 笔记，还是某个子主题（如 Docker Compose、网络）？
    ├─ 输出：是生成一份汇总报告，还是逐篇补全 frontmatter？
    ├─ 标准：整理到什么程度算完成？补全字段？加 summary？还是重新组织结构？
    └─ 优先级：今天就要，还是可以慢慢来？
    │
    ▼
你：回答完这几个问题
    │
    ▼
我：好的，需求已对齐。计划如下：
    1. obsidian-vault → 搜索所有 Docker 笔记
    2. obsidian-markdown → 逐篇检查 frontmatter
    3. write → 补全 summary 字段
    4. 输出整理报告
    开始吗？
```

### 3.3 对齐的深度取决于需求复杂度

| 需求类型 | 对齐深度 | 追问数量 |
|---------|---------|---------|
| "帮我查一下 Python 的 datetime 用法" | 浅 | 0-1 个问题 |
| "帮我整理知识库中所有 Docker 笔记" | 中 | 2-3 个问题 |
| "帮我设计一个自动化工作流" | 深 | 3-5 个问题 |
| "帮我写一个完整的项目方案" | 最深 | 5-8 个问题，可能多轮 |

## 四、阶段二详解：方案设计（我如何选 Skills）

对齐需求后，我会把任务拆解为子任务，并为每个子任务匹配最佳 Skill。

### 4.1 常见场景的 Skill 组合

#### 场景 1：知识库操作
```
你：帮我整理一下 xxx 的笔记

拆解：
├─ 搜索相关笔记           → obsidian-vault（grep 搜索）
├─ 逐篇检查 frontmatter   → obsidian-markdown（格式检查）
├─ 补全缺失字段           → write（润色 summary）
└─ 更新 MOC              → obsidian-vault（更新索引）
```

#### 场景 2：调研新主题
```
你：调研一下 xxx 技术

拆解：
├─ 初步了解              → read（读取官方文档/首页）
├─ 深度调研              → learn（六阶段研究）
│   或 deep-research（多源交叉验证）
├─ 社交媒体补充           → agent-reach（Twitter/社区观点）
└─ 沉淀为笔记             → obsidian-vault（创建笔记）
```

#### 场景 3：内容创作
```
你：写一篇关于 xxx 的文章

拆解：
├─ 调研素材              → read / learn
├─ 生成封面图             → baoyu-cover-image
├─ 生成配图               → baoyu-article-illustrator
├─ 润色文字               → write
└─ 发布到公众号            → baoyu-post-to-wechat
```

#### 场景 4：代码开发
```
你：实现 xxx 功能

拆解：
├─ 需求对齐               → think / grill-me（方案设计）
├─ 代码实现               → 直接编码
├─ 代码审查               → code-review
├─ 简化优化               → simplify
└─ 验证                  → verify / check
```

#### 场景 5：问题排查
```
你：这个 xxx 报错了

拆解：
├─ 定位问题               → hunt（系统化调试）
├─ 修复                   → 直接修复
├─ 验证修复               → verify
└─ 记录根因               → obsidian-vault（沉淀为笔记）
```

### 4.2 Skill 选择优先级

```
有现成的专用 Skill 吗？
  ├─ 有 → 用它（如 baoyu-cover-image 做封面图）
  └─ 没有 → 用通用 Skill 组合
            ├─ 需要调研 → learn / read / deep-research
            ├─ 需要编辑 → obsidian-vault / obsidian-markdown
            ├─ 需要润色 → write
            └─ 需要设计 → think / design
```

## 五、阶段三详解：执行

执行阶段的关键原则：

1. **每步可验证** — 每完成一个子任务，产出可检查的结果（文件、截图、报告）
2. **遇到问题及时反馈** — 如果某个 Skill 不适用或报错，立即告知并换方案
3. **保持进度透明** — 让你知道当前在哪一步、还剩几步

## 六、阶段四详解：验证与收尾

### 6.1 验证清单

执行完成后，我会自动检查：

- [ ] 是否满足对齐时定的验收标准？
- [ ] 所有交付物是否完整？
- [ ] 有没有遗漏的子任务？
- [ ] 结果是否可复现？（如果是自动化工作流）

### 6.2 收尾产出

每次执行完成后，我会输出：

```
✅ 完成总结
├─ 做了什么
├─ 用了哪些 Skills
├─ 产出了什么（文件路径/链接）
├─ 注意事项（如果有坑）
└─ 后续建议（可选）
```

### 6.3 固化为新 Skill

如果某个工作流**重复出现 3 次以上**，我会建议你把它固化为一个自定义 Skill，这样下次一句话就能触发整个流程。

## 七、你不需要做什么

| 你不需要 | 我会自动做 |
|---------|-----------|
| 说"先帮我分析一下需求" | 自动判断需求复杂度，决定追问深度 |
| 说"用 xxx skill" | 自动匹配最适合的 Skill 组合 |
| 说"先规划再执行" | 自动拆解任务、规划步骤 |
| 说"做完告诉我" | 自动输出完成总结 |

## 八、你只需要做一件事

**把你的需求说出来，越原始越好。** 不需要组织成完美的需求文档——模糊的、跳跃的、甚至前后矛盾的都可以。我会通过追问帮你理清。

```
✅ 好的输入：
  "帮我整理一下 Docker 笔记，就是那些讲容器化的，
   最近发现有些 frontmatter 不全，想补一下"

❌ 不需要的输入（我来帮你做）：
  "请使用 obsidian-vault skill 搜索所有含 Docker 标签的笔记，
   然后用 obsidian-markdown 检查 frontmatter，
   再用 write 补全 summary..."
```

## 九、实际例子

### 例子 1：简单需求

```
你：帮我查一下 Python 的 datetime 怎么格式化

我：（判断为浅需求，直接回答）
Python datetime 格式化用 strftime：
  from datetime import datetime
  now = datetime.now()
  now.strftime("%Y-%m-%d %H:%M:%S")  # → "2026-07-06 09:30:00"
  
常用格式代码：
  %Y - 四位年份  %m - 两位月份  %d - 两位日期
  %H - 24小时    %M - 分钟      %S - 秒
```

### 例子 2：中等需求

```
你：帮我整理一下知识库中所有讲 Docker 的笔记

我：（自动对齐）
好的，我先确认几个问题：
1. 范围：是所有 Docker 相关笔记，还是只看 02-Knowledge 下的？
2. 输出：是补全 frontmatter，还是重新组织目录结构？
3. 标准：summary 字段要写到什么程度？一句话概括还是详细描述？

你：02-Knowledge 下的，补全 frontmatter 就行，summary 一句话

我：（对齐完成，开始执行）
计划：
1. obsidian-vault → 搜索 02-Knowledge 下含 Docker 的笔记
2. obsidian-markdown → 逐篇检查 frontmatter
3. write → 补全缺失的 summary 字段
4. 输出整理报告

开始吗？
```

### 例子 3：复杂需求

```
你：我想搭建一个自动化工作流，每天从几个网站抓取 AI 相关新闻，
    然后整理成简报存到知识库里

我：（自动判断为深需求，多轮对齐）
好的，这个需求涉及多个环节，我逐一确认：

第一轮：范围
├─ 目标网站：有具体想抓的网站吗？还是我推荐？
├─ 内容类型：标题+链接就够了，还是需要全文摘要？
└─ 频率：每天一次？工作日还是每天？

第二轮：输出
├─ 简报格式：Markdown 笔记？还是特定的模板？
├─ 存储位置：03-Resources 下新建目录？还是 01-日常流？
└─ 要不要发到微信/其他渠道？

第三轮：技术选型
├─ 抓取方式：OpenCLI（有适配器的网站）还是 agent-browser（通用）？
├─ 去重：同一篇新闻出现多次怎么处理？
└─ 失败处理：某个网站抓不到怎么办？

...（多轮对齐后）

我：好的，需求已对齐。完整方案如下：
├─ 数据抓取：OpenCLI（HackerNews）+ agent-browser（其他网站）
├─ 内容处理：learn（摘要生成）
├─ 简报生成：obsidian-vault（按模板创建笔记）
├─ 定时执行：cronjob（每天早上 9 点）
└─ 可选推送：baoyu-post-to-wechat（发到公众号）

开始搭建吗？
```

## 十一、已有 Skills 映射对照

> 上面描述的四阶段工作流，并非从零发明——Skills 生态中已经有多个仓库在解决同样的问题。以下是已有 Skills 到各阶段的映射。

### 11.1 阶段一：需求对齐 — 已有 Skills

| 已有 Skill                   | 来源                      | 做什么                                             | 与本笔记的对应              |
| -------------------------- | ----------------------- | ----------------------------------------------- | -------------------- |
| `/grill-me`                | mattpocock/skills       | 非代码场景的需求追问，直到决策树所有分支都解决                         | 最接近的现成方案——用户调用，自动追问  |
| `/grill-with-docs`         | mattpocock/skills       | 追问 + 领域建模，同步更新 CONTEXT.md 和 ADR                 | 进阶版——不仅对齐需求，还沉淀为项目知识 |
| `interview-me`             | addyosmani/agent-skills | 一对一访谈，挖出用户真正想要什么（到 95% 置信度）                     | 需求对齐的标准化实现           |
| `/think`                   | tw93/Waza               | 挑战问题、压力测试设计、产出决策完备的计划                           | 偏方案设计，但包含需求挑战        |
| `doubt-driven-development` | addyosmani/agent-skills | 遇到不确定时主动停下来确认                                   | 执行中的需求对齐             |
| **do 工作流阶段 2: Clarify**    | stellarlinkco/myclaude  | 解决阻塞性歧义（条件触发）                                   | 内嵌在工作流中的对齐环节         |
| **SPARV 阶段 1: Specify**    | stellarlinkco/myclaude  | 10 分规格门（Value/Scope/Acceptance/Boundaries/Risk） | 最结构化的需求评分体系          |
| Think Before Coding        | andrej-karpathy-skills  | 先思考再编码，解决错误假设和隐藏困惑                              | 原则级对齐，一个文件即可         |

### 11.2 阶段二：方案设计 — 已有 Skills

| 已有 Skill | 来源 | 做什么 |
|-----------|------|--------|
| `/spec` | addyosmani/agent-skills | 先写 PRD（目标/命令/结构/测试/边界）再写代码 |
| `/plan` | addyosmani/agent-skills | 将 spec 分解为小而原子的可执行任务 |
| `planning-and-task-breakdown` | addyosmani/agent-skills | 同上，skill 形态 |
| `source-driven-development` | addyosmani/agent-skills | 先读现有代码再写新代码 |
| `context-engineering` | addyosmani/agent-skills | 优化 Agent 上下文利用效率 |
| `idea-refine` | addyosmani/agent-skills | 发散/收敛思维，把模糊想法变成具体方案 |
| `to-prd` | mattpocock/skills | 将当前对话综合为 PRD 并发布到 Issue Tracker |
| `to-issues` | mattpocock/skills | 将计划/spec/PRD 拆分为独立 Issue |
| `domain-modeling` | mattpocock/skills | 构建和精炼项目领域模型 |
| `codebase-design` | mattpocock/skills | 设计深度模块的规范和词汇 |
| `prototype` | mattpocock/skills | 构建可丢弃的原型验证设计 |
| `setup-matt-pocock-skills` | mattpocock/skills | 配置 Issue Tracker/标签/文档路径 |
| **do 阶段 3: Design** | stellarlinkco/myclaude | 产出最小变更实现方案 |
| **SPARV 阶段 2: Plan** | stellarlinkco/myclaude | 规划执行步骤 |

### 11.3 阶段三：执行 — 已有 Skills

| 已有 Skill | 来源 | 做什么 |
|-----------|------|--------|
| `/build` | addyosmani/agent-skills | 一次一个切片，逐步交付 |
| `incremental-implementation` | addyosmani/agent-skills | 同上，skill 形态 |
| `test-driven-development` | addyosmani/agent-skills | TDD 红→绿→重构循环 |
| `frontend-ui-engineering` | addyosmani/agent-skills | 前端 UI 工程最佳实践 |
| `api-and-interface-design` | addyosmani/agent-skills | API 设计规范 |
| `/tdd` | mattpocock/skills | 红-绿-重构 TDD 循环 |
| `/code` | stellarlinkco/myclaude | 实现功能 |
| `/debug` | stellarlinkco/myclaude | 调试问题 |
| `/test` | stellarlinkco/myclaude | 编写测试 |
| **do 阶段 4: Implement** | stellarlinkco/myclaude | 构建功能 |
| **do 阶段 4: Review** | stellarlinkco/myclaude | 代码审查 |
| **SPARV 阶段 3: Act** | stellarlinkco/myclaude | 执行计划 |

### 11.4 阶段四：验证与收尾 — 已有 Skills

| 已有 Skill | 来源 | 做什么 |
|-----------|------|--------|
| `/review` | addyosmani/agent-skills | 代码审查与质量门禁 |
| `/code-simplify` | addyosmani/agent-skills | 简化代码 |
| `/check` | tw93/Waza | 审查 diff、提取项目约束、处理发布/推送/验证 |
| `code-review` | mattpocock/skills | 双轴审查（标准合规 + Spec 实现） |
| `verify` | 通用 | 验证改动是否生效 |
| `security-and-hardening` | addyosmani/agent-skills | 安全加固审查 |
| `performance-optimization` | addyosmani/agent-skills | 性能优化 |
| `/ship` | addyosmani/agent-skills | 发布上线流程 |
| `git-workflow-and-versioning` | addyosmani/agent-skills | 主干开发 + 版本管理 |
| `ci-cd-and-automation` | addyosmani/agent-skills | CI/CD 自动化 |
| `documentation-and-adrs` | addyosmani/agent-skills | 文档 + 架构决策记录 |
| `deprecation-and-migration` | addyosmani/agent-skills | 废弃与迁移 |
| **do 阶段 5: Complete** | stellarlinkco/myclaude | 记录构建结果 |
| **SPARV 阶段 4: Review** | stellarlinkco/myclaude | 审查交付物 |
| **SPARV 阶段 5: Vault** | stellarlinkco/myclaude | 归档记录 |

### 11.5 完整工作流对比

以"实现一个功能"为例，对比各仓库的完整流程：

| 步骤   | 本笔记  | agent-skills      | mattpocock                   | Waza     | myclaude      |
| ---- | ---- | ----------------- | ---------------------------- | -------- | ------------- |
| 需求对齐 | ✅ 追问 | `interview-me`    | `/grill-with-docs`           | `/think` | do: Clarify   |
| 方案设计 | ✅ 拆解 | `/spec` → `/plan` | `domain-modeling` → `to-prd` | —        | do: Design    |
| 执行   | ✅ 分步 | `/build`          | `/tdd`                       | —        | do: Implement |
| 审查   | ✅ 验证 | `/review`         | `code-review`                | `/check` | do: Review    |
| 收尾   | ✅ 总结 | `/ship`           | —                            | —        | do: Complete  |

### 11.6 最佳实践：按场景选方案

| 你的场景 | 推荐方案 | 原因 |
|---------|---------|------|
| **快速对齐需求**（非代码） | `/grill-me`（mattpocock） | 一句话触发，自动追问到决策树全部分支解决 |
| **需求对齐 + 领域建模** | `/grill-with-docs`（mattpocock） | 对齐同时建立项目术语表，后续会话受益 |
| **完整工程流程** | agent-skills 全套（`/spec`→`/plan`→`/build`→`/test`→`/review`→`/ship`） | 23 个技能覆盖全生命周期 |
| **轻量习惯** | Waza 链式（`/think` → 实现 → `/check`） | 少而精，适合个人开发者 |
| **多智能体协作** | myclaude do 工作流（`/do`） | 自动编排多个 Agent 后端 |
| **极简原则** | karpathy 四大原则 | 一个 CLAUDE.md 文件，零安装成本 |

> **结论**：你不需要从零实现这个工作流。`/grill-me` 和 `interview-me` 已经能完成需求对齐，agent-skills 覆盖了完整的 spec→ship 流程。本笔记的价值在于**理解它们背后的共同模式**，以及**在 Hermes Agent 环境下如何组合使用**——因为 Hermes 的 Skills 生态与 Claude Code/Codex 不同，不是所有上述 skill 都能直接安装，但它们的**设计模式可以直接复用**到自定义 Skill 中。

## 十二、使用示例

> 以下示例展示在 Claude Code / Codex 中实际调用这些 Skill 的效果。注意：Hermes Agent 目前不直接支持这些斜杠命令，但**对话模式（直接描述需求）** 同样有效——我会自动匹配类似的工作流。

### 12.1 示例一：用 `/grill-me` 对齐需求（mattpocock）

**场景**：你想做一个命令行工具，但需求很模糊。

```
你：/grill-me 我想做一个 CLI 工具，用来管理我的笔记

Claude Code：（自动开始追问）
好的，我来帮你理清这个需求：

1. 目标用户是谁？你自己用，还是团队用？
2. 核心功能：你希望这个 CLI 能做什么？
   a) 搜索笔记？
   b) 创建新笔记？
   c) 整理标签？
   d) 导出为其他格式？
   e) 以上全部？
3. 输入输出：笔记存在哪里？本地文件？数据库？云服务？
4. 技术栈偏好：用 Node.js？Python？Rust？
5. 时间线：什么时候需要？MVP 还是完整版？

请先回答前两个问题，我们再继续。
```

**效果**：通过多轮追问，把"做个 CLI 工具"变成清晰的规格说明。

---

### 12.2 示例二：用 `interview-me` 做需求访谈（agent-skills）

**场景**：你想做一个数据分析仪表盘。

```
你：/spec 我想做一个数据分析仪表盘

Claude Code：（触发 interview-me）
好的，先做一次需求访谈，确保我们理解一致：

Q1: 这个仪表盘要展示什么类型的数据？
    └─ 用户：销售数据，按月份和地区

Q2: 谁会用这个仪表盘？
    └─ 用户：销售团队，大概 20 人

Q3: 他们最关心的三个指标是什么？
    └─ 用户：月度销售额、同比增长率、Top 10 客户

Q4: 数据源在哪里？
    └─ 用户：PostgreSQL 数据库，已有 API

Q5: 有什么设计偏好？
    └─ 用户：简洁，移动端友好

访谈完成，需求置信度 ~90%。接下来我生成 PRD 和任务分解。
```

**效果**：95% 置信度的需求规格，直接进入 `/plan` 阶段。

---

### 12.3 示例三：用 agent-skills 完整流程（spec→plan→build→test→review→ship）

**场景**：给一个 Python 项目添加用户认证功能。

```
你：/spec 给这个 Python 项目添加 JWT 用户认证

Claude Code：（先写 PRD）
## PRD: JWT 用户认证
### 目标
- 用户注册/登录
- JWT Token 签发与验证
- 受保护的路由中间件

### 验收标准
- [ ] 注册接口返回 token
- [ ] 登录接口验证密码并返回 token
- [ ] 过期 token 返回 401
- [ ] 测试覆盖率 > 80%

### 边界
- 不包含 OAuth 第三方登录
- 不包含密码重置

---

你：批准，继续

Claude Code：/plan
## 任务分解
1. 安装依赖（pyjwt, passlib）
2. 创建 auth 模块（hash 密码、签发 token、验证 token）
3. 创建注册/登录路由
4. 创建认证中间件
5. 写单元测试
6. 手动测试验证

---

你：开始

Claude Code：/build
（逐个任务实现...）

---

Claude Code：/test
（运行测试，覆盖率 85%）

---

Claude Code：/review
（代码审查，发现 2 个小问题，自动修复）

---

Claude Code：/ship
✅ 完成：
- 注册/登录 API 已实现
- JWT Token 机制
- 认证中间件
- 测试覆盖率 85%
- 已合并到 main 分支
```

**效果**：从一句话需求到上线，全流程 Skill 驱动。

---

### 12.4 示例四：用 Waza 链式轻量流程（think → 实现 → check）

**场景**：重构一个 React 组件。

```
你：/think 我想重构这个 UserCard 组件，它现在有 300 行，太长了

Claude Code：（启动 think skill）
好的，我来挑战这个方案：

1. 这个组件现在承担了几个职责？
   - 渲染用户信息
   - 处理编辑逻辑
   - 处理保存逻辑
   - 处理验证逻辑
   → 至少 4 个职责，违反了单一职责原则

2. 拆分的边界在哪里？
   - UserInfo（展示）
   - UserEditForm（编辑表单）
   - UserValidator（验证逻辑）

3. 有没有不需要改的部分？
   - 外部接口保持一致，调用方不需要改

4. 风险点？
   - 编辑状态管理要小心，避免状态不同步

方案确认后，开始实现。

---

你：批准，开始重构

（Claude Code 执行重构）

---

你：/check

Claude Code：（启动 check skill）
审查结果：
✅ 代码简化：从 300 行 → 3 个文件共 180 行
✅ 接口兼容：外部调用无需修改
✅ 测试通过：原有测试全部通过
✅ 无新增依赖

建议合并。
```

**效果**：轻量、快速，适合个人开发者的日常重构。

---

### 12.5 示例五：用 myclaude do 工作流（多智能体编排）

**场景**：跨模块功能开发，需要多 Agent 协作。

```
你：/do 添加用户登录功能

Claude Code：（启动 do 工作流）

阶段 1: Understand（并行探索）
├─ code-explorer → 扫描代码库，找到认证相关代码
├─ code-explorer → 找到用户模型和数据库配置
└─ 产出：代码库地图

阶段 2: Clarify（条件触发）
├─ 确认：使用 JWT 还是 Session？
├─ 确认：Token 有效期多久？
└─ 用户回答后继续

阶段 3: Design
├─ code-architect → 产出实现方案
└─ 文件规划：auth.py, middleware.py, routes.py

阶段 4: Implement + Review
├─ develop（Codex 后端）→ 实现代码
├─ code-reviewer → 审查代码
└─ 迭代修复

阶段 5: Complete
├─ 记录构建结果
└─ 输出总结报告
```

**效果**：自动编排多个 Agent 后端（Codex 写代码、Claude 做规划），适合复杂项目。

---

### 12.6 示例六：用 karpathy 四大原则（极简模式）

**场景**：不想装任何 Skill，只想让 Agent 行为更好。

```
你：（在 CLAUDE.md 中写入以下内容）

# CLAUDE.md
## Think Before Coding
在写任何代码之前，先分析问题、列出可能的方案、指出权衡。

## Simplicity First
优先选择最简单的方案。不要引入新的框架/库除非绝对必要。

## Surgical Changes
修改时只改需要改的地方。不要顺手重构无关代码。

## Goal-Driven Execution
每步完成后验证是否达到目标。测试通过才算完成。

---

然后正常对话：

你：帮我加一个导出 CSV 的功能

Claude Code：（受四大原则约束）
先分析：
1. 需求：从当前数据列表导出 CSV
2. 方案：Python csv 模块（标准库，无需新依赖）
3. 改动范围：只新增 export.py，不改现有代码
4. 验证：导出后检查 CSV 内容是否正确

开始实现...
```

**效果**：零安装成本，一个文件改变 Agent 行为方式。

---

### 12.7 示例七：在 Hermes Agent 中直接对话（无需斜杠命令）

**场景**：你在 Hermes Agent 中，没有安装任何第三方 Skill，直接描述需求。

```
你：我想了解一下 Kubernetes 的网络模型，帮我做个调研

Hermes Agent：（自动匹配工作流）
好的，我先确认几个问题：

1. 深度：是要一篇全面的介绍，还是重点看某个方面（如 CNI、Service Mesh）？
2. 产出：调研结果存为笔记，还是直接告诉你？
3. 时间范围：最新的实践，还是从基础开始？

你：全面的介绍，存为笔记，从基础开始

Hermes Agent：
好的，计划如下：
1. 先搜索知识库中已有的 K8s 网络笔记，避免重复
2. 用 web_search 获取最新资料
3. 综合整理为笔记，存入 02-Knowledge 下
开始吗？

你：开始

（执行过程...）

✅ 完成：
├─ 搜索到 3 篇已有笔记，补充了新的内容
├─ 新增笔记：Kubernetes网络模型.md
├─ 覆盖：CNI/Service/Pod网络/NetworkPolicy/Ingress
└─ 存放在：02-Knowledge/10-IT技术/容器与编排/K8s/
```

**效果**：在 Hermes Agent 中，**不需要斜杠命令**——直接描述需求，我会自动执行需求对齐→方案设计→执行→验证的完整流程。

---

### 12.8 各方案对比速查

| 方案 | 安装成本 | 学习成本 | 适合场景 | 一句话总结 |
|------|---------|---------|---------|-----------|
| **直接对话（Hermes）** | 零 | 零 | 日常所有场景 | 描述需求即可，我自动处理 |
| **karpathy 四大原则** | 写一个文件 | 1 分钟 | 想改 Agent 行为基调 | 四个原则改变 Agent 习惯 |
| **Waza** | `npx skills add` | 5 分钟 | 个人开发者轻量习惯 | 8 个斜杠命令覆盖核心习惯 |
| **mattpocock/skills** | `npx skills add` | 15 分钟 | TypeScript 项目/需求对齐 | `/grill-me` 是最好的需求对齐工具 |
| **agent-skills** | `/plugin install` | 30 分钟 | 团队标准化工程流程 | 23 个技能覆盖 spec→ship |
| **myclaude** | `npx github:` | 1 小时 | 多 Agent 协作复杂项目 | 自动编排多个 Agent 后端 |

---

## 十三、关联笔记

- [[03-通用skills最佳实践]] — Skills 使用心法与实战案例
- [[04-Skills生态全景]] — 所有可用 Skills 的完整清单
- [[01-快速说明]] — Agent Skills 概念入门
