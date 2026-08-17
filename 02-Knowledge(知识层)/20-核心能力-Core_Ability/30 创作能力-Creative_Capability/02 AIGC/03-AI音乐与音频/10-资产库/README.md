# 10-资产库

管理可复用声音资产及其索引。

资产库按能力领域组织，不再混合“内容类型”和“文件形态”两个分类维度。

## 目录规范

```text
10-资产库/

├─ 01-Music
│  ├─ BGM
│  ├─ Reference
│  └─ Presets
│
├─ 02-Voice
│  ├─ Character-Voice
│  ├─ Voice-Profile
│  ├─ Reference
│  └─ Presets
│
├─ 03-SFX
│  ├─ Environment
│  ├─ Foley
│  ├─ UI
│  └─ Presets
│
└─ 04-Shared
   ├─ Samples
   ├─ Metadata
   └─ License
```

## 存储规则

GitHub 保存：

- 元数据
- Prompt
- 参数
- 许可证信息
- 小型样例

大型文件：

- WAV
- FLAC
- 模型权重
- 大型素材包

优先存放外部资产盘/NAS，并在此保存索引。

## 与实验室关系

```text
实验生成
→ 08-实验室-Lab

验证成功
→ 进入资产库

形成生产链
→ 07-工作流
```
