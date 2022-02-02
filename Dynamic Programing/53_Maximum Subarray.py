"""
Given an integer array nums, find the contiguous subarray (containing at least one number)
which has the largest sum and return its sum.
A subarray is a contiguous part of an array.

Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

Example 2:
Input: nums = [1]
Output: 1

Example 3:
Input: nums = [5,4,-1,7,8]
Output: 23


Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104


Follow up: If you have figured out the O(n) solution,
try coding another solution using the divide and conquer approach, which is more subtle.
"""
#Try to write sudo for brute force:
# O(n^3)
import math
import List
def maxSubArray(self, nums: List[int]) -> int:
    n = len(nums)
    for i in range(0,n-1):   # the start point
        for j in range(0, n-1): # the end point
        #           for k in range(i, j+1): # represent subarrays
                   #     sum = nums[i] +......nums[j]
# 两层 for 循环，每个循环处理中，又计算了子数组的和，所以叠加起来实际上是三层 for 循环。

# 前缀和优化 O(N^2)
"""既然复杂度太高，就要想方法区去降维，把三层 for 循环，降低到一层循环。换句话讲，就是要把循环处理中的冗余计算，给精简掉。

其实从上面的推导中，不难发现，连续子数组的和，实际上是两个「前缀和」相减。即


sum(i, j) = pre_sum(j) - pre_sum(i - 1)
因此，如果提前计算好前缀和，那么计算子数组元素之和的第三层 for 循环就可以省去。即时间复杂度降低到 O(N^2)

"""
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_subarray = -math.inf
        for i in range(len(nums)):
            curr_subarray = 0
            for j in range(i, len(nums)):
                curr_subarray += nums[j]
                max_subarray = max(max_subarray, curr_subarray)

        return max_subarray

# Dynamic Programming:
# Whenever you see a question that asks for the maximum or minimum of something, consider Dynamic Programming as a possibility
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_subarray = nums[0]
        currSum = 0
        for n in nums:
            if currSum < 0:
                currSum = 0
            currSum += n
            max_subarray = max(max_subarray, currSum)

        return max_subarray