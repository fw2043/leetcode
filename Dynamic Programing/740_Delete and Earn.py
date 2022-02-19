"""
You are given an integer array nums. You want to maximize the number of points
you get by performing the following operation any number of times:

Pick any nums[i] and delete it to earn nums[i] points. Afterwards,
you must delete every element equal to nums[i] - 1 and every element equal to nums[i] + 1.
Return the maximum number of points you can earn by applying the above operation some number of times.

Example 1:

Input: nums = [3,4,2]
Output: 6
Explanation: You can perform the following operations:
- Delete 4 to earn 4 points. Consequently, 3 is also deleted. nums = [2].
- Delete 2 to earn 2 points. nums = [].
You earn a total of 6 points.

Example 2:
Input: nums = [2,2,3,3,3,4]
Output: 9
Explanation: You can perform the following operations:
- Delete a 3 to earn 3 points. All 2's and 4's are also deleted. nums = [3,3].
- Delete a 3 again to earn 3 points. nums = [3].
- Delete a 3 once more to earn 3 points. nums = [].
You earn a total of 9 points.

Constraints:

1 <= nums.length <= 2 * 104
1 <= nums[i] <= 104
"""
# maximum number of points
# the current decision impact the future decisions
# DP problem
# might have duplicate elements: sort and counter ====> nLogn
# counter will be the list we need to check
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        count = collections.Counter(nums)
        nums = sorted(list(set(nums)))  # nlogn
        # nums = [2,2,3,3,3,4] ====> nums = [2,3,4]
        # decisions at i only being impacted by i-1 and i-2
        earns1 = earns2 = 0
        for i in range(len(nums)):
            currEarn = nums[i] * count[nums[i]]
            # can't use both the current and previous:
            if i > 0 and nums[i] == nums[i - 1] + 1:
                temp = earns2
                earns2 = max(currEarn + earns1, earns2)
                earns1 = temp
            else:
                temp = earns2
                earns2 = currEarn + earns2
                earns1 = temp

        return earns2

