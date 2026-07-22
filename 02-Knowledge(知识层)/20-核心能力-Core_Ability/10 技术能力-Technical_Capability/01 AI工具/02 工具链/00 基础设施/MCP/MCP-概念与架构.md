---
title: MCP 概念与架构
domain: Core_Ability
tags: [MCP, 协议, Agent, 工具链]
status: 稳定
created: 2026-07-22
updated: 2026-07-22
summary: "MCP协议全景——从USB-C类比到企业级工具链，涵盖概念定义、使用方法、核心价值和场景矩阵"
source: 拆分自MCP深度解析与本地模型企业级应用指南.md
---
## 一、MCP 概念全景：从 USB-C 到企业级工具链

### 1.1 一句话定义

> **MCP（Model Context Protocol）是 AI 调用外部工具的 USB-C 接口。**  
> 它标准化了 LLM 与文件系统、数据库、API、浏览器等外部资源的连接方式，让任何符合标准的工具都能即插即用。

### 1.2 为什么叫 USB-C

| 类比 | USB-C | MCP |
|------|-------|-----|
| **标准化** | 一根线连手机、电脑、显示器、充电器 | 一个协议连文件、数据库、Git、浏览器、Slack |
| **即插即用** | 插入自动识别设备 | 配置后 AI 自动识别工具能力 |
| **厂商无关** | 不分苹果/安卓/Windows | 不分 OpenAI/Anthropic/本地模型 |
| **扩展性** | 转接头扩展更多接口 | 任意开发者可开发新 MCP Server |

### 1.3 MCP 与 A2A 的关系

```
用户请求
  │
  ├─→ 【A2A 层】Agent 之间协作（多个 Agent 分工）
  │     → 招聘主 Agent 委托 简历筛选 Agent 干活
  │
  └─→ 【MCP 层】Agent 调用工具（单个 Agent 的能力延伸）
        → 简历筛选 Agent 通过 MCP 连接数据库查简历
```

**核心区别：**
- **MCP** = Agent 怎么调用工具（内部能力延伸）
- **A2A** = Agent 之间怎么对话（外部协作分工）

### 1.4 技术架构五层

| 层级 | 组件 | 作用 |
|------|------|------|
| **传输层** | stdio / HTTP / SSE | 数据传输通道 |
| **协议层** | JSON-RPC 2.0 | 消息格式标准 |
| **能力层** | Tools / Resources / Prompts | 三种能力抽象 |
| **应用层** | MCP Client / Server | 客户端发起请求，服务端提供工具 |
| **生态层** | Registry / Marketplace | 工具注册与发现 |

### 1.5 三种核心能力

| 能力 | 说明 | 示例 |
|------|------|------|
| **Tools** | 函数调用，AI 主动执行动作 | read_file, execute_sql, send_slack_message |
| **Resources** | 只读数据，AI 查询信息 | file://project/README.md, db://users/schema |
| **Prompts** | 预设模板，标准化交互 | /code_review, /generate_tests |

---

## 二、MCP 如何使用：从安装到调用全流程

### 2.1 安装一个 MCP Server（以文件系统为例）

```bash
# 方法1：npx 直接运行（无需安装）
npx -y @modelcontextprotocol/server-filesystem /path/to/your/project

# 方法2：全局安装
npm install -g @modelcontextprotocol/server-filesystem

# 方法3：Python 环境
pip install mcp-server-filesystem
```

### 2.2 配置到 Claude Desktop / Cursor

```json
// ~/Library/Application Support/Claude/claude_desktop_config.json
// 或 ~/.cursor/mcp.json
{
  "mcpServers": {
    "filesystem": {
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-filesystem",
        "/Users/yourname/projects"
      ]
    },
    "git": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-git"]
    }
  }
}
```

### 2.3 配置到 OmniRoute（企业级统一管理）

```yaml
# OmniRoute 内置 95 个 MCP 工具，开箱即用
mcp:
  enabled: true
  auto_load: true  # 自动加载内置工具

  # 额外自定义工具
  custom_servers:
    - name: "company-crm"
      command: "node"
      args: ["/path/to/crm-mcp-server/index.js"]
      env:
        CRM_API_KEY: "${CRM_API_KEY}"

    - name: "internal-db"
      command: "npx"
      args: ["-y", "@modelcontextprotocol/server-postgres", "postgresql://localhost:5432/internal"]
```

### 2.4 AI 调用 MCP 的完整流程

```
用户：帮我读取项目根目录的 README.md
  │
  ├─→ AI 识别意图：需要读取文件
  ├─→ AI 查询可用 MCP Tools：发现 filesystem Server 有 read_file 工具
  ├─→ AI 生成调用请求：
  │     {
  │       "tool": "read_file",
  │       "arguments": { "path": "/path/to/project/README.md" }
  │     }
  ├─→ MCP Client 发送请求 → MCP Server (filesystem)
  ├─→ MCP Server 读取文件 → 返回内容
  ├─→ AI 接收内容 → 生成回答
  └─→ 用户看到：README.md 内容如下：...
```

### 2.5 开发自定义 MCP Server（Python 示例）

```python
# my_mcp_server.py
from mcp.server import Server
from mcp.types import Tool, TextContent
import sqlite3

app = Server("internal-database")

@app.tool()
async def query_employee(name: str) -> list[dict]:
    """Query employee information (internal database)"""
    conn = sqlite3.connect("/data/internal.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM employees WHERE name LIKE ?", (f"%{name}%",))
    results = cursor.fetchall()
    conn.close()
    return results

@app.tool()
async def get_department_budget(dept_id: int) -> dict:
    """Query department budget (sensitive operation, requires permission)"""
    # Permission check logic can be added here
    conn = sqlite3.connect("/data/internal.db")
    cursor = conn.cursor()
    cursor.execute("SELECT budget FROM departments WHERE id = ?", (dept_id,))
    result = cursor.fetchone()
    conn.close()
    return {"budget": result[0] if result else None}

if __name__ == "__main__":
    app.run()
```

---

## 三、MCP 作用与价值：为什么需要它

### 3.1 没有 MCP 的世界

```python
# 传统方式：每个工具都要写适配代码
# OpenAI 适配
def call_openai_with_file(prompt, file_path):
    file_content = read_file(file_path)
    messages = [{"role": "user", "content": f"{prompt}\n\n{file_content}"}]
    return openai.chat.completions.create(model="gpt-4", messages=messages)

# Claude 适配（完全不同的 API）
def call_claude_with_file(prompt, file_path):
    file_content = read_file(file_path)
    return anthropic.messages.create(
        model="claude-3",
        messages=[{"role": "user", "content": f"{prompt}\n\n{file_content}"}]
    )

# 每加一个模型、每加一个工具，都要重写适配代码
# 10 个模型 x 20 个工具 = 200 个适配函数
```

### 3.2 有 MCP 的世界

```python
# MCP 方式：一次配置，到处使用
# MCP Server 提供标准化接口
# 任何 MCP Client（Claude/Cursor/OmniRoute）都能自动识别和使用

# 开发者只需：开发 1 个 MCP Server
# 用户只需：配置 1 次
# AI 自动：识别工具 → 生成调用 → 获取结果
```

### 3.3 核心价值量化

| 维度 | 无 MCP | 有 MCP | 提升 |
|------|--------|--------|------|
| **集成效率** | 10 模型 x 20 工具 = 200 个适配 | 10 + 20 = 30 个配置 | **5 倍提升** |
| **开发周期** | 2 周/工具 | 2 天/工具 | **7 倍提升** |
| **安全审计** | 分散在各处 | 统一在 MCP Server | **覆盖率 100%** |
| **故障排查** | 难以定位 | 标准化日志 | **时间缩短 80%** |

---

## 四、MCP 场景矩阵：什么时候用、用什么

### 4.1 按任务类型选择 MCP Server

| 你要做什么                  | 推荐 MCP Server     | 配置复杂度 | 安全级别   |
| ---------------------- | ----------------- | ----- | ------ |
| **读取项目文件**             | filesystem        | 1星    | 低      |
| **操作 Git 仓库**          | git               | 2星    | 中      |
| **连接数据库**              | postgres / sqlite | 3星    | 高      |
| **查询 GitHub Issue/PR** | github            | 2星    | 中      |
| **发送 Slack 消息**        | slack             | 2星    | 中      |
| **操作 Notion 文档**       | notion            | 2星    | 低      |
| **网页抓取**               | puppeteer / fetch | 3星    | 中      |
| **执行 Shell 命令**        | command           | 4星    | **极高** |
| **访问内部 API**           | 自定义 fetch         | 3星    | 高      |
| **查询企业知识库**            | 自定义 vector-search | 4星    | 高      |

### 4.2 按安全级别选择

| 安全级别 | 允许的操作 | 推荐 MCP Server | 审计要求 |
|---------|-----------|----------------|---------|
| **公开级** | 只读公开文档 | fetch, filesystem(只读) | 可选 |
| **内部级** | 读取内部代码/文档 | filesystem, git, github | 记录访问日志 |
| **敏感级** | 查询数据库、调用内部 API | postgres, 自定义 API | 全量审计 |
| **核心级** | 执行命令、修改生产环境 | command(严格受限) | 双人复核 + 实时告警 |

### 4.3 企业级 MCP 权限控制

```yaml
# 动态权限配置示例
mcp_permissions:
  roles:
    - name: "developer"
      allowed_servers:
        - "filesystem"          # 只读项目文件
        - "git"                 # 读仓库
        - "github"              # 读 Issue/PR
        - "fetch"               # 查询公开文档
      denied_servers:
        - "command"             # 禁止执行命令
        - "postgres"            # 禁止直连数据库

    - name: "dba"
      allowed_servers:
        - "postgres"            # 只读查询
        - "sqlite"
      denied_operations:
        - "DELETE"
        - "DROP"
        - "UPDATE"

    - name: "devops"
      allowed_servers:
        - "command"
      command_whitelist:
        - "docker ps"
        - "kubectl get pods"
        - "systemctl status"
      command_blacklist:
        - "rm -rf"
        - "DROP DATABASE"
```

---

