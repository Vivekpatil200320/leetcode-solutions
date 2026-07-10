#!/usr/bin/env python3
"""
Progress dashboard generator for the LeetCode solutions repo.

Scans every category folder for solved problems (identified by the
"<number>. <title> (<difficulty>)" line in each file's docstring), then
regenerates the visual progress section of README.md between the
<!-- PROGRESS:START --> and <!-- PROGRESS:END --> markers.

Run from the repo root:
    python3 scripts/generate_progress.py

"Solved" is matched by problem number, so a file counts no matter which
folder it lives in. Add a problem to the CATALOG below to make it show up as
"unsolved" until its solution file exists.
"""

import os
import re
from datetime import datetime, timezone

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Difficulty presentation
DIFF_ORDER = {"Easy": 0, "Medium": 1, "Hard": 2}
DIFF_ICON = {"Easy": "🟢", "Medium": "🟡", "Hard": "🔴"}
DIFF_COLOR = {"Easy": "2ea043", "Medium": "d29922", "Hard": "f85149"}

# NeetCode-75-style catalog grouped by repo category.
# (problem_number, title, difficulty)
CATALOG = [
    ("01-arrays-hashing", "Arrays & Hashing", [
        (217, "Contains Duplicate", "Easy"),
        (242, "Valid Anagram", "Easy"),
        (1, "Two Sum", "Easy"),
        (49, "Group Anagrams", "Medium"),
        (347, "Top K Frequent Elements", "Medium"),
        (271, "Encode and Decode Strings", "Medium"),
        (238, "Product of Array Except Self", "Medium"),
        (128, "Longest Consecutive Sequence", "Medium"),
    ]),
    ("02-two-pointers", "Two Pointers", [
        (125, "Valid Palindrome", "Easy"),
        (15, "3Sum", "Medium"),
        (11, "Container With Most Water", "Medium"),
    ]),
    ("03-sliding-window", "Sliding Window", [
        (121, "Best Time to Buy and Sell Stock", "Easy"),
        (3, "Longest Substring Without Repeating Characters", "Medium"),
        (424, "Longest Repeating Character Replacement", "Medium"),
        (76, "Minimum Window Substring", "Hard"),
    ]),
    ("04-stack", "Stack", [
        (20, "Valid Parentheses", "Easy"),
        (155, "Min Stack", "Medium"),
        (150, "Evaluate Reverse Polish Notation", "Medium"),
        (739, "Daily Temperatures", "Medium"),
        (239, "Sliding Window Maximum", "Hard"),
        (84, "Largest Rectangle in Histogram", "Hard"),
    ]),
    ("05-binary-search", "Binary Search", [
        (704, "Binary Search", "Easy"),
        (153, "Find Minimum in Rotated Sorted Array", "Medium"),
        (33, "Search in Rotated Sorted Array", "Medium"),
    ]),
    ("06-linked-list", "Linked List", [
        (206, "Reverse Linked List", "Easy"),
        (21, "Merge Two Sorted Lists", "Easy"),
        (141, "Linked List Cycle", "Easy"),
        (143, "Reorder List", "Medium"),
        (19, "Remove Nth Node From End of List", "Medium"),
        (2, "Add Two Numbers", "Medium"),
    ]),
    ("07-trees", "Trees", [
        (226, "Invert Binary Tree", "Easy"),
        (104, "Maximum Depth of Binary Tree", "Easy"),
        (100, "Same Tree", "Easy"),
        (572, "Subtree of Another Tree", "Easy"),
        (235, "Lowest Common Ancestor of a BST", "Medium"),
        (102, "Binary Tree Level Order Traversal", "Medium"),
        (98, "Validate Binary Search Tree", "Medium"),
        (105, "Construct Binary Tree from Preorder and Inorder", "Medium"),
        (236, "Lowest Common Ancestor of a Binary Tree", "Medium"),
        (297, "Serialize and Deserialize Binary Tree", "Hard"),
        (124, "Binary Tree Maximum Path Sum", "Hard"),
    ]),
    ("08-tries", "Tries", [
        (208, "Implement Trie (Prefix Tree)", "Medium"),
        (211, "Design Add and Search Words Data Structure", "Medium"),
        (212, "Word Search II", "Hard"),
    ]),
    ("09-heap-priority-queue", "Heap / Priority Queue", [
        (1046, "Last Stone Weight", "Easy"),
        (215, "Kth Largest Element in an Array", "Medium"),
        (295, "Find Median from Data Stream", "Hard"),
        (23, "Merge k Sorted Lists", "Hard"),
    ]),
    ("10-backtracking", "Backtracking", [
        (78, "Subsets", "Medium"),
        (39, "Combination Sum", "Medium"),
        (46, "Permutations", "Medium"),
        (79, "Word Search", "Medium"),
        (51, "N-Queens", "Hard"),
    ]),
    ("11-graphs", "Graphs", [
        (200, "Number of Islands", "Medium"),
        (133, "Clone Graph", "Medium"),
        (207, "Course Schedule", "Medium"),
        (994, "Rotting Oranges", "Medium"),
        (417, "Pacific Atlantic Water Flow", "Medium"),
    ]),
    ("12-advanced-graphs", "Advanced Graphs", [
        (743, "Network Delay Time", "Medium"),
        (127, "Word Ladder", "Hard"),
    ]),
    ("13-dp-1d", "1-D Dynamic Programming", [
        (70, "Climbing Stairs", "Easy"),
        (198, "House Robber", "Medium"),
        (322, "Coin Change", "Medium"),
        (300, "Longest Increasing Subsequence", "Medium"),
    ]),
    ("14-dp-2d", "2-D Dynamic Programming", [
        (62, "Unique Paths", "Medium"),
        (1143, "Longest Common Subsequence", "Medium"),
        (72, "Edit Distance", "Medium"),
    ]),
    ("15-greedy", "Greedy", [
        (53, "Maximum Subarray", "Medium"),
        (55, "Jump Game", "Medium"),
        (134, "Gas Station", "Medium"),
    ]),
    ("16-intervals", "Intervals", [
        (57, "Insert Interval", "Medium"),
        (56, "Merge Intervals", "Medium"),
        (435, "Non-overlapping Intervals", "Medium"),
    ]),
    ("17-math-geometry", "Math & Geometry", [
        (48, "Rotate Image", "Medium"),
        (54, "Spiral Matrix", "Medium"),
        (73, "Set Matrix Zeroes", "Medium"),
    ]),
    ("18-bit-manipulation", "Bit Manipulation", [
        (136, "Single Number", "Easy"),
        (191, "Number of 1 Bits", "Easy"),
        (338, "Counting Bits", "Easy"),
        (190, "Reverse Bits", "Easy"),
    ]),
]

DOC_RE = re.compile(r"(\d+)\.\s+.*?\((Easy|Medium|Hard)\)")


def find_solved():
    """Return a dict {problem_number: (title, difficulty, relpath)} by scanning files."""
    solved = {}
    for entry in sorted(os.listdir(REPO_ROOT)):
        cat_dir = os.path.join(REPO_ROOT, entry)
        if not os.path.isdir(cat_dir) or not re.match(r"\d{2}-", entry):
            continue
        for fname in sorted(os.listdir(cat_dir)):
            if not fname.endswith(".py"):
                continue
            path = os.path.join(cat_dir, fname)
            with open(path, encoding="utf-8") as f:
                head = f.read(600)
            m = DOC_RE.search(head)
            if m:
                num = int(m.group(1))
                solved[num] = os.path.join(entry, fname)
    return solved


def bar(done, total, width=22):
    if total == 0:
        return "░" * width
    filled = round(width * done / total)
    return "█" * filled + "░" * (width - filled)


def pct(done, total):
    return 0 if total == 0 else round(100 * done / total)


def badge(label, value, color):
    label = label.replace(" ", "%20").replace("-", "--")
    value = str(value).replace(" ", "%20").replace("-", "--")
    return f"![{label}](https://img.shields.io/badge/{label}-{value}-{color})"


def build_dashboard(solved):
    total_problems = sum(len(probs) for _, _, probs in CATALOG)
    total_solved = 0
    diff_counts = {"Easy": [0, 0], "Medium": [0, 0], "Hard": [0, 0]}  # [solved, total]

    for _, _, probs in CATALOG:
        for num, _, diff in probs:
            diff_counts[diff][1] += 1
            if num in solved:
                total_solved += 1
                diff_counts[diff][0] += 1

    lines = []
    lines.append("<!-- PROGRESS:START -->")
    lines.append("")
    lines.append("## 📊 Progress Dashboard")
    lines.append("")
    lines.append(
        badge("Solved", f"{total_solved}%2F{total_problems}", "1f6feb")
        + " "
        + badge("Easy", f"{diff_counts['Easy'][0]}%2F{diff_counts['Easy'][1]}", DIFF_COLOR["Easy"])
        + " "
        + badge("Medium", f"{diff_counts['Medium'][0]}%2F{diff_counts['Medium'][1]}", DIFF_COLOR["Medium"])
        + " "
        + badge("Hard", f"{diff_counts['Hard'][0]}%2F{diff_counts['Hard'][1]}", DIFF_COLOR["Hard"])
    )
    lines.append("")
    lines.append("```text")
    lines.append(f"Overall   {bar(total_solved, total_problems)}  {total_solved}/{total_problems}  ({pct(total_solved, total_problems)}%)")
    lines.append(f"Easy      {bar(*diff_counts['Easy'])}  {diff_counts['Easy'][0]}/{diff_counts['Easy'][1]}")
    lines.append(f"Medium    {bar(*diff_counts['Medium'])}  {diff_counts['Medium'][0]}/{diff_counts['Medium'][1]}")
    lines.append(f"Hard      {bar(*diff_counts['Hard'])}  {diff_counts['Hard'][0]}/{diff_counts['Hard'][1]}")
    lines.append("```")
    lines.append("")

    # Category table
    lines.append("### By Category")
    lines.append("")
    lines.append("| Category | Progress | Solved |")
    lines.append("| :-- | :-- | :-: |")
    for _, name, probs in CATALOG:
        done = sum(1 for num, _, _ in probs if num in solved)
        lines.append(f"| {name} | `{bar(done, len(probs), 16)}` | {done}/{len(probs)} |")
    lines.append("")

    # Per-category checklists
    lines.append("### Problem Checklist")
    lines.append("")
    for folder, name, probs in CATALOG:
        done = sum(1 for num, _, _ in probs if num in solved)
        status = "✅" if done == len(probs) else ("🔸" if done else "⬜")
        lines.append(f"<details><summary>{status} <b>{name}</b> &nbsp;·&nbsp; {done}/{len(probs)}</summary>")
        lines.append("")
        for num, title, diff in sorted(probs, key=lambda p: (DIFF_ORDER[p[2]], p[0])):
            check = "x" if num in solved else " "
            slug = "-".join(re.sub(r"[^a-z0-9 ]", "", title.lower()).split())
            link = f"https://leetcode.com/problems/{slug}/"
            if num in solved:
                loc = solved[num]
                lines.append(f"- [x] {DIFF_ICON[diff]} **[{num}. {title}]({link})** &nbsp;→&nbsp; [`{loc}`]({loc})")
            else:
                lines.append(f"- [ ] {DIFF_ICON[diff]} [{num}. {title}]({link})")
        lines.append("")
        lines.append("</details>")
        lines.append("")

    stamp = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    lines.append(f"<sub>Auto-generated by `scripts/generate_progress.py` · last updated {stamp}</sub>")
    lines.append("")
    lines.append("<!-- PROGRESS:END -->")
    return "\n".join(lines)


def inject(readme_path, dashboard):
    with open(readme_path, encoding="utf-8") as f:
        content = f.read()
    pattern = re.compile(r"<!-- PROGRESS:START -->.*?<!-- PROGRESS:END -->", re.DOTALL)
    if pattern.search(content):
        content = pattern.sub(dashboard, content)
    else:
        # Insert after the first heading block (before "## Approach") if markers absent
        marker = "\n## Approach"
        idx = content.find(marker)
        if idx == -1:
            content = content.rstrip() + "\n\n" + dashboard + "\n"
        else:
            content = content[:idx] + "\n" + dashboard + "\n" + content[idx:]
    with open(readme_path, "w", encoding="utf-8") as f:
        f.write(content)


def main():
    solved = find_solved()
    dashboard = build_dashboard(solved)
    inject(os.path.join(REPO_ROOT, "README.md"), dashboard)
    total = sum(len(p) for _, _, p in CATALOG)
    print(f"Updated README.md — {len(solved)} solved / {total} cataloged.")


if __name__ == "__main__":
    main()
