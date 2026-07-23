---
title: 产品发布会开场视频 — Remotion 项目使用文档
domain: Core_Ability
tags: [Vibe Coding, Remotion, 视频, 产品发布, 使用指南]
status: 稳定
created: 2026-07-17
updated: 2026-07-17
summary: "60 秒产品发布会开场视频的完整使用说明——项目结构、自定义修改、渲染流程、常见问题。Vibe Coding 产出：用 remotion 生成的专业级视频项目。"
---

# 产品发布会开场视频 — 使用文档

> **提示**："用 remotion 做一个 60 秒的产品发布会开场视频：0-5s LOGO 淡入（发光粒子）→5-20s 3 个数据动效→20-45s 功能 3D 翻转→45-55s 评价轮播→55-60s CTA，深蓝+青色配色"
>
> 这是用 remotion 的 Vibe Coding 场景直接生成的项目。以下是如何使用、修改和渲染它。

---

## 项目信息

| 项目 | 值 |
|------|----|
| **项目路径** | `01 AI工具\03 vibe coding\product-launch-video\` |
| **技术栈** | Remotion v4 + React + TypeScript |
| **视频时长** | 60 秒 |
| **帧率** | 30 fps |
| **分辨率** | 1920 × 1080（Full HD） |
| **总帧数** | 1800 帧 |
| **配色方案** | 深蓝 `#0A1628`（主色）+ 青色 `#00D4FF`（强调色） |
| **代码总量** | 9 个文件，~400 行 TypeScript/React |

---

## 快速启动

```bash
# 进入项目目录
cd "X:\KMS\yeyunby\02-Knowledge(知识层)\20-核心能力-Core_Ability\10 技术能力-Technical_Capability\01 AI工具\03 vibe coding\product-launch-video"

# 如果 node_modules 不存在，先安装依赖
npm install

# 启动 Remotion Studio 预览（浏览器打开）
npx remotion studio

# 渲染完整视频
npx remotion render ProductLaunch out/video.mp4

# 渲染单个帧测试
npx remotion render ProductLaunch out/frame.png --frames=30
```

---

## 视频结构（5 段编排）

### 第 1 段：LOGO 开场（0-5s，帧 0-150）

**文件**：`src/segments/LogoIntro.tsx`

- **效果**：LOGO 文字从中心弹性缩放出现，带青色光晕，背景有径向渐变。副标题 "PRODUCT LAUNCH" 在末尾淡入。
- **动画**：`spring()` 弹性缓动 + `interpolate()` 渐入
- **Props**：`logoText`（LOGO 文字）、`accentColor`（光晕颜色）

**自定义修改示例**：
```
把 LogoIntro.tsx 中的 "PRODUCT LAUNCH" 改成你的副标题
把 spring config 的 damping 从 10 改到 8 让弹跳更明显
```

### 第 2 段：数据动效（5-20s，帧 150-600）

**文件**：`src/segments/DataAnimations.tsx`

- **效果**：分 3 个子段展示（每 5 秒切换）
  - 帧 150-300：4 个柱状图从底部弹出（用户增长/营收/城市/满意度）
  - 帧 300-450：增长曲线图（SVG path 绘制）
  - 帧 450-600：城市覆盖地图布局
- **数据**：`bars` 数组中的预设数据

**自定义修改示例**：
```
// 修改 DataAnimations.tsx 中的数据
var bars = [
  { h: 90, l: '用户增长', v: '2.5M' },
  { h: 75, l: '营收增长', v: '180%' },
  // ...添加你自己的数据
];
```

### 第 3 段：功能展示（20-45s，帧 600-1350）

**文件**：`src/segments/ProductFeatures.tsx`

- **效果**：6 个功能卡片分 2 行展示，每 12.5 秒出现一个。卡片有 3D 翻转 `rotateY(90deg → 0deg)` 进场动画，带青色边框和阴影。
- **布局**：3 列 × 2 行，每个卡片 500×280px
- **数据**：`features` 数组（标题 + 描述 + 图标 emoji）

**自定义修改示例**：
```
// 修改 ProductFeatures.tsx 中的功能列表
var features = [
  { title: '你的功能名', desc: '一句话描述', icon: '🚀' },
  // ...改为你的 6 个功能
];

// 调整进场速度：i * 125 中的 125 改大变慢、改小变快
```

### 第 4 段：客户评价（45-55s，帧 1350-1650）

**文件**：`src/segments/Testimonials.tsx`

- **效果**：5 条评价依次轮播，每 10 秒切换一条。每条从右侧滑入，停留，再淡出下一条。带引号装饰和分隔线。
- **数据**：`tdata` 数组（评价文字 + 作者 + 角色数据）

**自定义修改示例**：
```
// 修改 Testimonials.tsx 中的评价
var tdata = [
  { text: '你的客户评价', author: '姓名 · 职位', role: '关键数据' },
  // ...改为真实的评价
];
```

### 第 5 段：CTA 结尾（55-60s，帧 1650-1800）

**文件**：`src/segments/CTA.tsx`

- **效果**：公司名从顶部淡入 → Slogan 弹性放大（带青色光晕）→ "立即体验" 按钮渐入
- **Props**：`companyName`、`slogan`、`accentColor`

**自定义修改示例**：
```
// 在 Root.tsx 中修改 Props 默认值
defaultProps={{
  companyName: "你的公司名",
  logoText: "LOGO",
  slogan: "你的口号",
  accentColor: "#00D4FF",  // 改为你的品牌色
}}
```

---

## 自定义指南

### 修改颜色和品牌

在 `src/Root.tsx` 中修改 `defaultProps`：

```tsx
defaultProps={{
  companyName: "Acme Inc",         // 公司名称
  logoText: "ACME",               // LOGO 文字
  slogan: "让世界更智能",          // 品牌口号
  primaryColor: "#0A1628",        // 背景主色
  accentColor: "#00D4FF",         // 强调色（光晕/边框/按钮）
}}
```

### 修改视频时长/帧率

在 `src/Root.tsx` 中修改 `Composition` 参数：

```tsx
<Composition
  durationInFrames={1800}    // 60s × 30fps = 1800
  fps={30}                   // 改成 24 或 60
  width={1920}
  height={1080}
/>
```

### 修改数据

直接修改 segment 文件中的数据数组。所有数据都是常量数组，找到后替换即可。

### 添加新段落

在 `src/ProductLaunch.tsx` 中添加新的 `<Sequence>`：

```tsx
<Sequence from={1800} durationInFrames={300}>
  <YourNewSegment accentColor={accentColor} />
</Sequence>
```

然后在 `src/segments/` 中创建对应的组件文件。

### 预览单帧

```bash
# 渲染第 1 秒（帧 30）
npx remotion render ProductLaunch out/frame-01.png --frames=30

# 渲染第 10 秒（帧 300）
npx remotion render ProductLaunch out/frame-10.png --frames=300

# 渲染多个帧对比
npx remotion render ProductLaunch out/frame-%03d.png --frames=30-150-300-600-1350
```

---

## 渲染完整视频

```bash
# 默认渲染（MP4）
npx remotion render ProductLaunch out/video.mp4

# 高质量渲染
npx remotion render ProductLaunch out/video.mp4 --quality=100

# 指定编码器（更快）
npx remotion render ProductLaunch out/video.mp4 --codec=h264

# 缩略图比例渲染（快速测试）
npx remotion render ProductLaunch out/video.mp4 --scale=0.5
```

---

## 常见问题

### node_modules 缺失怎么办

```bash
cd "产品发布会视频项目路径"
npm install
```

如果 npm install 报错，尝试：
```bash
npm install --legacy-peer-deps
```

### 渲染很慢

- 先用小分辨率测试：`--scale=0.25`
- 用 `--frames=0-300` 只渲染前 10 秒试看
- 关闭 Remotion Studio，直接用 CLI 渲染

### 如何导出 GIF

```bash
npx remotion render ProductLaunch out/output.gif --codecy=gif
```

### 如何调整动画速度

每个 segment 文件中的 `spring()` config 控制弹性效果：

```tsx
// damping 越小弹跳越明显（默认 10-15）
spring({ frame: f, fps: 30, config: { mass: 0.5, damping: 10 } })

// mass 越大动画越慢（默认 0.5-0.8）
spring({ frame: f, fps: 30, config: { mass: 0.8, damping: 12 } })
```

### 如何添加背景音乐

在 `src/ProductLaunch.tsx` 中添加 `<Audio>` 组件：

```tsx
import { Audio } from "remotion";
import music from "./assets/background.mp3";

// 在 AbsoluteFill 内添加
<Audio src={music} volume={0.3} />
```

---

## 文件清单

| 文件 | 作用 | 行数 | 修改频率 |
|------|------|------|---------|
| `src/Root.tsx` | 注册视频、设置默认 Props | 22 | 每次修改品牌信息 |
| `src/ProductLaunch.tsx` | 5 段 Sequence 编排 | 34 | 增减段落时 |
| `src/segments/LogoIntro.tsx` | LOGO 开场动画 | 43 | 替换 LOGO 时 |
| `src/segments/DataAnimations.tsx` | 数据可视化 | 93 | 更换数据时 |
| `src/segments/ProductFeatures.tsx` | 功能卡片 | 58 | 修改功能列表时 |
| `src/segments/Testimonials.tsx` | 客户评价 | 50 | 更换评价时 |
| `src/segments/CTA.tsx` | 结尾号召 | 54 | 修改口号时 |
| `package.json` | 项目配置 | 33 | 添加依赖时 |

---

## 参考

- [[Vibe Coding 视频创作场景]] — 同目录下的 vibe coding 场景列表
- [[Codex-插件与技能系统]] — Remotion 插件的完整说明
