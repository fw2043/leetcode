"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.



Example 1:
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Example 2:
Input: strs = [""]
Output: [[""]]

Example 3:
Input: strs = ["a"]
Output: [["a"]]


Constraints:
1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letters.
"""
# Confirm: does the order of my output matter? No
# Approach 1: Sort them
# if we sort them like eat and tea --> aet
# Time complexity: O(nlogn)
# Space complexy:  O(nlogn)

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) < 1:
            return strs
        ans = {}
        for i in range(len(strs)):  # Input: strs = ["eat","tea","tan","ate","nat","bat"]
            # sort string (tea), if sorted string(aet) existed, then append the original string ['eat', 'tea']
            orginal = strs[i]
            sorted_str = ''.join(sorted(orginal))  # sorted('eat') === ['a','e','t'], need to join them together
            if sorted_str in ans:  # append if exists
                ans[sorted_str].append(orginal)
            else:  # initialize if not exits, note: have to be list: [orginal]
                ans[sorted_str] = [orginal]

        return ans.values() # return values not the keys

