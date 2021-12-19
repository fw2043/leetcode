#Divide and Conquer
# Time Complexity: O(nlogn) in worst case
# Space complexity is: O(n)
# https://www.youtube.com/watch?v=TzeBrDU-JaY
def merge_sort(nums):
    if len(nums) <= 1:
        return nums
    mid = len(nums) // 2
    # divide
    left = merge_sort(nums[:mid])
    right = merge_sort(nums[mid:])
    # conquar
    return merge(left, right)


def merge(left, right):
    res = []
    i = 0
    j = 0
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