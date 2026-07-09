"""
347. Top K Frequent Elements  (Medium)
https://leetcode.com/problems/top-k-frequent-elements/

Intuition:
    Count each value's frequency in a hash map, then order the distinct values
    by frequency (descending) and take the first k.

Time:  O(n log n)  - counting is O(n); sorting the distinct values dominates
Space: O(n)        - frequency map over distinct values

Follow-up (optimal): the interview-preferred solutions avoid the full sort:
  - Bucket sort by frequency -> O(n) time.
  - A size-k min-heap over the frequency map -> O(n log k) time.
This categorizes under heaps because the heap approach is the target pattern;
the sort-based version below is correct and accepted, but revisit it with a
heap once comfortable.
"""


class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        maps = {}
        for num in nums:
            if num not in maps:
                maps[num] = 1
            else:
                maps[num] += 1
        return sorted(maps, key=lambda x: maps[x], reverse=True)[:k]
