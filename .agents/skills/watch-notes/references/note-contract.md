# 单篇笔记输出合同

## 必须满足

- 一个视频任务只产生一篇目标笔记。
- 笔记包含 `%% watch-notes:start %%` 和 `%% watch-notes:end %%`。
- 图片只放入同名目录下的 `附件/`。
- 图片文件名为 `KF-NNN_HH-MM-SS.jpg`，按时间递增。
- 每张嵌图有相邻文字说明其用途。
- Whisper 时间戳是章节和截图定位的主索引。
- 有文稿时仅用于校正和补全表达，不能覆盖时间轴。

## Obsidian

- 图片：`![[附件/KF-001_00-01-20.jpg|720]]`
- 内部笔记：`[[笔记名]]`
- frontmatter 服从 vault 的 `SCHEMA.md`；无 schema 时至少包含 `title`、`summary`、`source`、`created`、`updated`。

## 普通 Markdown

- 图片：`![说明（00:01:20）](附件/KF-001_00-01-20.jpg)`
- 不使用 wikilink 或 Obsidian callout。

## 不允许

- 因视频较长而自动拆分多篇；
- 默认输出候选联系表；
- 用均匀抽帧代替语义判断；
- 连续堆图而不解释；
- 覆盖托管边界外的用户内容；
- 在输出中泄露 API key。
