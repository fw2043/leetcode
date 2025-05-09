"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]]
such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.


Example 1:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]

Example 2:
Input: nums = []
Output: []

Example 3:
Input: nums = [0]
Output: []


Constraints:
0 <= nums.length <= 3000
-105 <= nums[i] <= 105
"""
# Notice that the solution set must not contain duplicate triplets.
# Brute Force ---> O(n^3)
# Can we try to target O(n^2)
# First sort the array: O(nlogn)
# Using the experience two sum II: leetcode 167
# step 1: sort the array: O(nlogn)
# step 2: for each item nums[i], check two sums for left, right pointers:  O(n^2)
# When three sums == target, how to update the pointers?---> only update one pointer, every loop only update one pointer
# what if the element equal to the previous one # will give you duplicate result, so skip
#  such that i != j, i != k, and j != k ---> each item only use once: move the pointer which you chose(l) above more steps until nums[l] != nums[l-1]
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Input: nums = [-1,0,1,2,-1,4]
        res = []
        # step 1: sort the list
        nums.sort()
        # nums = [-1, -1, 0, 1, 2, 4]
        # step 2: check for each element, the two sums problem
        for i, a in enumerate(nums):
            if i > 0 and a == nums[i - 1]: # can't use deplicates triplets
                continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                threeSums = a + nums[l] + nums[r]
                if threeSums < 0:
                    l += 1
                elif threeSums > 0:
                    r -= 1
                else: # find one, might have more options, how to update the pointer: only update one of the two pointers
                    res.append([a, nums[l] ,nums[r]])
                    # [-2, -2, 0, 0, 2,2], a= -2, left = 0, right = 2
                    l += 1
                    while nums[l] == nums[l - 1] and l < r: # only use once
                        l += 1
        return res
# Time conplexity: O(n^2)
# Space complexity: O(n)










































