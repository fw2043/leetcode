"""
Given an array of integers nums and an integer k,
return the total number of continuous subarrays whose sum equals to k.
Example 1:

Input: nums = [1,1,1], k = 2
Output: 2

Example 2:
Input: nums = [1,2,3], k = 3
Output: 2

Constraints:
1 <= nums.length <= 2 * 104
-1000 <= nums[i] <= 1000
-107 <= k <= 107
"""
# continuous subarrays
# the value could be negative


# Approach 1: Brute Froce: O(n^2)
class Solution(object):
    def subarraySum(self, nums, k):
        """
        [-2,    1,    2,   -2,   5,   -2,   1] k = 3
        start, end
        """
        cnt = 0
        for start in range(len(nums)):
            total = 0
            for end in range(start, len(nums)):
                total += nums[end]
                if total == k:
                    cnt += 1
        return cnt

# Approach 2:
# since the total of a small subarray is part of the total of a big subarray
# can we use prefix sum approach?
# sum(nums[2, 6] = prefixSum[6] - prefixSum[2 - 1]
# sum(nums[i, j] = prefixSum[j] - prefixSum[i - 1]
# if k = prefixSum[j] - prefixSum[i - 1]: cnt+= 1
# Our goal is to find a i which can satisfy the  condition: prefixSum[i - 1] = prefixSum[j] - k
# for example: [1, -1, 1,1,1,1] k = 3
# res = 4
# HashMap to store the count for each prefix sum
# prefixSum as the key, count/time prefixSum happens as value
# default value: {0,1}
# O(n)

class Solution(object):
    def subarraySum(self, nums, k):
        # [1, -1, 1, 1, 1, 1] k =3
        # sum(nums[1, 5]) = prefix[5] - prefix[1 - 0]
        # sum(nums[i, j]) = prefix[j] - prefix[i - 1]
        # if k = prefix[j] - prefix[i - 1]: cnt +=1
        cnt = 0
        curSum = 0
        prefixSum = {0: 1}
        for n in nums:
            curSum += n
            diff = curSum - k
            # update cnt
            cnt += prefixSum.get(diff, 0)
            # update prefixSum
            prefixSum[curSum] = 1 + prefixSum.get(curSum, 0)

        return cnt
