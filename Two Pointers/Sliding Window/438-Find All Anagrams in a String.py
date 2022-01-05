"""
Given two strings s and p, return an array of all the start indices of p's anagrams in s.
You may return the answer in any order.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
typically using all the original letters exactly once.

Example 1:
Input: s = "cbaebabacd", p = "abc"
Output: [0,6]
Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".

Example 2:
Input: s = "abab", p = "ab"
Output: [0,1,2]
Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".


Constraints:
1 <= s.length, p.length <= 3 * 104
s and p consist of lowercase English letters.
"""
# Input: s = "abab", p = "ab"
# Output: [0,1,2]
# The key is that # Anagram means each count for each character in both of words are same : 1a, 1b, 2c
# So two hashmap are equal!
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # The key is that # Anagram means each count for each character in both of words are same : 1a, 1b, 2c
        # two hashmap are equal!

        # edge case:
        if len(p) > len(s):
            return []

        # pcount = Counter(p)
        pcount, scount = {}, {}
        for i in range(len(p)):
            pcount[p[i]] = 1 + pcount.get(p[i], 0)
            scount[s[i]] = 1 + scount.get(s[i], 0)  # Initialize the sliding window

        res = [0] if scount == pcount else []

        l = 0
        for r in range(len(p), len(s)):  # r start from index of length of p
            scount[s[r]] = 1 + scount.get(s[r], 0)
            scount[s[l]] -= 1
            if scount[s[l]] == 0:
                scount.pop(s[l])
            l += 1  # keep the distance = the length of p
            if scount == pcount:
                res.append(l)
        return res


