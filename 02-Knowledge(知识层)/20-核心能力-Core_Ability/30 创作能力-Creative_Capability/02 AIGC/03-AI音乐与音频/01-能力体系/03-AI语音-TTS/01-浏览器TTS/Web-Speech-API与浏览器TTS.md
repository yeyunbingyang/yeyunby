---
title: Web-Speech-API与浏览器TTS
tags: [TTS, WebSpeechAPI, 浏览器]
status: 稳定
created: 2026-08-17
updated: 2026-08-17
verified: 2026-08-17
summary: "浏览器 TTS 适合零部署预览；Web Speech API 的 SpeechSynthesis 广泛可用，但声音取决于设备/系统，不适合作为跨机器一致的最终配音引擎。"
---

# Web Speech API 与浏览器 TTS

## 定位

浏览器 TTS 最适合：

- HTML 原型即时试听
- 台词粗剪
- 无障碍朗读
- 没有后端服务时的兜底

不适合直接承担“固定角色跨集一致”的最终成片配音。

## Web Speech API

Web Speech API 分为：

- `SpeechSynthesis`：文本转语音
- `SpeechRecognition`：语音识别

`SpeechSynthesis` 可读取当前设备可用声音，并控制 `voice / rate / pitch / volume`。

```js
const synth = window.speechSynthesis;
const utter = new SpeechSynthesisUtterance('你好，这是预览语音。');
utter.lang = 'zh-CN';
utter.rate = 1.0;
synth.speak(utter);
```

## 为什么不同电脑声音不一样

Web Speech API 通常调用设备/操作系统提供的语音服务，因此：

- Windows / macOS / Android 可用声音不同
- Chrome / Edge 环境可能不同
- 同名语言未必有同一音色
- 用户系统更新后声音列表也可能变化

所以正式项目应该记录 `voice.name`，同时保留本地/在线 TTS 后端作为一致性方案。

## 浏览器内本地模型

另一条路线是 Kokoro.js / ONNX Runtime Web / transformers.js 等在浏览器内跑模型。它比系统 SpeechSynthesis 更可控，但首次模型下载、浏览器算力和兼容性要单独评估。

## 官方来源

- [MDN Web Speech API](https://developer.mozilla.org/en-US/docs/Web/API/Web_Speech_API)
- [MDN SpeechSynthesis](https://developer.mozilla.org/en-US/docs/Web/API/SpeechSynthesis)
- [Kokoro](https://github.com/hexgrad/kokoro)

## 相关

- [[本地TTS路线图-2026]]
- [[角色语音一致性设计]]