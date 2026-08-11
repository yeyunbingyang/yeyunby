# -*- coding: utf-8 -*-
import glob, os, sys
sys.stdout.reconfigure(encoding='utf-8')
base = r"02-Knowledge(知识层)/20-核心能力-Core_Ability/30 创作能力-Creative_Capability/02 AIGC/01-AI绘画与图像/20-丝袜商品效果图生成"

replacements = {
    "单产品丝袜格子图-SOP": "锁商品丝袜格子图-SOP",
    "多效果分类格子图-SOP": "分类批量丝袜格子图-SOP",
}

changed_files = 0
for p in glob.glob(base + "/**/*.md", recursive=True):
    with open(p, encoding='utf-8') as f:
        t = f.read()
    new_t = t
    for old, new in replacements.items():
        new_t = new_t.replace(old, new)
    if new_t != t:
        with open(p, 'w', encoding='utf-8') as f:
            f.write(new_t)
        rel = p.replace('\\', '/').replace(base + '/', '')
        print("更新:", rel)
        changed_files += 1

print("共更新", changed_files, "个文件")
