"""
Given two integer arrays nums1 and nums2, return an array of their intersection.
Each element in the result must be unique and you may return the result in any order.
Example 1:
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]

Example 2:
Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
Explanation: [4,9] is also accepted.

Constraints:
1 <= nums1.length, nums2.length <= 1000
0 <= nums1[i], nums2[i] <= 1000
"""
################################################################################################################################
from typing import List

"""
Method 1: hashmap
Time complexity:O (n + m)
Space complexity:O(min(n,m))
"""
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # choose a small one as look up
        if len(nums1) > len(nums2):
            return self.intersection(nums2, nums1)

        lookup = set()
        for i in nums1:
            if i not in lookup:
                lookup.add(i)
        intersection = []
        for i in nums2:
            if i in lookup:
                intersection.append(i)
        # narrow down lookup table
                lookup.discard(i)

        return intersection

"""
Method 2: sort two lists and use two pointers
Time complexity: O(n + m)
"""

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # sort the arrays, then two pointers
        nums1.sort()
        nums2.sort()
        result = set()
        i = j = 0

        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                ## intersection found, but might be duplicates
                if nums1[i] not in result:
                    result.add(nums1[i])
                i += 1
                j += 1

            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1

        return result

"""
Method 3: sort one of the lists and binary search
Time complexity: O(NlogN)

"""


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # sort the arrays, then binary search
        # search from smaller list:
        if len(nums1) > len(nums2):
            return self.intersection(nums2, nums1)

        result = set()
        for num in nums1:
            if self.findTarget(nums2, num) and num not in result:
                result.add(num)

        return result

    def findTarget(self, nums: List[int], target: int) -> bool:
        # sort the list:
        nums.sort()
        start, end = 0, len(nums) - 1
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] == target:
                return True
            elif nums[mid] > target:
                end = mid - 1
            else:
                start = mid + 1

        return False
