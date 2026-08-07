---
title: 我的 Skills 蒸馏
domain: Core_Ability
tags: [AI, Agent, Skills, 个人总结, 最佳实践]
status: 稳定
created: 2026-07-23
updated: 2026-08-02
related:
  - "03-通用skills最佳实践"
  - "01-快速入门"
  - "我的Skills清单"
summary: "个人 Skills 使用经验的持续记录。定期回顾高频使用的 skill、合并重复、优化触发精度。"
source: "内部实践整理；外部依据见正文链接"
verified: 2026-07-25
review_after: 2026-11-02
---

# 我的 Skills 蒸馏

> 根据 [[03-通用skills最佳实践#9.4 定期蒸馏|通用最佳实践中的蒸馏方法论]]，每 2-4 周回顾一次个人 Skills 使用情况。

---

## 当前已固化的技能方向

### 1. 资料归类整理

- **触发场景**：知识库/目录文件整理，需要批量移动、重命名、补全 frontmatter
- **常用组合**：obsidian-vault（搜索）→ obsidian-markdown（格式检查）→ write（补全 summary）
- **心得**：几乎每周都有，建议定期做知识库健康体检

### 2. GitHub 热门项目总结

- **触发场景**：从 GitHub 发现优秀的开源项目，总结收录到 03-Resources
- **已固化技能**：[[github-trending]]（日/周/月榜 + 上周 Wayback Machine 补抓）
- **常用工具**：github-trending + write + agent-reach（社区评价补充）
- **心得**：配合 agent-reach 做社区评价补充效果更好

### 3. 知识库：Obsidian + AI 技能

- **触发场景**：写笔记时涉及 Obsidian 格式（callout、wikilink、frontmatter）
- **常用技能**：[[Obsidian-Markdown语法参考]]、[[Obsidian-Agent操作指南]]

---

## 我的技能清单

当前共 **15 个知识库技能**（存放于 `X:\KMS\yeyunby\.agents\skills`）+ **20 个全局技能**（存放于 `C:\Users\h2967\.codex\skills`），按用途分类的完整登记见 [[我的Skills清单]]。

---

## Skills 管理记录

### 2026-07-23：重构后整理
- Obsidian 技能从 6+1 个文件合并为 2 篇指南
- 07-Skills调用机制 已合并到 03-通用skills最佳实践
- 3 篇 Python 数据抓取笔记移入 10-IT技术

### 2026-08-02：技能盘点
- 新增 [[github-trending]] 技能：抓取 GitHub 日/周/月热门榜单（含上周快照），脚本位于 `.agents/skills/github-trending/scripts/fetch-trending.ps1`
- 建立 [[我的Skills清单]] 总清单：15 个知识库技能 + 20 个全局技能，含用途与维护说明

### 待跟踪
- [ ] 是否有工作流重复 3 次以上 → 创建自定义 Skill？
- [ ] 哪些 Skill 的 description 不精准？
- [ ] 定期清理过时 Skill
