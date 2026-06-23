# 60-Day Frontend SWE Interview Curriculum

> Load this file whenever the user's role type is **Frontend** (or the frontend portion of Fullstack). The backend curriculum lives in `curriculum.md`.

## Structure
- **Weekdays (Mon–Fri):** 30–45 min → 1 concept block + 1 guided problem or coding drill
- **Weekends (Sat–Sun):** 2–3 hrs → deep topic block, frontend system design (FSD) session, or component design session
- **Week 9–10:** Mock interviews + revision only

### What "concept + problem" means for frontend
Weekday topics alternate between **DSA in JS/TS** (same patterns as backend, solved in JavaScript with JS-specific nuances), **JavaScript/Browser fundamentals** (event loop, closures, DOM, async), and **React/framework depth** (hooks, rendering, state). Weekend sessions run FSD mocks or Component Design challenges (the frontend equivalent of HLD + LLD).

---

## Phase 1: JS/TS Foundations + DSA Core (Weeks 1–4, Days 1–28)

### Week 1 — JavaScript Core: Execution, Scope, Closures
| Day | Type | Topic |
|-----|------|-------|
| 1 (Mon) | Weekday | Event loop deep dive: call stack, task queue, microtask queue, `setTimeout` vs Promise vs `queueMicrotask` |
| 2 (Tue) | Weekday | Closures + lexical scoping — write a debounce from scratch |
| 3 (Wed) | Weekday | `var` / `let` / `const`, hoisting, TDZ — explain + write quiz-style drills |
| 4 (Thu) | Weekday | Prototype chain + `this` binding (call/apply/bind, arrow vs regular) |
| 5 (Fri) | Weekday | DSA in JS: Sliding window + two pointers (solve in JS, discuss Map/Set vs object trade-offs) |
| 6 (Sat) | Weekend | JS deep dive: Implement `Promise.all`, `Promise.race`, `Promise.allSettled` from scratch |
| 7 (Sun) | Weekend | FSD Intro: What is Frontend System Design? The 5-step framework. Practice: "Design a Typeahead/Autocomplete" |

### Week 2 — Async JS, TypeScript, DSA Strings/Hashmaps
| Day | Type | Topic |
|-----|------|-------|
| 8 | Weekday | async/await, error handling, async patterns (retry, throttle, concurrent with limit) |
| 9 | Weekday | TypeScript: generics, utility types (Partial, Pick, Omit, ReturnType), discriminated unions |
| 10 | Weekday | DSA in JS: Hashmap/string patterns — anagram, substrings (JavaScript Map vs plain object) |
| 11 | Weekday | TypeScript: conditional types, infer, template literal types |
| 12 | Weekday | DSA: Sliding window on strings, Trie concept |
| 13 | Weekend | JS: Implement throttle + debounce + memoize from scratch; discuss real use cases |
| 14 | Weekend | **Assessment 1** — 2 DSA problems (arrays/strings, 35 min each in JS) + JS concept quiz (event loop, closure, prototype chain) |

### Week 3 — Browser Internals + DOM + DSA Trees
| Day | Type | Topic |
|-----|------|-------|
| 15 | Weekday | Browser rendering pipeline: CRP (HTML→DOM→CSSOM→RenderTree→Layout→Paint→Composite) |
| 16 | Weekday | Event delegation, bubbling/capturing, `stopPropagation` vs `preventDefault` |
| 17 | Weekday | DSA: Linked list pointer patterns (fast/slow, reverse) — in JS, discuss array vs LL |
| 18 | Weekday | Web storage: `localStorage`, `sessionStorage`, `IndexedDB`, cookies — use cases + security (XSS, CSRF) |
| 19 | Weekday | DSA: Trees — traversals (DFS/BFS iterative in JS), BST patterns, Tree DP |
| 20 | Weekend | Component Design: Design a **Modal / Dialog** component — API surface, focus trap, portal, keyboard nav, accessibility (ARIA, `role="dialog"`, `aria-modal`) |
| 21 | Weekend | FSD: Design an **Infinite Scroll Feed** — virtualization strategy, IntersectionObserver, pagination vs cursor, prefetching |

### Week 4 — React Fundamentals Deep Dive + DSA Graphs/Binary Search
| Day | Type | Topic |
|-----|------|-------|
| 22 | Weekday | React: Virtual DOM + reconciliation + the Fiber architecture (why Fiber, how it enables concurrent mode) |
| 23 | Weekday | React hooks deep dive 1: `useState`, `useEffect` (deps array edge cases, cleanup, double-fire in StrictMode) |
| 24 | Weekday | React hooks deep dive 2: `useRef`, `useCallback`, `useMemo` — when they actually help vs premature optimization |
| 25 | Weekday | DSA: Binary search + graph BFS/DFS patterns in JS |
| 26 | Weekday | React: `useContext`, `useReducer`, custom hooks — build a `useFetch` with loading/error/abort |
| 27 | Weekend | 3 DSA problems (tree + binary search + graph, solved in JS, 30 min each) + debrief |
| 28 | Weekend | **Assessment 2** — 2 DSA problems (trees + graphs, 40 min each) + React concept quiz (reconciliation, hook rules, rendering behavior) + mini FSD: Design a Typeahead |

---

## Phase 2: React Advanced + Component Architecture (LLD) (Weeks 5–7, Days 29–49)

### Week 5 — React Performance + Rendering Patterns
| Day | Type | Topic |
|-----|------|-------|
| 29 | Weekday | React rendering deep dive: when does a component re-render? `React.memo`, key prop, context gotchas |
| 30 | Weekday | Code splitting + lazy loading: `React.lazy`, `Suspense`, dynamic `import()`, route-based splitting |
| 31 | Weekday | DSA: Dynamic programming patterns in JS (1D DP, 2D DP — house robber, unique paths) |
| 32 | Weekday | SSR vs CSR vs SSG vs ISR — trade-offs, hydration, TTFB vs TTI vs LCP |
| 33 | Weekday | DSA: Heap/priority queue in JS (simulate with sorted array or binary heap), interval problems |
| 34 | Weekend | 3 DP + heap problems in JS |
| 35 | Weekend | FSD: Design a **File Upload Component** — chunked uploads, progress tracking, retry logic, drag-and-drop UX, state machine for upload lifecycle |

### Week 6 — Component Design Patterns (Frontend LLD)
| Day | Type | Topic |
|-----|------|-------|
| 36 | Weekday | Compound components pattern — build a flexible `<Tabs>` using `React.Children` or context |
| 37 | Weekday | Render props + HOC patterns — when to use each vs custom hooks |
| 38 | Weekday | DSA: Backtracking in JS (subsets, permutations, N-queens) |
| 39 | Weekday | State machine thinking for UI: model a multi-step form or a media player with XState / raw reducer |
| 40 | Weekday | DSA: Greedy + interval merge in JS |
| 41 | Weekend | Component Design deep dive: Design a **Data Table** — sorting, filtering, pagination, virtualized rows, column resizing, accessible keyboard navigation |
| 42 | Weekend | **Assessment 3** — 2 DSA problems (DP + backtracking, 40 min each) + Component Design: Design a **Toast / Notification** system (queue, stacking, auto-dismiss, a11y) |

### Week 7 — State Management + CSS Architecture
| Day | Type | Topic |
|-----|------|-------|
| 43 | Weekday | Global state deep dive: Redux vs Zustand vs Jotai vs React Query — when to use each, selector patterns |
| 44 | Weekday | CSS architecture: BEM, CSS Modules, CSS-in-JS (emotion/styled-components), utility-first (Tailwind) — trade-offs |
| 45 | Weekday | CSS layout mastery: Flexbox + Grid edge cases, responsive design patterns, container queries |
| 46 | Weekday | Web Workers + Service Workers: use cases, postMessage, caching strategies (cache-first, network-first, stale-while-revalidate) |
| 47 | Weekday | DSA: Bit manipulation + math patterns in JS |
| 48 | Weekend | Component Design: Design a **Form Builder** — dynamic fields, validation schema, field-level vs form-level error state, accessible error messages, controlled vs uncontrolled components |
| 49 | Weekend | FSD: Design **Google Docs (Collaborative Editor)** — OT vs CRDT, WebSocket vs polling, cursor sharing, conflict resolution, autosave |

---

## Phase 3: Frontend System Design Depth + Performance (Week 8, Days 50–56)

### Week 8 — Performance, Accessibility, Advanced FSD
| Day | Type | Topic |
|-----|------|-------|
| 50 | Weekday | Core Web Vitals: LCP, FID/INP, CLS — what affects each, how to diagnose with Lighthouse / Chrome DevTools |
| 51 | Weekday | Bundle optimization: tree shaking, chunk splitting, preload/prefetch, image optimization (WebP, lazy loading, srcset) |
| 52 | Weekday | Accessibility deep dive: WCAG 2.1 AA, ARIA roles/states/properties, focus management, screen-reader behavior |
| 53 | Weekday | Security: XSS (DOM, reflected, stored) + mitigation (CSP, sanitization); CSRF + SameSite cookies; CORS |
| 54 | Weekday | GraphQL vs REST from a frontend perspective: over-fetching, N+1, fragments, DataLoader, subscriptions |
| 55 | Weekend | FSD: Design a **Real-Time Dashboard** (stock ticker / live metrics) — WebSocket vs SSE vs long-polling, data normalization, throttled rendering, virtualized charts |
| 56 | Weekend | **Assessment 4** — Full mock: 1 DSA hard (45 min, JS) + 1 FSD (45 min): "Design a YouTube Video Player" + 1 Component Design: "Design a multi-select Combobox with search" |

---

## Phase 4: Mock Interviews + Revision (Weeks 9–10, Days 57–60+)

| Day | Topic |
|-----|-------|
| 57 | Weak topic revision (from your flagged list in mastery.md) |
| 58 | Full mock: 2 DSA problems timed in JS (45 min each) |
| 59 | Full mock FSD: end-to-end frontend system design in 45 min |
| 60 | Review mocks, write down gaps, final confidence check |

---

## Key Frontend System Design Problems to Cover
1. Typeahead / Autocomplete — debounce, caching, keyboard nav
2. Infinite Scroll Feed — virtualization, IntersectionObserver, cursor pagination
3. File Upload Component — chunked upload, progress, retry, drag-and-drop
4. Google Docs (Collaborative Editor) — OT/CRDT, WebSocket, conflict resolution
5. Real-Time Dashboard — WebSocket/SSE, throttled rendering, virtual charts
6. YouTube Video Player — adaptive bitrate, buffering, playback state machine, subtitles
7. Design System / Component Library — token system, polymorphic components, theming, tree-shaking
8. Shopping Cart — optimistic updates, persistence, multi-tab sync

## Key Component Design Problems to Cover
1. Modal / Dialog — focus trap, portal, keyboard nav, ARIA
2. Data Table — sort/filter/paginate, row virtualization, column resize, keyboard a11y
3. Toast / Notification System — queue, stack, auto-dismiss, a11y live regions
4. Form Builder — dynamic fields, validation, accessible errors, controlled vs uncontrolled
5. Multi-select Combobox — search, keyboard nav, screen reader, virtualized options
6. Date Picker — calendar grid, range selection, keyboard nav, locale
7. Drag-and-Drop List — touch support, ARIA, sortable algorithm

## JS/TS Deep-Dive Topics Cheatsheet
See `frontend-patterns.md` for concept notes per topic.

## Frontend System Design Framework
See `frontend-system-design.md` for the 5-step approach and deep-dive notes per FSD problem.
