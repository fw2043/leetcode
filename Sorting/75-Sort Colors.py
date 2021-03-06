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
# Method 1:  3 colors/buckets, left: 0, right: 2, middle: 1, can we use two pointers to store and track left and right colors
# and iterating the list, to decide if we need to put it to left or right
#  nums = [2,0,2,1,1,0]
# Method 2 Or use a dictionary, 0:2, 1:2, 2:2
# then change the nums in place based on the dictionary

# Method 3: quick partition:
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # bucket partition
        def partition(val, nums):
            nonlocal k
            for i in range(len(nums)):
                if nums[i] == val:
                    nums[k], nums[i] = nums[i], nums[k]
                    k += 1

        k = 0
        color = 0
        while color <= 2:
            partition(color, nums)
            color += 1


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
        # the condition: i < r
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
                # but not increase i, in case at the original r position, it is 0,
                # then we have to swap it with l
            else:
                i += 1


