# Interview Prep Coach — a Claude Skill

An adaptive **personal tutor + trainer** for software-engineering interview prep, built as a [Claude Skill](https://www.anthropic.com/news/skills). Supports **Backend, Frontend, and Fullstack** roles. Runs a structured multi-week plan with real LeetCode problems, debriefs every problem like a tutor, resurfaces weak topics with spaced-repetition variants, runs bi-weekly mock assessments, handles rest days, and re-plans itself when you fall behind.

Two editions — pick the one that matches your plan:

| | Cowork edition | Free-plan edition |
|--|---------------|-------------------|
| **Needs** | Claude Cowork (Desktop, paid) | Any Claude plan + Google Sheets connector |
| **Tracking** | Local files (auto read/write) | Google Sheet (5-tab tracker, auto read/write) |
| **Proactive ping** | Cowork Scheduled Task | Phone reminder → open Claude → "brief me" |
| **Folder** | `interview-prep-coach/` | `interview-prep-coach-free/` |

---

## What it does (both editions)

- **Role-aware from day one** — the setup interview asks if you're targeting Backend, Frontend, or Fullstack. The curriculum, session types, and assessments branch accordingly.
- **Daily sessions sized to your life** — short weekday sessions, longer weekend blocks. Tells you exactly what to do today: one pattern + one specific LeetCode problem (by name, number, and link).
- **Guided solving, not answer-dumping** — a hint ladder that escalates only when you're stuck, mirroring a real interview.
- **Diagnostic debrief** — after each problem, a few quick questions (how did it land? where was the friction?) calibrate difficulty and coaching focus.
- **Spaced-repetition variants** — shaky on a pattern? A *different* problem of the same pattern is queued a few days later.
- **Bi-weekly mock assessments** — timed, scored, logged, compared to last time.
- **Rest days** — "taking off today" shifts the plan forward, streak intact.
- **Adaptive re-planning** — fall behind and it offers triage / extend / intensify instead of guilt.

---

## Curricula at a glance

### Backend (~10 weeks)
1. **Weeks 1–5** — DSA foundations (arrays, strings, linked lists, stacks/queues, trees, binary search, graphs)
2. **Weeks 6–8** — advanced DSA (DP, heaps, intervals, greedy, backtracking, bit manipulation) + HLD depth + LLD intro
3. **Weeks 9–10** — mocks and revision

HLD problems (URL shortener, rate limiter, Twitter feed, chat system, distributed cache, etc.) sit on weekends. LLD (parking lot, BookMyShow, elevator) appears in weeks 7–8.

### Frontend (~10 weeks)
1. **Weeks 1–4** — JS/TS fundamentals (event loop, closures, async, TypeScript) + DSA in JavaScript + React core
2. **Weeks 5–7** — React advanced patterns + component architecture (compound components, state machines) + state management + CSS architecture
3. **Week 8** — performance (Core Web Vitals, bundle optimization), accessibility (WCAG, ARIA), frontend system design depth
4. **Weeks 9–10** — mocks and revision

Frontend system design problems (Typeahead, Infinite Scroll, Google Docs, Real-Time Dashboard, YouTube Player, etc.) sit on weekends. Component design (Modal, Data Table, Toast, Combobox) runs as "frontend LLD" sessions.

### Fullstack
Blends both curricula. The setup interview identifies your weaker side and tilts sessions accordingly.

---

## Install

### Cowork edition (local-file tracking)
1. Download or zip the `interview-prep-coach/` folder.
2. In Claude Cowork: **Settings → Skills → Upload**.
3. Say: **"Start my interview prep."**
   - On first run: short setup interview (role type, target, timeline, capacity, level, weak areas, start date).
   - Claude creates your `Interview-Prep/` project folder with `tracker.csv`, `progress.md`, and `mastery.md`.

**Set up the proactive ping (Cowork Scheduled Task):**

Create a Scheduled Task at your study times (e.g., weekdays 9 PM, weekends 3 PM) with this prompt:

> "Using my interview-prep-coach skill, run my daily prep brief. Read progress.md and tracker.csv in my Interview-Prep folder, figure out today's day number and topic, pick the specific LeetCode problem(s) for today (name + number + link), and lay out today's session so it's ready to start. Note my streak and whether I'm on track. If I marked a rest day or missed sessions, adjust first. End by asking: available / partial / rest / re-eval?"

Your session is prepared and waiting each day — you just show up and answer one word.

### Free-plan edition (Google Sheets tracking)
1. Install the **Google Sheets connector** in your Claude account.
2. Download or zip the `interview-prep-coach-free/` folder.
3. In Claude: **Settings → Skills → Upload**.
4. Say: **"Start my interview prep."**
   - On first run: same setup interview, then Claude creates a **"Interview-Prep-Tracker"** Google Spreadsheet with 5 tabs (Tracker, Config, Mastery, Assessments, WeeklyReviews) and writes your full day-by-day plan into it.
   - Set a daily phone reminder at your study time → open Claude → say "brief me".

---

## How it's organized

```
interview-prep-coach/               ← Cowork edition
├── SKILL.md                        # entry protocol, session types, role branching
├── assets/
│   ├── progress.md                 # dashboard template (filled at setup)
│   ├── mastery.md                  # topic mastery table
│   └── tracker.csv                 # placeholder; generated at setup
├── references/
│   ├── tutor-system.md             # methodology, tracking, assessments, rest days, re-planning
│   ├── curriculum.md               # backend 60-day week-by-week plan
│   ├── frontend-curriculum.md      # frontend 60-day week-by-week plan
│   ├── dsa-patterns.md             # DSA concept notes (templates, pitfalls, recognition signals)
│   ├── frontend-patterns.md        # JS/TS/React/browser concept notes
│   ├── hld-framework.md            # 6-step HLD framework + notes per system
│   ├── frontend-system-design.md   # 5-step FSD framework + FSD & component design notes
│   └── leetcode-bank.md            # curated real problems by topic
└── scripts/
    └── generate_schedule.py        # builds a date-mapped tracker from your start date

interview-prep-coach-free/          ← Free-plan edition (Google Sheets)
├── SKILL.md                        # same role branching, adapted for Sheets + no scheduled pings
└── references/
    ├── tutor-system.md             # same methodology, Sheets read/write instead of local files
    ├── curriculum.md               # (shared content)
    ├── frontend-curriculum.md      # (shared content)
    ├── dsa-patterns.md             # (shared content)
    ├── frontend-patterns.md        # (shared content)
    ├── hld-framework.md            # (shared content)
    ├── frontend-system-design.md   # (shared content)
    └── leetcode-bank.md            # (shared content)
```

---

## Customize

- **Change topics or problems** — edit `references/curriculum.md`, `references/frontend-curriculum.md`, or `references/leetcode-bank.md`.
- **Reshape the schedule** — edit topic sequences in `scripts/generate_schedule.py` (Cowork) or just tell Claude "swap week 3 and week 4" (free plan).
- **Change cadence** — edit your Scheduled Task prompt (Cowork) or just tell Claude your new study times (free plan, updates Config tab).

## Packaging into a `.skill`

```bash
# Zip the folder you want
zip -r interview-prep-coach.skill interview-prep-coach/
zip -r interview-prep-coach-free.skill interview-prep-coach-free/
```
Or upload the folder directly in Claude's Skills settings.

---

## Branches

- **`main`** — this generic, shareable version (personalizes itself via the setup interview).
- **`saurav-custom`** — a fully pre-configured personal instance (SDE-2 target, fixed dates/times) kept as an example of a filled-in plan.

## License

MIT — use it, fork it, make it yours.
