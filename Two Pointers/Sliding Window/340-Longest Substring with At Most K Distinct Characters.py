"""
Given a string s and an integer k,
return the length of the longest substring of s that contains at most k distinct characters.



Example 1:
Input: s = "eceba", k = 2
Output: 3
Explanation: The substring is "ece" with length 3.

Example 2:
Input: s = "aa", k = 1
Output: 2
Explanation: The substring is "aa" with length 2.


Constraints:
1 <= s.length <= 5 * 104
0 <= k <= 50
"""
# At most k distinct characters: dictionary to store distinct values
# the length of the dictionary would be the total number of distinct values in the current window

class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        # to store the elements we visited,
        # the length of it would be the total number of distict elemnts
        visited = {}
        l = 0
        res = 0
        for r in range(len(s)):
            visited[s[r]] = 1 + visited.get(s[r], 0)

            while len(visited) > k:  # update l if the lenghth of vistied > k
                visited[s[l]] -= 1
                # we need to delete the element if value is 0:
                if visited[s[l]] == 0:
                    del visited[s[l]]
                l += 1

            res = max(res, r - l + 1)

        return res