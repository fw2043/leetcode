"""
Given an integer array nums that may contain duplicates, return all possible subsets (the power set).
The solution set must not contain duplicate subsets. Return the solution in any order.

Example 1:
Input: nums = [1,2,2]
Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]

Example 2:
Input: nums = [0]
Output: [[],[0]]


Constraints:
1 <= nums.length <= 10
-10 <= nums[i] <= 10
"""
# Backtrack
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        def backtrack(start, subset, counter):
            if start >= len(nums):
                return
            res.append(subset[:])
            for i in range(start, len(counter)):
                num, freq = counter[i]
                if freq <= 0:
                    continue
                subset.append(num)
                # update total and counter

                counter[i] = (num, freq - 1)
                backtrack(i, subset, counter)
                # backtrack
                subset.pop()
                counter[i] = (num, freq)

        res = []
        # sort the list
        nums.sort()
        counter = Counter(nums)
        counter = [(c, counter[c]) for c in counter]
        # counter = [(1, 2), (2, 1), (5, 1), (6, 1), (7, 1), (10, 1)]
        backtrack(0, [], counter)
        return res


# DFS
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        """  # decision tree:
                      o
                    /   \
                   /     \
                [1]      []
               /   \     / \
              /      \   /  \
            [1,2]   [1]  [2]  []
          /     \  not choose 2\  / \  / \
        [1,2,2] [1,2] [1,3] [1] [2,2] [2] [3] []
        /\ /\....................
        .....................
        if for decision dfs(1), we decide to either choose 2 or not, then the second time, we don't inlucde the second 2
        """
        res = []
        # sort the list, so we can skip later
        nums.sort()

        def dfs(i, subset):
            if i == len(nums):
                res.append(subset[:])
                return

            # all subsets that include nums[i]: left child
            subset.append(nums[i])
            dfs(i + 1, subset)

            subset.pop()
            # all subsets taht don't include nums[i]: right child
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            dfs(i + 1, subset)

        dfs(0, [])
        return res

