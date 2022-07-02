"""
Given a collection of candidate numbers (candidates) and a target number (target),
find all unique combinations in candidates where the candidate numbers sum to target.

Each number in candidates may only be used once in the combination.
Note: The solution set must not contain duplicate combinations.



Example 1:
Input: candidates = [10,1,2,7,6,1,5], target = 8
Output:
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]

Example 2:
Input: candidates = [2,5,2,1,2], target = 5
Output:
[
[1,2,2],
[5]
]

Constraints:
1 <= candidates.length <= 100
1 <= candidates[i] <= 50
1 <= target <= 30
"""
# Combination Sum II则是每个数只能取一次，这就和最原始的题一样，那么pos递归传递的就是pos+1；
# 第二个不同是数组中可能有重复的数，维护一个visited辅助数组。
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        def backtrack(start, subset, total, counter):
            if start >= len(candidates) and total != target:
                return
            if total == target:
                res.append(subset[:])
                return
            for i in range(start, len(counter)):
                candidate, freq = counter[i]
                if total < target:
                    if freq <= 0:
                        continue
                    subset.append(candidate)
                    # update total and counter
                    total += candidate
                    counter[i] = (candidate, freq - 1)
                    backtrack(i, subset, total, counter)
                    # backtrack
                    subset.pop()
                    total -= candidate
                    counter[i] = (candidate, freq)

        res = []
        # sort the list
        candidates.sort()
        counter = Counter(candidates)
        counter = [(c, counter[c]) for c in counter]
        # counter = [(1, 2), (2, 1), (5, 1), (6, 1), (7, 1), (10, 1)]
        backtrack(0, [], 0, counter)
        return res

