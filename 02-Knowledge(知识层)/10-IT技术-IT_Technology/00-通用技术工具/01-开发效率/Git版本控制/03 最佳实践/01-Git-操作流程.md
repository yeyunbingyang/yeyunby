---
title: Git 操作最佳实践
domain: IT_Technology
tags: [Git, 最佳实践, 版本控制, 团队协作]
status: 稳定
created: 2026-06-06
summary: "Git日常操作的最佳实践速查手册，涵盖分支策略、提交规范、PR流程、协作模式与紧急处置，适合所有开发人员"
---

# Git 操作最佳实践

> 本文提炼自团队实践 + Conventional Commits + GitHub Flow，是面向所有开发人员的 Git 操作「宪章」。
> 后半篇保留了完整的一日操作演示，作为参考案例。

---

## 一、分支策略

### 1.1 核心原则

```
main ────────────────────────────────────────────→ 永远可发布
  │
  ├── feature/xxx     → 新功能分支（从 main 拉出，合并回 main）
  ├── fix/xxx         → 修复分支
  ├── hotfix/xxx      → 线上紧急修复（从 main 拉，合回 main + 同步到 develop 如需要）
  └── release/x.x.x   → 发布分支（如有发布周期）
```

### 1.2 命名规范

```
feature/<模块>-<任务编号>-<简短描述>
fix/<模块>-<任务编号>-<简短描述>
```

**示例：**
- `feature/order-1423-cursor-pagination` ✅
- `feature/BOB-TEST123` ❌ （无意义）
- `my-branch` ❌ （不知道做什么）

### 1.3 分支生命周期

```bash
# 创建
git checkout -b feature/order-1423-pagination

# 尽早推送（让团队知道你在这个事情上）
git push -u origin feature/order-1423-pagination

# 合并后立即删除
git branch -d feature/order-1423-pagination
git push origin --delete feature/order-1423-pagination
```

> 💡 **为什么尽早推送空分支？** 避免两个人同时做同一件事。

---

## 二、提交规范（Conventional Commits）

### 2.1 格式

```
<type>(<scope>): <subject>

<body>

Refs: #<ticket>
```

### 2.2 type 速查

| Type       | 用途        | 示例                                       |
| ---------- | --------- | ---------------------------------------- |
| `feat`     | 新功能       | `feat(order): add cursor pagination`     |
| `fix`      | 修 bug     | `fix(payment): null check for callback`  |
| `test`     | 测试        | `test(order): add pagination unit tests` |
| `docs`     | 文档        | `docs(api): update swagger for v2`       |
| `refactor` | 重构（不改变行为） | `refactor(user): extract token util`     |
| `perf`     | 性能优化      | `perf(order): add composite index`       |
| `chore`    | 杂务（构建/依赖） | `chore(deps): bump spring to 3.2`        |
| `ci`       | CI/CD     | `ci: add sonarqube scan step`            |

### 2.3 好的 vs 坏的 commit message

```bash
# ✅ 好
git commit -m "feat(order): implement cursor-based pagination

- Add CursorPagination utility class
- Modify OrderRepository to use composite index
- Benchmark: 45ms avg (was 1200ms)

Refs: #1423"

# ❌ 坏
git commit -m "fix"
git commit -m "update code"
git commit -m "asdf"
git commit -m "."
```

### 2.4 提交粒度

| 场景 | 做法 |
|------|------|
| 完成一个独立功能点 | 提交 |
| 修改了多个不相关文件 | 拆成多个提交（`git add -p`） |
| 写到一半去吃饭 | `git stash`，不要提交半成品 |
| 临时文件/本地配置 | **不要提交**，加入 `.gitignore` |

---

## 三、日常操作流程

### 3.1 早上上班（5 分钟仪式）

```bash
# 1. 检查当前状态
git status

# 2. 切到 main 拉最新
git checkout main
git pull origin main

# 3. 同步远程分支信息
git fetch origin --prune

# 4. 清理已合并的本地分支
git branch --merged main | grep -v "main" | xargs -r git branch -d
```

### 3.2 开发中（每完成一个功能点）

```bash
# 提交前自我审查
git diff                 # 看改了什么
git diff --cached        # 看暂存了什么（提交前最后确认）

# 选择性添加（避免一锅端）
git add src/main/java/com/shop/order/OrderQueryService.java
git add src/main/java/com/shop/order/CursorPagination.java

# 提交
git commit -m "feat(order): ..."

# 推送
git push origin feature/order-1423-pagination
```

### 3.3 同步 main（至少每天一次）

```bash
# 拉取 main 最新
git fetch origin

# 合并到当前分支
git merge origin/main --no-edit

# 如果有冲突：解决 → git add . → git commit
```

> ⚠️ **不要等 PR 才发现冲突**，每天同步一次 main，冲突成本最低。

### 3.4 午饭/下班前保存进度

```bash
# 未完成的工作 → stash，不要提交半成品
git stash push -m "WIP: OrderList page, filter panel pending"

# 切回 main（好习惯）
git checkout main

# 回来后
git checkout feature/xxx
git stash pop
```

---

## 四、PR 创建与代码审查

### 4.1 创建 PR 前自检清单

- [ ] 分支已同步 main（`git merge origin/main`）
- [ ] 本地编译通过
- [ ] 单元测试通过
- [ ] commit message 符合规范
- [ ] 不包含临时文件、注释掉的代码、`console.log`
- [ ] 没有将敏感信息（密码、密钥）提交

### 4.2 PR 描述模板

```markdown
## 变更内容
- 实现游标分页替代 offset/limit
- 添加复合索引

## 性能影响
| 指标 | 优化前 | 优化后 |
|------|--------|--------|
| 平均响应 | 1200ms | 45ms |

## 测试覆盖
- [x] 单元测试：12 个
- [x] 集成测试：已添加

## 兼容性
- API v2 新端点，不影响 v1

Refs: #1423
```

### 4.3 收到 Review 意见后

```bash
# 在同一个 feature 分支上修改，不要开新分支
git checkout feature/order-1423-pagination
# 修改代码...
git add .
git commit -m "fix(order): add exception handling for invalid cursor

Address review: https://github.com/xxx/pull/1456#discussion_r123

Refs: #1423"
git push origin feature/order-1423-pagination
# PR 会自动更新
```

---

## 五、协作模式

### 5.1 分支链协作（上游 → 下游）

当 Carol 的代码是 Dave 开发的前提时：

```
main ← Carol:feature/payment-callback-refactor
         ↑
       Dave:feature/inventory-callback-integration
```

```bash
# Dave 基于 Carol 的分支创建
git checkout -b feature/inventory-callback-integration \
  origin/feature/payment-callback-refactor

# Dave 提 PR 时，base 指向 Carol 的分支（不是 main）
# Carol 先合并 Dave 的 PR，再一起提 PR 到 main
```

### 5.2 不要做的事

| ❌ 不要 | ✅ 应该 |
|--------|--------|
| 直接在 `main` 上开发 | 永远从 feature 分支开发 |
| `git push --force` 到共享分支 | 仅在自己的 feature 分支上 force push |
| 提交一个 50 文件 3000 行的 PR | 拆成多个小 PR |
| commit 里混入格式化改动 | 格式化改动单独一个 commit |
| 不提 PR 直接推到 main | 永远通过 PR + Review 合并 |
| 本地分支堆积一个月 | 合并后删分支，保持清爽 |

---

## 六、常见问题处置

### 6.1 提交了不该提交的文件

```bash
# 方案 A：修改最后一次提交（还没 push）
git rm --cached secret.config
git commit --amend --no-edit
git push origin feature/xxx   # 如果已 push，需要 force

# 方案 B：已经 push 了
# 立即 revoke 密钥/密码，然后：
git rm --cached secret.config
git commit -m "chore: remove accidentally committed config"
git push origin feature/xxx
# 历史中仍然存在，需要使用 git filter-branch 或 BFG 清理
```

### 6.2 commit message 写错了

```bash
# 还没 push
git commit --amend -m "feat(order): correct message"

# 已经 push（仅限自己的 feature 分支）
git commit --amend -m "feat(order): correct message"
git push --force-with-lease origin feature/xxx
```

### 6.3 合并冲突

```bash
git merge origin/main
# CONFLICT in xxx.java

# 打开 IDE 解决冲突标记
# <<<<<<< HEAD
# =======
# >>>>>>> origin/main

# 解决后：
git add .
git commit -m "merge: resolve conflicts with main"
```

### 6.4 误删分支 / 代码丢失

```bash
# 查看最近操作记录
git reflog

# 恢复到误删前的 commit
git checkout -b recovered-branch <commit-hash>
```

### 6.5 线上紧急回滚

```bash
# 方案 A：revert（安全，保留历史）
git revert <bad-commit-hash>
git push origin main

# 方案 B：直接回退（危险！仅紧急情况下团队协调后用）
git reset --hard <good-commit-hash>
git push --force origin main
```

---

## 七、操作决策树

```
开始工作
├── 有未提交的修改？
│   ├── 已开发完成 → git add + commit + push
│   └── 开发一半   → git stash push
├── main 有更新？
│   └── git fetch origin && git merge origin/main
├── 功能开发中 →
│   ├── 完成一个独立点 → commit
│   ├── 需要团队看到  → push
│   └── 写到一半      → 继续写
└── 功能完成 →
    ├── 同步 main → 解决冲突
    ├── 运行测试  → 全部通过
    ├── 创建 PR   → 写清楚描述
    └── 等待 Review → Review → 修改 → 合并
```

---

## 八、速查命令卡片

```bash
# 日常
git status                    # 看状态
git log --oneline -10         # 看最近提交
git diff                      # 看未暂存的改动
git diff --cached             # 看暂存的改动

# 分支
git checkout -b <name>        # 新建并切换
git branch -d <name>          # 删除本地分支
git push origin --delete <name>  # 删除远程分支
git branch --merged main | grep -v main | xargs git branch -d  # 清理

# 暂存
git stash push -m "WIP: xxx"  # 暂存
git stash pop                 # 恢复最近暂存
git stash list                # 查看暂存列表

# 回溯
git checkout -- <file>        # 放弃单个文件修改
git reset HEAD <file>         # 取消暂存
git reset --soft HEAD~1       # 撤销 commit，保留改动
git revert <hash>             # 安全撤销（生成新 commit）

# 历史
git reflog                    # 操作历史（救命用）
git log --author="你的名字"    # 看自己的提交
git blame <file>              # 看每行谁改的

# 同步
git fetch origin --prune      # 拉取远程信息 + 清理已删除的分支
git merge origin/main         # 合并 main
git pull --rebase origin main # rebase 方式同步（保持线性历史）
```

---

## 参考案例：一日工作流演示

以下为原始详细演示，展示了 Tech Lead + 4 名开发人员一天的实际 Git 操作：

---

## 团队背景

| 角色 | 成员 | 负责模块 | 工作习惯 |
|------|------|----------|----------|
| Tech Lead | Alex | 代码审查、架构决策、发布管理 | 上午审查 PR，下午处理技术债务 |
| 后端 Dev 1 | Bob | 订单服务 (Java/Spring Boot) | 习惯早上写代码，下午联调 |
| 后端 Dev 2 | Carol | 支付服务 (Java/Spring Boot) | 上午需求分析，下午深度开发 |
| 后端 Dev 3 | Dave | 库存服务 (Java/Spring Boot) | 上午写单测，下午集成开发 |
| 前端 Dev | Eve | 管理后台 (React/TypeScript) | 上午对接口，下午写 UI |

---

### 09:00 - 上班开始：每日 Git 初始化仪式

**Alex (Tech Lead)**

```bash
cd ~/projects/shop-backend
git fetch origin --quiet
git checkout main && git pull origin main
# 清理已合并分支
git branch --merged main | grep -v "^* main$" | xargs -r git branch -d
# 查看昨日合并
git log --oneline --since="yesterday" main
```

**Bob (后端)** — 初始化工作分支，同步 main

```bash
git checkout main && git pull origin main
git fetch origin --prune
git checkout feature/order-query-optimization
git merge origin/main --no-edit
```

**Carol (后端)** — 创建今天的新分支

```bash
git checkout main && git pull origin main
git checkout -b feature/payment-1425-callback-refactor
git push -u origin feature/payment-1425-callback-refactor
```

**Dave (后端)** — 先写测试再写实现 (TDD)

```bash
git checkout -b feature/inventory-1426-reservation-logic
touch src/test/.../InventoryReservationServiceTest.java
git add . && git commit -m "test(inventory): add failing tests for reservation logic

- Test happy path
- Test failure path
- Test edge case: concurrent reservation

Refs: #1426"
git push origin feature/inventory-1426-reservation-logic
```

**Eve (前端)** — 发现 Bob 的分支，基于它做前端开发

```bash
git fetch origin
git checkout -b feature/admin-1423-order-cursor-pagination
git commit -m "feat(admin): add mock data for cursor-based order list

- Mock cursor pagination response format
- Prepare for backend integration

Refs: #1424"
git push -u origin feature/admin-1423-order-cursor-pagination
```

---

### 10:30 - 上午开发中段：提交与同步

**Bob** — 完成核心逻辑，第一次提交

```bash
git status
git add src/.../OrderQueryService.java src/.../OrderRepository.java src/.../CursorPagination.java
git diff --cached  # 提交前最后确认
git commit -m "feat(order): implement cursor-based pagination

- Add CursorPagination utility class with base64 encoding
- Modify OrderRepository to use composite index
- Benchmark: 45ms avg (was 1200ms)

Refs: #1423"
git push origin feature/order-1423-query-optimization
```

**Carol** — 接口定义完成，通知 Dave 协作

```bash
git add src/.../PaymentCallbackEvent.java src/.../PaymentCallbackHandler.java
git commit -m "feat(payment): define callback event and handler interface

- PaymentCallbackEvent: orderId, paymentId, status, reservationId
- PaymentCallbackHandler interface for inventory integration
- Add PaymentStatus enum

Refs: #1425"
git push origin feature/payment-1425-callback-refactor
# → Slack: "Dave, 接口定义已推送，可以基于此开发库存确认"
```

**Dave** — 基于 Carol 的分支协作开发

```bash
git fetch origin
git checkout -b feature/inventory-1425-callback-integration origin/feature/payment-1425-callback-refactor
# 开发库存确认逻辑...
git add . && git commit -m "feat(inventory): implement inventory confirmation

- Consume PaymentCallbackEvent
- Confirm reservation on payment success
- Rollback on payment failure
- Idempotency check via paymentId

Co-authored-by: Carol <carol@shop.com>
Refs: #1425"
git push -u origin feature/inventory-1425-callback-integration
# → PR base 指向 Carol 的分支（不是 main）
```

---

### 12:00 - 午饭前：保存工作进度

**Eve** — UI 写到一半，用 stash 保存

```bash
git stash push -m "WIP: OrderList page with cursor pagination, filter panel pending"
git checkout main  # 好习惯：离开时切回 main
# 饭后回来：
git checkout feature/admin-1423-order-cursor-pagination
git stash pop
```

**Bob** — 完成测试，提交准备 PR

```bash
./mvnw test  # 确认全部通过
git add src/test/.../OrderQueryServiceTest.java src/test/.../CursorPaginationTest.java
git commit -m "test(order): add comprehensive tests for cursor pagination

Tests run: 12, Failures: 0

Refs: #1423"
git push origin feature/order-1423-query-optimization
```

---

### 14:00 - 下午：PR 创建与审查

**Bob** — 创建 PR

```bash
git fetch origin && git merge origin/main --no-edit
git push origin feature/order-1423-query-optimization
# → GitHub 创建 PR，填写：
# Title: feat(order): optimize order query with cursor pagination
# Body: 变更内容、性能数据、测试覆盖、兼容性说明
# Reviewer: Alex
```

**Alex** — Code Review

```bash
git fetch origin pull/1456/head:pr-1456
git checkout pr-1456
git diff main...HEAD
./mvnw test  # 本地跑测试验证
# → GitHub 添加 review comment: "建议添加非法 cursor 异常处理"
```

**Bob** — 修改代码回应 Review

```bash
git checkout feature/order-1423-query-optimization
# 修改代码...
git add . && git commit -m "fix(order): add exception handling for invalid cursor

Address review: https://github.com/shop/pull/1456#discussion_r123

Refs: #1423"
git push origin feature/order-1423-query-optimization
# PR 自动更新
```

---

### 16:00 - 协作链合并

**Carol** — 审查并合并 Dave 的 PR

```bash
git fetch origin
git log --oneline feature/payment-1425-callback-refactor..origin/feature/inventory-1425-callback-integration
# → GitHub Approve + Merge Dave 的 PR 到 Carol 的分支
git checkout feature/payment-1425-callback-refactor
git pull origin feature/payment-1425-callback-refactor
# 现在 Carol 的分支包含两人工作，准备最终提 PR 到 main
```

---

### 17:00 - 傍晚：最终合并与清理

**Alex** — Squash merge Bob 的 PR

```bash
git checkout main && git pull origin main
git log --oneline -5  # 确认
git branch -d pr-1456
```

**Bob** — 合并后清理

```bash
git checkout main && git pull origin main
git branch -d feature/order-1423-query-optimization
git push origin --delete feature/order-1423-query-optimization
```

**Eve** — 对接已合并的后端接口

```bash
git checkout main && git pull origin main
git checkout feature/admin-1423-order-cursor-pagination
git merge origin/main --no-edit
# 替换 mock → 真实 API 调用
git add . && git commit -m "feat(admin): integrate real cursor-based order API

- Replace mock data with /api/v2/orders endpoint
- Handle cursor pagination in UI

Refs: #1424"
git push origin feature/admin-1423-order-cursor-pagination
```

---

### 18:00 - 下班前：每日收尾

**Alex** — 总结 + 打 tag

```bash
git log --oneline --since="today" main  # 今日合并
git tag -a sprint-24-day3 -m "Sprint 24 Day 3: order optimization merged"
git push origin sprint-24-day3
```

---

### 全天时间线汇总

| 时间 | Alex | Bob | Carol | Dave | Eve |
|------|------|-----|-------|------|-----|
| 09:00 | 检查所有仓库 | 初始化工作分支 | 创建新分支 | 创建分支+写测试 | 创建分支+mock开发 |
| 10:30 | 审查 PR | 核心逻辑提交 | 接口定义提交 | 协作开发 | UI开发 |
| 12:00 | 继续审查 | 测试提交 | 继续开发 | 继续开发 | stash保存进度 |
| 14:00 | 审查Bob PR | 创建PR | 继续开发 | 提交协作PR | 继续开发 |
| 15:00 | 提出review | 修改代码 | 审查Dave PR | 等待审查 | 继续开发 |
| 16:00 | 继续审查 | 等待合并 | 合并Dave PR | 等待合并 | 提交对接代码 |
| 17:00 | 合并Bob PR | 清理分支 | 继续完善 | - | 创建PR |
| 18:00 | 打tag总结 | 下班 | 下班 | 下班 | 下班 |
