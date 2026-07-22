---
title: OmniRoute 使用指南
domain: Core_Ability
tags: [OmniRoute, 模型路由, 网关, 安全]
status: 稳定
created: 2026-07-22
updated: 2026-07-22
summary: "OmniRoute 企业级AI网关配置指南——本地优先安全路由、236供应商支持、零信任架构"
source: 拆分自MCP-安全路由与配置速查.md
---

# OmniRoute 使用指南

> OmniRoute 是 236 供应商 AI 网关，支持本地优先安全路由、零信任架构和企业级合规审计。

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

