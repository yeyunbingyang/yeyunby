# 03-AI语音-TTS

> 文本到语音、声音克隆与角色语音生产能力层。

## 知识入口

- [[Web-Speech-API与浏览器TTS]]
- [[本地TTS路线图-2026]]
- [[在线TTS能力与选型]]
- [[声音克隆基础与参考音频规范]]
- [[角色语音一致性设计]]
- [[配音生成-本机TTS引擎选型]]

## 当前分工（2026-08）

```text
秒级预览 → Web Speech API / Kokoro
本地高质量 → IndexTTS2 / Fun-CosyVoice3 / GPT-SoVITS
在线高质量/低运维 → ElevenLabs 等 API
固定角色 → Voice Clone + 角色 Voice Profile
正式比较 → 08-实验室-Lab/TTS实验
```

模型版本、许可证与硬件统一放 `06-工具与模型`；本目录重点记录“如何把语音做稳定”。