---
title: Git 工作流选择指南
domain: IT_Technology
tags: [Git, 工作流, 分支策略, 团队规范]
status: 稳定
created: 2026-06-06
summary: "对比 GitHub Flow / GitLab Flow / Git Flow 三种主流工作流，给出按团队规模的选型建议与企业分支保护规范"
---

# Git 工作流选择指南

> 回答三个核心问题：
> 1. 能不能直接在 master/main 上开发？→ **不能**
> 2. 要不要先建 dev 开发分支？→ **看情况**
> 3. 小团队可以共用一条功能分支吗？→ **可以，但要知道风险**

---

## 一、为什么禁止直接操作 master/main

### 1.1 四个致命问题

| 问题 | 后果 |
|------|------|
| **无可追溯性** | 不知道谁改了哪一行，代码审查形同虚设 |
| **无法回滚** | 一堆提交混在 main 上，出问题只能人肉找哪个 commit 是坏的 |
| **阻塞发布** | 写到一半的代码直接上了 main，别人没法基于干净 base 做其他功能 |
| **没有 CI 闸门** | main 通常是触发 CI/CD 自动部署的分支，半成品代码会导致线上事故 |

### 1.2 企业共识

> **main/master 分支 = 生产环境代码的镜像。它只有两个来源：通过 PR/MR 合并进来的 feature 分支、hotfix 分支。**

阿里云开发者社区 Git 规范（[来源](https://developer.aliyun.com/article/758887)）明确：
- `master` 分支由 `release`、`hotfix` 分支合并，**禁止直接修改**
- `develop` 分支由 `feature` 分支合并，也不允许直接提交
- 所有合并必须通过 Pull Request + Code Review

---

## 二、三种主流工作流对比

### 2.1 速览

```
GitHub Flow (最简)               GitLab Flow (中等)              Git Flow (最复杂)
─────────────────               ─────────────────               ─────────────────
main ──────────────────→        main ───────────────────→      master ──────────────────→
  │                                │                               │
  ├── feature/A                    ├── feature/A                   develop ──────────────→
  ├── feature/B                    ├── feature/B                     │
  └── hotfix/X                     ├── pre-production ←─┐            ├── feature/A
                                   └── production ←─────┘            ├── feature/B
                                                                     ├── release/1.0
                                                                     └── hotfix/X
分支数: 最少                       分支数: 适中                      分支数: 最多
适合: 持续部署                     适合: 有 staging 环境             适合: 版本发布周期
```

### 2.2 详细对比

| 维度           | GitHub Flow         | GitLab Flow                           | Git Flow                             |
| ------------ | ------------------- | ------------------------------------- | ------------------------------------ |
| **永久分支数**    | 1 (main)            | 2~3 (main + pre-prod + prod)          | 2 (master + develop)                 |
| **临时分支类型**   | feature, hotfix     | feature, hotfix                       | feature, release, hotfix             |
| **合并目标**     | 全部 → main           | feature → main/main → pre-prod → prod | feature → develop → release → master |
| **发布方式**     | main 打 tag 即发布      | 逐级合并到 prod                            | release 分支测试后合并到 master              |
| **合并方式**     | Squash / Rebase     | Merge commit                          | Merge commit (--no-ff)               |
| **学习成本**     | ⭐ 最低                | ⭐⭐ 中等                                 | ⭐⭐⭐ 最高                               |
| **流程复杂度**    | ⭐ 最简单               | ⭐⭐ 适中                                 | ⭐⭐⭐ 最复杂                              |
| **CI/CD 耦合** | 强耦合（main = deploy）  | 中耦合（环境分支）                             | 弱耦合（手动发布）                            |
| **代表用户**     | GitHub 自身、SaaS 创业公司 | GitLab 自身、中型企业                        | 微软、IBM、传统软件企业                        |

### 2.3 各工作流的合并链路

**GitHub Flow**（最简单）
```
feature/A ──PR──→ main ──tag──→ 部署
feature/B ──PR──→ main
hotfix/X  ──PR──→ main
```

**GitLab Flow**（有 staging 环境）
```
feature/A ──PR──→ main ──MR──→ pre-production ──MR──→ production
                                    ↑ 部署到测试环境          ↑ 部署到生产环境
```

**Git Flow**（严格版本发布）
```
feature/A ──PR──→ develop ──→ release/1.0 ──→ master (打 tag v1.0)
feature/B ──PR──→ develop ──→              └─→ develop (同步回去)
hotfix/X  ──────────────→ master ──→ develop (同步回去)
```

---

## 三、要不要建 dev 开发分支？

### 3.1 不需要 dev 分支的场景（GitHub Flow）

```
main 就是日常开发的目标分支，不额外建 dev。
```

**条件：**
- 持续部署（每次合并 main 自动部署）
- CI/CD 流水线成熟（自动化测试覆盖高）
- 通过 feature flag 控制新功能曝光
- 团队规模 < 20 人

**优势：** 分支最少，流程最简，合并冲突最少
**劣势：** 要求测试自动化程度高，否则 main 容易被污染

### 3.2 需要 dev 分支的场景（GitLab Flow / Git Flow）

```
main 和生产环境严格对应，日常开发往 dev 或 pre-production 合并。
```

**条件：**
- 有明确的测试环境 / staging 环境
- main 有严格的门禁（必须特定角色才能合并）
- 需要"预发布验证"环节
- 团队 > 10 人或跨团队协作

### 3.3 决策公式

```
你的 CI/CD 能自动部署 main 吗？
├── 能 + 测试覆盖够 → GitHub Flow（不需要 dev）
│   架构: main ← feature/*
│
├── 能，但有 staging 环境 → GitLab Flow（需要 pre-production 环境分支）
│   架构: main ← feature/* → pre-production → production
│
└── 不能 / 有固定发布周期 → Git Flow（需要 dev + release）
    架构: master ← release/* ← develop ← feature/*
```

---

## 四、小团队能不能共用一条功能分支？

### 4.1 可以，但要知道什么场景适用

**常见做法：**

```
main
  └── feature/sprint-24-payment-refactor   ← 两人共用
        ├── Carol 开发支付回调
        └── Dave  开发库存确认
```

**适用条件：**
- 2~3 人紧密协作同一个大功能
- 功能内部有明确分工（不同文件或不同模块）
- 代码每天多次 push/pull，冲突控制在 1 天内

### 4.2 相对于独立分支的优劣

| | 共用一条 feature 分支 | 每人独立 feature 分支 |
|------|------|------|
| **同步成本** | 低（pull 就能拿到对端代码） | 中（需要跨分支 merge） |
| **冲突发现** | 立即发现 | 到合并 PR 时才发现 |
| **代码隔离** | 差（一人的 bug 阻塞全队） | 好（互不干扰） |
| **Review** | 混在一起，难以拆开审 | 每个 PR 独立审查 |
| **适用人数** | 2~3 人 | 任意规模 |

### 4.3 推荐做法：分支链模式

当两人协作时，**不共用同一条分支**，而是用**分支链**（已在 [[Git操作流程]] 中演示）：

```
main
  └── feature/payment-1425-callback-refactor   ← Carol 的分支
        └── feature/inventory-1425-callback-integration  ← Dave 基于 Carol 创建
                                                          ↑ PR base = Carol 的分支
```

**好处：**
- 每人仍有独立分支，可以独立 review
- Dave 不需要等 Carol 全部完成就能开始
- Carol 先合并 Dave 的 PR，再一起提 PR 到 main

### 4.4 什么时候"共用一条分支"没问题

只有一种情况：**结对编程 (Pair Programming)**，两人共用一台机器/一个终端，实际提交者是一个人。

除了这种情况，**始终建议每人一条分支**，哪怕最终合并到同一个上游。

---

## 五、企业 Git 分支保护规范

### 5.1 分支保护规则（GitHub / GitLab 通用）

```
main / master:
  ❌ 禁止直接 push（所有人，包括管理员）
  ✅ 只接受 Pull Request / Merge Request
  ✅ 至少 1 人 Approve 才能合并
  ✅ 必须通过 CI（测试、lint、build）
  ✅ 禁止 force push
  ✅ 合并前必须与 main 同步（no out-of-date branches）

develop (如果有):
  ❌ 禁止直接 push
  ✅ 只接受 feature 分支的 PR/MR
  ✅ 至少 1 人 Approve

release (如果有):
  ❌ 禁止直接 push
  ✅ 只接受 develop 的 PR/MR
  ✅ 仅 Lead/QA 有合并权限
```

### 5.2 中国互联网企业常见做法

根据阿里云、腾讯等公开规范，大中型团队普遍采用：

```
分支模型: Git Flow 简化版
  master       ← 生产环境，打 tag 标记版本
  develop      ← 日常开发集成分支（有些团队会省略，直接 feature → master）
  feature/*    ← 每人每条功能一个分支，命名: feature/<模块>-<需求编号>
  hotfix/*     ← 线上紧急修复
  release/*    ← 预发布（部分团队保留，部分团队省略）

合并要求:
  - 所有合并必须通过 Merge Request
  - 至少 1 位 Senior 工程师 Code Review
  - CI 流水线必须全部通过（单元测试 + 代码扫描 + 构建）
  - Squash merge 为主（保持主分支提交历史干净）
```

---

## 六、你的团队该选哪个？决策树

```
一问团队规模
├── 1~3 人 → GitHub Flow（main + feature/*）
├── 4~10 人 → GitHub Flow 或 GitLab Flow（视 CI 成熟度）
└── 10+ 人 → GitLab Flow 或 Git Flow

二问发布方式
├── 持续部署（随时上线） → GitHub Flow
├── 有 staging 环境     → GitLab Flow
└── 固定发布窗口        → Git Flow

三问是否需要 dev 分支
├── main 自动触发部署   → 不需要 dev（main 就是开发目标）
├── main 有门禁/审批     → 需要 dev 或 pre-production 环境分支
└── 多环境（dev/staging/prod） → GitLab Flow 环境分支
```

### 6.1 推荐：最实用的"轻量规范"

对于 3~10 人团队，推荐 **GitHub Flow + 保护规则**：

```
┌─────────────────────────────────────────────────────┐
│ main (保护分支)                                       │
│  ├── tag: v1.0.0                                    │
│  ├── tag: v1.1.0                                    │
│  └── ...                                            │
│                                                      │
│ 所有开发: feature/<module>-<id>-<desc>               │
│   → PR → Review → Squash merge → main               │
│                                                      │
│ 紧急修复: hotfix/<desc>                              │
│   → PR → 紧急 Review → merge → main                 │
│                                                      │
│ 规则:                                                │
│  1. main 禁止直接 push                               │
│  2. PR 至少 1 人 Approve                            │
│  3. CI 必须通过                                      │
│  4. commit 必须符合 Conventional Commits            │
│  5. 每天至少同步一次 main                            │
│  6. 合并后立即删除 feature 分支                      │
└─────────────────────────────────────────────────────┘
```

---

## 七、你当前笔记的操作流程属于哪种？

你在 [[Git操作流程]] 中描述的 5 人团队一天操作，本质上是 **GitHub Flow**（feature → main），加了一层**分支链协作**模式。这是非常务实的选择——既不需要 Git Flow 那么多分支，又有清晰的合并路径。

如果未来团队增长到 **10 人以上** 或引入**多环境部署**（dev → staging → prod），再考虑升级到 GitLab Flow 或 Git Flow。

---

## 相关笔记

- [[Git操作流程]] — 最佳实践总纲：具体命令与日常操作
- [[03-Knowledge(知识层)/10-IT技术-IT_Technology/00-通用技术工具/Git版本控制/GIT]] — Git 完整课程笔记（安装、基础命令）
- [[03-Knowledge(知识层)/10-IT技术-IT_Technology/00-通用技术工具/Git版本控制/gitlab实践问题]] — GitLab 平台实践
- [[03-Knowledge(知识层)/10-IT技术-IT_Technology/00-通用技术工具/Git版本控制/GitHub与GitLab]] — 两大平台对比
