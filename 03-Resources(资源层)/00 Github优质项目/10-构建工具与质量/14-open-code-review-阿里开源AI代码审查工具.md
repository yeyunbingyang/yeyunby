---
title: "OpenCodeReview 阿里开源 AI 代码审查工具"
tags: [GitHub, 开源, AI, 代码审查, 代码质量, 安全]
type: 工具
status: 待评估
created: 2026-07-28
updated: 2026-07-28
verified: 2026-07-28
review_after: 2026-08-28
source: https://github.com/alibaba/open-code-review
related: [Github优质项目-MOC]
summary: "14.6k⭐ · 今日新增980⭐——OpenCodeReview 将确定性规则流水线与LLM Agent结合，输出行级审查意见并内置空指针、并发、XSS和SQL注入规则"
---

# OpenCodeReview 阿里开源 AI 代码审查工具

## 项目定位

OpenCodeReview 是源自阿里巴巴内部实践的 AI 代码审查 CLI，通过传统规则与 LLM Agent 混合架构发现缺陷并生成精确到行的审查意见。

## 核心特点

- 内置 NPE、线程安全、XSS、SQL 注入等规则。
- 支持 OpenAI 与 Anthropic 兼容模型端点。
- 可作为 CLI、GitHub Action、插件或 Agent Skill 接入研发流程。
- 确定性检查负责稳定规则，LLM 处理需要上下文判断的问题。

## 注意事项

- AI 审查不能替代测试、静态分析、人工评审和安全审计。
- 将私有代码发送给外部模型前，必须核对数据保留和合规策略。
- 上线前应以真实仓库评估误报率、漏报率和 Token 成本。

**许可证：** Apache-2.0  
**推荐程度：** ★★★★☆  

## 相关导航

- [[Github优质项目-MOC]]
