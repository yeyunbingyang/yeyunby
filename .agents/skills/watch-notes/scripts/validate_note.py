#!/usr/bin/env python3
"""验证 watch-notes 单篇笔记及其图片附件。"""

from __future__ import annotations

import argparse
import re
from pathlib import Path

from PIL import Image


OBSIDIAN_PATTERN = re.compile(r"!\[\[([^|\]]+)(?:\|[^\]]+)?\]\]")
MARKDOWN_PATTERN = re.compile(r"!\[[^\]]*\]\(([^)]+)\)")
FRAME_PATTERN = re.compile(r"KF-(\d{3})_(\d{2})-(\d{2})-(\d{2})\.jpe?g$", re.I)


def frame_key(path: Path) -> tuple[int, int]:
    match = FRAME_PATTERN.search(path.name)
    if not match:
        raise ValueError(f"附件命名不合法：{path.name}")
    number, hour, minute, second = map(int, match.groups())
    return number, hour * 3600 + minute * 60 + second


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("note", type=Path)
    parser.add_argument("--mode", choices=("obsidian", "markdown"), default="obsidian")
    args = parser.parse_args()

    note = args.note.resolve()
    errors: list[str] = []
    if not note.is_file():
        print(f"错误：笔记不存在：{note}")
        return 1

    text = note.read_text(encoding="utf-8")
    if text.count("%% watch-notes:start %%") != 1 or text.count("%% watch-notes:end %%") != 1:
        errors.append("托管区块标记必须各出现一次")

    pattern = OBSIDIAN_PATTERN if args.mode == "obsidian" else MARKDOWN_PATTERN
    links = pattern.findall(text)
    if len(links) != len(set(links)):
        errors.append("存在重复图片嵌入")

    referenced: list[Path] = []
    for link in links:
        target = (note.parent / link.replace("/", "\\")).resolve()
        referenced.append(target)
        if not target.is_file():
            errors.append(f"图片不存在：{link}")
            continue
        try:
            with Image.open(target) as image:
                image.verify()
        except Exception as exc:
            errors.append(f"图片无法解码：{link}（{exc}）")

    generated = sorted((note.parent / "附件").glob("KF-*.jpg")) if (note.parent / "附件").exists() else []
    orphaned = set(generated) - set(referenced)
    if orphaned:
        errors.append("存在未引用的生成图片：" + "、".join(path.name for path in orphaned))

    try:
        keys = [frame_key(path) for path in referenced]
        numbers = [key[0] for key in keys]
        times = [key[1] for key in keys]
        if numbers != list(range(1, len(numbers) + 1)):
            errors.append("图片编号不是从 001 开始连续递增")
        if times != sorted(times):
            errors.append("图片时间戳未递增")
    except ValueError as exc:
        errors.append(str(exc))

    if errors:
        for error in errors:
            print(f"错误：{error}")
        return 1
    print(f"通过：{note}，共 {len(referenced)} 张图片")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
