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
# Are they all positive integers? or could be negative?  ---> Yes

# Approach 1: Brute Force: O(n^3)
# Considers each number in nums, attempting to count as high as possible from that number using only numbers in nums.
# After it counts too high (i.e. currentNum refers to a number that nums does not contain).
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest_streak = 0

        for num in nums:
            current_num = num
            current_streak = 1

            while current_num + 1 in nums:
                current_num += 1
                current_streak += 1

            longest_streak = max(longest_streak, current_streak)

        return longest_streak

# Approach 2: Sorting: O(nlogn)
# Before we do anything, we check for the base case input of the empty array.
# The longest sequence in an empty array is, of course, 0, so we can simply return that.
# For all other cases, we sort nums and consider each number after the first (because we need to compare each number to its previous number).
# If the current number and the previous are equal, then our current sequence is neither extended nor broken, so we simply move on to the next number.
# If they are unequal, then we must check whether the current number extends the sequence (i.e. nums[i] == nums[i-1] + 1).
# If it does, then we add to our current count and continue. Otherwise, the sequence is broken,
# so we record our current sequence and reset it to 1 (to include the number that broke the sequence).
# It is possible that the last element of nums is part of the longest sequence, so we return the maximum of the current sequence and the longest one.

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # [100,4,200,1,3,2, 1]
        # [1, 1, 2, 3, 4, 100, 200]
        # sort the list
        # compare the current one with the previous one, there are 3 stuiations:
        # if equal, don't need to update the longest_streak, just move on
        # if current_num = the previous one + 1: current_streak += 1
        # if current_num != the previous one + 1: reset current_streak = 1 and

        if not nums:
            return 0
        # sort the list
        nums = sorted(nums)

        longest_streak = 1
        current_streak = 1

        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:  # if they are equal, do nothing, just move on
                if nums[i] == nums[i - 1] + 1:
                    current_streak += 1

                else:
                    longest_streak = max(longest_streak, current_streak)
                    current_streak = 1

        return max(longest_streak, current_streak)

# Approach 3: HashSet
# O(n)
# This optimized algorithm contains only two changes from the brute force approach:
# the numbers are stored in a HashSet (or Set, in Python) to allow O(1) lookups,
# and we only attempt to build sequences from numbers that are not already part of a longer sequence.
# This is accomplished by first ensuring that the number that would immediately precede the current number in a sequence is not present,
# as that number would necessarily be part of a longer sequence.
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        longest_streak = 1

        nums_set = set(nums)

        current_streak = 1
        for num in nums:
            # find the start of a sequence
            if num - 1 not in nums_set:
                current_num = num
                current_streak = 1
                # calculate the lenght of the sequence
                while current_num + 1 in nums_set:
                    current_num += 1
                    current_streak += 1

                longest_streak = max(longest_streak, current_streak)

        return longest_streak