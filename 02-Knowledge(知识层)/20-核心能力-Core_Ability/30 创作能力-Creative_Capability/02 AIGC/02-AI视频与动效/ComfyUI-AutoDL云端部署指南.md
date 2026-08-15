---
title: ComfyUI AutoDL 云端部署指南
domain: Core_Ability
tags:
  - AIGC
  - ComfyUI
  - AutoDL
  - 云端部署
status: 稳定
created: 2026-08-14
updated: 2026-08-14
verified: 2026-08-14
review_after: 2026-11-14
source: "https://www.autodl.com/docs/quick_start/ ; https://github.com/Comfy-Org/ComfyUI"
related:
  - "[[AI视频与动效-MOC]]"
  - "[[AI绘画与图像-MOC]]"
  - "[[MiniMax-H3-ComfyUI本地部署指南|ComfyUI 本地部署（MiniMax H3）]]"
  - "[[06-ComfyUI-+⭐节点式StableDiffusion工作流工具|ComfyUI Stable Diffusion 工作流]]"
summary: "在 AutoDL 上跑 ComfyUI 只需掌握“租实例→装 ComfyUI→下载模型→6006 端口映射→关机”五步，其中“镜像”（PyTorch/CUDA 环境）与“模型”（FLUX/SDXL 权重）是两回事"
---

# ComfyUI AutoDL 云端部署指南

> [!important] 核心澄清
> AutoDL 的「快速开始」教的不是 ComfyUI，而是「如何开一台 Linux GPU 容器」。ComfyUI 是你要在这个容器里进一步部署、运行的软件。最容易混淆的三件事是：**镜像 ≠ 模型**，**实例 ≠ 已有 ComfyUI**，**端口 ≠ localhost:8188**。

## 概念分层

把 AutoDL 的「环境 / 镜像 / 模型」拆开看，层级关系如下：

```text
AutoDL
│
├─ GPU              ← 4090 / 5090 / A6000...
├─ Ubuntu           ← 操作系统
├─ CUDA
└─ PyTorch
      ↑
      └── 这些 = 运行环境 / AutoDL 镜像

ComfyUI             ← 你安装的应用程序

ComfyUI/models
├─ FLUX / SDXL / Wan / LoRA / ControlNet / VAE
      ↑
      └── 这些才是我们平时说的 AI 模型
```

AutoDL 已提供大量带 **PyTorch + CUDA + Python** 的基础镜像，因此不需要像在一台全新 Linux 服务器上那样从零装显卡驱动、CUDA 和 PyTorch。

## 三层部署路线

### 第一层：AutoDL 创建 GPU 环境

```text
AutoDL 控制台 → 租用新实例 → 选择 GPU（如 4090 24GB / 5090 32GB）
→ 选择 PyTorch 镜像 → 创建实例
```

这一步完成后，你拿到的是类似 `Ubuntu + Python + CUDA + PyTorch + RTX 4090` 的环境，**还不等于已经有 ComfyUI**。

### 第二层：在里面装 ComfyUI

打开 AutoDL 的 **我的实例 → JupyterLab → Terminal**，执行：

```bash
cd /root/autodl-tmp
git clone https://github.com/Comfy-Org/ComfyUI.git
cd ComfyUI
pip install -r requirements.txt
```

完成这一步，结构才变成：

```text
AutoDL GPU服务器 → PyTorch / CUDA → ComfyUI
```

ComfyUI 官方开源项目本身就是运行在 Python/PyTorch 环境里的节点式生成引擎。

### 第三层：下载模型

模型放在 `/root/autodl-tmp/ComfyUI/models/` 下，例如：

```text
ComfyUI/models
├── diffusion_models/   └── flux.safetensors
├── loras/              └── character.safetensors
├── vae/                └── ae.safetensors
├── checkpoints/
├── text_encoders/
├── controlnet/
└── upscale_models/
```

> [!tip] 下载比上传省一次传输
> 不需要走 `HuggingFace → 本地电脑 → 上传 AutoDL`，直接 `HuggingFace / ModelScope → AutoDL` 更省事。

## 端口映射（与本地最大的不同）

本地电脑直接访问 `localhost:8188` 即可，但 AutoDL 实例没有普通意义上的独立公网 IP。它默认提供 **6006 和 6008** 的公网映射，其他端口需走 SSH 隧道。因此不能照搬普通云服务器教程里的 `--listen 0.0.0.0` 然后指望 `IP:8188` 直接访问。

适合 AutoDL 的方式是让 ComfyUI 直接跑在映射端口：

```bash
cd /root/autodl-tmp/ComfyUI
python main.py --listen 0.0.0.0 --port 6006
```

然后在 AutoDL 的 **自定义服务 → 6006 → 复制平台提供的网址 → 浏览器打开**，即回到熟悉的「打开网页 → 拖节点 → 生成图片」。

## 关键概念对照

| 名称 | 实际是什么 |
| --- | --- |
| AutoDL 实例 | 云端 GPU 电脑 / 容器 |
| AutoDL 镜像 | Ubuntu + CUDA + Python + PyTorch 环境 |
| ComfyUI | AI 生成软件 |
| ComfyUI 工作流 | 节点配置 |
| FLUX / Wan / SDXL | AI 模型 |
| `.safetensors` | 模型文件 |
| `custom_nodes` | ComfyUI 插件 |

> [!warning] 最容易搞混
> **AutoDL 的「镜像」≠ FLUX/SDXL 模型。**

## 关机与数据保留

- 普通关机后，实例的数据和环境都会保存，再开机无需重新配置和上传。
- 连续关机 15 天实例会被释放，需注意官方数据保留规则。

最终结构可以固定为：

```text
AutoDL 5090
├─ ComfyUI          ← 装一次
├─ custom_nodes     ← 装一次
├─ models
│   ├─ FLUX / Wan / ControlNet / LoRA   ← 各下载一次
└─ workflows        ← 保存你的工作流

不用时 → 关机停止 GPU 运行计费
下次 → 开机 → 启动 ComfyUI → 继续使用
```

## 结论

如果只是用 ComfyUI，不需要完整学习 AutoDL 文档里的「训练模型」流程。掌握 **创建实例 → JupyterLab/Terminal → 文件目录 → 6006 服务 → 关机** 这五件事基本就够了。

## 参考资料

- [AutoDL 快速开始](https://www.autodl.com/docs/quick_start/)
- [AutoDL 基础配置（镜像）](https://www.autodl.com/docs/base_config/)
- [AutoDL 开放端口](https://www.autodl.com/docs/port/)
- [Comfy-Org/ComfyUI](https://github.com/Comfy-Org/ComfyUI)

## 相关笔记

- [[AI视频与动效-MOC]]
- [[AI绘画与图像-MOC]]
- [[MiniMax-H3-ComfyUI本地部署指南|ComfyUI 本地部署（MiniMax H3）]]
- [[06-ComfyUI-+⭐节点式StableDiffusion工作流工具|ComfyUI Stable Diffusion 工作流]]
