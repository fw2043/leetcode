"""
Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.
There is only one repeated number in nums, return this repeated number.
You must solve the problem without modifying the array nums and uses only constant extra space.

"""

##############################################################
# Solve by solution< similar to Koko loves eating banana
#########################
# you cannot modify the array, so we can't use sort method

"""
Binary Search
"""




"""
Hashmap
"""
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        visited = set()
        for i in range(0, len(nums)):
            if nums[i] not in visited:
                visited.add(nums[i])
            else:
                return nums[i]
        return -1
