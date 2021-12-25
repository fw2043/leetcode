"""
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
You must write an algorithm that runs in O(n) time.

Example 1:
Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9


Constraints:
0 <= nums.length <= 105
-109 <= nums[i] <= 109
"""
# What if the length is 1 or empty ---> edge cases
# Is there any duplicate? YES, for example:
# Are they all postive intergers? or could be negative?  ---> Yes

# If we try to sort them first, even quick sort still takes O(nlogn), but we need to run in O(n) time!

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # input: nums = [100,4,200,1,3,2]
        # use hashset to get all unique nums
        # find the start num of the sequence, then check if we can find next(+1) and next.etc until next is not in set
        num_set = set(nums)
        length = 0
        for num in nums:
            if (num - 1) not in num_set:  # # find start: will be  100, 200, and 1
                start = num
                while start in num_set:
                    start += 1

                length = max(length, start - num)

        return length

