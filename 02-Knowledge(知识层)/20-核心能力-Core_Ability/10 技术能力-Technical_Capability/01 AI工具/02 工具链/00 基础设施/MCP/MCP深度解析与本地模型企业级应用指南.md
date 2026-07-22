---
title: MCP深度解析与本地模型企业级应用指南
domain: Core_Ability
tags: [MCP, 归档, 已拆分]
status: 归档
created: 2026-07-21
updated: 2026-07-22
summary: 已拆分为三篇独立笔记：MCP-概念与架构 / MCP-企业级应用与本地部署 / MCP-安全路由与配置速查
---

# MCP 深度解析与本地模型企业级应用指南

> **整理日期**: 2026-07-21  
> **核心聚焦**: MCP 概念落地 × 本地模型企业安全实践 × 本地 RAG 构建  
> **策略原则**: 本地模型 = 隐私堡垒 + 离线可用；云端 = 质量天花板；MCP = 能力延伸器

---

## 目录

1. [MCP 概念全景：从 USB-C 到企业级工具链](#一mcp-概念全景从-usb-c-到企业级工具链)
2. [MCP 如何使用：从安装到调用全流程](#二mcp-如何使用从安装到调用全流程)
3. [MCP 作用与价值：为什么需要它](#三mcp-作用与价值为什么需要它)
4. [MCP 场景矩阵：什么时候用、用什么](#四mcp-场景矩阵什么时候用用什么)
5. [MCP 实际落地案例（企业级）](#五mcp-实际落地案例企业级)
6. [本地模型：企业安全视角下的核心定位](#六本地模型企业安全视角下的核心定位)
7. [本地模型 vs 云端：文件编写与联网的深层差异](#七本地模型-vs-云端文件编写与联网的深层差异)
8. [本地 RAG 构建：企业知识库实践](#八本地-rag-构建企业知识库实践)
9. [本地模型 + MCP：企业安全 Agent 工作流](#九本地模型--mcp企业安全-agent-工作流)
10. [OmniRoute 配置：本地优先安全路由](#十omniroute-配置本地优先安全路由)
11. [附录：MCP Server 速查表](#十一附录mcp-server-速查表)

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

## 五、MCP 实际落地案例（企业级）

### 5.1 案例一：金融风控系统（招商银行）

**场景**: 智能风控引擎需要实时对接 10+ 外部数据源（征信、舆情、交易记录）

**方案**:
```
MCP Server 层:
  ├── credit-mcp (征信查询)
  ├── news-mcp (舆情监控)
  ├── transaction-mcp (交易记录)
  └── risk-model-mcp (风控模型)

AI Agent 层:
  └── Risk Assessment Agent
      → 通过 MCP 并行调用 4 个数据源
      → 聚合结果 → 生成风险评估报告
```

**成效**:
- 风险识别准确率提升 **22%**
- 欺诈案件减少 **40%**
- 敏感数据访问审计覆盖率 **100%**

### 5.2 案例二：工业物联网（华为云）

**场景**: 汽车制造企业需要监控 5000+ 生产线传感器

**方案**:
```
MCP Server 层 (部署在边缘节点):
  ├── sensor-temperature-mcp
  ├── sensor-vibration-mcp
  ├── sensor-pressure-mcp
  └── plc-controller-mcp

AI Agent 层:
  └── Predictive Maintenance Agent
      → 实时采集传感器数据（MCP）
      → 异常检测 → 预测故障
      → 自动触发维护工单
```

**成效**:
- 设备故障率降低 **28%**
- 生产效率提升 **18%**
- 维护成本降低 **40%**（故障提前 72 小时预测）

### 5.3 案例三：AI 编程工作流（Claude Code + MCP）

**场景**: 开发团队需要 AI 自动读取代码、分析依赖、提交 PR

**方案**:
```
Claude Code (Agent)
  ├── MCP: filesystem → 读取项目文件
  ├── MCP: git → 分析代码变更
  ├── MCP: github → 创建 PR、添加评论
  └── MCP: command → 运行测试、检查 lint

工作流:
  1. 用户：重构这个模块的异常处理
  2. Claude → filesystem 读取相关文件
  3. Claude → git 分析历史变更
  4. Claude 生成修改方案 → 用户确认
  5. Claude → command 运行测试
  6. Claude → github 创建 PR
```

**成效**:
- 开发效率提升 **35%**
- UI 测试覆盖率从 60% 提升至 **95%**

### 5.4 案例四：企业知识库 RAG（医疗行业）

**场景**: 医院需要 AI 辅助诊断，同时保证患者数据不出域

**方案**:
```
本地部署:
  ├── 本地 LLM (Qwen3-Coder 32B)
  ├── MCP: vector-search (本地向量数据库)
  ├── MCP: his-system (医院 HIS 系统)
  └── MCP: medical-literature (医学文献库)

工作流:
  1. 医生输入症状
  2. AI → MCP: his-system 调取患者历史病历
  3. AI → MCP: vector-search 检索相似病例
  4. AI → MCP: medical-literature 查询最新研究
  5. AI 生成诊断建议报告（本地处理，数据不出域）
```

**成效**:
- 诊断准确率 **92%**
- 报告生成时间 **< 30 秒**
- 患者数据 **100% 本地处理**

### 5.5 案例五：微信支付 MCP（商业化闭环）

**场景**: AI 内容平台需要闭环支付能力

**方案**:
```
AI 内容生成 Agent
  └── MCP: wechat-pay
      → create_native_payment (生成付款码)
      → verify_payment (验证支付)
      → deliver_content (交付内容)

工作流:
  用户：写一首关于夏天的诗
  AI：这首诗需要 1 分钱，请扫码支付
  用户支付 → AI 验证 → AI 生成并交付诗歌
```

**成效**:
- 付费率提升 **28%**
- 复购率提升 **15%**（毫秒级优惠券推送）
- 形成 收款-数据-优化-增收 闭环

---

## 六、本地模型：企业安全视角下的核心定位

### 6.1 为什么企业必须考虑本地模型

| 风险维度 | 云端模型 | 本地模型 |
|---------|---------|---------|
| **数据泄露** | 数据上传至第三方服务器 | 数据绝对不出域 |
| **训练数据滥用** | 默认用于模型训练（需手动关闭） | 不可能被训练 |
| **合规审计** | 难以通过等保/密评 | 完全可控，审计友好 |
| **网络依赖** | 必须联网，断网即失效 | 可完全离线运行 |
| **供应商锁定** | 依赖单一厂商 | 开源模型，自主可控 |
| **成本不可控** | 按量计费，用量突增风险 | 硬件一次性投入 |
| **跨境传输** | 数据可能出境（GDPR/PIPL 风险） | 数据物理隔离 |

### 6.2 企业安全分级部署策略

```
┌─────────────────────────────────────────────┐
│  核心数据区（最高安全）                       │
│  → 本地模型 + 本地 RAG + 本地 MCP            │
│  → 金融交易数据、患者病历、核心代码           │
│  → 物理隔离，无网络出口                       │
├─────────────────────────────────────────────┤
│  内部数据区（高安全）                         │
│  → 本地模型 + 内部 MCP Server                 │
│  → 内部文档、员工信息、项目资料               │
│  → 内网访问，受控出口                         │
├─────────────────────────────────────────────┤
│  一般数据区（中等安全）                       │
│  → 国内云端模型（备案）+ 审计                 │
│  → 公开文档、一般性代码、测试数据             │
│  → 可联网，但需标识和审计                     │
├─────────────────────────────────────────────┤
│  公开数据区（低安全）                         │
│  → 国外云端模型（按需）                        │
│  → 开源项目、公开论文、技术调研               │
│  → 无敏感信息，可自由使用                       │
└─────────────────────────────────────────────┘
```

### 6.3 本地模型的企业安全优势

| 安全要求 | 本地模型实现方式 |
|---------|----------------|
| **等保三级** | 本地部署，物理隔离，可控审计 |
| **密评（密码评测）** | 自管密钥，国密算法支持 |
| **数据不出境** | 完全内网运行，无跨境传输 |
| **最小权限** | MCP 权限控制，字段级访问 |
| **操作审计** | 全量 MCP 调用日志，可追溯 |
| **灾备恢复** | 本地备份，自主恢复策略 |

---

## 七、本地模型 vs 云端：文件编写与联网的深层差异

### 7.1 本地模型不联网：是劣势也是优势

| 维度 | 云端模型（联网） | 本地模型（不联网） |
|------|-----------------|-------------------|
| **信息时效性** | 可查询最新新闻、文档 | 知识截止于训练数据 |
| **外部 API 调用** | 可调用搜索引擎、天气、股价 | 无法直接访问互联网 |
| **信息准确性** | 可能搜到错误/过时信息 | 依赖内置知识，相对稳定 |
| **隐私风险** | 查询内容上传至搜索引擎 | 完全本地，零泄露 |
| **确定性** | 搜索结果每次不同 | 相同输入相同输出 |

**关键洞察**: 本地模型不联网不是缺陷，而是**设计特性**。在企业场景下，这恰恰是安全优势。

### 7.2 联网需求的替代方案：本地 RAG + MCP

```
用户提问：最新的 React 19 特性有哪些？

云端方案：
  AI → 联网搜索 → 获取最新博客/文档 → 回答

本地方案（企业安全）：
  AI → MCP: vector-search → 查询本地知识库（定期同步官方文档）
      → MCP: fetch → 查询预批准的内部文档站点
      → 基于本地缓存回答

差异：
  - 信息可能滞后 1-7 天（取决于同步频率）
  - 但绝对安全、可控、可审计
```

### 7.3 本地模型文件编写的劣势与应对

| 劣势 | 原因 | 应对方案 |
|------|------|---------|
| **代码质量略低** | 32B 模型 vs 1T+ 云端模型 | 简单任务本地写，复杂任务云端 fallback |
| **长文件处理受限** | 上下文 128K vs 1M | 分段处理 + 本地 RAG 检索 |
| **多语言混合弱** | 训练数据以中文/英文为主 | 选择 Qwen3（29+ 语言）或针对性微调 |
| **缺乏最新框架知识** | 知识截止于训练日期 | 定期更新本地知识库（RAG） |
| **创意/架构设计弱** | 参数量限制 | 架构设计用云端，实现用本地 |

**核心策略**: 本地模型负责 **实现**（编码、文档、查询），云端模型负责 **设计**（架构、创新、复杂推理）。

---

## 八、本地 RAG 构建：企业知识库实践

### 8.1 为什么本地 RAG 是本地模型的必备搭档

> 本地模型知识截止于训练日期，无法获取最新信息。RAG（检索增强生成）让本地模型能够查询企业私有知识库，弥补这一缺陷。

```
没有 RAG 的本地模型：
  用户：我们公司 2026 年的请假政策是什么？
  本地模型：我不知道，我的知识截止于 2025 年。

有 RAG 的本地模型：
  用户：我们公司 2026 年的请假政策是什么？
  本地模型 → RAG 检索 → 找到《员工手册 2026 版》→ 根据最新政策...
```

### 8.2 本地 RAG 架构

```
┌─────────────────────────────────────────────┐
│  数据源层                                    │
│  ├── 内部文档（Word/PDF/Markdown）           │
│  ├── 代码仓库（Git 历史 + 注释）             │
│  ├── 数据库（产品信息、客户数据）             │
│  ├── 邮件/聊天记录（脱敏后）                  │
│  └── 外部文档（定期同步的技术文档）           │
├─────────────────────────────────────────────┤
│  处理层（Embedding + 索引）                    │
│  ├── 文本分块（Chunking）                     │
│  ├── 向量化（Embedding Model）               │
│  │   └── 本地部署：bge-large-zh / m3e        │
│  └── 索引存储（Vector DB）                   │
│      └── ChromaDB / Milvus / Qdrant（本地）  │
├─────────────────────────────────────────────┤
│  检索层（RAG）                               │
│  ├── 语义检索（向量相似度）                    │
│  ├── 关键词检索（BM25）                       │
│  └── 混合检索（Semantic + Keyword）           │
├─────────────────────────────────────────────┤
│  生成层（本地 LLM）                          │
│  └── Qwen3-Coder 32B / DeepSeek-R1 32B      │
│      → 接收检索结果 + 用户问题 → 生成回答     │
└─────────────────────────────────────────────┘
```

### 8.3 本地 RAG 实施步骤

```bash
# Step 1: 安装本地向量数据库
pip install chromadb

# Step 2: 准备 Embedding 模型（本地）
# 下载 bge-large-zh 到本地
# https://huggingface.co/BAAI/bge-large-zh

# Step 3: 文档处理与索引
python << 'EOF'
from langchain.document_loaders import DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import Chroma

# 加载文档
loader = DirectoryLoader("/company/docs", glob="**/*.md")
docs = loader.load()

# 分块
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)
chunks = text_splitter.split_documents(docs)

# 本地 Embedding（数据不出域）
embeddings = HuggingFaceEmbeddings(
    model_name="/local/models/bge-large-zh"
)

# 创建本地向量数据库
vectorstore = Chroma.from_documents(
    documents=chunks,
    embedding=embeddings,
    persist_directory="/company/vector_db"
)
vectorstore.persist()
EOF

# Step 4: 配置 MCP Server 连接 RAG
# 开发自定义 MCP Server 封装向量检索
```

### 8.4 自定义 RAG MCP Server

```python
# rag_mcp_server.py
from mcp.server import Server
from mcp.types import Tool, TextContent
import chromadb
from sentence_transformers import SentenceTransformer

app = Server("company-knowledge-base")

# 加载本地向量数据库
client = chromadb.PersistentClient(path="/company/vector_db")
collection = client.get_collection("company_docs")
model = SentenceTransformer("/local/models/bge-large-zh")

@app.tool()
async def search_knowledge(query: str, top_k: int = 5) -> list[dict]:
    """Search enterprise knowledge base"""
    # 本地 Embedding 查询
    query_embedding = model.encode(query).tolist()

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=top_k
    )

    return [
        {
            "content": doc,
            "source": meta["source"],
            "score": score
        }
        for doc, meta, score in zip(
            results["documents"][0],
            results["metadatas"][0],
            results["distances"][0]
        )
    ]

@app.tool()
async def get_document_by_id(doc_id: str) -> str:
    """Get full content of specified document"""
    result = collection.get(ids=[doc_id])
    return result["documents"][0] if result["documents"] else "Not found"

if __name__ == "__main__":
    app.run()
```

### 8.5 本地 RAG 与 MCP 结合使用

```json
// mcp_config.json
{
  "mcpServers": {
    "company-kb": {
      "command": "python",
      "args": ["/company/mcp/rag_mcp_server.py"]
    },
    "filesystem": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-filesystem", "/company/projects"]
    }
  }
}
```

```
用户：帮我查一下去年 Q3 的销售数据，并生成一份分析报告
  │
  ├─→ AI → MCP: company-kb → search_knowledge("Q3 销售数据")
  │       → 返回相关文档片段
  ├─→ AI → MCP: filesystem → 读取 /company/projects/sales/q3_data.csv
  ├─→ AI 分析数据 → 生成报告
  └─→ AI → MCP: filesystem → 写入 /company/reports/q3_analysis.md
```

---

## 九、本地模型 + MCP：企业安全 Agent 工作流

### 9.1 完整工作流架构

```
┌─────────────────────────────────────────────┐
│  用户层（开发者/员工）                        │
│  ├── Cursor / VS Code（编码场景）             │
│  ├── Claude Code（协作场景）                  │
│  └── 自定义 Web UI（业务场景）                │
├─────────────────────────────────────────────┤
│  Agent 层（本地运行）                         │
│  ├── 本地 LLM（Qwen3-Coder 32B）              │
│  ├── 本地 RAG（ChromaDB + bge-large-zh）     │
│  └── MCP Client（OmniRoute / Claude Desktop） │
├─────────────────────────────────────────────┤
│  MCP Server 层（本地/内网）                   │
│  ├── filesystem（项目文件）                    │
│  ├── git（代码仓库）                          │
│  ├── company-kb（企业知识库）                 │
│  ├── postgres（内部数据库，只读）              │
│  └── internal-api（内部系统接口）              │
├─────────────────────────────────────────────┤
│  数据层（本地存储）                           │
│  ├── 代码仓库（Git）                          │
│  ├── 文档库（Markdown/PDF）                   │
│  ├── 向量数据库（ChromaDB）                   │
│  └── 业务数据库（PostgreSQL）                  │
└─────────────────────────────────────────────┘
```

### 9.2 企业级安全编码工作流

```yaml
# 安全编码 Agent 工作流
workflow:
  name: "secure-code-development"

  trigger:
    - user_request: "开发新功能"

  steps:
    # Step 1: 需求理解（本地）
    - name: "understand-requirement"
      model: "local:qwen3-coder-32b"
      mcp_tools:
        - "company-kb:search_knowledge"  # 查询产品需求文档
      output: "requirement_analysis"

    # Step 2: 架构设计（云端 fallback）
    - name: "architecture-design"
      model: "claude:claude-fable-5"      # 复杂任务 fallback 云端
      condition: "complexity == 'high'"
      input: "requirement_analysis"
      output: "architecture_doc"

    # Step 3: 代码实现（本地）
    - name: "code-implementation"
      model: "local:qwen3-coder-32b"
      mcp_tools:
        - "filesystem:read_file"           # 读取现有代码
        - "filesystem:write_file"           # 写入新代码
        - "git:diff"                        # 查看变更
      input: "architecture_doc"
      output: "code_changes"

    # Step 4: 本地测试（本地）
    - name: "local-testing"
      model: "local:qwen3-coder-32b"
      mcp_tools:
        - "command:run_tests"              # 运行测试（受限命令）
      input: "code_changes"
      output: "test_results"

    # Step 5: 安全审查（本地优先，复杂 fallback）
    - name: "security-review"
      model: "local:qwen3-coder-32b"
      fallback: "claude:claude-fable-5"
      mcp_tools:
        - "company-kb:search_knowledge"    # 查询安全规范
      input: "code_changes"
      output: "security_report"

    # Step 6: 提交代码（本地）
    - name: "commit-code"
      model: "local:qwen3-coder-32b"
      mcp_tools:
        - "git:commit"
        - "git:push"
      condition: "test_results == 'passed' && security_report == 'clean'"
```

### 9.3 数据分级处理策略

| 数据级别 | 处理方式 | 模型选择 | MCP 工具 |
|---------|---------|---------|---------|
| **公开数据** | 直接处理 | 本地/云端均可 | 任意 |
| **内部数据** | 本地处理 | 本地模型 | 内网 MCP |
| **敏感数据** | 本地 + 脱敏 | 本地模型 | 受限 MCP |
| **核心数据** | 本地 + 审批 | 本地模型 | 双人复核 |

---

## 十、OmniRoute 配置：本地优先安全路由

### 10.1 企业安全路由策略

```yaml
# omni-route.config.yaml (企业安全版)
version: "3.0"

# ========== 本地模型 Provider（企业核心）==========
providers:
  ollama:
    base_url: "http://localhost:11434/v1"
    api_key: "ollama"
    models:
      - id: "qwen2.5-coder:32b"
        context: 128000
        cost_in: 0
        cost_out: 0
        local: true
        security_level: "core"  # 核心数据可用
      - id: "qwen3:8b"
        context: 131072
        cost_in: 0
        cost_out: 0
        local: true
        security_level: "general"
    region: "local"

  # 本地 vLLM（团队共享）
  vllm-local:
    base_url: "http://localhost:8000/v1"
    api_key: "local"
    models:
      - id: "qwen3-8b-awq"
        context: 32768
        cost_in: 0
        cost_out: 0
        local: true
        security_level: "internal"
    region: "local"

  # --- 国内云端（备案合规）---
  deepseek:
    api_key: "${DEEPSEEK_API_KEY}"
    base_url: "https://api.deepseek.com/v1"
    models:
      - id: "deepseek-v4-pro"
        context: 1000000
        cost_in: 0.43
        cost_out: 0.87
        security_level: "general"  # 一般数据可用
    region: "domestic"

  kimi:
    api_key: "${KIMI_API_KEY}"
    base_url: "https://api.moonshot.cn/v1"
    models:
      - id: "kimi-k3"
        context: 1000000
        cost_in: 3.00
        cost_out: 15.00
        security_level: "general"
    region: "domestic"

  # --- 国外云端（高端复杂任务）---
  claude:
    api_key: "${ANTHROPIC_API_KEY}"
    models:
      - id: "claude-fable-5"
        context: 1000000
        cost_in: 10.00
        cost_out: 50.00
        security_level: "public"  # 仅公开数据
    region: "international"

  openai:
    api_key: "${OPENAI_API_KEY}"
    models:
      - id: "gpt-5.6-sol"
        context: 1100000
        cost_in: 5.00
        cost_out: 30.00
        security_level: "public"
    region: "international"

# ========== 安全路由规则 ==========
routing:
  default_strategy: "security_first"

  rules:
    # 1. 核心数据（最高优先级）→ 强制本地
    - name: "core-data-local-only"
      priority: 100
      condition: |
        data_classification == 'core'
        || contains_pii == true
        || contains_financial_data == true
      action:
        target: "ollama:qwen2.5-coder:32b"
        fallback: "ollama:qwen3:8b"
      reason: "核心数据绝对本地处理，禁止出域"
      block_cloud: true  # 明确禁止云端 fallback

    # 2. 敏感数据 → 本地优先
    - name: "sensitive-data-local"
      priority: 90
      condition: |
        data_classification == 'sensitive'
        || contains_internal_api == true
      action:
        target: "ollama:qwen2.5-coder:32b"
        fallback: "vllm-local:qwen3-8b-awq"
      reason: "敏感数据优先本地，fallback 到内网 vLLM"

    # 3. 内部数据 → 本地或国内云端
    - name: "internal-data-domestic"
      priority: 80
      condition: |
        data_classification == 'internal'
        || source == 'company-kb'
      action:
        target: "ollama:qwen3:8b"
        fallback: "deepseek:deepseek-v4-pro"
      reason: "内部数据可用本地或备案国内模型"

    # 4. 一般数据 → 国内云端默认
    - name: "general-data-domestic"
      priority: 70
      condition: |
        data_classification == 'general'
        || task_type == 'code_completion'
      action:
        target: "deepseek:deepseek-v4-pro"
        fallback: "ollama:qwen3:8b"
      reason: "一般数据优先性价比国内模型"

    # 5. 公开数据 → 可用国外高端
    - name: "public-data-international"
      priority: 60
      condition: |
        data_classification == 'public'
        && network_type == 'international'
      action:
        target: "claude:claude-fable-5"
        fallback: "openai:gpt-5.6-sol"
      reason: "公开数据可用国外高端模型获取最佳质量"

    # 6. 复杂架构设计（公开数据）→ 云端
    - name: "complex-architecture"
      priority: 55
      condition: |
        task_type == 'architecture_design'
        && data_classification == 'public'
      action:
        target: "claude:claude-fable-5"
        fallback: "openai:gpt-5.6-sol"
      reason: "复杂架构设计需要最强模型"

    # 7. 默认 fallback
    - name: "default-local"
      priority: 1
      condition: "true"
      action:
        target: "ollama:qwen3:8b"
      reason: "默认本地模型，安全优先"

# ========== MCP 安全配置 ==========
mcp:
  enabled: true
  auto_load: true

  # 安全审计
  audit:
    enabled: true
    log_path: "/var/log/omniroute/mcp-audit.log"
    retention: "180d"
    log_fields:
      - timestamp
      - user_id
      - mcp_server
      - tool_name
      - arguments_hash
      - result_status
      - data_classification

  # 权限控制
  permissions:
    - role: "developer"
      allowed_servers:
        - "filesystem"
        - "git"
        - "company-kb"
      denied_servers:
        - "command"
        - "postgres"

    - role: "dba"
      allowed_servers:
        - "postgres"
      allowed_operations:
        - "SELECT"
      denied_operations:
        - "DELETE"
        - "DROP"
        - "UPDATE"

    - role: "admin"
      allowed_servers:
        - "*"  # 所有 Server
      command_whitelist:
        - "docker ps"
        - "kubectl get pods"

# ========== 故障转移（安全模式）==========
fallback:
  # 本地模型失败时的处理
  local_failure:
    - error_type: "ollama_not_running"
      action: "alert_admin"
      message: "本地模型服务异常，请检查 Ollama"
    - error_type: "out_of_memory"
      action: "switch_to_smaller_local_model"
      target: "ollama:qwen3:8b"
    - error_type: "local_timeout"
      action: "queue_for_retry"
      max_retry: 3
      # 核心数据禁止 fallback 到云端
      condition: "data_classification != 'core'"
      cloud_fallback: "deepseek:deepseek-v4-pro"

  # 云端模型失败时的处理
  cloud_failure:
    timeout_ms: 10000
    error_types: ["timeout", "rate_limit", "connection_error"]
    retry_count: 2
    fallback_to: "ollama:qwen3:8b"  # 云端失败回退本地

# ========== 成本监控（企业级）==========
monitoring:
  cost_alerts:
    - threshold: 100.0
      unit: "USD/day"
      action: "warn"
      notify: "admin@company.com"
    - threshold: 500.0
      unit: "USD/day"
      action: "switch_to_local_only"
      target: "ollama:qwen3:8b"
      reason: "成本过高，强制本地模式"

  # 本地模型性能监控
  local_metrics:
    track_latency: true
    track_tokens_per_second: true
    track_memory_usage: true
    track_gpu_utilization: true
    alert_on:
      - condition: "latency > 10s"
        action: "scale_up_vllm"
      - condition: "gpu_utilization > 95%"
        action: "alert_admin"
```

---

## 十一、附录：MCP Server 速查表

### 11.1 官方/社区 MCP Server 清单

| 类别 | Server 名称 | 安装命令 | 功能 | 安全级别 |
|------|------------|---------|------|---------|
| **文件系统** | filesystem | `npx -y @modelcontextprotocol/server-filesystem` | 读写本地文件 | 低 |
| **Git** | git | `npx -y @modelcontextprotocol/server-git` | 代码仓库操作 | 中 |
| **GitHub** | github | `npx -y @modelcontextprotocol/server-github` | Issue/PR/代码 | 中 |
| **GitLab** | gitlab | `npx -y @modelcontextprotocol/server-gitlab` | MR/CI 操作 | 中 |
| **数据库** | postgres | `npx -y @modelcontextprotocol/server-postgres` | SQL 查询 | **高** |
| **数据库** | sqlite | `npx -y @modelcontextprotocol/server-sqlite` | SQLite 操作 | **高** |
| **网络** | fetch | `npx -y @modelcontextprotocol/server-fetch` | HTTP 请求 | 中 |
| **浏览器** | puppeteer | `npx -y @modelcontextprotocol/server-puppeteer` | 网页自动化 | 中 |
| **搜索** | brave-search | `npx -y @modelcontextprotocol/server-brave-search` | 搜索 | 低 |
| **Slack** | slack | `npx -y @modelcontextprotocol/server-slack` | 消息发送 | 中 |
| **Notion** | notion | `npx -y @modelcontextprotocol/server-notion` | 文档管理 | 低 |
| **Google Drive** | google-drive | `npx -y @modelcontextprotocol/server-gdrive` | 文件读写 | 中 |
| **Redis** | redis | `npx -y @modelcontextprotocol/server-redis` | 缓存操作 | 中 |
| **命令** | command | 自定义 | Shell 执行 | **极高** |
| **向量检索** | vector-search | 自定义 | 语义检索 | **高** |
| **企业知识库** | company-kb | 自定义 | 内部文档检索 | **高** |

### 11.2 自定义 MCP Server 开发模板

```python
# template_mcp_server.py
from mcp.server import Server
from mcp.types import Tool, TextContent, Resource
from typing import Any
import json

app = Server("your-service-name")

# ===== Tool 定义 =====
@app.tool()
async def your_tool_name(param1: str, param2: int = 10) -> dict:
    """
    Tool description: AI uses this to decide whether to call this tool

    Args:
        param1: Description of parameter 1
        param2: Description of parameter 2 (default 10)

    Returns:
        Structure of return result
    """
    # Implementation logic
    result = await your_business_logic(param1, param2)
    return {
        "status": "success",
        "data": result
    }

# ===== Resource 定义（只读数据）=====
@app.resource("data://your-resource")
async def get_resource() -> str:
    """Provide static data or configuration information"""
    return json.dumps({
        "version": "1.0",
        "last_updated": "2026-07-21"
    })

# ===== Prompt 定义（预设模板）=====
@app.prompt()
async def your_prompt_template() -> str:
    """Preset prompt template"""
    return """
    You are a professional XX engineer. Please follow these requirements:
    1. Follow team coding standards
    2. Add necessary comments
    3. Include error handling logic
    """

if __name__ == "__main__":
    # Support both stdio and HTTP transport
    import asyncio
    asyncio.run(app.run(transport="stdio"))
```

### 11.3 企业级 MCP 开发 checklist

```
[ ] 1. Define clear Tool descriptions (AI decides whether to call based on this)
[ ] 2. Parameter validation (type, range, required fields)
[ ] 3. Permission control (role-based access control)
[ ] 4. Audit logs (record every call)
[ ] 5. Error handling (friendly error messages, no internal details exposed)
[ ] 6. Rate limiting (prevent abuse)
[ ] 7. Data desensitization (sensitive fields not returned to AI)
[ ] 8. Timeout control (prevent long-term blocking)
[ ] 9. Health check (MCP Server status monitoring)
[ ] 10. Documentation update (sync Tool description when changes occur)
```

---

> **核心总结**:  
> **MCP 是 AI 的手脚**，让本地模型能够操作文件、查询数据库、调用 API；  
> **本地 RAG 是 AI 的记忆**，让本地模型能够访问企业私有知识；  
> **两者结合 = 企业级安全 Agent**：数据不出域、操作可审计、权限可控制。  
> 云端模型作为外脑，仅在处理公开数据或复杂架构设计时 fallback 调用。

