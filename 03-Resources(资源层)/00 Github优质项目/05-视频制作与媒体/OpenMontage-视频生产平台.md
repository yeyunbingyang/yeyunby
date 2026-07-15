---
name: openmontage-installation-guide
description: OpenMontage 视频生产平台的安装过程、使用方法和注意事项
metadata:
  type: reference
  project: OpenMontage
---

# OpenMontage 安装与运行指南

> 基于 `calesthio/OpenMontage` 仓库（当前本地为 `amartya-dev/OpenMontage` 的 fork，最新提交 f8d9463）

## 系统环境

| 项目 | 值 |
|------|-----|
| 操作系统 | Windows 11 Pro |
| Python | 3.11.15（要求 >= 3.10） |
| Node.js | v22.19.0 |
| npm | 11.16.0 |

## 安装步骤

### 1. 克隆仓库

```bash
git clone https://github.com/calesthio/OpenMontage.git
cd OpenMontage
```

### 2. 安装 Python 核心依赖

```bash
pip install -r requirements.txt
```

这会安装：`pyyaml`, `pydantic`, `jsonschema`, `python-dotenv`, `Pillow`, `numpy`, `requests`, `google-auth`, `google-genai`, `openai`, `fastapi`, `uvicorn`, `watchfiles`

**注意**：如果使用 Hermes Agent 等 AI 框架附带的 Python 环境，可能已有大部分包。`google-genai` 和 `openai` 可能需要升级到较新版本。

### 3. 以开发模式安装项目包

```bash
pip install -e .
```

**必须执行这一步**，否则 Python 找不到 `tools.tool_registry` 等模块。`setup.py` 中的 `find_packages()` 会扫描当前目录下的所有 Python 包。

**⚠️ 特别警告**：`pip install -e .` 必须在 OpenMontage **项目根目录**下执行。如果 `remotion-composer/` 目录下也有一个 `setup.py` 或类似文件，pip 可能会错认目标目录——请确认安装的是 `openmontage==0.1.0` 而不是其他包。

### 4. 安装 Remotion 前端依赖

```bash
cd remotion-composer && npm install
```

安装约 200 个 npm 包。会下载 Chrome Headless Shell（~113MB）用于服务端渲染。

**注意**：Remotion 的首次渲染需要下载 Headless Chrome，后续渲染会缓存。如果在中国大陆网络环境，Chrome 下载可能较慢，但会自动重试。

### 5. 配置环境变量

```bash
cp .env.example .env
```

编辑 `.env` 填入 API Key。**不配置任何 Key 也能运行演示视频**（仅用 Remotion 本地渲染）。推荐优先配置：

| API Key | 解锁能力 |
|---------|---------|
| `FAL_KEY` | FLUX 图像、Kling 视频、MiniMax 视频、Seedance 视频、Recraft 图像 |
| `GOOGLE_API_KEY` | Google TTS、Imagen 图像、Gemini Omni 视频 |
| `ELEVENLABS_API_KEY` | TTS 语音旁白 + 音乐生成 |
| `OPENAI_API_KEY` | OpenAI TTS + GPT Image 2 + Sora 视频 |

### 6. 验证安装——运行能力预检

```bash
python -c "from tools.tool_registry import registry; import json; registry.discover(); print(json.dumps(registry.provider_menu_summary(), indent=2, ensure_ascii=False))"
```

预期输出包含三大渲染引擎状态：
- `composition_runtimes.ffmpeg` — 始终可用
- `composition_runtimes.remotion` — 需 npm install 成功
- `composition_runtimes.hyperframes` — 需 Node >= 22 + npx

### 7. 运行零密钥演示视频

```bash
# 查看可用演示
python render_demo.py --list

# 选择一个演示渲染（约 750 帧，3-5 分钟）
python render_demo.py code-to-screen
```

输出路径：`projects/demos/renders/<demo-name>.mp4`

## 安装后结构

```
OpenMontage/
├── .env                  # API Key 配置（从 .env.example 复制）
├── requirements.txt      # Python 核心依赖
├── setup.py              # 项目包配置
├── tools/                # Python 工具（BaseTool 体系）
│   ├── tool_registry.py  # 工具注册表——能力发现的核心
│   ├── tts_selector.py   # 语音合成选择器
│   ├── image_selector.py # 图像生成选择器
│   └── video/            # 视频相关工具
├── skills/               # 创作技能（层 2）
├── .agents/skills/       # 供应商技能（层 3）
├── remotion-composer/    # Remotion React 合成前端
├── pipeline_defs/        # 流水线定义（YAML）
├── lib/                  # 基础设施（checkpoint、pipeline_loader）
└── projects/             # 生产项目目录（gitignored）
```

## 常用命令

| 命令 | 用途 |
|------|------|
| `make setup` | 一键安装所有依赖（Python + npm + Piper TTS） |
| `make preflight` | 运行能力预检 |
| `make demo` | 渲染所有演示视频 |
| `make demo-list` | 列出可用演示 |
| `make test` | 运行测试 |
| `make install-dev` | 安装开发依赖 |
| `make install-gpu` | 安装 GPU 加速依赖（需 NVIDIA GPU） |
| `make hyperframes-doctor` | 诊断 HyperFrames 运行环境 |
| `make clean` | 清理 `__pycache__` |

## 注意事项

### 已知问题

1. **Hermes Agent 冲突**：如果使用 Hermes Agent 的 venv，其 `openai==2.24.0` 和 `Pillow==12.2.0` 可能与项目要求的版本冲突。不影响核心功能，但会打印 warnings。

2. **首次渲染慢**：Remotion 首次渲染需要下载 Chrome Headless Shell（~113MB）和 webpack 打包，约 3-5 分钟。后续渲染会缓存（显示 "⚡️ Cached bundle"）。

3. **HyperFrames 缓存**：首次使用 HyperFrames 时 npx 需要下载包，约 30-60s。运行 `npx --yes hyperframes --version` 可预热。

4. **pip 的源**：如果在中国大陆，pip 可能会自动使用阿里云镜像（`mirrors.aliyun.com`），无需额外配置。

5. **Windows 路径**：项目使用 PosixPath 风格路径，remotion-composer 内的 `file://` URI 在 Windows 上需要额外斜杠处理（`file:///C:/...`）。该问题已在 commit `9c9b1be` 中修复。

### 架构要点

- **AI Agent 是核心智能**：OpenMontage 不是一个传统 CLI 工具，它是"AI 代理驱动的视频生产系统"。所有创作决策由 AI 读取 YAML 流水线定义和 Markdown 技能文档后驱动 Python 工具执行。
- **三层指令体系**：
  - Layer 1 (`tools/`)：什么工具存在、可用、成本
  - Layer 2 (`skills/`)：如何用这些工具做流水线
  - Layer 3 (`.agents/skills/`)：供应商 API 的提示词工程和参数优化
- **三大渲染引擎并行**：FFmpeg（纯剪辑）、Remotion（React 动画合成）、HyperFrames（HTML/CSS/GSAP 合成），`video_compose` 自动路由。
- **流水线必须遵守**：所有视频生产必须通过流水线系统（`pipeline_defs/*.yaml`），不能直接调用 API。

### 如何开始创作

详情见 `AGENT_GUIDE.md` → Rule Zero。大致流程：

1. 告诉 AI "做一个关于 X 的视频"
2. AI 选择流水线 → 运行预检 → 展示能力菜单
3. AI 提交概念方案和制作计划 → 用户批准
4. 按阶段执行：研究 → 提案 → 剧本 → 场景规划 → 资产生成 → 剪辑 → 合成
5. 每个阶段有审核和人工确认点

### 开发推荐

- 阅读 `AGENT_GUIDE.md` —— 这是完整的操作说明书
- 阅读 `PROJECT_CONTEXT.md` —— 架构概览
- 阅读具体流水线的 `pipeline_defs/<pipeline>.yaml` 了解流程
- 对每个流水线阶段，阅读对应的 `skills/pipelines/<pipeline>/<stage>-director.md`
