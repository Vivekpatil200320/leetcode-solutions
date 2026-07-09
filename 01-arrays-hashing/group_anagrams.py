"""
49. Group Anagrams  (Medium)
https://leetcode.com/problems/group-anagrams/

Intuition:
    Anagrams share the same sorted letters, so the sorted string is a canonical
    key. Bucket every word under its sorted-letter key; each bucket is one
    anagram group.

Time:  O(n * k log k)  - n words, sorting each word of length k
Space: O(n * k)        - all words stored across the buckets

Note: LeetCode's judge pre-imports `defaultdict`; the explicit import below
keeps this file runnable on its own.
"""

from collections import defaultdict


class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        grp = defaultdict(list)
        for word in strs:
            key = tuple(sorted(word))
            grp[key].append(word)
        return list(grp.values())
