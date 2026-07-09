"""
242. Valid Anagram  (Easy)
https://leetcode.com/problems/valid-anagram/

Intuition:
    Count each character in `s` (+1) and decrement for each character in `t`
    (-1). If the two strings are anagrams, every count nets out to zero. Any
    non-zero count means the letters don't match up.

Time:  O(n)  - two passes over the strings
Space: O(1)  - at most 26 lowercase-letter keys in the count map

Follow-up (Unicode): the same counting approach still works since the map keys
are arbitrary characters, not fixed to the 26-letter alphabet.
"""


class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        count = {}
        for c in s:
            count[c] = count.get(c, 0) + 1
        for c in t:
            count[c] = count.get(c, 0) - 1
        return all(v == 0 for v in count.values())
