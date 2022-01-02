"""
Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order,
find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1]
and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

Return the indices of the two numbers, index1 and index2,
added by one as an integer array [index1, index2] of length 2.
The tests are generated such that there is exactly one solution. You may not use the same element twice.

Example 1:
Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].

Example 2:
Input: numbers = [2,3,4], target = 6
Output: [1,3]
Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return [1, 3].

Example 3:
Input: numbers = [-1,0], target = -1
Output: [1,2]
Explanation: The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2. We return [1, 2].


Constraints:
2 <= numbers.length <= 3 * 104
-1000 <= numbers[i] <= 1000
numbers is sorted in non-decreasing order.
-1000 <= target <= 1000
The tests are generated such that there is exactly one solution.
"""


# in non-decreasing order
# exactly one solution
#  may not use the same element twice.
# Using hashmap is not the best way, because it does not take advantage of information: sorted array!
# Time complexity: O(n)
# space complexity: O(n)
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        prevMap = {}
        for i, n in enumerate(numbers):
            diff = target - n
            if diff in prevMap:
                return (prevMap[diff] + 1, i + 1)
            prevMap[n] = i
# If we take advantage of sorted array inforamation:
# Two Pointers
# Time complexity: O(n)
# space complexity: O(1) ---> no extra space needed
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1
        while left < right:
            currSum = numbers[left] + numbers[right]
            if currSum == target:
                return ([left + 1, right + 1])
            elif currSum < target:
                left += 1
            else:
                right -= 1


