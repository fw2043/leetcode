"""
Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.

Letters are case sensitive, for example, "Aa" is not considered a palindrome here.


Example 1:
Input: s = "abccccdd"
Output: 7
Explanation:
One longest palindrome that can be built is "dccaccd", whose length is 7.

Example 2:
Input: s = "a"
Output: 1

Example 3:
Input: s = "bb"
Output: 2


Constraints:
1 <= s.length <= 2000
s consists of lowercase and/or uppercase English letters only.
"""
# Case sensetive
# only the midell one with odd length can only be unique, like "abccccdd", we can only use either a or b, not both
# all even + any of odd characters
# input: s = "abccccdd"
# Palindrome could be "dccaccd" or "dccbccd" ----> all even + one odd

class Solution:
    def longestPalindrome(self, s: str) -> int:
        # Step 1: Get the information of this string
        count = Counter(s)
        # count = {}
        # for char in s:
        #     if char in count.keys():
        #         count[char] += 1
        #     else:
        #         count[char] = 1
        # print(count)
        # Step 2: try to build a palindrome
        # If all the characters are even,
        result = 0
        mark = 0

        for i in count.keys():
            if count[i] % 2 == 1:  # odd
                mark += 1
            result += count[i] // 2

        return result * 2 + 1 if mark > 0 else result * 2