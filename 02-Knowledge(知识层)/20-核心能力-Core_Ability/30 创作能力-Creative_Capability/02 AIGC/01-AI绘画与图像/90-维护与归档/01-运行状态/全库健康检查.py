#!/usr/bin/env python3
"""检查 AI绘画与图像知识库的 YAML、链接、JSON、Python、图片、重复文件与路径长度。"""
from pathlib import Path
from collections import defaultdict, Counter
from datetime import date
import re, json, py_compile, hashlib, tempfile

ROOT = Path(__file__).resolve().parents[2]
OUT = Path(__file__).with_name("当前健康检查.json")
OUT_DIRECTORY = Path(__file__).with_name("当前目录清单.json")
OUT_VERSION = Path(__file__).with_name("当前版本清单.json")
USER_BASE = r"X:\KMS\yeyunby\02-Knowledge(知识层)\20-核心能力-Core_Ability\30 创作能力-Creative_Capability\02 AIGC\01-AI绘画与图像"
GENERATED = date.today().isoformat()

try:
    import yaml
except Exception:
    yaml = None
try:
    from PIL import Image
except Exception:
    Image = None

result = {
    "generated": GENERATED,
    "root": str(ROOT),
    "file_count": 0,
    "markdown_count": 0,
    "image_count": 0,
    "json_count": 0,
    "python_count": 0,
    "video_count": 0,
    "yaml_errors": [],
    "markdown_relative_link_errors": [],
    "wiki_unresolved": [],
    "wiki_ambiguous": [],
    "json_errors": [],
    "python_errors": [],
    "image_errors": [],
    "duplicate_group_count": 0,
    "max_simulated_windows_path_length": 0,
}

files = [p for p in ROOT.rglob("*") if p.is_file()]
result["file_count"] = len(files)
counts = Counter(p.suffix.lower() for p in files)
result["markdown_count"] = counts[".md"]
result["image_count"] = sum(counts[x] for x in (".png", ".jpg", ".jpeg", ".webp"))
result["json_count"] = counts[".json"]
result["python_count"] = counts[".py"]
result["video_count"] = sum(counts[x] for x in (".mp4", ".mov", ".webm", ".mkv"))
result["max_simulated_windows_path_length"] = max(
    [len(USER_BASE + "\\" + str(p.relative_to(ROOT)).replace("/", "\\")) for p in files] or [0]
)

fence_re = re.compile(r"```.*?```", re.S)
relative_re = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
wiki_re = re.compile(r"!?\[\[([^\]]+)\]\]")

by_stem = defaultdict(list)
for p in files:
    by_stem[p.stem].append(p)

for p in ROOT.rglob("*.md"):
    text = p.read_text(encoding="utf-8")
    data = None
    if yaml is not None:
        if not text.startswith("---\n"):
            result["yaml_errors"].append({"path": str(p.relative_to(ROOT)), "error": "missing YAML frontmatter"})
        else:
            end = text.find("\n---\n", 4)
            if end < 0:
                result["yaml_errors"].append({"path": str(p.relative_to(ROOT)), "error": "unclosed YAML frontmatter"})
            else:
                try:
                    data = yaml.safe_load(text[4:end])
                    if not isinstance(data, dict):
                        raise ValueError("frontmatter is not a mapping")
                except Exception as e:
                    result["yaml_errors"].append({"path": str(p.relative_to(ROOT)), "error": str(e)})

    # 历史归档保留当时的原始链接，仅校验当前活动笔记的导航。
    if isinstance(data, dict) and data.get("status") == "归档":
        continue

    visible = fence_re.sub("", text)
    for raw in relative_re.findall(visible):
        target = raw.strip().split("#", 1)[0]
        if not target or target.startswith(("http://", "https://", "mailto:", "#", "data:")):
            continue
        if target.startswith("<") and target.endswith(">"):
            target = target[1:-1]
        if not (p.parent / target).exists():
            result["markdown_relative_link_errors"].append({"source": str(p.relative_to(ROOT)), "target": target})

    for raw in wiki_re.findall(visible):
        raw = raw.replace("\\|", "|")
        target = raw.split("|", 1)[0].split("#", 1)[0].strip()
        if not target:
            continue
        candidates = []
        variants = []
        if target.startswith(("./", "../")):
            variants.append((p.parent / target).resolve())
        elif "/" in target or "\\" in target:
            normalized = target.replace("\\", "/")
            variants.extend([ROOT / normalized, p.parent / normalized])
        else:
            candidates = list(by_stem.get(target, [])) or list(by_stem.get(Path(target).stem, []))
        for v in variants:
            if v.exists():
                candidates.append(v)
            if not v.suffix:
                for ext in (".md", ".png", ".jpg", ".jpeg", ".webp", ".json", ".py", ".mp4"):
                    if v.with_suffix(ext).exists():
                        candidates.append(v.with_suffix(ext))
        unique = []
        seen = set()
        for c in candidates:
            key = str(c.resolve())
            if key not in seen:
                seen.add(key)
                unique.append(c)
        if not unique:
            result["wiki_unresolved"].append({"source": str(p.relative_to(ROOT)), "target": target})
        elif len(unique) > 1 and "/" not in target and "\\" not in target:
            result["wiki_ambiguous"].append({
                "source": str(p.relative_to(ROOT)),
                "target": target,
                "matches": [str(x.relative_to(ROOT)) for x in unique],
            })

for p in ROOT.rglob("*.json"):
    if p == OUT:
        continue
    try:
        json.loads(p.read_text(encoding="utf-8"))
    except Exception as e:
        result["json_errors"].append({"path": str(p.relative_to(ROOT)), "error": str(e)})

for p in ROOT.rglob("*.py"):
    if p.resolve() == Path(__file__).resolve():
        continue
    try:
        tmp = Path(tempfile.gettempdir()) / (hashlib.md5(str(p).encode()).hexdigest() + ".pyc")
        py_compile.compile(str(p), doraise=True, cfile=str(tmp))
    except Exception as e:
        result["python_errors"].append({"path": str(p.relative_to(ROOT)), "error": str(e)})

if Image is not None:
    for p in files:
        if p.suffix.lower() in {".png", ".jpg", ".jpeg", ".webp"}:
            try:
                with Image.open(p) as im:
                    im.verify()
            except Exception as e:
                result["image_errors"].append({"path": str(p.relative_to(ROOT)), "error": str(e)})

excluded_hash = {"当前目录清单.json", "当前健康检查.json", "当前版本清单.json"}
hash_groups = defaultdict(list)
for p in files:
    if p.name in excluded_hash:
        continue
    hash_groups[hashlib.sha256(p.read_bytes()).hexdigest()].append(p)
result["duplicate_group_count"] = sum(1 for group in hash_groups.values() if len(group) > 1)

OUT.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")

version = {
    "version": "2026.08.08-simplified-structure-v1",
    "generated": GENERATED,
    "base": "2026.08.06-five-part-canonical-v1",
    "changes": [
        "根 MOC 作为唯一总入口",
        "提示词活动正文收敛为七篇",
        "资产与工作流入口和规范并入 MOC",
        "实验方法与模板收敛为单篇权威正文",
        "历史拆分版集中归档",
        "Frontmatter、标题、链接和附件完成全量校验",
        "CURRENT、目录清单、版本清单和健康检查同步更新",
    ],
    "canonical_template": "01-提示词/01-通用提示词模板.md",
    "standard": "01-提示词/06-提示词设计与失败排查.md",
    "health_file": "当前健康检查.json",
    "change_log": "../03-发布与变更记录/2026/2026-08-08-目录简化实施与验证记录.md",
    "counts": {
        "file_count": result["file_count"],
        "markdown_count": result["markdown_count"],
        "image_count": result["image_count"],
        "json_count": result["json_count"],
        "python_count": result["python_count"],
        "video_count": result["video_count"],
    },
}
OUT_VERSION.write_text(json.dumps(version, ensure_ascii=False, indent=2), encoding="utf-8")

# 目录清单包含自身大小，重复计算直至输出稳定。
for _ in range(5):
    current_files = sorted((p for p in ROOT.rglob("*") if p.is_file()), key=lambda p: p.relative_to(ROOT).as_posix())
    directory = {
        "generated": GENERATED,
        "file_count": len(current_files),
        "files": [
            {"path": p.relative_to(ROOT).as_posix(), "size": p.stat().st_size}
            for p in current_files
        ],
    }
    content = json.dumps(directory, ensure_ascii=False, indent=2)
    if OUT_DIRECTORY.exists() and OUT_DIRECTORY.read_text(encoding="utf-8") == content:
        break
    OUT_DIRECTORY.write_text(content, encoding="utf-8")

summary = {k: len(v) if isinstance(v, list) else v for k, v in result.items()}
print(json.dumps(summary, ensure_ascii=False, indent=2))
