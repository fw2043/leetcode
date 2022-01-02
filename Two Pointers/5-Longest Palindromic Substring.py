"""
Given a string s, return the longest palindromic substring in s.

Example 1:
Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.

Example 2:
Input: s = "cbbd"
Output: "bb"


Constraints:
1 <= s.length <= 1000
s consist of only digits and English letters.
"""


# Only consit alphanumeric: meaning alphabet letter (a-z) and numbers (0-9)
# Case sensitive?
# The goal is to find a substring which has the longest palindrome
# Brute Force: Time complexity: O(n^3) = n * n^2, for each character we need to check if the substring is palindrome
# Can we do it better?
# go through each character and for each character as center, we expand out-words to left and right
# to see if there is palindrome b <-a -> b (a is the center), if it is, then update the result
class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ''
        resLen = 0
        for i in range(len(s)):
            # odd length
            l = r = i
            while l >= 0 and r < len(s) and s[l] == s[r]:  # if it is the palindrome in the center of i
                if (r - l + 1) > resLen:  # if it is longer, then update the result
                    res = s[l: r + 1]
                    resLen = r - l + 1
                l -= 1
                r += 1

            # even length:
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:  # if it is the palindrome in the center of i
                if (r - l + 1) > resLen:  # if it is longer, then update the result
                    res = s[l: r + 1]
                    resLen = r - l + 1
                l -= 1
                r += 1

        return res
# Time complexity: O(n^2)
# Space complexity: O(n^2)
