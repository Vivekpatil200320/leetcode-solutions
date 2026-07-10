"""
36. Valid Sudoku  (Medium)
https://leetcode.com/problems/valid-sudoku/

Intuition:
    A board is valid if no digit repeats within any row, column, or 3x3 box.
    Track the digits seen in each row, each column, and each box (keyed by
    (r//3, c//3)). Walking every filled cell once, a value that's already in
    its row/column/box set means an immediate violation.

Time:  O(1)  - the board is fixed at 9x9, so at most 81 cells are visited
Space: O(1)  - the row/column/box sets hold at most 9 digits each
"""

from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = {}
        cols = {}
        boxes = {}

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue

                val = board[r][c]

                if val in rows.get(r, set()):
                    return False
                if val in cols.get(c, set()):
                    return False
                if val in boxes.get((r // 3, c // 3), set()):
                    return False

                rows[r] = rows.get(r, set()) | {val}
                cols[c] = cols.get(c, set()) | {val}
                boxes[(r // 3, c // 3)] = boxes.get((r // 3, c // 3), set()) | {val}

        return True
