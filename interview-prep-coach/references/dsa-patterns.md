# DSA Pattern Reference Notes

## How to Use This File
Claude reads this when you're in a concept revision or problem-solving session. Each pattern has: the core idea, when to recognize it, the template, and common pitfalls.

---

## 1. Sliding Window

**Core Idea:** Maintain a window [l, r] over an array/string. Expand right, shrink left when constraint violated.

**Recognize when:**
- "subarray/substring of size k"
- "longest/shortest subarray satisfying condition"
- "all substrings with property X"

**Template:**
```python
l = 0
for r in range(len(arr)):
    # add arr[r] to window
    while window_invalid():
        # remove arr[l] from window
        l += 1
    # update answer
```

**Pitfalls:** Forgetting to shrink window; off-by-one on window size; not tracking what's "in" the window.

---

## 2. Two Pointers

**Core Idea:** Two indices moving toward each other (or same direction) to reduce O(n²) to O(n).

**Recognize when:**
- Sorted array + pair/triplet sum
- Palindrome check
- Remove duplicates in-place

**Template:**
```python
l, r = 0, len(arr) - 1
while l < r:
    if condition: l += 1
    elif condition: r -= 1
    else: # found answer
```

---

## 3. Prefix Sum

**Core Idea:** presum[i] = sum of arr[0..i-1]. Range sum query = presum[r] - presum[l].

**Recognize when:** Multiple range sum queries; subarray sum equals k (use hashmap of prefix sums).

**Key trick:** `count of subarrays with sum k` → hashmap `{prefix_sum: count}`, look for `current_sum - k`.

---

## 4. Binary Search (on Answer)

**Core Idea:** Don't just search sorted arrays — search on the *answer space* when: answer is monotonic and you can check feasibility.

**Recognize when:**
- "minimum/maximum X such that condition holds"
- "kth smallest/largest"
- Anything with "capacity", "speed", "days"

**Template:**
```python
lo, hi = min_possible, max_possible
while lo < hi:
    mid = (lo + hi) // 2
    if feasible(mid):
        hi = mid
    else:
        lo = mid + 1
return lo
```

---

## 5. BFS / Level-Order

**Core Idea:** Queue-based traversal. Use when: shortest path in unweighted graph, level-by-level processing.

**Template:**
```python
from collections import deque
q = deque([start])
visited = {start}
while q:
    node = q.popleft()
    for neighbor in graph[node]:
        if neighbor not in visited:
            visited.add(neighbor)
            q.append(neighbor)
```

---

## 6. DFS (Iterative + Recursive)

**Core Idea:** Stack-based or recursive. Use for: connectivity, paths, cycle detection, topological sort.

**When to use recursive vs iterative:** Recursive is cleaner for trees; iterative avoids stack overflow for deep graphs.

---

## 7. Topological Sort

**Core Idea:** Order nodes in a DAG such that all edges go forward. Use Kahn's algorithm (BFS-based) or DFS-based.

**Recognize when:** "prerequisites", "order of tasks", "dependency resolution", "course schedule".

**Kahn's Template:**
```python
indegree = {node: 0 for node in graph}
for node in graph:
    for neighbor in graph[node]:
        indegree[neighbor] += 1

queue = deque([n for n in indegree if indegree[n] == 0])
order = []
while queue:
    node = queue.popleft()
    order.append(node)
    for neighbor in graph[node]:
        indegree[neighbor] -= 1
        if indegree[neighbor] == 0:
            queue.append(neighbor)
```

---

## 8. Union-Find (Disjoint Set Union)

**Core Idea:** Track which components nodes belong to. Union merges, Find checks connectivity.

**Recognize when:** Dynamic connectivity, "number of connected components", "redundant connection", Kruskal's MST.

**Template:**
```python
parent = list(range(n))
rank = [0] * n

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])  # path compression
    return parent[x]

def union(x, y):
    px, py = find(x), find(y)
    if px == py: return False
    if rank[px] < rank[py]: px, py = py, px
    parent[py] = px
    if rank[px] == rank[py]: rank[px] += 1
    return True
```

---

## 9. Dijkstra's Algorithm

**Core Idea:** Greedy shortest path for weighted graphs (non-negative weights). Min-heap of (dist, node).

**Template:**
```python
import heapq
dist = {node: float('inf') for node in graph}
dist[start] = 0
heap = [(0, start)]

while heap:
    d, node = heapq.heappop(heap)
    if d > dist[node]: continue
    for neighbor, weight in graph[node]:
        if dist[node] + weight < dist[neighbor]:
            dist[neighbor] = dist[node] + weight
            heapq.heappush(heap, (dist[neighbor], neighbor))
```

---

## 10. Monotonic Stack

**Core Idea:** Stack that maintains increasing or decreasing order. Helps find "next greater/smaller element".

**Recognize when:** Next greater element, daily temperatures, largest rectangle in histogram, trapping rain water.

**Template (next greater):**
```python
stack = []
result = [-1] * len(arr)
for i, val in enumerate(arr):
    while stack and arr[stack[-1]] < val:
        result[stack.pop()] = val
    stack.append(i)
```

---

## 11. Dynamic Programming — Common Patterns

### 1D DP (Fibonacci family)
`dp[i]` depends on `dp[i-1]`, `dp[i-2]`. House robber, climbing stairs.

### Grid DP
`dp[i][j]` depends on `dp[i-1][j]` and `dp[i][j-1]`. Unique paths, min path sum.

### Knapsack
Include/exclude decision. `dp[i][w]` = max value using first i items with weight limit w.

### Interval DP
`dp[i][j]` = answer for subarray/string from i to j. Burst balloons, palindrome partition.

### DP on Strings (LCS family)
`dp[i][j]` = answer using first i chars of s1 and first j chars of s2.

**Key insight:** When you see "optimal substructure" + "overlapping subproblems" → DP. Draw the recurrence before coding.

---

## 12. Backtracking Template

**Core Idea:** Build candidate solutions incrementally, abandon ("backtrack") when constraint violated.

**Recognize when:** Generate all subsets/permutations/combinations, N-Queens, Sudoku solver, word search.

```python
def backtrack(start, current):
    if base_case:
        result.append(current[:])
        return
    for choice in choices[start:]:
        current.append(choice)
        backtrack(next_start, current)
        current.pop()
```

---

## 13. Heap Patterns

**Top-K elements:** Min-heap of size K. Push each element; if size > K, pop.

**K-way merge:** Min-heap of (value, list_index, element_index). Always pop min, push next from same list.

**Two heaps (median finder):** Max-heap for lower half, min-heap for upper half. Balance sizes.

---

## 14. Intervals

**Sort by start time.** Then:
- **Merge:** if current.start <= prev.end → merge
- **Insert:** find position, merge overlaps
- **Meeting rooms:** sort, check if any overlap → use min-heap of end times for minimum rooms

---

## 15. Tree Patterns

**Any path problem:** Think "what does each node return to its parent?" vs "what does each node use from both children?"

**Diameter / max path sum:** At each node, compute left + right (both children) for global answer, but return max(left, right) + 1 to parent.

**LCA:** Two approaches — recursive (if node is p or q, return it) or binary lifting for repeated queries.

**Serialize/Deserialize:** Preorder traversal with null markers is cleanest.
