# GitHub 今日热门项目 — hyperframes 视频

> 调研数据来自 GitHub API 实时抓取（2026-07-17）。视频用 hyperframes 渲染。

## 文件说明

| 文件 | 说明 |
|------|------|
| `GitHubDaily.html` | hyperframes 主合成文件（GSAP 动画 + 字幕） |

## 渲染步骤

```bash
# 1. 进入目录
cd "X:\KMS\yeyunby\02-Knowledge(知识层)\20-核心能力-Core_Ability\10 技术能力-Technical_Capability\01 AI工具\03 vibe coding\github-daily-video"

# 2. 初始化 hyperframes 项目
hyperframes init

# 3. 预览
hyperframes preview GitHubDaily.html

# 4. 渲染视频
hyperframes render GitHubDaily.html out/video.mp4

# 5. 添加 TTS 配音
hyperframes tts GitHubDaily.html --voice=zh-CN-XiaoxiaoNeural

# 6. 生成字幕
hyperframes transcribe out/video.mp4 --lang=zh
```

### 如果 hyperframes CLI 不可用

直接用浏览器打开 `GitHubDaily.html` 即可预览动画效果（GSAP 会自动播放）。

## 视频结构（60 秒）

| 时间 | 场景 | 内容 |
|------|------|------|
| 0-10s | 开场 | GitHub 今日热门项目 · 精选 Top 5 |
| 10-20s | 项目 1 | guanlan — RSS 阅读器 (TypeScript/25⭐) |
| 20-30s | 项目 2 | Pinscope — 电路审查工具 (Python/23⭐) |
| 30-40s | 项目 3 | Glob3R — 3D 重建 (Python/13⭐) |
| 40-50s | 项目 4 | AgentCore AGUI — Agent 框架 (TypeScript/10⭐) |
| 50-60s | 项目 5 | gba-hashcat — GBA 密码破解 (C++/9⭐) |

## 数据来源

GitHub Search API: `q=created:>2026-07-16&sort=stars&order=desc&per_page=10`
