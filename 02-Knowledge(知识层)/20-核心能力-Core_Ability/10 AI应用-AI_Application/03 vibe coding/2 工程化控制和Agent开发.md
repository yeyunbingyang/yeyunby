# Claude Code 使用指南

适用版本：Claude Code CLI（截至 2026 年 7 月）  
官方文档：[https://code.claude.com/docs](https://code.claude.com/docs)

---

## 目录

1. [上下文压缩控制](https://www.yuque.com/xxcls/vibecoding/ia0yu2m1v3sl537p#1-%E4%B8%8A%E4%B8%8B%E6%96%87%E5%8E%8B%E7%BC%A9%E6%8E%A7%E5%88%B6)
2. [Memory 记忆管理](https://www.yuque.com/xxcls/vibecoding/ia0yu2m1v3sl537p#2-memory-%E8%AE%B0%E5%BF%86%E7%AE%A1%E7%90%86)
3. [代码回退管理](https://www.yuque.com/xxcls/vibecoding/ia0yu2m1v3sl537p#3-%E4%BB%A3%E7%A0%81%E5%9B%9E%E9%80%80%E7%AE%A1%E7%90%86)
4. [自定义技能开发](https://www.yuque.com/xxcls/vibecoding/ia0yu2m1v3sl537p#4-%E8%87%AA%E5%AE%9A%E4%B9%89%E6%8A%80%E8%83%BD%E5%BC%80%E5%8F%91)
5. [代码审查](https://www.yuque.com/xxcls/vibecoding/ia0yu2m1v3sl537p#5-%E4%BB%A3%E7%A0%81%E5%AE%A1%E6%9F%A5)
6. [实用技巧与进阶功能](https://www.yuque.com/xxcls/vibecoding/ia0yu2m1v3sl537p#6-%E5%AE%9E%E7%94%A8%E6%8A%80%E5%B7%A7%E4%B8%8E%E8%BF%9B%E9%98%B6%E5%8A%9F%E8%83%BD)
7. [配置参考速查](https://www.yuque.com/xxcls/vibecoding/ia0yu2m1v3sl537p#7-%E9%85%8D%E7%BD%AE%E5%8F%82%E8%80%83%E9%80%9F%E6%9F%A5)

---

## 1. 上下文压缩控制

### 1.1 核心概念

Claude Code 的上下文窗口有限（通常约 200K tokens）。随着对话进行，历史消息、代码片段、工具调用结果不断累积，最终会触发"上下文窗口满"的情况。有效的上下文管理是保持长会话生产力的**最关键技能**。

### 1.2 `/compact` 命令

**这是最重要的上下文管理命令。**

```
/compact
```

**工作原理**：

- Claude 读取完整对话历史，生成结构化摘要
- 摘要内容包括：已完成的任务、已做的决策、修改过的文件、关键事实
- 早期对话被替换为压缩摘要，仅保留最近的若干轮完整对话
- 压缩后释放大量上下文空间，可以继续工作

**使用时机**：

- ✅ **主动压缩**：每 30-50 轮对话后主动执行，不要等 Claude "开始遗忘"才压缩
- ✅ **任务切换时**：完成一个大任务、开始新任务前
- ✅ **响应变慢时**：对话历史过长会导致处理速度下降
- ✅ **开始出现遗忘迹象**：Claude 开始忽略早期指令时

**注意事项**：

- 压缩是**不可逆**的——压缩后无法恢复被丢弃的原始对话
- 压缩质量取决于对话结构的清晰度——如果对话混乱，摘要也会遗漏信息
- 压缩前可以手动总结关键点告诉 Claude

### 1.3 自动压缩（Auto-Compact）

Claude Code 在上下文接近上限时会**自动触发压缩**，你会在界面看到提示。但依赖自动压缩有以下问题：

- 自动压缩发生在"快满"的时候，此时 Claude 可能已经因为上下文拥挤而表现下降
- 主动 `/compact` 比被动等待自动压缩效果更好

### 1.4 减少上下文消耗的技巧

#### 控制输出量

- **精准提问**：明确指定你需要什么，避免开放式问题产生大量输出
- **文件读取策略**：不要一次性读取整个大文件，指定行范围或搜索特定函数
- **避免不必要的工具调用**：不要让 Claude 重复读取同一文件

#### CLAUDE.md 精简

CLAUDE.md 在每次会话启动时加载到上下文中。保持精简（建议 50-100 行）：

```
# 项目概述
简短描述（2-3 行）

# 常用命令
npm run dev      # 启动开发服务器
npm test         # 运行测试
npm run build    # 构建

# 关键约定
- 使用 TypeScript 严格模式
- 组件文件用 PascalCase
- API 路由放在 src/routes/
```

#### 使用 `.gitignore` 风格的上下文过滤

Claude Code 会自动忽略 `.gitignore` 中的文件和二进制文件，不会将它们加载到上下文中。善用这个特性减少无关文件进入上下文。

### 1.5 上下文状态查看

你可以通过以下方式了解当前上下文使用情况：

- Claude 在每次响应后会显示 token 使用统计（部分版本）
- 观察响应速度：明显变慢 → 可能需要 `/compact`
- 如果 Claude 开始"忘记"本轮对话中你说过的重要信息 → 上下文可能已经滚动或压缩过

---

## 2. Memory 记忆管理

### 2.1 三层记忆体系

Claude Code 的记忆系统分为三个层次：

|                   |                               |      |          |
| ----------------- | ----------------------------- | ---- | -------- |
| 层次                | 位置                            | 作用域  | 加载时机     |
| **项目级 CLAUDE.md** | `<project>/CLAUDE.md`         | 当前项目 | 每次会话启动   |
| **项目级 MEMORY.md** | `<project>/.claude/MEMORY.md` | 当前项目 | 会话中可按需检索 |
| **用户级 MEMORY.md** | `~/.claude/MEMORY.md`         | 所有项目 | 会话中可按需检索 |


### 2.2 CLAUDE.md —— 项目宪法

`CLAUDE.md` 是最重要的记忆载体，它在**每次会话初始化时完整加载**到上下文中。

**应该包含的内容**：

````
# 项目名称

## 概述
这是一个 xxx 项目，用于 xxx。技术栈：React + TypeScript + Node.js。

## 构建与运行
```bash
npm install          # 安装依赖
npm run dev          # 启动开发服务器（端口 3000）
npm test             # 运行单元测试
npm run test:e2e     # 运行端到端测试
npm run build        # 生产构建
````

## 项目结构

- `src/components/` - React 组件
- `src/pages/` - 页面路由
- `src/api/` - API 调用层
- `src/utils/` - 工具函数

## 编码规范

- 组件使用函数式组件 + Hooks
- 状态管理使用 Zustand
- API 请求统一走 `src/api/client.ts`
- 使用 Tailwind CSS，不要自行写 CSS 文件

## 重要约定

- 不要直接修改 `src/generated/`，那是自动生成的
- 环境变量通过 `.env.example` 声明
- PR 之前运行 `npm run lint && npm test`

**创建方式**：
- 手动创建：直接编写 `.md` 文件放在项目根目录
- `/init` 命令：交互式引导创建 CLAUDE.md

**最佳实践**：
- ✅ 保持简短（建议不超过 200 行），信息密度高
- ✅ 优先写"约定"而非"文档"——告诉 Claude **怎么做**而非**是什么**
- ✅ 定期更新——项目演进后及时同步
- ❌ 不要把整个 README 复制进去
- ❌ 不要写 Claude 可以从代码中自动推断的信息


### 2.3 Memory 文件 —— 持久化记忆

Claude Code 支持将**单个事实或偏好**存储为独立的记忆文件。

**文件结构**：
```markdown
---
name: prefer-tabs-over-spaces
description: 用户偏好使用 Tab 缩进
metadata:
  type: user
---
```
用户在所有项目中使用 Tab 而非空格进行缩进。
**Why:** 用户认为 Tab 更灵活，每个开发者可以自行设置宽度。
**How to apply:** 所有代码编辑使用 Tab 缩进，宽度为 4。

**记忆类型**：

|   |   |
|---|---|
|类型|用途|
|`user`|用户身份、角色、偏好|
|`feedback`|用户给出的纠正和反馈|
|`project`|项目目标、约束、非代码事实|
|`reference`|外部资源链接|

**关联记忆**：使用 `[[slug-name]]` 语法关联相关的记忆文件。

**关键命令**：

- 直接告诉 Claude 记住某事：`"记住我使用 pnpm 而非 npm"`
- Claude 会自动创建/更新对应的记忆文件

### 2.4 记忆管理原则

1. **不存代码能推导的信息**：项目结构、git 历史、代码内容不应放入记忆
2. **不存仅限本次对话的信息**：只在本次对话相关的临时事实不需要持久化
3. **及时更新**：偏好改变时告知 Claude 更新记忆
4. **定期审查**：`~/.claude/MEMORY.md` 中的内容可能会过时

---

## 3. 代码回退管理

### 3.1 安全检查点策略

在让 Claude 做重大改动之前，**务必**创建检查点：

```
# 方案1：Git commit 作为检查点
git add -A && git commit -m "checkpoint: before refactoring auth module"

# 方案2：Git stash（不想 commit 时）
git stash push -m "checkpoint: before claude changes"

# 方案3：创建专用分支
git checkout -b experiment/claude-refactor
```

### 3.2 撤销 Claude 的改动

根据改动状态选择不同的回退方式：

```
# 级别1：文件还未 staged，完全丢弃改动
git checkout -- <file>          # 单个文件
git checkout -- .               # 所有文件
git restore .                   # 现代写法

# 级别2：文件已 staged 但未 commit
git reset HEAD <file>           # 取消暂存
git checkout -- <file>          # 丢弃改动

# 级别3：已 commit 但未 push
git reset --soft HEAD~1         # 保留改动在 working tree
git reset --hard HEAD~1         # 完全丢弃改动

# 级别4：已 push
git revert HEAD                 # 创建反向提交（安全，建议用这个）
git reset --hard HEAD~1 && git push --force  # 强制回退（危险！）
```

### 3.3 Git Worktree 隔离

Worktree 允许在独立目录中工作，不影响主工作区：

```
# 创建隔离工作区
git worktree add ../project-experiment experiment-branch

# 查看所有 worktree
git worktree list

# 在隔离区完成工作后，清理
git worktree remove ../project-experiment
```

**适用场景**：

- 试验性重构
- 并行处理多个任务
- Claude Code 的 `/batch` 功能底层就是 worktree

### 3.4 Claude Code 内置的回退机制

#### 对话中的自然撤销

直接告诉 Claude：

- `"撤销你刚才的改动"` —— Claude 会尝试反操作
- `"恢复到 xxx 之前的状态"` —— 指定回退点
- `"把 xxx 文件恢复到改之前"` —— 针对特定文件

#### 备份目录

Claude Code 在 `~/.claude/backups/` 维护了文件备份（如果启用了该功能）。可以在需要时手动恢复。

#### File History

`~/.claude/file-history/` 目录保存了文件修改历史记录。

### 3.5 安全建议

1. **重要的代码先 commit**：这条怎么强调都不过分
2. **在专用分支工作**：别在 main 分支上直接试验
3. **定期检查 diff**：`git diff` 看看 Claude 改了什么
4. **理解改动再继续**：如果你看不懂某个改动，让 Claude 解释
5. **小步提交**：每次小改动后 commit，而不是等所有工作完成

---

## 4. 自定义技能开发

### 4.1 技能系统概述

技能（Skills）是 Claude Code 的扩展机制，分为内置技能和自定义技能。每个技能是一个可以被 `/skill-name` 调用的功能单元。

### 4.2 创建自定义技能

#### 方式一：通过 settings.json 注册简单技能

最简单的技能就是一个指令模板：

```
{
  "skills": {
    "test": "Run the project tests. Use: npm test",
    "deploy-staging": "Deploy to staging. Steps: 1) npm run build 2) npm run deploy:staging 3) Verify at staging.example.com"
  }
}
```

配置在：

- 项目级：`<project>/.claude/settings.local.json`
- 用户级：`~/.claude/settings.json`

#### 方式二：通过插件目录创建技能

在 `~/.claude/plugins/` 下创建技能文件：

```
~/.claude/plugins/
└── my-skill/
    └── skill.md          # 技能定义
```

`skill.md` 的结构：

```
---
name: my-skill
description: 运行自定义的 lint 检查并自动修复
---

# my-skill

## 触发条件
当用户输入 `/my-skill` 或提到 "运行 lint 检查" 时触发。

## 执行步骤
1. 运行 `npm run lint` 获取所有 lint 错误
2. 按错误类型分组
3. 对于可自动修复的错误（如 prettier 格式），自动应用修复
4. 对于需要手动判断的错误，逐一向用户确认
5. 修复后再次运行 lint 确认无错误
```

### 4.3 Hooks 钩子系统

Hooks 允许在特定事件前后自动执行脚本。

#### 支持的 Hook 类型

|   |   |
|---|---|
|Hook|触发时机|
|`pre-command`|执行任意命令之前|
|`post-command`|执行任意命令之后|
|`on-start`|Claude Code 会话启动时|
|`on-complete`|Claude Code 工作完成时|
|`pre-edit`|编辑文件之前|
|`post-edit`|编辑文件之后|

#### 配置示例

```
{
  "hooks": {
    "pre-command": {
      "command": "echo 'Claude 即将执行命令'",
      "description": "记录所有即将执行的命令"
    },
    "post-command": {
      "command": "./scripts/check-breaking-changes.sh",
      "description": "检查是否引入了破坏性变更"
    },
    "on-start": {
      "command": "git fetch --all",
      "description": "启动时拉取最新远程分支"
    }
  }
}
```

#### Hook 脚本可以访问的环境变量

|   |   |
|---|---|
|变量|说明|
|`CLAUDE_EVENT_TYPE`|事件类型（pre-command / post-command 等）|
|`CLAUDE_COMMAND`|将要执行或已执行的命令|
|`CLAUDE_FILE_PATH`|正在编辑的文件路径|
|`CLAUDE_WORKING_DIR`|当前工作目录|

### 4.4 权限管理

通过 settings.json 精细化控制 Claude 的操作权限：

```
{
  "permissions": {
    "allow": [
      "npm test",
      "npm run lint",
      "git status",
      "git diff"
    ],
    "allow-dry-run": [
      "rm -rf",
      "git push"
    ],
    "deny": [
      "rm -rf /",
      "git push --force origin main"
    ]
  }
}
```

权限级别：

- `allow`：无需确认直接执行
- `allow-dry-run`：先展示计划，需要确认才执行
- `ask`：每次询问（默认）
- `deny`：完全禁止

使用 `/fewer-permission-prompts` 技能可以自动分析你的使用记录并生成合理的权限配置。

---

## 5. 代码审查

### 5.1 内置审查命令概览

|   |   |   |
|---|---|---|
|命令|用途|审查范围|
|`/code-review`|代码质量审查|当前工作区 diff|
|`/review`|PR 审查|指定的 Pull Request|
|`/verify`|手动验证改动|实际运行应用确认功能|
|`/security-review`|安全审查|当前分支变更|

### 5.2 `/code-review` 详解

```
/code-review            # 默认审查（中等深度）
/code-review --fix      # 审查并自动修复发现的问题
/code-review --comment  # 审查并将发现发布为 PR 内联评论
```

**审查维度**：

- 🐛 正确性 Bug：逻辑错误、边界情况遗漏、空值处理
- 🔒 安全性：注入漏洞、敏感信息泄露、权限问题
- ♻️ 代码复用：重复代码、可以简化的逻辑
- 📐 代码风格：命名规范、代码结构、可读性
- ⚡ 性能：不必要的计算、内存泄漏、异步处理

**Effort 级别**：

|   |   |   |   |
|---|---|---|---|
|级别|深度|耗时|适用场景|
|`low`|快速扫描|少|小改动、格式修复|
|`medium`|标准审查|中|常规 PR|
|`high`|深度分析|多|核心逻辑、安全敏感代码|
|`xhigh`/`max`|全面审查|最多|关键基础设施、安全审计|

### 5.3 `/review` —— PR 审查

```
/review <PR_URL>
```

**工作原理**：

1. 检出 PR 分支
2. 分析完整 diff
3. 生成结构化审查报告：

```
## Code Review Summary

### Critical Issues
- [file:line] 未处理的 Promise rejection 可能导致未捕获异常

### Suggestions
- [file:line] 考虑将重复的 fetch 逻辑提取为自定义 Hook
- [file:line] 建议使用 useMemo 缓存计算结果

### Praise
- 错误边界处理得很好
- 测试覆盖率充分
```

### 5.4 `/verify` —— 手动验证

```
/verify
```

适用于需要实际运行应用来确认改动生效的场景：

- 前端 UI 改动：启动开发服务器，在浏览器中检查
- API 改动：发送实际请求验证响应
- CLI 工具：运行命令行确认输出

### 5.5 `/security-review` —— 安全审查

专门针对安全问题的深度审查：

- SQL 注入、XSS、CSRF
- 敏感信息（API Key、密码）是否被提交
- 依赖项是否有已知漏洞
- 认证授权逻辑是否正确

### 5.6 最佳实践

1. **commit 前审查**：养成 `/code-review` 再 commit 的习惯
2. **分级审查**：普通改动 `medium`，核心模块 `high` 或 `max`
3. **结合测试**：先让 Claude 写测试，再用 `/verify` 确认通过
4. **大 PR 分文件审查**：一次改 20 个文件则分多次审查
5. **审查后不要盲从**：Claude 的审查建议需要人工判断是否采纳

---

## 6. 实用技巧与进阶功能

### 6.1 对话管理技巧

#### 任务分解

长任务拆分为多个短对话，每个对话聚焦一个子任务：

```
❌ "重构整个认证模块、数据层、UI 层"
✅ 对话1："重构认证模块的 token 管理"
   对话2："重构认证的数据层查询"
   对话3："重构登录和注册页面 UI"
```

每次对话结束后，在下一个对话开始时提供上下文摘要。

#### 精确引用

引用文件时使用 `file.ts:42` 格式，Claude 会直接定位到具体行：

```
请查看 src/api/auth.ts:120-150 的 token 刷新逻辑
```

#### 利用 Plan Mode

在复杂任务开始前进入 Plan Mode 确认方案：

```
这个任务比较复杂，请先进入 Plan Mode 设计方案。
```

Plan Mode 中 Claude 会探索代码库、设计实施路径，在得到你的确认后再动手写代码。这避免了返工。

### 6.2 子代理（Sub-agent）并行处理

Claude Code 可以派生子代理并行处理独立任务：

**适用场景**：

- 同时研究多个技术方案
- 并行审查多个文件
- 同时搜索不同维度的信息

**示例提示**：

```
请同时做三件事：
1. 审查 src/api/ 下所有文件的错误处理
2. 审查 src/components/ 下所有组件的性能
3. 审查 src/utils/ 下所有工具函数的测试覆盖
```

Claude 会自动决定哪些任务可以并行处理。

### 6.3 Keyboard Shortcuts

|   |   |
|---|---|
|快捷键|功能|
|`Ctrl+C`|取消当前操作 / 中断 Claude 输出|
|`Ctrl+D`|退出会话|
|`↑/↓`|浏览命令历史|
|`Ctrl+L`|清屏|
|`Ctrl+R`|搜索命令历史|
|`Enter`|发送消息|
|`Shift+Enter`|换行（多行输入模式）|

可通过 `~/.claude/keybindings.json` 自定义。

### 6.4 IDE 集成

#### VS Code 扩展

安装 Claude Code VS Code 扩展后：

- 在编辑器内直接与 Claude 对话
- 选中代码后 `Cmd+Shift+L` 发送给 Claude
- 内联编辑建议
- 文件 diff 预览

#### JetBrains 插件

支持 IntelliJ IDEA、WebStorm、PyCharm 等。

### 6.5 MCP 服务器扩展

MCP（Model Context Protocol）允许为 Claude Code 添加额外工具：

```
{
  "mcpServers": {
    "github": {
      "command": "npx",
      "args": ["-y", "@anthropic/mcp-server-github"],
      "env": {
        "GITHUB_TOKEN": "${GITHUB_TOKEN}"
      }
    },
    "postgres": {
      "command": "npx",
      "args": ["-y", "@anthropic/mcp-server-postgres"],
      "env": {
        "DATABASE_URL": "postgresql://localhost/mydb"
      }
    }
  }
}
```

常见的 MCP 服务器：数据库查询、文件系统操作、API 集成、第三方服务。

### 6.6 Token 预算与成本控制

#### 设置 Effort Level

```
# 命令行参数
claude --effort low     # 快速、省 token
claude --effort medium  # 默认
claude --effort high    # 深度分析

# 或在 settings.json 中
{
  "effortLevel": "high"
}
```

#### 理解 Effort Level

- `low`：快速回答，较少工具调用，适合简单问题
- `medium`：标准分析深度，适合日常开发
- `high`：深度分析，更多验证步骤，适合复杂重构
- `xhigh`/`max`：最大深度，多次交叉验证，适合安全审计等关键任务

### 6.7 环境变量速查

|   |   |
|---|---|
|变量|说明|
|`ANTHROPIC_BASE_URL`|自定义 API 端点（如使用代理）|
|`ANTHROPIC_AUTH_TOKEN`|API 认证 Token|
|`ANTHROPIC_MODEL`|默认模型|
|`ANTHROPIC_DEFAULT_HAIKU_MODEL`|轻量任务使用的模型|
|`CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC`|设为 `1` 禁用遥测|
|`CLAUDE_CODE_EFFORT_LEVEL`|全局 Effort Level|

### 6.8 管道和脚本集成

Claude Code 支持管道输入：

```
# 将文件内容管道给 Claude
cat error.log | claude "分析这个错误日志"

# 将 git diff 管道给 Claude
git diff | claude "审查这些改动"

# 非交互式执行
claude -p "解释 src/main.ts 的架构" > analysis.md
```

### 6.9 回话管理

```
# 恢复上一次会话
claude --resume

# 列出最近的会话
claude --list-sessions

# 指定会话名称
claude --session "debug-auth-issue"
```

### 6.10 不太为人所知但非常实用的功能

#### 1. `/loop` 定时循环

```
/loop 5m /code-review
/loop 10m "检查 CI 状态"
```

定期自动执行指定任务。适合监控场景。

#### 2. `/statusline` 状态栏

```
/statusline
```

在终端底部显示持久状态栏：当前任务、token 用量、活跃模型。

#### 3. 非交互模式

```
# 一次性问答
claude -p "这个项目的入口文件是什么？"

# 输出到文件
claude -p "生成 API 文档" > api-docs.md
```

#### 4. 文件搜索效率

不要用 `cat`/`head`/`tail` 等 shell 命令查看文件，直接让 Claude 读：

```
❌ "运行 cat src/utils.ts"
✅ "查看 src/utils.ts"
```

Claude 有专门的 Read 工具，比 shell 命令更高效。

#### 5. 利用 `!` 前缀在对话中运行命令

在对话中输入 `!<command>` 会直接在当前会话执行：

```
!git status
!npm test
```

#### 6. Debug 模式

```
/debug
```

开启详细日志，用于排查权限问题、连接问题等。

#### 7. Team Onboarding

```
/team-onboarding
```

根据你的使用模式生成团队上手指南。

---

## 7. 配置参考速查

### 7.1 配置文件位置

|   |   |   |
|---|---|---|
|文件|作用域|优先级|
|`<project>/.claude/settings.local.json`|项目|最高|
|`~/.claude/settings.json`|用户|中|
|环境变量|会话|最低|

### 7.2 settings.json 完整示例

```
{
  "env": {
    "ANTHROPIC_BASE_URL": "https://api.deepseek.com/anthropic",
    "ANTHROPIC_AUTH_TOKEN": "sk-xxx",
    "ANTHROPIC_MODEL": "deepseek-v4-pro[1m]",
    "CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC": "1"
  },
  "effortLevel": "high",
  "theme": "dark",
  "permissions": {
    "allow": [
      "npm test",
      "npm run lint",
      "git status",
      "git diff",
      "git log"
    ],
    "deny": [
      "rm -rf /",
      "git push --force origin main"
    ]
  },
  "hooks": {
    "pre-command": {
      "command": "echo '[Claude] 即将执行命令'"
    }
  },
  "skills": {
    "deploy-staging": "Deploy current branch to staging. Steps: npm run build && npm run deploy:staging"
  },
  "mcpServers": {
    "github": {
      "command": "npx",
      "args": ["-y", "@anthropic/mcp-server-github"]
    }
  }
}
```

### 7.3 目录结构总览

```
~/.claude/
├── settings.json          # 用户全局配置
├── MEMORY.md              # 用户级记忆
├── memory/                # 分文件的记忆存储
├── history.jsonl          # 命令历史
├── keybindings.json       # 自定义快捷键
├── plugins/               # 自定义技能插件
├── backups/               # 文件备份
├── file-history/          # 文件修改历史
├── sessions/              # 会话存档
├── projects/              # 项目级记忆（按项目存储）
└── plans/                 # Plan Mode 保存的计划

<project>/
├── CLAUDE.md              # 项目级记忆（会话启动时加载）
└── .claude/
    ├── settings.local.json # 项目级配置
    └── MEMORY.md           # 项目级记忆
```

---

## 附录：典型工作流

### A. 新功能开发流程

```
1. git checkout -b feature/new-login
2. git commit -m "checkpoint: before new login feature"  # 创建检查点
3. 在 Claude Code 中描述需求
4. Claude 进入 Plan Mode 设计方案
5. 确认方案后 Claude 开始编码
6. /code-review 审查改动
7. /verify 手动验证功能
8. git commit -m "feat: new login flow"
```

### B. Bug 修复流程

```
1. git checkout -b fix/login-timeout
2. 向 Claude 描述 Bug 现象和复现步骤
3. Claude 定位问题并修复
4. /code-review --fix 审查并自动修复小问题
5. npm test 确认无回归
6. git commit
```

### C. 代码审查流程

```
1. 完成本地改动后
2. /code-review（审查工作区 diff）
3. 根据建议修改
4. /verify 验证
5. 提交 PR
6. /review <PR_URL>（可选，让 Claude 再审查一遍 PR）
```

---

**注意**：本文档基于 Claude Code 截至 2026 年 7 月的功能编写。Claude Code 迭代频繁，建议定期查阅[官方文档](https://code.claude.com/docs)获取最新信息。如果你使用了第三方 API 代理（如 DeepSeek），部分功能的行为可能与官方版本存在差异。