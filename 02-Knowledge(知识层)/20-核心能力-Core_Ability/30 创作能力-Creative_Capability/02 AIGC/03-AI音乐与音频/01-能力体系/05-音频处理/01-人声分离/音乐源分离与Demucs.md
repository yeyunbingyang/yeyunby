---
title: 音乐源分离与Demucs
tags: [音频处理, 源分离, Demucs, Stem]
status: 稳定
created: 2026-08-17
updated: 2026-08-17
verified: 2026-08-17
review_after: 2026-10-17
summary: "源分离将混合音乐拆为 vocals/drums/bass/other 等 Stem；Demucs 仍是重要技术基线，但 Meta 官方仓库已归档，生产使用应固定可工作的版本。"
---

# 音乐源分离与 Demucs

## 用途

源分离不是“去人声”这么单一，它是后续 AI 音乐编辑的基础步骤：

```text
原曲
├─ vocals
├─ drums
├─ bass
└─ other
```

有了 Stem 后可以：

- 保留原唱，只重做伴奏
- 单独替换鼓组或低音
- 为 Remix / Audio-to-Audio 提供更干净条件
- 单独修复人声
- 做 Karaoke / 字幕 / 对齐

## Demucs 当前状态

Meta/Facebook Research 的 `facebookresearch/demucs` 仓库已于 **2025-01-01** 归档并设为只读。官方 README 指向作者维护的 `adefossez/demucs` fork，并说明以重要 bug 修复为主，不属于活跃功能开发。

因此 2026 的正确使用方式不是“追最新版 Demucs”，而是：

1. 选择确认可运行的发行版本/commit。
2. 固定 Python / Torch / CUDA 环境。
3. 保存分离模型名称与参数。
4. 对关键音乐做人工试听，不只看 SDR 指标。

## AI 音乐中的典型流程

```text
原曲
→ Demucs 分离
→ vocals 保留
→ accompaniment / stems 送入 ACE-Step 或 Stable Audio 3
→ 生成新编曲
→ 与原 vocals 对齐
→ 混音 / 母带
```

## 分离验收

- 人声里是否残留鼓/和弦
- 伴奏里是否残留明显主唱
- 高频是否出现水声/金属伪影
- 鼓瞬态是否被削弱
- 混回后是否产生相位或空间异常

## 官方来源

- [facebookresearch/demucs](https://github.com/facebookresearch/demucs)
- [adefossez/demucs](https://github.com/adefossez/demucs)

## 相关

- [[原音乐风格化改编-需求与模型选型]]
- [[混音母带与AI音频验收]]