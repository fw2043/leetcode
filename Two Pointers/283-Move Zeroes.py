"""
Given an integer array nums, move all 0's to the end of it
while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

Example 1:
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]

Example 2:
Input: nums = [0]
Output: [0]


Constraints:
1 <= nums.length <= 104
-231 <= nums[i] <= 231 - 1

Follow up: Could you minimize the total number of operations done?
"""
# In-place operation: two pointers
# maintaining the relative order of the non-zero elements.
# check every non-zero element and move them to the begin of the list:
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # input: [0,1,0,3,12]
        i = p = 0
        while p < len(nums):
            if nums[p] != 0:
                nums[i] = nums[p]
                i += 1
            p += 1
        # now the new list: [1,3,12,3,12]
        while i < len(nums):
            nums[i] = 0
            i += 1
# Or exchange
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # input: [0,1,0,3,12]
        i = 0
        for p in range(len(nums)):
            if nums[p]:
                nums[i], nums[p] = nums[p], nums[i]
                i += 1


