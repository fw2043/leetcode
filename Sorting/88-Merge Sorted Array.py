"""
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function,
but instead be stored inside the array nums1.
To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged,
and the last n elements are set to 0 and should be ignored. nums2 has a length of

Example 1:
Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.

Example 2:
Input: nums1 = [1], m = 1, nums2 = [], n = 0
Output: [1]
Explanation: The arrays we are merging are [1] and [].
The result of the merge is [1].

Example 3:
Input: nums1 = [0], m = 0, nums2 = [1], n = 1
Output: [1]
Explanation: The arrays we are merging are [] and [1].
The result of the merge is [1].
Note that because m = 0, there are no elements in nums1. The 0 is only there to ensure the merge result can fit in nums1.

Constraints:
nums1.length == m + n
nums2.length == n
0 <= m, n <= 200
1 <= m + n <= 200
-109 <= nums1[i], nums2[j] <= 109
"""
# merge in reverse order, update from the last of nums1:

#### they are sorted array---->
#  [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
        # nums1 and nums2 are sorted, and nums1 has enough space for adding nums2
        # ---> put items in nums2 to nums1 backfoward,  [1,2,3,0,0,6], [2,5]
        # 6 > 3, so put 6 to last one,
        # 5 > 3, put 5 to the second last one
        # 2 < 3, then have to find right one t
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """


        # last index of nums1
        write_pointer  = m + n - 1

        # merge in reverse order
        while m > 0 and n > 0:
            if nums1[m - 1] > nums2[n - 1]:
                nums1[write_pointer ] = nums1[m - 1]
                m -= 1
            else:
                nums1[write_pointer ] = nums2[n - 1]
                n -= 1
            write_pointer  -= 1

        # fill nums1 with leftover nums2 elements
        while n > 0:
            nums1[write_pointer ] = nums2[n - 1]
            n -= 1
            write_pointer  -= 1

# Heap
# Time complexity: O(log(m+n)
# space complexity: O(log(n+m))
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        h = list()
        for i in range(m):  #O(logm)
            heapq.heappush(h, nums1[i])
        for i in range(n):  #O(logn)
            heapq.heappush(h, nums2[i])
        for i in range(n + m): # O(log(n+m))
            nums1[i] = heapq.heappop(h)
        return nums1
