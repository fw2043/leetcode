"""
Given an integer array nums of unique elements, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.


Example 1:

Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
Example 2:

Input: nums = [0]
Output: [[],[0]]


Constraints:

1 <= nums.length <= 10
-10 <= nums[i] <= 10
All the numbers of nums are unique.
"""
# unique in solution set ----> no duplicate in soluntion subset, another example which can have duplicate in leetcode 90
# [1,3] and [3,1] are same, so if we check [1,3], we don't have to check [3,1]
# Backtracking

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        def backtrack(subset, start):
            # add subset to the result at every call
            res.append(subset[:])
            # end
            if start >= len(nums):
                return
            # parameter start can make sure we only check the element after the current one,
            # so that we have [1,3], we don't have to check [3,1]
            for i in range(start, len(nums)):
                subset.append(nums[i])
                backtrack(subset, i + 1)
                subset.pop()

        res = []
        backtrack([], 0)
        return res


# DFS:
# go through each item: dfs(0) ---> dfs(1)-----> dfs(i) until i > len(nums)
# for each item, we have two options: either include it to the subset or not
# from neetcode video

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
         o
      /    \
   [1]      []
   /  \        / \
[1, 2]  [1]   [2] []
/  \    /  \  / \ /\
[1,2,3] [1,2] [1,3] [1] [2,3] [2] [3] []

"""
        res = []
        subset = []

        def dfs(i):
            if i >= len(nums):
                res.append(subset[:])
                return
                # decision to include nums[i]:
            subset.append(nums[i])
            dfs(i + 1)

            # decision not to include nums[i]:
            subset.pop()
            dfs(i + 1)

        dfs(0)
        return res






