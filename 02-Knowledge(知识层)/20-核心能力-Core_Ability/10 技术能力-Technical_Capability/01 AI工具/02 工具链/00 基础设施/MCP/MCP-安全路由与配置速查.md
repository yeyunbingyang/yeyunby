---
title: MCP 安全路由与配置速查
domain: Core_Ability
tags: [MCP, OmniRoute, 安全, 配置, 速查]
status: 稳定
created: 2026-07-22
updated: 2026-07-22
summary: "MCP企业安全Agent工作流与OmniRoute配置，附全部MCP Server速查表"
source: 拆分自MCP深度解析与本地模型企业级应用指南.md
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
