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
# HashMap to store the count for each prefix sum
# prefix as the key, count/time prefix happens as value
# default value: {0,1}
# O(n)

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        curSum = 0
        presum = {0: 1}
        # find how many times we can meet sum[right] - sum[left] = k
        for n in nums:
            # update the current sum[right]
            curSum += n
            # diff == sum[left]
            diff = curSum - k

            res += presum.get(diff, 0)

            # update curSum count
            presum[curSum] = 1 + presum.get(curSum, 0)

        return res

# Brute Froce: O(n^2)
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        n = len(nums)
        presum = [0 for i in range(n + 1)]

        for i in range(1, n + 1):
            presum[i] = presum[i - 1] + nums[i - 1]

        for i in range(n):
            for j in range(i, n):
                if presum[j + 1] - presum[i] == k:
                    res += 1

        return res

