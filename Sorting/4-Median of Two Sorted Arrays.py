"""
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

Example 1:
Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.

Example 2:
Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.


Constraints:

nums1.length == m
nums2.length == n
0 <= m <= 1000
0 <= n <= 1000
1 <= m + n <= 2000
-106 <= nums1[i], nums2[i] <= 106
"""
# edge cases: one of them is empty or both of them are empty
# sorted lists: merge them -----> merge, O(m+n)
# However, the requirement is: O(log (m+n)), so have to binary search solution?
# Method 1:

# Method 2: Merge them and get median
# Time complexity: O(m + n)
# Space complexity: O(m + n)
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Time complexity: O(m + n)
        # Space complexity: O(m + n)
        def merge(left, right):
            if len(left) == 0 and len(right) > 0:
                return right
            if len(right) == 0 and len(left) > 0:
                return left
            res = []
            i, j = 0, 0
            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    res.append(left[i])
                    i += 1
                else:
                    res.append(right[j])
                    j += 1
            res += left[i:]
            res += right[j:]
            return res

        # merge the lists in order
        nums = merge(nums1, nums2)
        # find the median
        length = len(nums)
        idx = (length - 1) // 2
        if length % 2:
            return nums[idx]
        else:
            return (nums[idx] + nums[idx + 1]) / 2


