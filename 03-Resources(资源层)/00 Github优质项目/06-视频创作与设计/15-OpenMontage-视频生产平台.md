---
title: "OpenMontage AI 视频生产平台"
tags: [GitHub, 开源, AI视频, Agent, Pipeline, Skills, 视频生成]
type: 工具
status: 稳定
created: 2026-07-17
updated: 2026-08-15
verified: 2026-08-15
review_after: 2026-09-15
source: https://github.com/calesthio/OpenMontage
related: [Github优质项目-MOC, claude-video-分析, remotion-skills-视频编程技能, AI工具链与Agent实践-MOC]
summary: "OpenMontage 把视频制作交给编程 Agent 编排：通过 pipeline_defs/skills/tools 三层架构，用自然语言驱动研究→提案→脚本→场景规划→素材→剪辑→Remotion/HyperFrames/FFmpeg 合成，并提供零 API 路径供入门"
---

# OpenMontage AI 视频生产平台

## 一句话说明

OpenMontage 不是传统 GUI 视频软件，而是把视频制作交给编程 Agent（Claude Code / Cursor / Codex / Copilot / Windsurf）编排的平台：你用自然语言提需求，Agent 读取项目里的流水线、技能和工具后执行制作，最终产出 `final.mp4`。

## 基本信息

**类型：** 创作工具
**链接：** https://github.com/calesthio/OpenMontage

## 它和普通 AI 视频软件的区别

普通 AI 视频软件是「打开 GUI 点按钮」；OpenMontage 是「打开项目 → AI Agent 阅读 OpenMontage → 你直接向 Agent 提制作需求」。Agent 本身就是编排器，而不是一个把所有步骤硬编码死的固定 Python 程序。

## 工作主线

```text
你的需求
   ↓
选择视频流水线
   ↓
研究
   ↓
提案
   ↓
脚本
   ↓
场景规划
   ↓
生成/寻找素材
   ↓
剪辑
   ↓
Remotion / HyperFrames / FFmpeg 合成
   ↓
自动质检
   ↓
final.mp4
```

标准结构可概括为：

```text
研究 -> 提案 -> 脚本 -> 场景规划 -> 资产生成 -> 剪辑 -> 合成
```

## 三层知识架构

| 层 | 目录 | 含义 |
|---|---|---|
| 第 1 层 | `tools/` + `pipeline_defs/` | 「存在什么」——真正执行操作的程序 + 做事情的流程 |
| 第 2 层 | `skills/` | 「如何使用它」——告诉 AI 怎么把事情做好 |
| 第 3 层 | `.agents/skills/` | 「如何工作」 |

对应关系：

```text
pipeline_defs = 做事情的流程
skills = 告诉 AI 怎么把事情做好
tools = 真正执行操作的程序
```

## 安装

### 前置条件

- Python 3.10+
- Node.js 18+
- FFmpeg
- 一个 AI 编程助手：Claude Code / Cursor / Codex / GitHub Copilot / Windsurf

### 下载项目

```powershell
git clone https://github.com/calesthio/OpenMontage.git
cd OpenMontage
```

### 自动安装

```powershell
make setup
```

### Windows 手动安装（无 make 时）

```powershell
py -3 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt

cd remotion-composer
npm install
cd ..

python -m pip install piper-tts
Copy-Item .env.example .env
```

> [!tip] npm install 报错
> Windows 下 `npm install` 若出现 `ERR_INVALID_ARG_TYPE`，改执行：
> ```powershell
> npx --yes npm install
> ```

## 零 API 快速上手

第一次学习不要配置任何 API，也不接 Kling、Veo。OpenMontage 自带一条零 API 路径：

```text
Piper TTS
Archive.org
NASA
Wikimedia Commons
Remotion
HyperFrames
FFmpeg
内置字幕
```

即使 `.env` 里这些全为空，仍然能做视频：

```text
FAL_KEY=
OPENAI_API_KEY=
GOOGLE_API_KEY=
RUNWAY_API_KEY=
```

### 第一个练习

```text
制作一个 30 秒的动画解说视频，
主题是：为什么天空是蓝色的。

要求：
- 中文旁白
- 中文字幕
- 16:9
- 不使用付费 API
- 优先使用本地和免费工具
```

把整个 OpenMontage 文件夹在 Cursor / Claude Code / Codex 中打开，把这段话直接发给 Agent。这就是 OpenMontage 最核心的使用方式。

## 流水线一览

| 你想做什么 | 应该理解成 |
| --- | --- |
| 科普视频 | Animated Explainer |
| 动态图形 | Animation |
| 数字人口播 | Avatar Spokesperson |
| 电影预告 | Cinematic |
| 长视频切 Shorts | Clip Factory |
| 真实素材纪录片 | Documentary Montage |
| 真人素材 + AI | Hybrid |
| 翻译配音 | Localization & Dub |
| 播客转视频 | Podcast Repurpose |
| 软件教程 | Screen Demo |
| 真人口播 | Talking Head |

制作时可以直接指定流水线提高控制力，例如：

```text
使用 Animated Explainer pipeline。
```

## 参考视频复刻

支持 YouTube / Short / Reel / TikTok / 本地视频作为参考。工作流不是复制原视频，而是：

```text
参考视频
 ↓
分析文案
 ↓
分析 Hook
 ↓
分析节奏
 ↓
分析镜头
 ↓
分析关键帧
 ↓
分析视觉风格
 ↓
产生 2～3 个原创方案
```

示例：

```text
这是一个我非常喜欢的 YouTube Short。
请给我制作一个类似的视频，但主题改为量子计算。
```

系统会回答保留什么（节奏 / Hook / 结构 / 基调）、改变什么（主题 / 视觉 / 角度 / 旁白）、预计成本、实际工具。

## 接入 API

零 API 视频跑通后，再编辑 `.env`：

```env
FAL_KEY=xxx
OPENAI_API_KEY=xxx
GOOGLE_API_KEY=xxx
```

不必一口气配置全部，可以从 `FAL_KEY` 开始，它覆盖较多图像/视频模型。能力关系大致是：

```text
FAL      → FLUX / Veo / Kling / MiniMax / Recraft
OpenAI   → TTS / GPT Image
Google   → Imagen / Google TTS
Runway   → Gen-4
xAI      → Grok Image / Grok Video
```

## 环境能力自查

遇到「为什么没有 Veo / 为什么没调 Kling / 为什么用 Piper / 为什么用静态图片」时，不要猜，直接看：

查看当前环境支持什么：

```powershell
python -c "from tools.tool_registry import registry; import json; registry.discover(); print(json.dumps(registry.support_envelope(), indent=2))"
```

查看 Provider 菜单：

```powershell
python -c "from tools.tool_registry import registry; import json; registry.discover(); print(json.dumps(registry.provider_menu(), indent=2))"
```

## Remotion 与 HyperFrames

OpenMontage 不只是视频生成模型包装器，还自己做视频合成：

| 运行时 | 适合 |
| --- | --- |
| Remotion | 解说视频、数据视频、字幕、卡片、图表、图片动画、Talking Head、React 动画 |
| HyperFrames | 动态图形、动态排版、产品发布、网页转视频、SVG 动画、GSAP、角色绑定动画 |

系统在提案阶段确定 `render_runtime`，不会渲染到一半切换。看到 `render_runtime: remotion` 就知道最后主要走 React / Remotion 合成。

## 学习路线

```text
LEVEL 1  安装 OpenMontage
LEVEL 2  零 API 生成 30 秒视频
LEVEL 3  认识 projects / renders / assets
LEVEL 4  理解 pipeline_defs
LEVEL 5  理解 skills
LEVEL 6  理解 tools registry
LEVEL 7  添加一个 API
LEVEL 8  使用 Kling / Veo / FLUX
LEVEL 9  参考视频 → 新视频
LEVEL 10 修改 / 新建自己的 Pipeline
```

- 1～3 是「会用」
- 4～6 是「看懂 OpenMontage」
- 7～9 是「正式生产」
- 10 属于「二次开发」

> [!tip] 建议
> 不要从头背 README，先把第一个 30 秒零 API 视频完整跑通，再研究流水线和 Skill。

## 注意事项

- 安装命令、流水线列表和 API 供应商会随版本变化，使用前以官方 README 为准。
- `support_envelope()` 和 `provider_menu()` 是判断当前环境能力的一手依据，不要靠猜。

## 相关导航

- [[Github优质项目-MOC]]
- [[claude-video-分析]]
- [[remotion-skills-视频编程技能]]
- [[AI工具链与Agent实践-MOC]]
