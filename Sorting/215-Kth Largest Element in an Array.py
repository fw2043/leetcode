"""
Given an integer array nums and an integer k, return the kth largest element in the array.
Note that it is the kth largest element in the sorted order, not the kth distinct element.

Example 1:
Input: nums = [3,2,1,5,6,4], k = 2
Output: 5

Example 2:
Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4

Constraints:
1 <= k <= nums.length <= 104
-104 <= nums[i] <= 104
"""
# k is the  is the kth largest element in the sorted order
# what if only one element, the the length is smaller than k: 1 <= k <= nums.length <= 104
# duplicates? ---> it is the kth largest element in the sorted order, not the kth distinct element.

# you might be able to use heap

# the better one is: Quick Select
# the average running time is O(N)
# the worst case is O(n^2)---> pick the largest one as pivot
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        # Quick Select:
        # Time complexity:
        # Average is: O(n)
        # worst case: O(n^2)
        # space complexity:
        # nums = [3,2,1,5,6,4], k = 2
        # the index of the kth largest elements we are looking for:
        k = len(nums) - k

        def quickSelect(l, r):
            pivot, p = nums[r], l
            for i in range(l, r):
                if nums[i] <= pivot:
                    nums[p], nums[i] = nums[i], nums[p]
                    p += 1
                # here we get  [3,2,1,5,6,4], p =5
                # at p, we know all elements left of p are smaller than pivot, so swap pivot and p,
                # we put pivot in the right position
            nums[p], nums[r] = pivot, nums[p]
            # now the list is: [3,2,1,4,6,6]
            # on the left side of p, the left side does not have to be in order, so have to do recursive call
            if p > k:
                return quickSelect(l, p - 1)
            # in the right side, recursive call
            elif p < k:
                return quickSelect(p + 1, r)
            # pivot is the number we are looking for
            else:
                return nums[p]

        return quickSelect(0, len(nums) - 1)





