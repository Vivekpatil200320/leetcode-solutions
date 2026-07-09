"""
217. Contains Duplicate  (Easy)
https://leetcode.com/problems/contains-duplicate/

Intuition:
    Track seen values in a set. The first time a value reappears, we know a
    duplicate exists and can return early. If we finish the pass, every element
    was distinct.

Time:  O(n)  - single pass, O(1) average set membership check
Space: O(n)  - the `seen` set may hold up to n distinct values
"""


class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False
