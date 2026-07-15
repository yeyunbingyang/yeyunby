---
title: "宝玉 Skills 内容创作技能集"
tags: [GitHub, 开源, AI, Skills, 内容创作, 小红书, 微信公众号, 翻译, 中文]
type: 工具
status: 待评估
created: 2026-07-06
updated: 2026-07-16
source: https://github.com/JimLiu/baoyu-skills
related: [anthropics-skills-官方Skills仓库]
summary: "宝玉（JimLiu）出品的 20+ 中文内容创作 Agent Skills——小红书图片卡片/信息图/幻灯片/漫画/封面图/公众号发布/翻译/YouTube 转录等，适合中文创作者"
---

# 宝玉 Skills 内容创作技能集

https://github.com/JimLiu/baoyu-skills

## 基本信息

**类型：** 工具（Skill 集合）
**链接：** https://github.com/JimLiu/baoyu-skills
**安装：** `npx skills add jimliu/baoyu-skills`
**适用领域：** 中文内容创作、社交媒体发布、翻译、图像生成
**推荐程度：** ★★★★★
**Stars：** 未统计
**语言：** Markdown + Shell
**许可证：** MIT

## 是什么

**宝玉（JimLiu）** 出品的 20+ Agent Skills，专注中文内容创作与发布。配套图书《图解 Skill —— AI 提效实战指南》系统讲解 Skill 设计方法。覆盖小红书/微信公众号/微博/推特等多平台内容生成与发布。

## 技能分类

### 内容技能（Content Skills）

| 技能 | 功能 |
|------|------|
| **baoyu-xhs-images** | 小红书图片卡片生成器——12 种风格 × 6 种布局 × 3 种配色 |
| **baoyu-infographic** | 专业信息图生成器——21 种布局 × 21 种视觉风格 |
| **baoyu-diagram** | SVG 图表生成（流程图/时序图/架构图/示意图/类图） |
| **baoyu-cover-image** | 文章封面图生成——5 维定制系统 |
| **baoyu-slide-deck** | 幻灯片生成——16 种风格预设，输出 PPTX+PDF |
| **baoyu-comic** | 知识漫画创作——5 种画风 × 7 种基调 |
| **baoyu-article-illustrator** | 文章插图生成——类型 × 风格 × 色板三维系统 |

### 发布技能

| 技能 | 功能 |
|------|------|
| **baoyu-post-to-x** | 发布到 X/Twitter（普通帖子 + X 文章） |
| **baoyu-post-to-wechat** | 发布到微信公众号（API/浏览器/远程 API 三种方式） |
| **baoyu-post-to-weibo** | 发布到微博（文字/图片/视频/头条文章） |

### AI 生成技能

| 技能 | 功能 |
|------|------|
| **baoyu-image-gen** | 多后端图像生成（OpenAI/Azure/Google/OpenRouter/DashScope/MiniMax/即梦/豆包/Replicate） |
| **baoyu-danger-gemini-web** | Gemini Web 交互（文本 + 图片生成） |

### 工具技能

| 技能 | 功能 |
|------|------|
| **baoyu-youtube-transcript** | YouTube 字幕下载（多语言/翻译/章节/说话人识别） |
| **baoyu-url-to-markdown** | URL → Markdown 抓取 |
| **baoyu-danger-x-to-markdown** | X/Twitter 内容 → Markdown |
| **baoyu-compress-image** | 图片压缩 |
| **baoyu-format-markdown** | Markdown 格式化（frontmatter/标题/摘要） |
| **baoyu-markdown-to-html** | Markdown → HTML（公众号兼容主题） |
| **baoyu-translate** | 三模式翻译（快速/标准/精翻） |
| **baoyu-wechat-summary** | 微信群聊精华提取 |
| **baoyu-electron-extract** | Electron 应用源码提取 |

## 安装

```bash
# 按需安装（不要全装——每个 skill 占用上下文）
npx skills add jimliu/baoyu-skills

# 或安装单个 skill
npx skills add jimliu/baoyu-skills --skill baoyu-cover-image
```

## 环境配置

API 密钥放在 `~/.baoyu-skills/.env`（用户级）或 `.baoyu-skills/.env`（项目级）：

```bash
OPENAI_API_KEY=sk-xxx
GOOGLE_API_KEY=xxx
DASHSCOPE_API_KEY=sk-xxx
```

## 评价

- **优点**：中文内容创作生态最完善的 Skill 集、小红书/公众号/微博全覆盖、多后端图像生成灵活、有配套图书系统讲解、MIT 开源
- **局限**：部分技能依赖第三方 API（需配置密钥）、baoyu-danger-* 使用逆向工程 API 有风险
- **是否值得长期保留**：✅ 重点关注——中文内容创作者的最佳 Skill 集合
