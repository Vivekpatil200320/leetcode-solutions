"""
238. Product of Array Except Self  (Medium)
https://leetcode.com/problems/product-of-array-except-self/

Intuition:
    output[i] = (product of everything to the left of i) * (product of
    everything to the right of i). First pass fills each slot with the running
    left/prefix product; second pass (walking backwards) multiplies in the
    running right/postfix product. No division, and the output array doubles as
    the working buffer.

Time:  O(n)  - two linear passes
Space: O(1)  - excluding the output array (constraint-compliant)
"""

from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [1] * n

        for i in range(1, n):
            answer[i] = answer[i - 1] * nums[i - 1]

        r = 1
        for i in range(n - 1, -1, -1):
            answer[i] = answer[i] * r
            r = r * nums[i]

        return answer
