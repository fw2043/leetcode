"""
Given an array nums of distinct integers, return all the possible permutations.
You can return the answer in any order.

Example 1:
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

Example 2:
Input: nums = [0,1]
Output: [[0,1],[1,0]]

Example 3:
Input: nums = [1]
Output: [[1]]


Constraints:

1 <= nums.length <= 6
-10 <= nums[i] <= 10
All the integers of nums are unique.
"""
# ##################################################
"""
求一个数组的全排列，思路就是将数组当做一个池子，
第一次取出一个数，
然后在池子里剩下的数中再任意取一个数此时组成两个数，
然后再在池子中剩下的数里取数，直到无数可取，即取完一次，形成一个排列。
"""
# very important confirmation that: distinct integers, otherwise we can not use this method,
# check leetcode 47
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """

                    o
                   / \  \
                 /    \   \
                /      \    \
            1           2     3
        /    \        /  \   /  \
        2     3      1    3  1   2
       /      /      /    \  \    \
       3      2      3    1   2    1

   """
        def backtrack(subset):
            # base case:
            if len(subset) == len(nums):
                res.append(subset[:])
                # subset: the number(s) are choosen, nums: all the numbers in the pool
            for i in range(len(nums)):
                # only choose the number which has not been choosen yet,
                # because the numbers in the pool is distinct
                if nums[i] in subset:
                    continue
                subset.append(nums[i])
                backtrack(subset)
                # from [1,2,3] to [1,2], to [1], then go to [1,3,2], then.......
                subset.pop()

        res = []
        backtrack([])
        return res