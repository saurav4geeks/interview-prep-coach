# LeetCode Problem Bank — Concept-Tag Matrix

## How Claude selects problems

**For daily sessions:**
1. Get today's pattern from the curriculum / Tracker row.
2. Filter this bank by `Pattern` column.
3. Cross-check Tracker `Notes` column for previously solved problem numbers — exclude those.
4. Pick by: difficulty matching user's current level (SDE1 = L1/L2, SDE2 = L2/L3, SDE3 = L3/Optimal) × famous-sheet priority (B75 > NC150 > S250 for core coverage).
5. If all problems for a pattern are already solved: generate a fresh unseen LeetCode problem of equivalent difficulty and tag it `[generated]` in the Tracker Notes.

**For assessments:** Pick from the mock sets at the bottom. Always check the Assessments tab for previously used problem numbers.

**Famous sheet key:** `B75` = Blind 75 · `NC150` = NeetCode 150 · `S250` = Striver's SDE Sheet · `L79` = Striver's Last Moment 79

**Level key:** `L1` = SDE1 (easy–medium) · `L2` = SDE2 (medium–hard fluent) · `L3` = SDE3 (hard, optimal)

**JS✓** = fully solvable in JS/TS (use for frontend sessions; see JS Gotchas section)

---

## Pattern Coverage Index

| Pattern | L1 | L2 | L3 | Total |
|---------|----|----|-----|-------|
| Arrays & Hashing | 3 | 4 | 2 | 9 |
| Sliding Window | 2 | 4 | 2 | 8 |
| Two Pointers | 3 | 3 | 1 | 7 |
| Prefix Sum | 2 | 2 | 1 | 5 |
| Kadane / Subarray | 1 | 2 | 2 | 5 |
| Stack & Monotonic Stack | 2 | 3 | 2 | 7 |
| Queue / Deque | 1 | 2 | 1 | 4 |
| Linked List | 3 | 3 | 2 | 8 |
| Binary Search | 3 | 4 | 2 | 9 |
| Trees | 4 | 5 | 3 | 12 |
| Trie | 1 | 2 | 1 | 4 |
| Graphs (BFS/DFS) | 2 | 4 | 3 | 9 |
| Topological Sort | 1 | 2 | 1 | 4 |
| Shortest Path | 1 | 2 | 1 | 4 |
| Union-Find | 1 | 2 | 1 | 4 |
| DP — 1D | 2 | 3 | 2 | 7 |
| DP — 2D / Grid | 1 | 3 | 2 | 6 |
| DP — Knapsack | 1 | 2 | 2 | 5 |
| DP — String / Interval | 1 | 2 | 2 | 5 |
| Heap / Priority Queue | 2 | 3 | 2 | 7 |
| Intervals | 2 | 3 | 1 | 6 |
| Greedy | 2 | 3 | 2 | 7 |
| Backtracking | 1 | 3 | 2 | 6 |
| Bit Manipulation | 2 | 2 | 2 | 6 |
| Math | 2 | 2 | 1 | 5 |
| **Total** | | | | **~168** |

---

## Problem Matrix

### Arrays & Hashing

| # | Problem | LC# | Level | Sheets | Company | JS✓ |
|---|---------|-----|-------|--------|---------|-----|
| 1 | Two Sum | 1 | L1 | B75 NC150 S250 L79 | Amazon Google Meta | ✓ |
| 2 | Valid Anagram | 242 | L1 | B75 NC150 S250 | Amazon Microsoft | ✓ |
| 3 | Contains Duplicate | 217 | L1 | B75 NC150 S250 | Amazon | ✓ |
| 4 | Group Anagrams | 49 | L2 | B75 NC150 S250 | Amazon Google | ✓ |
| 5 | Top K Frequent Elements | 347 | L2 | B75 NC150 S250 | Amazon Meta | ✓ |
| 6 | Product of Array Except Self | 238 | L2 | B75 NC150 S250 L79 | Amazon Microsoft | ✓ |
| 7 | Encode and Decode Strings | 271 | L2 | B75 NC150 | Google | ✓ |
| 8 | Longest Consecutive Sequence | 128 | L2 | B75 NC150 S250 | Google Amazon | ✓ |
| 9 | Subarray Sum Equals K | 560 | L3 | NC150 S250 | Amazon Google | ✓ |

### Sliding Window

| # | Problem | LC# | Level | Sheets | Company | JS✓ |
|---|---------|-----|-------|--------|---------|-----|
| 10 | Best Time to Buy and Sell Stock | 121 | L1 | B75 NC150 S250 L79 | Amazon Microsoft | ✓ |
| 11 | Longest Substring Without Repeating | 3 | L1 | B75 NC150 S250 L79 | Amazon Google Meta | ✓ |
| 12 | Longest Repeating Character Replacement | 424 | L2 | B75 NC150 S250 | Google | ✓ |
| 13 | Permutation in String | 567 | L2 | NC150 S250 | Microsoft | ✓ |
| 14 | Minimum Window Substring | 76 | L2 | B75 NC150 S250 L79 | Amazon Google | ✓ |
| 15 | Sliding Window Maximum | 239 | L2 | S250 L79 | Amazon Google | ✓ |
| 16 | Fruit Into Baskets | 904 | L2 | S250 | Google | ✓ |
| 17 | Max Consecutive Ones III | 1004 | L3 | NC150 | Amazon | ✓ |

### Two Pointers

| # | Problem | LC# | Level | Sheets | Company | JS✓ |
|---|---------|-----|-------|--------|---------|-----|
| 18 | Valid Palindrome | 125 | L1 | B75 NC150 S250 | Meta Amazon | ✓ |
| 19 | Two Sum II — Sorted Array | 167 | L1 | NC150 S250 | Amazon | ✓ |
| 20 | 3Sum | 15 | L2 | B75 NC150 S250 L79 | Amazon Google Meta | ✓ |
| 21 | Container With Most Water | 11 | L2 | B75 NC150 S250 L79 | Amazon Google | ✓ |
| 22 | Trapping Rain Water | 42 | L2 | B75 NC150 S250 L79 | Amazon Google Meta | ✓ |
| 23 | 4Sum | 18 | L2 | S250 | Amazon | ✓ |
| 24 | Remove Nth Node From End of List | 19 | L3 | B75 NC150 S250 | Microsoft | ✓ |

### Prefix Sum

| # | Problem | LC# | Level | Sheets | Company | JS✓ |
|---|---------|-----|-------|--------|---------|-----|
| 25 | Range Sum Query — Immutable | 303 | L1 | S250 | Amazon | ✓ |
| 26 | Find Pivot Index | 724 | L1 | NC150 | Amazon | ✓ |
| 27 | Subarray Sum Equals K | 560 | L2 | NC150 S250 | Amazon Google | ✓ |
| 28 | Product of Array Except Self | 238 | L2 | B75 NC150 S250 | Amazon | ✓ |
| 29 | Count Subarrays With Given XOR | — | L3 | S250 | Amazon | ✓ |

### Kadane / Subarray

| # | Problem | LC# | Level | Sheets | Company | JS✓ |
|---|---------|-----|-------|--------|---------|-----|
| 30 | Maximum Subarray | 53 | L1 | B75 NC150 S250 L79 | Amazon Microsoft | ✓ |
| 31 | Maximum Product Subarray | 152 | L2 | B75 NC150 S250 | Amazon | ✓ |
| 32 | Longest Turbulent Subarray | 978 | L2 | — | — | ✓ |
| 33 | Maximum Sum Circular Subarray | 918 | L3 | NC150 | Amazon | ✓ |
| 34 | Count Subarrays With Fixed Bounds | 2444 | L3 | — | Amazon | ✓ |

### Stack & Monotonic Stack

| # | Problem | LC# | Level | Sheets | Company | JS✓ |
|---|---------|-----|-------|--------|---------|-----|
| 35 | Valid Parentheses | 20 | L1 | B75 NC150 S250 L79 | Amazon Google Meta | ✓ |
| 36 | Min Stack | 155 | L1 | B75 NC150 S250 | Amazon Microsoft | ✓ |
| 37 | Daily Temperatures | 739 | L2 | NC150 S250 | Amazon Google | ✓ |
| 38 | Car Fleet | 853 | L2 | NC150 | — | ✓ |
| 39 | Largest Rectangle in Histogram | 84 | L2 | B75 S250 L79 | Amazon Google | ✓ |
| 40 | Asteroid Collision | 735 | L3 | S250 | Amazon | ✓ |
| 41 | Remove K Digits | 402 | L3 | S250 | Amazon Google | ✓ |

### Queue / Deque

| # | Problem | LC# | Level | Sheets | Company | JS✓ |
|---|---------|-----|-------|--------|---------|-----|
| 42 | Number of Recent Calls | 933 | L1 | — | — | ✓ |
| 43 | Design Circular Queue | 622 | L2 | S250 | Amazon Microsoft | ✓ |
| 44 | Sliding Window Maximum | 239 | L2 | S250 L79 | Amazon Google | ✓ |
| 45 | First Negative in Every Window of K | — | L3 | S250 | Amazon | ✓ |

### Linked List

| # | Problem | LC# | Level | Sheets | Company | JS✓ |
|---|---------|-----|-------|--------|---------|-----|
| 46 | Reverse Linked List | 206 | L1 | B75 NC150 S250 L79 | Amazon Microsoft | ✓ |
| 47 | Merge Two Sorted Lists | 21 | L1 | B75 NC150 S250 L79 | Amazon Microsoft | ✓ |
| 48 | Linked List Cycle | 141 | L1 | B75 NC150 S250 | Amazon | ✓ |
| 49 | Reorder List | 143 | L2 | B75 NC150 S250 | Microsoft | ✓ |
| 50 | Remove Nth Node From End | 19 | L2 | B75 NC150 S250 | Microsoft | ✓ |
| 51 | LRU Cache | 146 | L2 | B75 NC150 S250 L79 | Amazon Google Meta | ✓ |
| 52 | Merge K Sorted Lists | 23 | L3 | B75 NC150 S250 L79 | Amazon Google | ✓ |
| 53 | Reverse Nodes in K-Group | 25 | L3 | S250 L79 | Amazon Google | ✓ |

### Binary Search

| # | Problem | LC# | Level | Sheets | Company | JS✓ |
|---|---------|-----|-------|--------|---------|-----|
| 54 | Binary Search | 704 | L1 | NC150 S250 | — | ✓ |
| 55 | Find Minimum in Rotated Sorted Array | 153 | L1 | B75 NC150 S250 | Amazon Microsoft | ✓ |
| 56 | Koko Eating Bananas | 875 | L1 | NC150 S250 | Amazon Google | ✓ |
| 57 | Search in Rotated Sorted Array | 33 | L2 | B75 NC150 S250 L79 | Amazon Microsoft | ✓ |
| 58 | Time Based Key-Value Store | 981 | L2 | NC150 | Amazon | ✓ |
| 59 | Capacity to Ship Packages Within D Days | 1011 | L2 | S250 | Amazon | ✓ |
| 60 | Find Median of Two Sorted Arrays | 4 | L2 | B75 NC150 S250 L79 | Amazon Google | ✓ |
| 61 | Min Days to Make m Bouquets | 1482 | L3 | S250 | Amazon | ✓ |
| 62 | Aggressive Cows (Stall placement) | — | L3 | S250 | — | ✓ |

### Trees (BST + Traversal + Tree DP)

| # | Problem | LC# | Level | Sheets | Company | JS✓ |
|---|---------|-----|-------|--------|---------|-----|
| 63 | Invert Binary Tree | 226 | L1 | B75 NC150 S250 | Amazon Google | ✓ |
| 64 | Maximum Depth of Binary Tree | 104 | L1 | B75 NC150 S250 | Amazon | ✓ |
| 65 | Balanced Binary Tree | 110 | L1 | S250 | Amazon | ✓ |
| 66 | Same Tree | 100 | L1 | NC150 S250 | — | ✓ |
| 67 | Binary Tree Level Order Traversal | 102 | L2 | B75 NC150 S250 L79 | Amazon Microsoft | ✓ |
| 68 | Lowest Common Ancestor of BST | 235 | L2 | B75 NC150 S250 | Amazon Microsoft | ✓ |
| 69 | Binary Tree Right Side View | 199 | L2 | NC150 S250 | Amazon | ✓ |
| 70 | Validate Binary Search Tree | 98 | L2 | B75 NC150 S250 | Amazon Microsoft | ✓ |
| 71 | Kth Smallest in BST | 230 | L2 | B75 NC150 S250 | Amazon Google | ✓ |
| 72 | Construct Tree from Preorder+Inorder | 105 | L2 | B75 NC150 S250 | Amazon Google | ✓ |
| 73 | Binary Tree Maximum Path Sum | 124 | L3 | B75 NC150 S250 L79 | Amazon Meta | ✓ |
| 74 | Serialize and Deserialize Binary Tree | 297 | L3 | B75 NC150 S250 | Amazon Google | ✓ |
| 75 | Count Good Nodes in Binary Tree | 1448 | L3 | NC150 | — | ✓ |

### Trie

| # | Problem | LC# | Level | Sheets | Company | JS✓ |
|---|---------|-----|-------|--------|---------|-----|
| 76 | Implement Trie | 208 | L1 | B75 NC150 S250 | Amazon Google | ✓ |
| 77 | Design Add and Search Words | 211 | L2 | B75 NC150 | Amazon | ✓ |
| 78 | Word Search II | 212 | L2 | B75 NC150 S250 | Amazon Google | ✓ |
| 79 | Maximum XOR of Two Numbers | 421 | L3 | S250 | Google | ✓ |

### Graphs (BFS / DFS)

| # | Problem | LC# | Level | Sheets | Company | JS✓ |
|---|---------|-----|-------|--------|---------|-----|
| 80 | Number of Islands | 200 | L1 | B75 NC150 S250 L79 | Amazon Google | ✓ |
| 81 | Clone Graph | 133 | L1 | B75 NC150 S250 | Amazon Microsoft | ✓ |
| 82 | Flood Fill | 733 | L2 | S250 | Amazon | ✓ |
| 83 | Walls and Gates | 286 | L2 | NC150 | Google | ✓ |
| 84 | Rotting Oranges | 994 | L2 | NC150 S250 | Amazon Google | ✓ |
| 85 | Pacific Atlantic Water Flow | 417 | L2 | B75 NC150 S250 | Amazon | ✓ |
| 86 | Number of Connected Components | 323 | L2 | B75 NC150 S250 | — | ✓ |
| 87 | Word Ladder | 127 | L3 | S250 L79 | Amazon Google | ✓ |
| 88 | Surrounded Regions | 130 | L3 | NC150 S250 | — | ✓ |

### Topological Sort

| # | Problem | LC# | Level | Sheets | Company | JS✓ |
|---|---------|-----|-------|--------|---------|-----|
| 89 | Course Schedule | 207 | L1 | B75 NC150 S250 L79 | Amazon Google | ✓ |
| 90 | Course Schedule II | 210 | L2 | B75 NC150 S250 | Amazon Google | ✓ |
| 91 | Find Eventual Safe States | 802 | L2 | S250 | Amazon | ✓ |
| 92 | Alien Dictionary | 269 | L3 | B75 NC150 S250 | Amazon Google Meta | ✓ |

### Shortest Path (Dijkstra / Weighted)

| # | Problem | LC# | Level | Sheets | Company | JS✓ |
|---|---------|-----|-------|--------|---------|-----|
| 93 | Network Delay Time | 743 | L1 | NC150 S250 | Amazon Google | ✓ |
| 94 | Path With Minimum Effort | 1631 | L2 | S250 | Google | ✓ |
| 95 | Cheapest Flights Within K Stops | 787 | L2 | NC150 S250 | Amazon | ✓ |
| 96 | Swim in Rising Water | 778 | L3 | NC150 | Google | ✓ |

### Union-Find

| # | Problem | LC# | Level | Sheets | Company | JS✓ |
|---|---------|-----|-------|--------|---------|-----|
| 97 | Number of Provinces | 547 | L1 | S250 | Amazon | ✓ |
| 98 | Redundant Connection | 684 | L2 | NC150 S250 | — | ✓ |
| 99 | Accounts Merge | 721 | L2 | NC150 S250 | Amazon Google | ✓ |
| 100 | Making a Large Island | 827 | L3 | S250 | Google | ✓ |

### DP — 1D

| # | Problem | LC# | Level | Sheets | Company | JS✓ |
|---|---------|-----|-------|--------|---------|-----|
| 101 | Climbing Stairs | 70 | L1 | B75 NC150 S250 L79 | Amazon Microsoft | ✓ |
| 102 | House Robber | 198 | L1 | B75 NC150 S250 | Amazon Microsoft | ✓ |
| 103 | Min Cost Climbing Stairs | 746 | L2 | NC150 S250 | Amazon | ✓ |
| 104 | House Robber II | 213 | L2 | B75 NC150 S250 | — | ✓ |
| 105 | Decode Ways | 91 | L2 | B75 NC150 S250 | Amazon Meta | ✓ |
| 106 | Longest Increasing Subsequence | 300 | L2 | B75 NC150 S250 L79 | Amazon Google | ✓ |
| 107 | Partition Equal Subset Sum | 416 | L3 | B75 NC150 S250 L79 | Amazon | ✓ |

### DP — 2D / Grid

| # | Problem | LC# | Level | Sheets | Company | JS✓ |
|---|---------|-----|-------|--------|---------|-----|
| 108 | Unique Paths | 62 | L1 | B75 NC150 S250 | Amazon Google | ✓ |
| 109 | Minimum Path Sum | 64 | L2 | S250 | Amazon | ✓ |
| 110 | Maximal Square | 221 | L2 | S250 | Amazon Google | ✓ |
| 111 | Maximal Rectangle | 85 | L2 | S250 | Amazon | ✓ |
| 112 | Dungeon Game | 174 | L3 | S250 | Amazon | ✓ |
| 113 | Cherry Pickup II | 1463 | L3 | — | Google | ✓ |

### DP — Knapsack

| # | Problem | LC# | Level | Sheets | Company | JS✓ |
|---|---------|-----|-------|--------|---------|-----|
| 114 | 0/1 Knapsack | — | L1 | S250 | Amazon | ✓ |
| 115 | Coin Change | 322 | L2 | B75 NC150 S250 L79 | Amazon Google Microsoft | ✓ |
| 116 | Coin Change II | 518 | L2 | NC150 S250 | — | ✓ |
| 117 | Target Sum | 494 | L3 | NC150 S250 | Amazon | ✓ |
| 118 | Last Stone Weight II | 1049 | L3 | S250 | — | ✓ |

### DP — String / Interval

| # | Problem | LC# | Level | Sheets | Company | JS✓ |
|---|---------|-----|-------|--------|---------|-----|
| 119 | Longest Common Subsequence | 1143 | L1 | B75 NC150 S250 L79 | Amazon Google | ✓ |
| 120 | Edit Distance | 72 | L2 | B75 NC150 S250 L79 | Amazon Google Microsoft | ✓ |
| 121 | Longest Palindromic Subsequence | 516 | L2 | S250 | Amazon | ✓ |
| 122 | Burst Balloons | 312 | L3 | S250 | Google | ✓ |
| 123 | Palindrome Partitioning II | 132 | L3 | S250 | Amazon Google | ✓ |

### Heap / Priority Queue

| # | Problem | LC# | Level | Sheets | Company | JS✓ |
|---|---------|-----|-------|--------|---------|-----|
| 124 | Kth Largest Element in Array | 215 | L1 | B75 NC150 S250 L79 | Amazon Microsoft | ✓ |
| 125 | Last Stone Weight | 1046 | L1 | NC150 | — | ✓ |
| 126 | K Closest Points to Origin | 973 | L2 | B75 NC150 S250 | Amazon Google Meta | ✓ |
| 127 | Task Scheduler | 621 | L2 | B75 NC150 S250 | Amazon Google | ✓ |
| 128 | Design Twitter | 355 | L2 | NC150 | — | ✓ |
| 129 | Find Median from Data Stream | 295 | L3 | B75 NC150 S250 L79 | Amazon Google | ✓ |
| 130 | IPO | 502 | L3 | NC150 | — | ✓ |

### Intervals

| # | Problem | LC# | Level | Sheets | Company | JS✓ |
|---|---------|-----|-------|--------|---------|-----|
| 131 | Meeting Rooms | 252 | L1 | B75 NC150 S250 | Amazon Microsoft | ✓ |
| 132 | Merge Intervals | 56 | L1 | B75 NC150 S250 L79 | Amazon Google Microsoft | ✓ |
| 133 | Insert Interval | 57 | L2 | B75 NC150 S250 | Amazon Google | ✓ |
| 134 | Non-overlapping Intervals | 435 | L2 | B75 NC150 S250 | — | ✓ |
| 135 | Meeting Rooms II | 253 | L2 | B75 NC150 S250 L79 | Amazon Google | ✓ |
| 136 | Minimum Interval to Include Each Query | 1851 | L3 | NC150 | — | ✓ |

### Greedy

| # | Problem | LC# | Level | Sheets | Company | JS✓ |
|---|---------|-----|-------|--------|---------|-----|
| 137 | Jump Game | 55 | L1 | B75 NC150 S250 L79 | Amazon Microsoft | ✓ |
| 138 | Jump Game II | 45 | L1 | NC150 S250 | Amazon | ✓ |
| 139 | Gas Station | 134 | L2 | NC150 S250 | Amazon | ✓ |
| 140 | Hand of Straights | 846 | L2 | NC150 | — | ✓ |
| 141 | Partition Labels | 763 | L2 | NC150 S250 | Amazon Google | ✓ |
| 142 | Merge Triplets to Form Target | 1899 | L2 | NC150 | — | ✓ |
| 143 | Valid Parenthesis String | 678 | L3 | NC150 S250 | Amazon | ✓ |

### Backtracking

| # | Problem | LC# | Level | Sheets | Company | JS✓ |
|---|---------|-----|-------|--------|---------|-----|
| 144 | Subsets | 78 | L1 | B75 NC150 S250 | Amazon Google | ✓ |
| 145 | Permutations | 46 | L2 | NC150 S250 L79 | Amazon Google Meta | ✓ |
| 146 | Combination Sum | 39 | L2 | B75 NC150 S250 L79 | Amazon | ✓ |
| 147 | Word Search | 79 | L2 | B75 NC150 S250 | Amazon Microsoft | ✓ |
| 148 | N-Queens | 51 | L3 | S250 L79 | Amazon Google | ✓ |
| 149 | Sudoku Solver | 37 | L3 | S250 | — | ✓ |

### Bit Manipulation

| # | Problem | LC# | Level | Sheets | Company | JS✓ |
|---|---------|-----|-------|--------|---------|-----|
| 150 | Single Number | 136 | L1 | B75 NC150 S250 | Amazon | ✓ |
| 151 | Number of 1 Bits | 191 | L1 | B75 NC150 S250 | Microsoft | ✓ |
| 152 | Counting Bits | 338 | L2 | B75 NC150 S250 | Amazon | ✓ |
| 153 | Missing Number | 268 | L2 | B75 NC150 S250 | Amazon Microsoft | ✓ |
| 154 | Reverse Bits | 190 | L2 | B75 NC150 S250 | — | ✓ |
| 155 | Sum of Two Integers | 371 | L3 | B75 NC150 S250 | — | ✓ |

### Math

| # | Problem | LC# | Level | Sheets | Company | JS✓ |
|---|---------|-----|-------|--------|---------|-----|
| 156 | Palindrome Number | 9 | L1 | S250 | Amazon | ✓ |
| 157 | Power of Two | 231 | L1 | S250 | — | ✓ |
| 158 | Rotate Image | 48 | L2 | B75 NC150 S250 | Amazon Microsoft | ✓ |
| 159 | Spiral Matrix | 54 | L2 | B75 NC150 S250 | Amazon Google Microsoft | ✓ |
| 160 | Set Matrix Zeroes | 73 | L3 | B75 NC150 S250 | Amazon Microsoft | ✓ |

---

## JS DSA Gotchas (Frontend sessions — read before solving)

All problems above are JS/TS-compatible. Key differences from Python that trip up frontend engineers:

```js
// ── No built-in heap ──────────────────────────────────────────────────────
// Simple approach for interviews: sorted array (ok for small k)
const minHeap = [];
const push = (val) => { minHeap.push(val); minHeap.sort((a,b) => a-b); }
const pop  = ()    => minHeap.shift();

// For real heap: implement with array (ask interviewer if you can use a library)
// In production: use 'heap-js' npm package

// ── Map vs Object ─────────────────────────────────────────────────────────
// Object: string keys only, prototype pollution risk
// Map: any key type, O(1) get/set, ordered insertion → always prefer for freq counting
const freq = new Map();
freq.set(key, (freq.get(key) ?? 0) + 1);
for (const [k, v] of freq) { /* ... */ }

// ── Set ──────────────────────────────────────────────────────────────────
const seen = new Set([1,2,3]);
seen.has(1);    // O(1)
seen.add(4);
seen.delete(1);

// ── Array sort is LEXICOGRAPHIC by default ───────────────────────────────
[10, 9, 2].sort();            // [10, 2, 9]  ❌ WRONG for numbers
[10, 9, 2].sort((a,b)=>a-b); // [2, 9, 10]  ✓

// ── Number precision ─────────────────────────────────────────────────────
Number.MAX_SAFE_INTEGER; // 9007199254740991 (2^53 - 1)
// Use BigInt for overflow-prone problems: BigInt(n), n ** 2n, etc.

// ── Infinity ─────────────────────────────────────────────────────────────
let min = Infinity, max = -Infinity;

// ── String operations ────────────────────────────────────────────────────
s.split('').reverse().join(''); // reverse a string
s.charCodeAt(0);                // char → ASCII (vs Python ord())
String.fromCharCode(65);        // ASCII → char (vs Python chr())

// ── BFS template ─────────────────────────────────────────────────────────
const queue = [start];
const visited = new Set([start]);
while (queue.length) {
  const node = queue.shift(); // O(n) — ok for interviews; for perf use pointer
  for (const nei of graph.get(node) ?? []) {
    if (!visited.has(nei)) { visited.add(nei); queue.push(nei); }
  }
}

// ── DFS / Recursion ──────────────────────────────────────────────────────
// Same as Python. Memoization:
const memo = new Map();
function dp(i, j) {
  const key = `${i},${j}`;
  if (memo.has(key)) return memo.get(key);
  const res = /* ... */;
  memo.set(key, res);
  return res;
}

// ── Deque (two-pointer / sliding window) ─────────────────────────────────
// No built-in deque. Use array with index pointer instead of shift():
let left = 0;
for (let right = 0; right < n; right++) {
  while (/* condition */) left++;
  // window is nums[left..right]
}
```

---

## Curated Mock Sets (Assessment Use)

Always check the Assessments tab for previously used problem numbers before picking.

**Assessment 1 (Day ~14) — L1/L2, Arrays + Strings + Hashmaps:**
Pick 2 unseen from: #4 (Group Anagrams), #6 (Product Except Self), #9 (Subarray Sum K), #8 (Longest Consecutive), #11 (Longest Substring)

**Assessment 2 (Day ~28) — L2, LL + Stack + Trees + Binary Search:**
Pick 2 unseen from: #51 (LRU Cache), #39 (Largest Rectangle), #67 (Level Order), #73 (Max Path Sum), #60 (Find Median Two Arrays)

**Assessment 3 (Day ~42) — L2/L3, Graphs + DP:**
DSA: Pick 2 unseen from: #84 (Rotting Oranges), #87 (Word Ladder), #85 (Pacific Atlantic), #92 (Alien Dictionary), #122 (Burst Balloons)
HLD: Design a system from hld-framework.md not used in a previous assessment

**Assessment 4 (Day ~56) — L3, Full mock:**
DSA: Pick 2 unseen from: #52 (Merge K Sorted), #129 (Find Median Stream), #92 (Alien Dictionary), #107 (Partition Equal Subset), #123 (Palindrome Partition II)
HLD: Full 45-min mock (previously unused system)
LLD: Pick from lld-framework.md Tier list (check Assessments tab for previously used problems)

**SDE3 Supplement (post Day 56 or for L3 users):**
#118 (Target Sum), #123 (Palindrome Partition II), #130 (IPO), #149 (Sudoku Solver), #87 (Word Ladder), #96 (Swim in Rising Water)
