---
name: github-trending
description: 抓取并汇总 GitHub 热门项目（日榜/周榜/月榜，含上周历史周榜）。当用户提到 GitHub 热门、trending、日榜、周榜、月榜、上周热门项目、本周热门仓库、star 增长最快的项目时使用。输出为 Markdown 榜单，可归档到知识库资源层。
---

# GitHub 热门项目榜单

抓取 GitHub Trending 官方页面，输出日榜、周榜、月榜；由于官方 Trending 无历史，上周周榜通过 Wayback Machine 快照还原，另用 GitHub Search API 补充"上周新发布热门仓库"。

## 触发场景

- 用户问"GitHub 最近有什么热门项目 / 本周 / 上周 / 本月热门"
- 用户想了解 star 增长最快的仓库、AI/开发工具新动态
- 用户分享 trending 链接（如 `https://github.com/trending?since=weekly`）并要求汇总

## 工作流程

1. 声明使用 `github-trending` 技能（中文输出）。
2. 运行 `scripts/fetch-trending.ps1` 抓取数据（需联网；Windows 下优先 `curl.exe`，失败时尝试 `Invoke-WebRequest`）。
3. 解析 HTML/JSON，提取每榜前 N 条：仓库名、描述、语言、star 总数、增长数。
4. 上周数据：查询 Wayback Machine `wayback/available` 接口找上周快照，若存在则抓取 `id_` 原始页并解析；若不存在，改用 GitHub Search API 按 `created` 时间范围近似。
5. 输出 Markdown 榜单（含数据来源与抓取日期），如需落盘则写入知识库 `03-Resources(资源层)/` 对应目录。

## 输出格式

```
### 今日榜 Top N（since=daily）
1. [owner/repo](url) — 描述｜语言｜★总数（+今日增长）

### 本周榜 Top N（since=weekly）
...

### 本月榜 Top N（since=monthly）
...

### 上周榜 Top N（Wayback 快照日期）
...

### 上周新发布热门（created 范围，Search API）
...
```

末尾附 2-4 条观察结论（本周热点主题、新面孔、趋势）。

## 注意事项

- GitHub Trending 页面结构为 `<article class="Box-row">`，解析时按此切分；如结构变化，改用搜索 API 兜底。
- 上周快照的 star 数为快照时刻数据，与当前值有差异，需在输出中标注快照日期。
- 第三方 Trending API（gitterapp、github-trending-api.com）经常失效或反爬，不要作为主数据源。
- 抓取遵守 GitHub/archive.org 使用限制，单次抓取 5-6 个请求即可，不做高频轮询。
