"""
Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.

Example 1:
Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]

Example 2:
Input: nums = [2,0,1]
Output: [0,1,2]
"""
"""Constraints:

n == nums.length
1 <= n <= 300
nums[i] is 0, 1, or 2.
"""
# edge case: if only one color

# Partition method
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        # global viarable
        self.k = 0
        """
        Do not return anything, modify nums in-place instead.
        """
        colors = [0, 1, 2]
        # partition the list:
        color = 0
        while color <= 2:
            self.partitionList(nums, color)
            color += 1

    def partitionList(self, nums: List[int], val):

        for i in range(len(nums)):
            # swap
            if nums[i] == val:
                nums[self.k], nums[i] = nums[i], nums[self.k]

                self.k += 1

# can we improve the method above to be: O(n) running time?
# one-pass: 3 buckets---> two pointers, one points to left, and another to right

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # partition/ bucket sort
        l, r = 0, len(nums) - 1
        i = 0
        while i <= r:
            # left bucket/case
            if nums[i] == 0:
                nums[l], nums[i] = nums[i], nums[l]
                l += 1
                i += 1
                # i >= l always true
            # right bucket/case
            elif nums[i] == 2:
                nums[r], nums[i] = nums[i], nums[r]
                r -= 1
                # decrease r
                # but not increase i, in case at the original r postition, it is 0,
                # then we have to swap it with l
            else:
                i += 1


