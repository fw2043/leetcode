"""
Given an integer array nums of length n and an integer target,
find three integers in nums such that the sum is closest to target.
Return the sum of the three integers.
You may assume that each input would have exactly one solution.

Example 1:
Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

Example 2:
Input: nums = [0,0,0], target = 1
Output: 0

Constraints:
3 <= nums.length <= 1000
-1000 <= nums[i] <= 1000
-104 <= target <= 104
"""
# use one pointer i to lock one element and then check all the other elements 's
# possiblities using two pointers to check
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        # step 1: sort the array:
        nums.sort()
        # input: nums = [-4, -1, 2, 1]
        # initialzie result:
        result = nums[0] + nums[1] + nums[len(nums) - 1]

        for i, a in enumerate(nums):
            if i > 0 and a == nums[i - 1]:
                continue

            l, r = i + 1, len(nums) - 1
            while l < r:
                curVal = a + nums[l] + nums[r]
                if curVal == target:
                    return target
                if abs(curVal - target) < abs(result - target):
                    result = curVal
                if curVal < target:
                    l += 1
                else:
                    r -= 1
        return result
