---
title: Obsidian Markdown 语法参考
description: Obsidian 风味 Markdown 语法完整指南——wikilinks、embeds、callouts、properties、comments 等扩展语法
aliases:
  - obsidian-markdown
  - Obsidian 风味 Markdown
tags:
  - obsidian
  - markdown
  - syntax
  - reference
created: 2026-07-23
updated: 2026-07-23
status: 稳定
domain: Core_Ability
source: kepano/obsidian-skills (obsidian-markdown)
summary: "Obsidian 扩展 Markdown 语法的完整参考——wikilinks、embeds、callouts、frontmatter properties、tags、comments、数学公式、Mermaid 图表等。"
related: []
verified: 2026-07-25
review_after: 2026-10-25
---

# Obsidian Markdown 语法参考

> Obsidian 扩展了 CommonMark/GFM。本手册仅覆盖 Obsidian 特有语法，标准 Markdown 为前置知识。

---

## 1. 内部链接 (Wikilinks)

```markdown
[[笔记名]]
[[笔记名|显示文字]]
[[笔记名#标题]]          链接到标题
[[笔记名#^块ID]]         链接到块
```

定义块 ID：`这一段可以被链接。^我的块ID`

---

## 2. 嵌入 (Embeds)

```markdown
![[笔记名]]               嵌入完整笔记
![[笔记名#标题]]           嵌入特定段落
![[图片.png|300]]         指定宽度
![[文档.pdf#page=3]]      嵌入 PDF 指定页
![[Base.base#视图名]]      嵌入 Base 视图
```

搜索嵌入：

````markdown
```query
tag:#project status:done
```
````

---

## 3. Callouts (提示框)

```markdown
> [!note]          基础
> [!warning] 标题   自定义标题
> [!faq]-           默认折叠（`-` 折叠，`+` 展开）
```

| 类型 | 别名 |
|------|------|
| `note` | — |
| `abstract` | summary, tldr |
| `info` | — |
| `tip` | hint, important |
| `success` | check, done |
| `question` | help, faq |
| `warning` | caution, attention |
| `failure` | fail, missing |
| `danger` | error |
| `bug` | — |
| `example` | — |
| `quote` | cite |

### 嵌套

```markdown
> [!question] 外层
> > [!note] 内层
> > 嵌套内容
```

---

## 4. 属性 (Frontmatter)

```yaml
---
title: 我的笔记
date: 2024-01-15
tags: [project, active]
aliases: [别名]
cssclasses: [custom-class]
---
```

| 类型 | 示例 |
|------|------|
| 文本 | `title: My Title` |
| 数字 | `rating: 4.5` |
| 布尔 | `completed: true` |
| 日期 | `date: 2024-01-15` |
| 列表 | `tags: [one, two]` |
| 链接 | `related: "[[Other Note]]"` |

---

## 5. 标签

```markdown
#标签
#嵌套/标签
```

---

## 6. 注释

```markdown
这是可见 %%但这是隐藏的%% 文字。
%%
整块隐藏
%%
```

---

## 7. 其他语法

```markdown
==高亮文字==

内联公式：$e^{i\pi} + 1 = 0$

块公式：
$$
\frac{a}{b} = c
$$

脚注[^1]。
[^1]: 内容。
内联脚注。^[这是内联。]
```

---

## 参考链接

- [Obsidian Flavored Markdown](https://help.obsidian.md/obsidian-flavored-markdown)
- [内部链接](https://help.obsidian.md/links)
- [嵌入文件](https://help.obsidian.md/embeds)
- [Callouts](https://help.obsidian.md/callouts)
