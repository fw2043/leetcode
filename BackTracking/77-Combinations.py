"""
Given two integers n and k, return all possible combinations of k numbers out of the range [1, n].

You may return the answer in any order.


Example 1:
Input: n = 4, k = 2
Output:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]

Example 2:
Input: n = 1, k = 1
Output: [[1]]


Constraints:

1 <= n <= 20
1 <= k <= n
"""
#  all possible combinations ----> brute force: recursion, dfs, backtracking
# combination is different to permutation
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        path = []

        def backtracking(start, path):
            if len(path) == k:
                # shalow copy in case the change for path later won't impact the result
                res.append(path.copy())
                return
            for i in range(start, n + 1):
                path.append(i)
                backtracking(i + 1, path)
                path.pop()

        backtracking(1, [])
        return res

