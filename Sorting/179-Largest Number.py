"""
Given a list of non-negative integers nums, arrange them such that they form the largest number and return it.
Since the result may be very large, so you need to return a string instead of an integer.

Example 1:
Input: nums = [10,2]
Output: "210"

Example 2:
Input: nums = [3,30,34,5,9]
Output: "9534330"


Constraints:
1 <= nums.length <= 100
0 <= nums[i] <= 109
"""
# for string type: '9' + '30' = '930' which is greater than '309'
# so we can sort the list based on the logic above
# if it is sorting problem, then we can use quick sort, merge sort, insertion sort, selection sort, buddle sort.etc
# Quick sort
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        # quick sort
        def quick_sort(nums, l, r):
            # base case
            if l >= r:
                return
            p = partition(nums, l, r)
            quick_sort(nums, l, p - 1)
            quick_sort(nums, p + 1, r)

        def partition(nums, l, r):
            pivot = nums[r]
            # set pivot is the last one, the larger ones will be at the left, and smaller ones will be at the right
            i = l - 1
            for j in range(l, r):
                # condition for swapping
                if str(pivot) + str(nums[j]) <= str(nums[j]) + str(pivot):
                    i += 1
                    nums[i], nums[j] = nums[j], nums[i]
            nums[i + 1], nums[r] = nums[r], nums[i + 1]
            return i + 1

        # call quick sort function
        quick_sort(nums, 0, len(nums) - 1)
        return str(int(''.join(map(str, nums))))
        # ''.join(map(str, nums) wont work for case: input [0,0], output '0', int('00') = 0

# Merge sort
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        # merge sort
        def merge_sort(nums):
            if len(nums) <= 1:
                return nums
            mid = len(nums) // 2
            # divide
            left = merge_sort(nums[:mid])
            right = merge_sort(nums[mid:])
            # conquer
            return merge(left, right)

        def merge(left, right):
            res = []
            i, j = 0, 0
            while i < len(left) and j < len(right):
                if str(left[i]) + str(right[j]) >= str(right[j]) + str(left[i]):
                    res.append(left[i])
                    i += 1

                else:
                    res.append(right[j])
                    j += 1
            res += left[i:]
            res += right[j:]
            return res

        # call quick sort function
        result = merge_sort(nums)
        return str(int(''.join(map(str, result))))
        # ''.join(map(str, nums) wont work for case: input [0,0], output '0', int('00') = 0

