"""
271. Encode and Decode Strings  (Medium)
https://leetcode.com/problems/encode-and-decode-strings/

Intuition:
    Length-prefix encoding. Prepend each string with its length and a "#"
    delimiter: "5#hello3#abc". On decode, read digits up to the "#" to learn
    the length, then slice exactly that many characters — so the delimiter is
    never confused with "#" characters inside the payload.

Time:  O(n)  - n = total characters across all strings, for both encode/decode
Space: O(n)  - the encoded string / decoded list
"""

from typing import List


class Solution:
    def encode(self, strs: List[str]) -> str:
        result = ""
        for s in strs:
            result += str(len(s)) + "#" + s
        return result

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        while i < len(s):
            j = s.index("#", i)
            length = int(s[i:j])
            word = s[j + 1 : j + 1 + length]
            i = j + 1 + length
            result.append(word)
        return result
