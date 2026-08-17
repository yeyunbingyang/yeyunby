---
title: GPT-SoVITS - 少样本声音克隆与本地TTS
tags: [GPT-SoVITS, VoiceClone, TTS, 本地TTS, AI语音]
status: 持续更新
created: 2026-08-17
updated: 2026-08-17
summary: "GPT-SoVITS 是面向少样本声音克隆与多语言 TTS 的开源 WebUI/工具链，核心价值是用极少参考音频快速建立可本地运行的角色声音。"
source: https://github.com/RVC-Boss/GPT-SoVITS
---

# GPT-SoVITS - 少样本声音克隆与本地TTS

## 一句话定位

> GPT-SoVITS = **少样本声音克隆 + 多语言 TTS + 数据集处理 + 训练/推理 WebUI + API**。

它不只是一个“输入文字生成语音”的模型，更像一套从参考音频处理、标注、训练到推理的本地声音克隆工作台。

## 核心能力

### 1. Zero-shot TTS

官方说明可输入约 **5 秒参考语音**，直接进行零样本语音合成。

适合：

- 快速试听某个角色音色
- 验证参考音频是否合格
- 不训练模型先做 Demo
- 临时角色配音

### 2. Few-shot TTS

官方说明使用约 **1 分钟训练数据**即可进行少样本微调，以提升音色相似度与自然度。

适合：

- 固定角色长期使用
- 视频旁白角色
- 动漫/漫剧人物配音
- 游戏 NPC / 虚拟角色
- 建立个人 Voice Profile

### 3. 跨语言合成

当前官方 README 列出的语言包括：

- 中文
- 英文
- 日文
- 韩文
- 粤语

因此参考声音与最终输出语言不必完全相同，适合多语言角色资产。

### 4. 数据集工具链

WebUI 集成或配套了多种声音数据处理工具，包括：

- 人声/伴奏分离
- 音频自动切片
- ASR 自动转写
- 文本标注
- 训练数据整理
- GPT / SoVITS 模型训练
- TTS 推理

这也是 GPT-SoVITS 相比“单纯 TTS 推理模型”更实用的地方：**训练前的数据处理流程基本被串起来了。**

## 工作流理解

```text
授权声音素材
   ↓
清理音频 / 去伴奏 / 降低混响
   ↓
自动切片
   ↓
ASR 转写 + 文本校对
   ↓
5 秒参考音频 Zero-shot 测试
   ↓
相似度足够？
   ├─ 是 → 直接推理
   └─ 否 → 整理约 1 分钟以上高质量数据进行 Few-shot 微调
   ↓
保存角色声音模型 / Voice Profile
   ↓
WebUI 或 API 批量生成角色语音
```

## 与 yeyunby 声音资产体系的关系

建议把 GPT-SoVITS 看成 **Voice Profile 的一个执行引擎**，不要让角色身份绑定到单一模型。

例如：

```yaml
voice_id: CHARACTER_V01
identity_ref: neutral.wav
style_ref: gentle.wav
engine: GPT-SoVITS
engine_version: pinned
model_path: models/CHARACTER_V01/
language: zh
notes: 少样本角色声音克隆
```

这样未来切换到 CosyVoice、IndexTTS 或其他模型时，角色声音资产仍然可以复用。

## 本地部署

### Windows 快速方式

官方提供 Windows 整合包，典型启动入口为：

```text
go-webui.bat
```

也提供 PowerShell 启动方式：

```text
go-webui.ps1
```

这与 Windows 项目脚本的 **BAT 外层入口 + PowerShell 内层逻辑** 思路比较一致。

### 源码安装方式

官方当前推荐的 Windows 安装流程之一：

```powershell
conda create -n GPTSoVits python=3.10
conda activate GPTSoVits
pwsh -F install.ps1 --Device <CU126|CU128|CPU> --Source <HF|HF-Mirror|ModelScope> [--DownloadUVR5]
```

启动：

```powershell
python webui.py
```

### Docker

仓库同时提供 Dockerfile 与 docker-compose，可选择 CUDA 完整版或 Lite 版本。

Lite 版本会减少部分 ASR / UVR5 相关组件，适合只需要推理能力的环境。

## API

仓库根目录提供：

```text
api.py
api_v2.py
```

因此 GPT-SoVITS 不必只通过 WebUI 使用，也可以作为本地语音服务接入：

- 视频生成流水线
- 自动旁白
- 角色对白系统
- AI Agent 语音输出
- 批量短视频配音
- OpenMontage / VideoTool 一类自动视频工具

推荐的工程关系：

```text
上层应用
  ↓
TTS Adapter
  ↓
GPT-SoVITS API
  ↓
Voice Profile / 模型权重
  ↓
WAV 输出
```

不要让业务代码直接强绑定 GPT-SoVITS 的具体接口，最好加一层 TTS Adapter，方便以后替换模型。

## 数据集格式

官方 `.list` 标注格式：

```text
vocal_path|speaker_name|language|text
```

例如：

```text
D:\GPT-SoVITS\data\001.wav|character01|zh|这是一段角色测试语音。
```

这类文本标注文件应该和原始音频、处理后音频、模型权重分开保存，避免数据资产混乱。

## 优点

- 极少参考音频即可开始测试
- 少样本训练门槛低
- 中文生态成熟
- 支持多语言
- 本地部署
- 自带完整 WebUI
- 集成音频切片、ASR、标注等工具
- 提供 API，容易进入自动化生产链
- 很适合建立固定动漫/视频角色声音

## 注意点

### 参考音频质量仍然是核心

低质量参考音频会直接导致：

- 音色相似度下降
- 背景噪声被学习
- 混响被复制
- 发音不稳定
- 情绪与身份混在一起

因此先遵循 [[声音克隆基础与参考音频规范]]，再考虑训练。

### Zero-shot 不等于稳定角色资产

5 秒参考音频适合快速测试，但长期角色使用更应该验证：

- 不同文本下的身份稳定性
- 长句稳定性
- 情绪变化后的身份保持
- 多语言切换后的音色保持
- 多次推理是否出现明显漂移

### 模型版本需要固定

GPT-SoVITS 更新速度较快。项目生产环境不应始终追 `main`，应记录：

```yaml
engine: GPT-SoVITS
repo_commit: <commit-sha>
model_version: <version>
python: 3.10
cuda: <version>
```

这样出现音质变化时可以回溯。

## 版本状态说明（2026-08-17）

GitHub 的 Latest Release 页面仍显示 **2025-06-06 发布的 `20250606v2pro`**；与此同时，当前 `main` 分支 README 已经介绍 **v2 ProPlus**，仓库在 2026 年仍有代码更新。

所以实际部署时：

> **不要只依据 GitHub Latest Release 判断主线当前能力，应同时检查 main README、Changelog 与目标整合包版本。**

生产项目则反过来，应主动固定一个已验证版本，而不是自动追最新代码。

## 在 yeyunby 中的定位

```text
03-AI音乐与音频
└─ 03-AI语音-TTS
   ├─ 02-本地TTS
   ├─ 04-Voice-Clone
   │  ├─ 声音克隆基础与参考音频规范.md
   │  └─ GPT-SoVITS-少样本声音克隆与本地TTS.md
   └─ 05-角色语音
```

知识关系：

```text
声音克隆基础
   ↓
GPT-SoVITS（具体执行工具）
   ↓
角色 Voice Profile
   ↓
角色语音一致性
   ↓
视频 / 动漫 / Agent / 旁白生产
```

## 推荐学习顺序

1. [[声音克隆基础与参考音频规范]]
2. 准备一份合法、干净的 5～10 秒参考音频
3. 用 GPT-SoVITS 做 Zero-shot 测试
4. 对相似度、发音、长句进行验收
5. 再准备约 1 分钟以上高质量数据做 Few-shot
6. 保存 Voice Profile 与版本信息
7. 最后接入视频或角色生产流水线

## 来源

- [RVC-Boss/GPT-SoVITS](https://github.com/RVC-Boss/GPT-SoVITS)
- [GPT-SoVITS Changelog](https://github.com/RVC-Boss/GPT-SoVITS/tree/main/docs)

## 相关

- [[声音克隆基础与参考音频规范]]
- [[本地TTS路线图-2026]]
- [[角色语音一致性设计]]
