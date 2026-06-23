# Interview Prep Coach — a Claude Skill

An adaptive **personal tutor + trainer** for software-engineering interview prep (DSA, LLD, HLD), built as a [Claude Skill](https://www.anthropic.com/news/skills). It runs a structured multi-week plan with real LeetCode problems, tracks your progress in local files, debriefs every problem like a tutor, resurfaces weak topics with fresh variants, runs bi-weekly mock assessments, handles rest days, and re-plans itself when you fall behind.

Designed for **Claude Cowork** (Desktop), where it can:
- ping you on a schedule (Scheduled Tasks) with the day's session prepared,
- read/write your progress files directly — no copy-paste, no spreadsheets to maintain.

It also works in the regular Claude app, just without the proactive ping and auto-logging.

---

## What it does

- **Daily sessions sized to your life** — short weekday sessions, longer weekend blocks. It tells you exactly what to do today: one pattern + one specific LeetCode problem (by name, number, and link).
- **Guided solving, not answer-dumping** — a hint ladder that escalates only when you're stuck, mirroring a real interview.
- **Diagnostic debrief** — after each problem it asks a couple of quick questions (how did it land? where was the friction?) and uses your answers to calibrate difficulty and coaching focus.
- **Spaced-repetition variants** — shaky on a pattern? It schedules a *different* problem of the same pattern a few days later to build genuine comfort.
- **Bi-weekly mock assessments** — timed, scored, logged, and compared to last time so you can see the trajectory.
- **Rest days** — say "taking off today" any day; it shifts the plan forward and keeps your streak.
- **Adaptive re-planning** — fall behind and it offers concrete options (triage / extend / intensify) instead of guilt.
- **Weekly check** — only when genuinely needed, it suggests one extra weekend block to shore up a weak area.

## Curriculum at a glance

A ~10-week arc (configurable):
1. **Weeks 1–5** — DSA foundations & patterns (arrays, strings, linked lists, stacks/queues, trees, binary search, graphs).
2. **Weeks 6–8** — advanced patterns (DP, heaps, intervals, greedy, backtracking, bit manipulation) + HLD depth, LLD intro.
3. **Weeks 9–10** — mocks and revision.

HLD topics (URL shortener, rate limiter, chat, Twitter feed, etc.) sit on weekends; LLD (parking lot, BookMyShow) appears later. All patterns come with concept notes and a curated LeetCode problem bank (Blind 75 / NeetCode staples).

---

## Install

1. Download the `.skill` file (or zip this `interview-prep-coach/` folder into one — see *Packaging* below).
2. In the Claude app: **Settings → Skills → upload**.
3. Open Claude (ideally Cowork on Desktop) and say: **"Start my interview prep."**
   - On first run it asks a few setup questions (target role, timeline, weekday/weekend time, current level, weak areas, start date, study times) and builds your personalized plan + tracker.

## Set up the proactive ping (Cowork, Desktop, paid plan)

In Cowork, create a **Scheduled Task** at your study times (e.g., weekdays 9 PM, weekends 3 PM) with this prompt:

> "Using my interview-prep-coach skill, run my daily prep brief. Read progress.md and tracker.csv in my Interview-Prep folder, figure out today's day number and topic, pick the specific LeetCode problem(s) for today (name + number + link), and lay out today's session so it's ready for me to start. Note my streak and whether I'm on track. If I marked a rest day or missed sessions, adjust first. End by asking: available / partial / rest / re-eval?"

Now your session is prepared and waiting each day — you just show up and answer one word.

---

## How it's organized

```
interview-prep-coach/
├── SKILL.md                      # the operating manual (entry protocol, session types, autonomy)
├── references/
│   ├── tutor-system.md           # methodology, tracking, assessments, rest days, debrief, scheduling
│   ├── curriculum.md             # the week-by-week plan
│   ├── dsa-patterns.md           # concept notes per pattern (templates, pitfalls)
│   ├── leetcode-bank.md          # curated real problems by topic
│   └── hld-framework.md          # 6-step HLD framework + notes per system
├── assets/
│   ├── progress.md               # dashboard template (filled at setup)
│   ├── mastery.md                # topic mastery table
│   └── tracker.csv               # placeholder; real tracker generated at setup
└── scripts/
    └── generate_schedule.py      # builds a date-mapped tracker from your start date
```

## Customize

- Edit `references/curriculum.md` and `references/leetcode-bank.md` to change topics or problems.
- Edit the topic sequences in `scripts/generate_schedule.py` to reshape the plan.
- Change cadence/times by editing your Scheduled Task and `progress.md`.

## Packaging into a `.skill`

If you have Anthropic's `skill-creator` tools:
```bash
python -m scripts.package_skill interview-prep-coach ./dist
```
Otherwise a plain zip of the `interview-prep-coach/` folder works for upload.

---

## Branches

- **`main`** — this generic, shareable version (personalizes itself via the setup interview).
- **`saurav-custom`** — a fully pre-configured personal instance (SDE-2 target, fixed dates/times) kept as an example of a filled-in plan.

## License

MIT — use it, fork it, make it yours.
