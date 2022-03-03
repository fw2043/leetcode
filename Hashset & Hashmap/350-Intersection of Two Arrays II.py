"""
Given two integer arrays nums1 and nums2, return an array of their intersection.
Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.

Example 1:
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]

Example 2:
Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
Explanation: [9,4] is also accepted.


Constraints:
1 <= nums1.length, nums2.length <= 1000
0 <= nums1[i], nums2[i] <= 1000
"""
# Follow up:
# What if the given array is already sorted? How would you optimize your algorithm?
# What if nums1's size is small compared to nums2's size? Which algorithm is better?
# What if elements of nums2 are stored on disk, and the memory is limited
# such that you cannot load all elements into the memory at once?

# conform that: Each element in the result must appear as many times as it shows in both arrays===> dict/Counter not set
# Counter for the first list
# go through the second list, find one in counter, then decrease the value
# Time complexity: O(n +m)
# Space complexity: O(n)
# Check leetcode 349
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # dict or Counter
        # counts = collection.Counter(nums1)
        res = []
        counts = {}
        for num in nums1:
            counts[num] = counts.get(num, 0) + 1

        for num in nums2:
            if num in counts and counts[num] > 0:
                res.append(num)
                counts[num] -= 1
        return res
# Follow up:
# What if the given array is already sorted? How would you optimize your algorithm?
# Classic two pointer iteration, i points to nums1 and j points to nums2.
# Because a sorted array is in ascending order, so if nums1[i] > nums[j], we need to increment j, and vice versa.
# Only when nums1[i] == nums[j], we add it to the result array.
# Time Complexity O(max(N, M)). Worst case, for example, would be nums1 = {100}, and nums2 = {1, 2, ..., 100 }.

# What if nums1's size is small compared to nums2's size? Which algorithm is better?
# This one is a bit tricky. Let's say nums1 is K size.
# Then we should do binary search for every element in nums1.
# Each lookup is O(log N), and if we do K times, we have O(K log N).
# If K this is small enough, O(K log N) < O(max(N, M)). Otherwise, we have to use the previous two pointers method.
# let's say A = [1, 2, 2, 2, 2, 2, 2, 2, 1], B = [2, 2]. For each element in B, we start a binary search in A. To deal with duplicate entry, once you find an entry, all the duplicate element is around that that index, so you can do linear search scan afterward.
#
# Time complexity, O(K(logN) + N).
# Plus N is worst case scenario which you have to linear scan every element in A.
# But on average, that shouldn't be the case.
# so I'd say the Time complexity is O(K(logN) + c), c (constant) is number of linear scan you did.

# What if elements of nums2 are stored on disk,
# and the memory is limited such that you cannot load all elements into the memory at once?
# This one is open-ended. But Map-Reduce I believe is a good answer.

