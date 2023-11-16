"""
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

Example 1:

Input: nums = [1,2,3,1]
Output: true
Example 2:

Input: nums = [1,2,3,4]
Output: false
Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true


Constraints:

1 <= nums.length <= 105
-109 <= nums[i] <= 109
"""
# Clarify if we can use extra memory or not:
# if yes---- hashset
# if not ----> sorted and iterate each item

# Brute Force SOLUTION: search each item if they exist in the list
# Tiem complexity: O(n^2)
# Space complexity: O(1)
def containsDuplicate(self, nums):
    for i in range(0, len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] == nums[j]:
                return True
    return False

# Sort the list first, then checj adjacent items
# Tiem complexity: O(nlog(n))
# Space complexity: O(n)
def containsDuplicate(self, nums):
    # SORT THE LIST: nlog(n) without extra memory
    nums = sorted(nums)
    for i in range(0, len(nums) - 1):
        if nums[i] == nums[i + 1]:
            return True
    return False


# Hashset
# Tiem complexity: O(n)
# Space complexity: O(n)
# Method 1: iterate each item and add it to the hashset if it does not exist in hashset, if it exists, return true
def containsDuplicate(self, nums):
    hashset = set()
    for n in nums:
        if n in hashset:
            return True
        hashset.add(n)
    return False

# Method 2: put all the items to hashset, and check the length of hashset, if it is smaller than the length of the array
# then the array has duplicates
def containsDuplicate(self, nums):
    hashset = set(nums)
    if len(hashset) < len(nums):
        return True
    return False
