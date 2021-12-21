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




