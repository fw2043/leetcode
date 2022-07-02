"""
Given a string s, return true if the s can be palindrome after deleting at most one character from it.

Example 1:
Input: s = "aba"
Output: true
Example 2:

Input: s = "abca"
Output: true
Explanation: You could delete the character 'c'.
Example 3:

Input: s = "abc"
Output: false


Constraints:

1 <= s.length <= 105
s consists of lowercase English letters.
"""
# generally how to check if a string is panlidrone
# check the string, if found mismatch, then delete(move pointers) and check the substring
class Solution:
    def ispanlindrone(self, s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True

    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l < r:
            if s[l] != s[r]:
                return self.ispanlindrone(s, l + 1, r) or self.ispanlindrone(s, l, r - 1)
            l += 1
            r -= 1
        return True