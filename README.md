# Interview Prep Coach

> **A Claude Cowork Skill** — your personal adaptive tutor for software-engineering interviews.  
> Drop it into any Cowork project, type `start prep`, and get a structured, daily-coached 8-week plan that adapts as you go.

![Demo](https://github.com/saurav4geeks/interview-prep-coach/raw/main/assets/demo.gif)

---

## Features

| | Feature | What it does |
|---|---|---|
| 🎯 | **Role-specific tracks** | Backend (DSA → LLD → HLD), Frontend (DSA in JS/TS → React → FSD), or Fullstack |
| 📅 | **Adaptive daily sessions** | Brief → real LeetCode problem → hint ladder → silent auto-log |
| 🪜 | **5-step hint ladder** | Nudge → Direction → Pattern reveal → Walkthrough → Full reveal + timed rewrite |
| 📊 | **Bi-weekly assessments** | Timed, hint-free mock on Days 14/28/42/56 — scores feed back into the plan |
| 📁 | **Autonomous tracking** | Claude reads/writes your local files directly — no connectors, no paste steps |
| 🔁 | **Spaced repetition** | Weak topics resurface 3–5 days later with fresh same-pattern problems |
| 📈 | **SDE1 / SDE2 / SDE3 leveling** | Difficulty adapts to your target; promotes/demotes on assessment scores |
| ⏰ | **Proactive pings** | Cowork Scheduled Task fires your daily brief at your chosen time |

---

## Quick start

### 1 — Install the skill

Download [`interview-prep-coach.skill`](https://github.com/saurav4geeks/interview-prep-coach/releases/latest) from the latest release and install via **Settings → Skills → Install from file**.

### 2 — Open a Cowork project

Create or open any project (e.g. "Prep").

### 3 — Run setup

```
start prep
```

Claude asks 4 questions (role, target level, timeline, daily time) and bootstraps your `Interview-Prep/` folder.

### 4 — Daily sessions

```
brief me
```

Or set up a Scheduled Task so your brief fires automatically each morning.

---

## Session commands

| Command | What happens |
|---|---|
| `start prep` | First-run setup interview |
| `brief me` / `what's today` | Daily briefing + today's problem |
| `available` | Full session |
| `partial` | Compressed session — still counts, streak intact |
| `rest` | Log rest day, shift schedule +1, no guilt |
| `re-eval` | Re-planning dialogue — triage, extend, or intensify |
| `hint` | Next rung on the ladder (up to 5 levels) |
| `mock` / `test me` | Bi-weekly assessment mode |
| `where am I` | Progress overview |

---

## Problem bank

168 curated problems across 25 patterns, tagged by sheet membership:

| Tag | Sheet |
|---|---|
| **B75** | Blind 75 |
| **NC150** | NeetCode 150 |
| **S250** | Striver's SDE Sheet |
| **L79** | Striver's Last Moment 79 |

Includes JS/TS DSA gotchas + 4 pre-built mock assessment sets.

---

## Tracking files

Claude reads and writes these files directly at session end — no connectors required:

```
Interview-Prep/
├── tracker.csv          # date-mapped sessions: status, time, problem, rating, notes
├── progress.md          # streak, completion %, level, weak areas, next-up
├── mastery.md           # per-topic confidence: new → building → solid → mastered
└── weekly-reviews.md    # weekend debrief entries
```

---

## Repo layout

```
interview-prep-coach/              <- repo root
├── README.md
├── assets/
│   └── demo.gif
├── interview-prep-coach/          <- Cowork edition
│   ├── SKILL.md
│   ├── assets/                    <- templates copied on first run
│   ├── scripts/
│   └── references/
│       ├── tutor-system.md
│       ├── leetcode-bank.md
│       ├── dsa-patterns.md
│       ├── curriculum.md
│       ├── hld-framework.md
│       ├── lld-framework.md
│       ├── frontend-patterns.md
│       ├── frontend-system-design.md
│       └── frontend-curriculum.md
└── interview-prep-coach-free/     <- free-plan edition (Google Sheets tracking)
```

---

## Target bar

**Backend (SDE-2):** LeetCode mediums fluently + hards with hints · 45-min HLD with tradeoffs · Clean LLD with SOLID · Thinking out loud.

**Frontend (mid-level):** Mediums in JS/TS · Event loop, closures, React reconciliation cold · 45-min FSD with component architecture + performance tradeoffs · Accessible component APIs.

**Fullstack:** Meet both bars — identify which side is being tested per round and bring the right depth.

---

## Built with

- [Claude Cowork](https://claude.ai) — skill runner
- Claude — powers every session
- Local file I/O — zero-connector tracking
- Cowork Scheduled Tasks — proactive daily pings

---

## License

MIT
