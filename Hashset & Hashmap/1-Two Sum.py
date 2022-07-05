"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.



Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]


Constraints:
2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.
"""
# follow up what if the list is sorted: leetcode 167: two pointers



# Conform that there is alway one and only one valid answer
# You may not use the same element twice.
# Approach 1: Brute Force: O(n^2)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return (i, j)

# Approach 2: Hashmap with one pass: O(N)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # input = [2,7,11,15]
        # when we check 2,  9-2 = 5, then we need to find the index of 5
        # to do this we might need a hashmap to map value to index

        prevMap = {}  # val: index
        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i


