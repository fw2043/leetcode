"""
Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The relative order of the elements may be changed.

Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.

Return k after placing the final result in the first k slots of nums.

Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.
"""
# ask question:
# does it matter if the first elements not being removed return in any order, if the order is changed?
# --need to sort them or not,
# or change the order
# does it matter what we leave beyond the returned k ---if it is okay I keep the removed elements there

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        for i in range(len(nums)):
            # partitions problem
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k



