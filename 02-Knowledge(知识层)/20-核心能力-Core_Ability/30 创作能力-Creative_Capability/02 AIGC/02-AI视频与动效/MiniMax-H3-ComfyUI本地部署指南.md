---
title: MiniMax H3 ComfyUI 本地部署指南
domain: Core_Ability
tags:
  - AIGC
  - AI视频
  - ComfyUI
  - 本地部署
status: 稳定
created: 2026-08-14
updated: 2026-08-14
verified: 2026-08-14
review_after: 2026-09-14
source: "https://docs.comfy.org/tutorials/video/minimax/minimax-h3"
related:
  - "[[AI视频与动效-MOC]]"
  - "[[06-ComfyUI-+⭐节点式StableDiffusion工作流工具|ComfyUI Stable Diffusion 工作流]]"
  - "[[本机AI音乐项目适配评估]]"
summary: "MiniMax H3 可通过 ComfyUI 0.30.0 以上版本纯本地生成带立体声音频的视频，本机 RTX 4060 Laptop 8GB 可依赖 Dynamic VRAM 低规格运行，但部署前必须解决 C 盘空间不足"
---

# MiniMax H3 ComfyUI 本地部署指南

> [!important] 本机结论
> MiniMax H3 已开放权重，并由 ComfyUI 原生支持，无需安装第三方 H3 生成节点。当前 **RTX 4060 Laptop 8GB + 32GB 内存**可以尝试本地运行，但低于官方已验证的 12GB 显存稳妥配置，必须使用小模型、Dynamic VRAM、高速磁盘和低分辨率起步。当前 C 盘仅余约 0.1GB，是部署前必须先解决的阻塞项。

## 模型能力与部署边界

MiniMax H3 是可联合理解文本、图像、视频和音频的全模态生成模型。ComfyUI 提供以下原生工作流：

| 模式 | 作用 | 使用的扩散模型 |
| --- | --- | --- |
| T2V | 根据提示词生成视频与同步音频 | `fl2va` |
| I2V | 根据首帧或首尾帧生成视频 | `fl2va` |
| R2V | 用图片、视频或音频锁定角色、风格、动作、镜头或声音 | `ref2va` |

官方能力上限包括约 15 秒、24fps、最高 2K 输出及原生立体声音频，但消费级低显存设备不应直接从上限规格开始。首次验证应使用 480p、5 秒和官方默认工作流。

> [!warning] API 节点不等于本地推理
> 旧版 `MinimaxHailuoVideoNode` 等合作方节点调用的是在线 API。真正的 H3 本地方案应使用开放权重、ComfyUI 原生 MiniMax H3 节点和本地 `safetensors` 模型文件。

## 本机适配评估

| 硬件 | 当前检测结果 | 影响 |
| --- | --- | --- |
| GPU | NVIDIA GeForce RTX 4060 Laptop | 支持 CUDA，本地推理路线成立 |
| 显存 | 8188MiB，约 8GB | 可依赖 Dynamic VRAM 运行，但模型换入换出明显，速度较慢 |
| 内存 | 31.6GB | 属于最低可尝试档，生成时应关闭浏览器视频、游戏和大型图形软件 |
| NVIDIA 驱动 | 610.62 | 可使用当前 CUDA 13 版 ComfyUI Portable |
| C 盘 | 约 0.1GB 可用 | 无法承受临时文件、缓存和分页文件，必须先释放空间 |
| F/X 盘 | 各约 1.6TB 可用 | 适合存放 ComfyUI、模型和输出；优先选择高速本地 SSD |

官方团队公开验证的稳妥最低配置是 RTX 3060 12GB、32GB 内存和高速 NVMe；社区已有 8GB 显存运行成功的案例，但不能把它视为相同稳定性或速度保证。

## 推荐部署方案

### 1. 部署前准备

- [ ] C 盘至少释放 30～50GB，保证临时目录和分页文件可用
- [ ] 将 ComfyUI、模型、Hugging Face 缓存和输出统一放到 F 盘高速 SSD
- [ ] 预留至少 60GB 给 T2V/I2V；若还需要 R2V，建议预留 90GB 以上
- [ ] 关闭占用 GPU 或大量内存的程序
- [ ] 检查输入素材的版权和模型社区许可证

建议目录：

```text
F:\AI\ComfyUI-H3\
```

### 2. 安装 ComfyUI

优先使用官方 Windows Portable，避免手动组合 Python、PyTorch 和 CUDA：

1. 从 [ComfyUI Windows Portable 官方页面](https://docs.comfy.org/installation/comfyui_portable_windows)下载 NVIDIA 标准便携包。
2. 解压到 `F:\AI\ComfyUI-H3\`，不要放到 C 盘。
3. 运行 `update\update_comfyui.bat` 更新到最新版本。
4. 运行 `run_nvidia_gpu.bat` 启动。
5. 在控制台确认 GPU 为 RTX 4060 Laptop，且 PyTorch 使用 CUDA。

MiniMax H3 要求 ComfyUI 0.30.0 或更高版本。当前标准 Portable 使用 Python 3.13 和 CUDA 13.0，适合官方推荐的 INT8 ConvRot 模型。

### 3. 加载官方工作流

打开 ComfyUI 后进入：

```text
模板库 → Video → MiniMax H3
```

根据任务选择 `MiniMax H3 T2V`、`MiniMax H3 I2V` 或 `MiniMax H3 R2V`。模板会检查缺失模型并提示下载，这是最简单且不易放错目录的安装方式。

若模板库没有 MiniMax H3，说明 ComfyUI 或工作流模板版本过旧，应先完成更新，不要立即安装来历不明的第三方节点。

## 模型选择与目录

### T2V / I2V 最小组合

```text
ComfyUI/
└── models/
    ├── diffusion_models/
    │   └── minimax_h3_fl2va_pruned_int8_convrot.safetensors
    ├── text_encoders/
    │   └── qwen3vl_32b_minimax_h3_nvfp4_awq.safetensors
    └── vae/
        ├── minimax_h3_video_vae_fp16.safetensors
        └── minimax_h3_audio_vae_fp32.safetensors
```

这套组合约占 42GB，是当前本机首选。NVFP4/AWQ 文本编码器不要求 Blackwell GPU；在 CUDA 13 环境下，扩散模型优先使用 `int8_convrot`，仅在不兼容时退回 `fp8_scaled`。

### R2V 附加模型

R2V 使用独立权重，需要额外下载：

```text
ComfyUI/models/diffusion_models/
└── minimax_h3_ref2va_pruned_int8_convrot.safetensors
```

模型与官方工作流：[Comfy-Org/MiniMax-H3](https://huggingface.co/Comfy-Org/MiniMax-H3)

## 首次运行参数

首次测试的目标是验证完整管线，不是追求最终画质：

| 参数 | 建议值 |
| --- | --- |
| 模式 | 先 T2V，再 I2V，最后 R2V |
| 画幅 | 16:9 |
| 像素量 | 0.4MP，约 864×480 |
| 时长 | 5 秒 |
| 帧率 | 24fps，保持模板默认值 |
| Steps | 先保持官方模板默认值 |
| 批次 | 1 |
| 音频 | 开启，用于验证视频与 Audio VAE 全链路 |

成功生成后，再逐步增加到 0.7MP、1.0MP 或更长时长。每次只改一个变量并记录耗时、显存、内存和画面质量。

## 低显存优化顺序

1. **保持最新版 ComfyUI**：Dynamic VRAM 已默认启用，会按需在显存、内存和磁盘之间调度模型。
2. **先降低分辨率和时长**：这是最稳定、最容易判断效果的减负方式。
3. **关闭无关程序**：32GB 内存是低显存卸载的重要缓冲区。
4. **基础工作流跑通后再装 SageAttention**：官方文档称可显著加速，但安装包必须匹配 PyTorch 与 CUDA 版本。
5. **出现系统内存或分页压力时再测试 `--disable-pinned-memory`**：这是社区低内存配置，不应在首次运行前盲目叠加参数。

> [!tip] SageAttention 接法
> 可通过 KJNodes 的 `Patch Sage Attention KJ` 节点接在 `UNETLoader` 与 `BasicGuider` 之间，并将 `sage_attention` 设为 `auto`；也可在启动时使用 `--use-sage-attention`。应先保存一份未经加速修改的官方基线工作流。

## 常见故障排查

| 现象 | 优先检查 |
| --- | --- |
| 模板中没有 MiniMax H3 | ComfyUI 是否达到 0.30.0，是否更新了工作流模板 |
| `model not found` | 文件名和 `diffusion_models`、`text_encoders`、`vae` 目录是否正确 |
| 加载 INT8 时崩溃 | 是否使用当前 CUDA 13 Portable、最新版 PyTorch 与 `comfy-kitchen` |
| CUDA OOM | 降到 0.4MP/5秒/批次1，关闭其他 GPU 程序，确认 Dynamic VRAM 生效 |
| 系统卡死或内存耗尽 | 检查 C 盘、分页文件、可用内存及模型所在磁盘速度 |
| 首次生成特别慢 | 首次包含模型加载、文本编码及 VAE 初始化，应与第二次相同参数运行对比 |
| 输出没有声音 | 检查 Audio VAE 是否加载，以及保存节点是否输出带音轨的 MP4 |
| R2V 角色不稳定 | 使用 `<Picture 1>`、`<Video 1>`、`<Audio 1>` 明确引用顺序和各素材职责 |

## 验收清单

- [ ] ComfyUI 版本不低于 0.30.0
- [ ] 控制台正确识别 RTX 4060 Laptop 和 CUDA
- [ ] 四个 T2V/I2V 模型文件被节点正确识别
- [ ] 864×480、5 秒、批次 1 能完成生成
- [ ] 输出 MP4 同时包含视频和立体声音频
- [ ] 第二次相同参数生成没有异常变慢或内存持续增长
- [ ] 记录总耗时、采样耗时、显存峰值和内存峰值
- [ ] 基线成功后再测试 SageAttention 或社区量化模型

## 参考资料

- [MiniMax H3 ComfyUI 官方教程](https://docs.comfy.org/tutorials/video/minimax/minimax-h3)
- [ComfyUI 版 MiniMax H3 模型仓库](https://huggingface.co/Comfy-Org/MiniMax-H3)
- [MiniMax H3 官方发布说明](https://minimaxi.com/blog/minimax-h3)
- [ComfyUI Windows Portable 安装文档](https://docs.comfy.org/installation/comfyui_portable_windows)
- [Dynamic VRAM 官方说明](https://blog.comfy.org/p/dynamic-vram-in-comfyui-saving-local)
- [RTX 4060 Laptop 8GB 社区运行案例](https://www.reddit.com/r/StableDiffusion/comments/1vfky6e/minimax_h3_will_run_on_a_4060_laptop_fyi/)

## 相关笔记

- [[AI视频与动效-MOC]]
- [[06-ComfyUI-+⭐节点式StableDiffusion工作流工具|ComfyUI Stable Diffusion 工作流]]
- [[本机AI音乐项目适配评估]]
