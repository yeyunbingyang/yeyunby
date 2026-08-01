#!/usr/bin/env python3
"""规范化语义提示点，并生成定点抽帧计划。"""

from __future__ import annotations

import argparse
import json
from pathlib import Path


OFFSETS = (-1.0, 0.0, 1.5)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("input", type=Path, help="提示点 JSON 文件")
    parser.add_argument("--output", type=Path, required=True, help="输出计划 JSON")
    parser.add_argument("--merge-window", type=float, default=3.0, help="相邻提示点合并秒数")
    args = parser.parse_args()

    cues = json.loads(args.input.read_text(encoding="utf-8"))
    kept = []
    priority_rank = {"P0": 0, "P1": 1, "P2": 2}
    for cue in sorted(cues, key=lambda item: float(item["timestamp"])):
        cue["timestamp"] = float(cue["timestamp"])
        cue.setdefault("priority", "P1")
        if cue["priority"] == "P2":
            continue
        if kept and cue["timestamp"] - kept[-1]["timestamp"] <= args.merge_window:
            if priority_rank[cue["priority"]] < priority_rank[kept[-1]["priority"]]:
                kept[-1] = cue
            else:
                kept[-1].setdefault("merged_reasons", []).append(cue.get("reason", ""))
            continue
        kept.append(cue)

    timestamps = sorted({
        round(max(0.0, cue["timestamp"] + offset), 3)
        for cue in kept
        for offset in OFFSETS
    })
    result = {"cues": kept, "timestamps": timestamps}
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    print(",".join(str(value) for value in timestamps))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
