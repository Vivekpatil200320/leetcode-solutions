# 75-Day DSA Roadmap → Repo Mapping

This file maps the **75-Day DSA Roadmap** to the **18-category repo structure**. Use this as your study guide while keeping the conceptual organization of the repo (each folder is a distinct pattern, not just a time block).

---

## Days 1–6: Foundations
*Complexity analysis, recursion fundamentals, understand Big-O. No code yet — mostly theory and review.*

**Repo focus:** None (these are prerequisites)

**Action:** Watch NeetCode's "Big O Notation" video, then solve 1–2 warm-up problems from any folder to refresh.

---

## Days 7–12: Arrays, Strings & Hashing
*Master hash maps, frequency counting, prefix/suffix patterns, in-place mutations.*

**Repo folders:**
- `01-arrays-hashing/` (solve 5–6 problems)

**Problems to solve:**
- Two Sum
- Group Anagrams
- Product of Array Except Self
- Subarray Sum Equals K
- (Pick 1–2 more from the folder)

---

## Days 13–18: Two Pointers & Sliding Window
*Learn opposite and same-direction pointer techniques. Fixed and variable-size windows.*

**Repo folders:**
- `02-two-pointers/` (solve 3–4 problems)
- `03-sliding-window/` (solve 3–4 problems)

**Problems to solve:**
- Three Sum
- Container With Most Water
- Longest Substring Without Repeating Characters
- Minimum Window Substring

---

## Days 19–24: Linked Lists
*Dummy nodes, pointer rewiring, cycle detection, reversal, merging.*

**Repo folders:**
- `06-linked-list/` (solve 5–6 problems)

**Problems to solve:**
- Reverse Linked List
- Merge Two Sorted Lists
- Linked List Cycle
- Reorder List

---

## Days 25–30: Stacks & Queues
*LIFO/FIFO processing, monotonic stacks, expression evaluation, queue-based simulation.*

**Repo folders:**
- `04-stack/` (solve 5–6 problems)

**Problems to solve:**
- Valid Parentheses
- Min Stack
- Evaluate Reverse Polish Notation
- Daily Temperatures
- Sliding Window Maximum
- Largest Rectangle in Histogram

---

## Days 31–36: Trees (Basic)
*DFS/BFS traversals, BST properties, tree depth, symmetry, LCA of BST.*

**Repo folders:**
- `07-trees/` (solve 5–6 problems from "Basic" subset)

**Problems to solve:**
- Maximum Depth of Binary Tree
- Invert Binary Tree
- Validate Binary Search Tree
- Binary Tree Level Order Traversal

---

## Days 37–42: Trees (Advanced)
*Tree construction, path sum, serialization, subtree matching, tree-to-linked-list.*

**Repo folders:**
- `07-trees/` (solve 5–6 problems from "Advanced" subset)

**Problems to solve:**
- Serialize and Deserialize Binary Tree
- Lowest Common Ancestor of Binary Tree
- Binary Tree Maximum Path Sum

---

## Days 43–48: Backtracking
*State space exploration, decision trees, pruning, permutations, subsets, word search.*

**Repo folders:**
- `10-backtracking/` (solve 6 problems)

**Problems to solve:**
- Subsets
- Permutations
- Combination Sum
- Word Search

---

## Days 49–54: Heaps & Tries
*Min/max heaps, top-K patterns, two-heap problems, K-way merging, trie construction and search.*

**Repo folders:**
- `09-heap-priority-queue/` (solve 3–4 problems)
- `08-tries/` (solve 2–3 problems)

**Problems to solve:**
- Kth Largest Element in an Array
- Top K Frequent Elements
- Merge K Sorted Lists
- Implement Trie (Prefix Tree)

---

## Days 55–60: Graphs
*Graph representation, DFS/BFS, connected components, topological sort, shortest path, grid problems.*

**Repo folders:**
- `11-graphs/` (solve 3–4 problems)
- `12-advanced-graphs/` (solve 2–3 problems)

**Problems to solve:**
- Number of Islands
- Clone Graph
- Course Schedule
- Rotting Oranges
- Network Delay Time

---

## Days 61–66: Dynamic Programming & Greedy
*Memoization vs. tabulation, 1D DP, 2D DP, knapsack patterns, greedy choice property.*

**Repo folders:**
- `13-dp-1d/` (solve 2–3 problems)
- `14-dp-2d/` (solve 2–3 problems)
- `15-greedy/` (solve 1–2 problems)

**Problems to solve:**
- House Robber
- Coin Change
- Longest Common Subsequence
- Jump Game

---

## Days 67–71: Company-Style Interview Practice
*Mock interview conditions. Clarify → brute force → pattern → optimize → clean code.*

**Repo folders:**
- All folders (pick 10 problems you found hardest so far; re-solve from memory)

**Action:**
- Pick one problem from each major category
- Solve it on a whiteboard (paper or Coderpad, no IDE autocomplete)
- Write clean, production-ready code
- Explain time/space complexity out loud
- Identify edge cases
- Target: 45–60 minutes per problem

---

## Days 72–75: Final Interview Sprint
*Timed mocks. Fast pattern recognition. Verbal explanations. Calm recovery from stuck states.*

**Repo folders:**
- All folders (pick problems you've solved before; re-solve under time pressure)

**Action:**
- Day 72: Timed mock #1 (3 problems in 90 minutes)
- Day 73: Review mistakes, drill weak patterns
- Day 74: Timed mock #2 (3 problems in 90 minutes, with verbal explanation)
- Day 75: Light review, templates, complexity cheatsheet

---

## How to Use This Mapping

1. **Follow the day blocks.** Each week, focus on the folder(s) listed for that day range.
2. **Solve in order within each folder.** The problems are sequenced by difficulty and progression within each pattern.
3. **Don't skip days.** The order matters — two-pointers requires understanding arrays first, graphs require understanding trees first.
4. **Track your progress.** Mark problems as solved in the folder.
5. **Re-solve hard problems.** If you get stuck, review the pattern, then solve it again from memory 2–3 days later.

---

## Interview Day Reminders

- **Clarify before coding:** Ask about constraints, examples, edge cases.
- **Brute force first:** Show you understand the problem, even if slow.
- **Optimize step-by-step:** "I notice this is O(n²). Can I use a hash map to make it O(n)?"
- **Clean code:** Variable names matter. Comments for non-obvious logic.
- **Complexity by memory:** State time and space complexity *before* you code.
- **Test edge cases:** Empty input, single element, duplicates, negative numbers, etc.

Good luck! 🎯
