"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
typically using all the original letters exactly once.


Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false


Constraints:

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.
"""
# Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase:
# ege case: if the length is different: false
# sort them and compare
# Counter
# Approach 1: Sort them and compare
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        # O(nlogn)
        s =sorted(s)
        t = sorted(t)
        for i in range(len(s)):
            if s[i] != t[i]:
                return False
        return True

# Approach 2: Counter/hashmap
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        # counts = Counter(s)
        counts = {}
        for ch in s:
            counts[ch] = counts.get(ch, 0) + 1

        for ch in t:
            if ch in counts:
                counts[ch] -= 1
            else:
                return False

        # check if the values in counts are 0
        for value in counts.values():
            if value != 0:
                return False
        return True