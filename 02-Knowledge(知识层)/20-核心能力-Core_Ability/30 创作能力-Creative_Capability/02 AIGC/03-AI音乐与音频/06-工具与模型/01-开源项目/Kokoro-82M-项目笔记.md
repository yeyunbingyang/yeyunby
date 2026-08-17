---
title: Kokoro-82M-项目笔记
tags: [TTS, Kokoro, 轻量模型, CPU, 本地部署, 开源项目]
status: 稳定
created: 2026-08-17
updated: 2026-08-17
verified: 2026-08-17
review_after: 2026-10-17
source: https://github.com/hexgrad/kokoro
summary: "Kokoro-82M 是轻量开放权重 TTS，适合作为本地快速试听、CPU/端侧和浏览器路线的基础引擎。"
---

# Kokoro 82M 项目笔记

## 一句话定位

**Kokoro-82M = 小模型、快速、成本低的本地 TTS 预览引擎。**

它不负责追求 IndexTTS-2.5 / GPT-SoVITS 那种角色克隆上限，而是承担声音生产链中的“快速试听”和轻量部署。

## 核心特点

官方当前说明：

- 82M 参数
- open-weight TTS
- 权重采用 Apache 许可
- Python 推理库可直接 `pip install kokoro`
- 输出示例为 24kHz
- 支持 speed 参数
- 使用 Misaki G2P
- 支持普通话、日文、西班牙文、法文、印地语、意大利文、巴西葡萄牙文、英式/美式英语等管线

普通话需要：

```bash
pip install "misaki[zh]"
```

日文需要：

```bash
pip install "misaki[ja]"
```

## 快速安装

```bash
pip install "kokoro>=0.9.4" soundfile
```

部分语言和英文 OOD fallback 需要 `espeak-ng`。

Windows 上官方 README 提供了独立安装 `espeak-ng` 的路线。

## Python 最小示例

```python
from kokoro import KPipeline
import soundfile as sf

pipeline = KPipeline(lang_code='z')

generator = pipeline(
    '你好，这是快速语音预览。',
    voice='zf_xiaobei',
    speed=1,
)

for i, (_, _, audio) in enumerate(generator):
    sf.write(f'{i}.wav', audio, 24000)
```

> voice 名称应以当前模型实际提供的 voice 资产为准；这里的知识重点是管线结构，不把某个 voice 名当作永久接口。

## 在整个音频体系里的角色

Kokoro 最适合放在：

```text
脚本 / 文案
  ↓
Kokoro 快速试听
  ↓
确定节奏、句子长度、对白结构
  ↓
IndexTTS-2.5 / CosyVoice3 / GPT-SoVITS 正式生成
```

这样可以避免每次修改一句对白都调用更重的角色克隆模型。

## 适合的任务

| 任务 | 适合度 | 说明 |
|---|---:|---|
| 快速试听 | ★★★★★ | 核心定位 |
| CPU / 低资源本地 TTS | ★★★★★ | 82M 参数 |
| 文本编辑器语音预览 | ★★★★★ | 启动简单 |
| 浏览器/ONNX 衍生路线 | ★★★★☆ | 社区生态丰富，需单独验证具体实现 |
| 普通旁白 | ★★★★☆ | 成本低、速度快 |
| 固定角色声音克隆 | ★★☆☆☆ | 不是主要定位 |
| 强情绪角色演绎 | ★★☆☆☆ | 不替代主力角色 TTS |
| 训练角色专属模型 | ★☆☆☆☆ | 应使用其他路线 |

## 与主力 TTS 的分工

```text
Kokoro
→ 快速试听 / CPU / 端侧 / 草稿

IndexTTS-2.5
→ 高质量零样本角色对白

Fun-CosyVoice3
→ 多语言/方言/流式服务

GPT-SoVITS
→ 固定角色训练与长期声音资产
```

## 许可证

官方 README 明确说明 Kokoro 权重为 **Apache licensed weights**，适合从个人项目到生产部署。

实际集成时仍应分别检查：

- `kokoro` 推理库
- Kokoro-82M 权重
- Misaki / espeak-ng
- 使用的 voice 资产

不要因为主模型宽松就忽略整个依赖链的许可证。

## 后续实验建议

1. 中文 100 / 500 / 2000 字长文本速度
2. CPU RTF 与内存占用
3. 中文数字、英文缩写、专有名词发音
4. speed 0.8 / 1.0 / 1.2 对自然度影响
5. 不同 voice 音色稳定性
6. 与 Edge TTS 做快速预览质量对比
7. 浏览器 ONNX / WebGPU 路线验证

## 相关

- [[本地TTS路线图-2026]]
- [[Fun-CosyVoice3-项目笔记]]
- [[IndexTTS-2.5-项目笔记]]
- [[GPT-SoVITS-项目笔记]]
- [[Web-Speech-API与浏览器TTS]]
