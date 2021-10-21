"""
A peak element is an element that is strictly greater than its neighbors.
Given an integer array nums, find a peak element, and return its index. If the array contains multiple peaks, return the index to any of the peaks.
You may imagine that nums[-1] = nums[n] = -∞.
You must write an algorithm that runs in O(log n) time.

Example 1:
Input: nums = [1,2,3,1]
Output: 2
Explanation: 3 is a peak element and your function should return the index number 2.

Example 2:
Input: nums = [1,2,1,3,5,6,4]
Output: 5
Explanation: Your function can return either index number 1 where the peak element is 2, or index number 5 where the peak element is 6.

Constraints:
1 <= nums.length <= 1000
-231 <= nums[i] <= 231 - 1
nums[i] != nums[i + 1] for all valid i.

"""
from typing import List

"""
Binary search
"""
# my methond:
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return 0
        if len(nums) == 2:
            return nums.index(max(nums))

        start, end = 0, len(nums) - 1
        while start < end:
            # in case of overflow
            mid = start + (end - start) // 2
            # case [1,2,1,2,1
            if start == 0 and end == 1 and nums[end] > nums[start]:
                return 1

            if nums[mid - 1] < nums[mid] and nums[mid + 1] < nums[mid]:
                return mid

            elif nums[mid - 1] < nums[mid]:
                start = mid + 1
            else:
                end = mid - 1
            print(start, end)

        return start

# A better way:
"""
Imagine it as climbing a peak. Now the left and right ends are at -infinity and there is no plateau 
so there is a  peak to be guaranteed. Now check the middle element,if the next element is less 
this means that we are on our downward journey in the peak,so the peak is at the left part i.e end=mid 
(Note:This element might be the peak as the next element is less therefore we included it).
And if the next element is greater than the current,this means that we are climbing the peak therefore peak 
happens to be on the right part(Note:This element can't be the peak).So s=mid+1
"""
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:

        start, end = 0, len(nums) - 1
        while start < end:
            # in case of overflow
            mid = start + (end - start) // 2

            if nums[mid] < nums[mid + 1]:
                start = mid + 1  # start point won't be the peak, so check from mid +1
            else:
                end = mid  # mid might be the peak, beacause nums[mid] > nums[mid+1], so end = mid
        return start