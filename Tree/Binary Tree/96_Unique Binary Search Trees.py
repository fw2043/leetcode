"""
Given an integer n, return the number of structurally unique BST's (binary search trees)
which has exactly n nodes of unique values from 1 to n.

Example 1:
Input: n = 3
Output: 5
Example 2:

Input: n = 1
Output: 1


Constraints:

1 <= n <= 19
"""
# Similar to leetcode 95
# recursion:
# base case: 0 node, 1 node, 2 nodes ====> multiple base cases---> dictionary, and they might have duplicates
# recursion steps: for each root node: #_unique_left_sbutree * #_unique_right_subtree
# Time complexity: O(n^2)
# space complexity: O(n)

class Solution:
    def numTrees(self, n: int) -> int:
        ans = {0: 1, 1: 1, 2: 2}
        return self.helper(n, ans)

    def helper(self, n, ans):
        if n in ans:
            return ans[n]
        res = 0
        for i in range(n):
            res += self.helper(i, ans) * self.helper(n - i - 1, ans)

        ans[n] = res  # save running time
        return res