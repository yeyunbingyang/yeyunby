---
title: "Remotion Skills 视频编程技能"
tags: [GitHub, 开源, AI, Skills, Remotion, 视频, React]
type: 工具
status: 待评估
created: 2026-07-06
updated: 2026-07-16
source: https://github.com/remotion-dev/skills
related: []
summary: "Remotion 官方 Skill——用 React/TypeScript 编程式生成视频的最佳实践，含动画/字幕/音频/3D/图表/动态时长等完整指南"
---

# Remotion Skills 视频编程技能

https://github.com/remotion-dev/skills

## 基本信息

**类型：** 工具（Skill）
**链接：** https://github.com/remotion-dev/skills
**安装：** `npx skills add remotion-dev/skills`
**适用领域：** 编程式视频生成、React 动画、视频编辑自动化
**推荐程度：** ★★★★☆
**Stars：** 未统计
**语言：** TypeScript + Markdown

## 是什么

**Remotion 官方 Skill**——指导 AI Agent 使用 Remotion（React 视频渲染库）的最佳实践。从项目脚手架到动画设计、字幕、音频、3D、图表、视觉效果、动态时长计算，全流程覆盖。

## 核心内容

### 项目脚手架
```bash
npx create-video@latest --yes --blank --no-tailwind my-video
```

### 动画原则
- 使用 `useCurrentFrame()` + `interpolate()` 驱动动画
- 优先 `interpolate()` 而非 `spring()`（除非需要物理运动）
- 使用 `Easing.bezier()` 自定义缓动
- **禁止** CSS transitions/animations——它们不会正确渲染
- **禁止** Tailwind 动画类名

### 推荐写法
```tsx
// ✅ 推荐：单独 CSS transform 属性
style={{
  scale: interpolate(frame, [0, 100], [0, 1]),
  translate: interpolate(frame, [0, 100], ["0px 0px", "100px 100px"]),
  rotate: interpolate(frame, [0, 100], ["20deg", "90deg"]),
}}

// ❌ 不推荐：组合 transform 字符串
style={{ transform: `scale(${scale})` }}
```

### 资源管理
- 资源放在 `public/` 目录
- 使用 `staticFile()` 引用
- 图片用 `<Img>` 组件，视频用 `<Video>`（来自 `@remotion/media`）
- 音频用 `<Audio>` 组件
- 支持远程 URL

### 序列与时间
- `<Sequence>` 控制时间偏移和持续时间
- `from` 参数延迟内容，`durationInFrames` 限制时长
- 内联内容使用 `layout="none"`

## 评价

- **优点**：官方维护、最佳实践权威、覆盖 Remotion 全 API
- **局限**：仅适用于 Remotion 场景
- **是否值得长期保留**：🔖 参考——有视频编程需求时使用
