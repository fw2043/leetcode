"""
Given an m x n integers matrix, return the length of the longest increasing path in matrix.

From each cell, you can either move in four directions: left, right, up, or down.
You may not move diagonally or move outside the boundary (i.e., wrap-around is not allowed).

Example 1:
Input: matrix = [[9,9,4],[6,6,8],[2,1,1]]
Output: 4
Explanation: The longest increasing path is [1, 2, 6, 9].

Example 2:
Input: matrix = [[3,4,5],[3,2,6],[2,2,1]]
Output: 4
Explanation: The longest increasing path is [3, 4, 5, 6]. Moving diagonally is not allowed.

Example 3:
Input: matrix = [[1]]
Output: 1

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 200
0 <= matrix[i][j] <= 231 - 1
"""
# at node 4, from 4--->9, we don't have to go from 9 to others, because we already did that: Memoization
# DFS + Memoization
# 0 <= matrix[i][j] <= 231 - 1

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        dp = {}  # (r,c): LIP( Longest Increasing Path) to avoid deplicate computation

        def dfs(r, c, prevVal):
            # stop points:
            if r >= rows or r < 0 or c >= cols or c < 0 or matrix[r][c] <= prevVal:
                return 0
            # if the node is already visited:
            if (r, c) in dp:
                return dp[(r, c)]
            # 4 directions check:
            res = 1
            res = max(res, 1 + dfs(r + 1, c, matrix[r][c]))
            res = max(res, 1 + dfs(r - 1, c, matrix[r][c]))
            res = max(res, 1 + dfs(r, c + 1, matrix[r][c]))
            res = max(res, 1 + dfs(r, c - 1, matrix[r][c]))
            dp[(r, c)] = res
            return res

        # do dfs for each node:
        for r in range(rows):
            for c in range(cols):
                # the values > 0, so set the preval = -1
                dfs(r, c, -1)

        return max(dp.values())

# Time complexity : O(mn). Each vertex/cell will be calculated once and only once, and each edge will be visited once and only once.
# Space complexity: O(mn).The cache dominates the space complexity.