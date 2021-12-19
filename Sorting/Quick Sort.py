# # Time Complexity:
# O(nlogn) in average case
# O(n^2) in worst case
# # Space complexity is: O(1) in-place
## https://www.youtube.com/watch?v=COk73cpQbFQ
# pivot--->partition into left and right sublist
# sort the left and right sublist of the list
# divide and conquar stratagy
def quick_sort(nums):
    n = len(nums)

    def quick(left, right):
        if left >= right:
            return nums
        pivot = left
        i = left
        j = right
        while i < j:
            while i < j and nums[j] > nums[pivot]:
                j -= 1
            while i < j and nums[i] <= nums[pivot]:
                i += 1
            nums[i], nums[j] = nums[j], nums[i]
        nums[pivot], nums[j] = nums[j], nums[pivot]
        quick(left, j - 1)
        quick(j + 1, right)
        return nums

    return quick(0, n - 1)


