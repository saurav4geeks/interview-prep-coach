#!/usr/bin/env python3
"""
Generate a date-mapped prep tracker for the interview-prep-coach skill.

Usage:
    python generate_schedule.py --start 2026-06-24 --weeks 10 \
        --assessments 2026-07-04,2026-07-18,2026-08-01,2026-08-15 \
        --out tracker.csv

Rules:
  - Weekday-type sessions (short) land Mon-Fri; weekend-type (long) land Sat/Sun.
  - Topics are drawn in order from the built-in sequence (edit below to customize).
  - Dates given in --assessments are marked as TEST WEEKEND rows.
The skill computes the assessment dates as the Saturdays nearest the end of
weeks 2, 4, 6, 8 if you don't pass --assessments.
"""
import argparse, csv
from datetime import date, timedelta

WEEKDAY_TOPICS = [
    "Sliding window - concept + 1 problem",
    "Two pointers - concept + 1 problem",
    "Prefix sum - concept + 1 problem",
    "Kadane's / subarray patterns + 1 problem",
    "Mixed array problem (untimed)",
    "Anagram / hashmap patterns + 1 problem",
    "Sliding window on strings + 1 problem",
    "Trie - concept + 1 problem",
    "String DP intro (LCS) + 1 problem",
    "Mixed string/hashmap problem",
    "Linked list pointer patterns (fast/slow reverse)",
    "Monotonic stack - concept + 1 problem",
    "Queue and deque patterns + 1 problem",
    "LRU Cache pattern (LL + hashmap)",
    "Mixed LL/stack problem",
    "Binary search on answer - concept + 1 problem",
    "BST patterns (validate LCA) + 1 problem",
    "Tree traversals (iterative DFS BFS) + 1 problem",
    "Tree DP (diameter max path sum) + 1 problem",
    "Mixed tree / binary search problem",
    "Graph BFS/DFS (islands components) + 1 problem",
    "Topological sort (course schedule) + 1 problem",
    "Dijkstra / shortest path + 1 problem",
    "Union-Find - concept + 1 problem",
    "Mixed graph problem",
    "DP 1D (house robber family) + 1 problem",
    "DP 2D grid (unique paths) + 1 problem",
    "Knapsack pattern + 1 problem",
    "Interval / string DP + 1 problem",
    "Mixed DP problem",
    "Heap patterns (top-K merge K) + 1 problem",
    "Intervals (merge meeting rooms) + 1 problem",
    "Greedy patterns + 1 problem",
    "Two heaps (median finder) + 1 problem",
    "Mixed heap/greedy problem",
    "Backtracking template (subsets permutations)",
    "Backtracking with pruning (N-Queens) + 1 problem",
    "Bit manipulation tricks + 1 problem",
    "Math patterns (sieve GCD modular) + 1 problem",
    "LLD intro: SOLID principles + Parking Lot",
]

WEEKEND_TOPICS = [
    "DSA block: 3 array problems (easy-med-hard)",
    "HLD intro: pillars + Design a URL Shortener",
    "DSA block: 3 hashmap/string problems",
    "HLD: Design Pastebin / Key-Value Store",
    "DSA block: 3 stack/queue/LL problems",
    "HLD: Design a Rate Limiter (token bucket Redis)",
    "DSA block: 3 tree + binary search problems",
    "HLD: Design a Notification System (Kafka fan-out)",
    "DSA block: 3 graph problems (BFS-topo-Dijkstra)",
    "HLD: Design Search Autocomplete (trie caching)",
    "DSA block: 3 DP problems",
    "HLD: Design Twitter Feed (fanout strategies)",
    "DSA block: 3 heap/interval/greedy problems",
    "HLD: Design Distributed Cache (consistent hashing)",
    "LLD deep dive: BookMyShow / Library System",
    "HLD: Design WhatsApp/Chat (WebSockets queues)",
    "Revision: weakest flagged topics",
    "Mock: full HLD end-to-end (45 min)",
    "Mock review + final gaps + confidence check",
    "Buffer / catch-up session",
]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--start", required=True, help="YYYY-MM-DD, Day 1")
    ap.add_argument("--weeks", type=int, default=10)
    ap.add_argument("--assessments", default="", help="comma-separated YYYY-MM-DD")
    ap.add_argument("--out", default="tracker.csv")
    args = ap.parse_args()

    start = date.fromisoformat(args.start)
    assess = set()
    if args.assessments:
        assess = {date.fromisoformat(s) for s in args.assessments.split(",")}

    rows, wd_i, we_i, d, day = [], 0, 0, start, 1
    end = start + timedelta(days=args.weeks * 7 - 1)
    while d <= end:
        week = ((d - start).days // 7) + 1
        if d in assess:
            topic, stype = "TEST WEEKEND - timed mock assessment (scored and logged)", "Assessment"
        elif d.weekday() >= 5:
            topic = WEEKEND_TOPICS[we_i] if we_i < len(WEEKEND_TOPICS) else "Buffer / revision"
            we_i += 1; stype = "Weekend (2-3 hr)"
        else:
            topic = WEEKDAY_TOPICS[wd_i] if wd_i < len(WEEKDAY_TOPICS) else "Revision / extra problems"
            wd_i += 1; stype = "Weekday (30-45 min)"
        rows.append([day, d.strftime("%a %d %b %Y"), f"W{week}", stype, topic, "", "", "", "", ""])
        day += 1; d += timedelta(days=1)

    with open(args.out, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["Day #", "Date", "Week", "Session Type", "Planned Topic",
                    "Completed (Y/P/N/Rest)", "Time (min)", "Problems", "Self-Rating (1-5)", "Notes"])
        w.writerows(rows)
    print(f"Wrote {len(rows)} rows to {args.out} ({start} .. {end})")


if __name__ == "__main__":
    main()
