# 60-Day SDE-2 Prep Curriculum — Backend Role

> **Role branching:** This file covers the **Backend** curriculum. For Frontend, load `references/frontend-curriculum.md` instead. For Fullstack, use this file as the base and weave in frontend-curriculum.md weekend blocks, tilting toward whichever side is weaker.

## Structure
- **Weekdays (Mon–Fri):** 30–45 min → 1 pattern concept + 1 guided problem
- **Weekends (Sat–Sun):** 2–3 hrs → deep topic block or full HLD/LLD session
- **Week 9–10:** Mock interviews + revision only

---

## Phase 1: DSA Foundations & Patterns (Weeks 1–5, Days 1–35)

### Week 1 — Arrays, Sliding Window, Two Pointers
| Day | Type | Topic |
|-----|------|-------|
| 1 (Mon) | Weekday | Sliding window concept + 1 easy-medium |
| 2 (Tue) | Weekday | Two pointers concept + 1 medium |
| 3 (Wed) | Weekday | Prefix sum concept + 1 medium |
| 4 (Thu) | Weekday | Kadane's / subarray patterns + 1 medium |
| 5 (Fri) | Weekday | Mixed array problem (untimed first attempt) |
| 6 (Sat) | Weekend | 3 array problems (easy → medium → medium-hard) + pattern review |
| 7 (Sun) | Weekend | HLD Intro: What is system design? Pillars (scalability, availability, consistency, latency). Practice: "Design a URL Shortener" |

### Week 2 — Strings, Hashmaps, Sets
| Day | Type | Topic |
|-----|------|-------|
| 8 | Weekday | Anagram / hashmap patterns |
| 9 | Weekday | Sliding window on strings |
| 10 | Weekday | Trie concept + problems |
| 11 | Weekday | String DP intro (longest common subsequence idea) |
| 12 | Weekday | Mixed string problem |
| 13 | Weekend | 3 hashmap/string problems |
| 14 | Weekend | HLD: Design a Pastebin / Key-Value Store. Focus: storage layer, replication basics |

### Week 3 — Linked Lists, Stacks, Queues
| Day | Type | Topic |
|-----|------|-------|
| 15 | Weekday | Linked list pointer patterns (fast/slow, reverse) |
| 16 | Weekday | Monotonic stack concept |
| 17 | Weekday | Queue & deque patterns |
| 18 | Weekday | LRU Cache pattern (combines LL + hashmap) |
| 19 | Weekday | Mixed problem |
| 20 | Weekend | 3 problems (stack/queue/LL mix) |
| 21 | Weekend | HLD: Design a Rate Limiter. Focus: token bucket, sliding window counter, Redis |

### Week 4 — Trees & Binary Search
| Day | Type | Topic |
|-----|------|-------|
| 22 | Weekday | Binary search on answer concept |
| 23 | Weekday | BST patterns (validate, serialize, LCA) |
| 24 | Weekday | Tree traversals (iterative DFS, BFS, level order) |
| 25 | Weekday | Tree DP (diameter, max path sum) |
| 26 | Weekday | Mixed tree/BS problem |
| 27 | Weekend | 3 tree + binary search problems |
| 28 | Weekend | HLD: Design a Notification System. Focus: pub-sub, Kafka basics, fan-out |

### Week 5 — Graphs
| Day | Type | Topic |
|-----|------|-------|
| 29 | Weekday | BFS/DFS patterns (connected components, island problems) |
| 30 | Weekday | Topological sort (DAG, course schedule pattern) |
| 31 | Weekday | Dijkstra / shortest path concept |
| 32 | Weekday | Union-Find concept + problems |
| 33 | Weekday | Mixed graph problem |
| 34 | Weekend | 3 graph problems (BFS → topo → Dijkstra) |
| 35 | Weekend | HLD: Design a Search Autocomplete. Focus: trie, caching, CDN |

---

## Phase 2: Advanced Patterns + HLD Depth (Weeks 6–8, Days 36–56)

### Week 6 — Dynamic Programming
| Day | Type | Topic |
|-----|------|-------|
| 36 | Weekday | DP patterns: 1D (fibonacci family, house robber) |
| 37 | Weekday | DP patterns: 2D (grid, unique paths) |
| 38 | Weekday | Knapsack pattern |
| 39 | Weekday | Interval DP / string DP |
| 40 | Weekday | Mixed DP problem |
| 41 | Weekend | 3 DP problems (easy → medium → medium-hard) |
| 42 | Weekend | HLD: Design Twitter Feed. Focus: fanout on write vs read, sharding |

### Week 7 — Heaps, Intervals, Greedy
| Day | Type | Topic |
|-----|------|-------|
| 43 | Weekday | Heap patterns (top-K, merge K lists) |
| 44 | Weekday | Interval merge/insert/sweep |
| 45 | Weekday | Greedy patterns (activity selection, gas station) |
| 46 | Weekday | Two heaps pattern (median finder) |
| 47 | Weekday | Mixed problem |
| 48 | Weekend | 3 heap/interval/greedy problems |
| 49 | Weekend | HLD: Design a Distributed Cache (Memcached/Redis). Focus: consistent hashing, eviction |

### Week 8 — Backtracking, Bit Manipulation, Math
| Day | Type | Topic |
|-----|------|-------|
| 50 | Weekday | Backtracking template (subsets, permutations, N-queens) |
| 51 | Weekday | Backtracking with pruning |
| 52 | Weekday | Bit manipulation tricks |
| 53 | Weekday | Math patterns (prime sieve, GCD, modular arithmetic) |
| 54 | Weekday | LLD intro: SOLID principles + 1 design (Parking Lot) |
| 55 | Weekend | LLD deep dive: Design a BookMyShow / Library System |
| 56 | Weekend | HLD: Design a WhatsApp/Chat System. Focus: WebSockets, message queues, storage |

---

## Phase 3: Mock + Revision (Weeks 9–10, Days 57–60+)

### Week 9
| Day | Topic |
|-----|-------|
| 57 | Weak topic revision (from your own flagged list) |
| 58 | Full mock: 2 DSA problems timed (45 min each) |
| 59 | Full mock HLD: end-to-end design in 45 min |
| 60 | Review mocks, write down gaps, final confidence check |

---

## Key HLD Topics to Cover (mapped to weekends above)
1. URL Shortener — hashing, redirect, analytics
2. Pastebin — blob storage, TTL, sharding
3. Rate Limiter — token bucket, Redis, distributed counters
4. Notification System — Kafka, push/pull, fan-out
5. Search Autocomplete — trie, caching, ranking
6. Twitter Feed — timeline generation, fanout strategies
7. Distributed Cache — consistent hashing, eviction policies
8. Chat System — WebSockets, message persistence, delivery guarantees

## LLD Topics (Weekend blocks + buffer)
1. Parking Lot
2. BookMyShow / Movie Ticket Booking
3. Elevator 