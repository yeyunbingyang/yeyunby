# AGENTS.md

This file provides guidance to Codex (Codex.ai/code) when working with code in this repository.

## Project overview

This is an Obsidian-based personal knowledge management vault (知识库). All content is Chinese-language Markdown with YAML frontmatter. There is no build step, no test suite, no linting — the "code" is the notes themselves.

## Repository structure (6-layer architecture)

```
MOC知识地图.md              # Top-level navigation — read this first
00-System(支撑层)/          # Meta-rules, templates, workflows, dashboards
   ├── Rules/               # Naming conventions, tag system, clearance rules
   ├── Templates/           # 6 note templates (+ 1 in 02-Daily)
   ├── Runtime_Data/        # Project/skill dashboards, note statistics
   └── SCHEMA.md            # Frontmatter specification
01-Inbox(入库层)/           # Transient holding area — target: empty daily
02-Daily(日志规划层)/       # Daily notes, weekly reviews, phase plans
03-Knowledge(知识层)/       # Core knowledge organized into 3 domains:
   ├── 10-IT技术-IT_Technology/
   ├── 30-认知层-Cognition/
   └── 20-核心能力-Core_Ability/
04-Resources(资源层)/       # 外部资源（GitHub项目、软件工具、课程、网站、素材、AI）
05-Trends(趋势层)/          # Tech trend tracking (monthly/yearly/GitHub/radar)
06-Archive(归档层)/         # Stale content, preserved but not maintained
```

## Key architectural patterns

- **MOC (Map of Content)**: Each domain has a `领域名-MOC.md` that serves as a navigational index. MOCs only link and summarize — they don't contain long-form content. When a MOC accumulates 10+ links on a topic, split out a sub-MOC.
- **Frontmatter**: Every knowledge note requires YAML frontmatter per `00-System(支撑层)/SCHEMA.md`. Critical field: `summary` (one-sentence conclusion, not a description of what the note "is about"). `status` flows: `计划 → 草稿 → 稳定`, with `改进` for revisions and `归档` for retirement.
- **Domain values**: `IT_Technology`, `Cognition`, `Core_Ability` — these are the only valid `domain` frontmatter values.
- **Naming**: Chinese with hyphens as separators. No dates in filenames. No spaces. MOC files end in `-MOC.md`. Templates end in `-模板.md`.
- **Templater**: Templates use Templater syntax (`<% tp.date.now("...") %>`). Do not replace these with hardcoded dates.
- **Dataview**: MOCs use Dataview queries to auto-aggregate notes by status/domain/tags. Query syntax references `KnowledgeBase/` as the vault root in FROM clauses.

## Editing conventions

- Internal links use `[[wikilink]]` syntax, not Markdown links.
- When creating a new knowledge note, always: (1) add frontmatter, (2) link it back to the relevant MOC.
- When adding a note to a MOC, update both the MOC's link list AND its Dataview query if applicable.
- The `02-Daily(日志规划层)/日记-模板.md` and `00-System(支撑层)/Templates/日记-模板.md` must stay in sync — any change to one applies to the other.
- Archive before deleting: move to `06-Archive/`, change status to `归档`, optionally leave a redirect comment at the old location.

## Current state

- **运维云原生** is the most developed domain (7 modules, ~60 notes, most lacking frontmatter — they are task-driven practical guides).
- **认知层** and **核心能力** are skeletons: MOCs exist but contain few or no actual knowledge notes.
- The 复盘 (retrospective) system was recently integrated: KPT for daily/weekly, GRAI for phases, PDCA for system-level meta-review. See `03-Knowledge/30-认知层-Cognition/03-学习方法论/复盘指南.md`.
- `MOC知识地图.md` is the single source of truth for the overall directory tree — keep it current when adding or reorganizing directories.
