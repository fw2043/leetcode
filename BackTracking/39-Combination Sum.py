"""
Given an array of distinct integers candidates and a target integer target,
return a list of all unique combinations of candidates where the chosen numbers sum to target.
You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times.
Two combinations are unique if the frequency of at least one of the chosen numbers is different.

It is guaranteed that the number of unique combinations that sum up to target is less than 150 combinations
for the given input.


Example 1:
Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Explanation:
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.

Example 2:
Input: candidates = [2,3,5], target = 8
Output: [[2,2,2,2],[2,3,3],[3,5]]

Example 3:
Input: candidates = [2], target = 1
Output: []


Constraints:
1 <= candidates.length <= 30
1 <= candidates[i] <= 200
All elements of candidates are distinct.
1 <= target <= 500
"""
#Combination Sum其实求的是一个subsets问题，在给定的数组中任意取几个数和为最后的target，这其中一个数可以被重复取。
#因此大致思路和subsets问题一致：
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(start, subset, total):
            if start >= len(candidates) and total != target:
                return
            if total == target:
                res.append(subset[:])
                return

            for i in range(start, len(candidates)):
                if total < target:
                    subset.append(candidates[i])
                    total += candidates[i]
                    # start from itself so that it can have duplicate
                    backtrack(i, subset, total)
                    subset.pop()
                    total -= candidates[i]

        res = []
        backtrack(0, [], 0)
        return res

# DFS
# how to limit duplicate computation, if the sum > target ---> stop
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, curr, total):
            if total == target:
                res.append(curr[:])
                return
            if total > target or i >= len(candidates):
                return
            # include candidates[i]
            curr.append(candidates[i])
            # updata total
            dfs(i, curr, total + candidates[i])
            # not include candidates[i]
            curr.pop()
            dfs(i + 1, curr, total)

        dfs(0, [], 0)
        return res



