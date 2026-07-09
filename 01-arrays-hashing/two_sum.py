"""
1. Two Sum  (Easy)
https://leetcode.com/problems/two-sum/

Intuition:
    One pass with a hash map. For each number, check whether its complement
    (target - num) has already been seen. If so, we have our pair; otherwise
    record the current number and its index for future lookups.

Time:  O(n)  - single pass, O(1) average hash lookups
Space: O(n)  - the `seen` map may hold up to n entries
"""


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        seen = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i
