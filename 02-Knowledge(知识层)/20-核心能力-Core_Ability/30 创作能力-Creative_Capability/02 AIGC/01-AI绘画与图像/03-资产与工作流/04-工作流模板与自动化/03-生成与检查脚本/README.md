---
title: 生成与检查脚本说明
status: 稳定
status_cn: 使用中
maturity: usable
maturity_cn: 可用
tags:
- README
- 资产管理
created: 2026-08-05
updated: 2026-08-05
summary: 生成与检查脚本说明的说明、索引或生产记录。
domain: Core_Ability
content_type: readme
scope: asset
---

# 生成与检查脚本

只存放跨项目可复用脚本。脚本生成的报告进入 `90-维护与归档/`，项目专属脚本保留在项目目录。
## 资产层健康检查

```bash
python 资产层健康检查.py "03-资产与工作流" --output 资产健康检查结果.json
```

检查元数据、Markdown 相对链接、JSON、重复哈希和 Windows 路径长度。脚本只读业务资产，仅写入指定结果文件。
