"""
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed,
the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected
and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house,
return the maximum amount of money you can rob tonight without alerting the police.

Example 1:

Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.

Example 2:

Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
Total amount you can rob = 2 + 9 + 1 = 12.


Constraints:

1 <= nums.length <= 100
0 <= nums[i] <= 400
"""
# 1. the maximum
# it will automatically contact the police if two adjacent houses were broken into on the same night.---->
# 2. The current decision will impact the futreu decisions
# Dynamic Programming
# money is postive interger, so at least 2 houses, won't rober one if there are more than 2 houses
# 1. A function or array that answers the problem for a given state
# function dp(i) that returns the maximum amount of money you can rob up to
#or array: dp[i] represents the maximum amount of money you can rob up to.
# 2.  A recurrence relation to transition between states
# dp(i) ===> decisions: choose (dp(i-2) + nums[i]) or not (dp(i-1))
# max(dp(i-2) + nums[i], dp(i))
# 3. Base case: dp(0) = nums[0], dp(1) = max(nums[0], nums[1])
# Remember: we need to memoize the function: array or hashmap
# Time complexity: O(n)
# Space complexity: O(n)
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        # using an array to memorize
        dp = [0] * len(nums)
        # base case:
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])  # Recurrence relation

        return dp[-1]