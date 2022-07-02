"""
An ugly number is a positive integer whose prime factors are limited to 2, 3, and 5.
Given an integer n, return the nth ugly number.

Example 1:
Input: n = 10
Output: 12
Explanation: [1, 2, 3, 4, 5, 6, 8, 9, 10, 12] is the sequence of the first 10 ugly numbers.

Example 2:
Input: n = 1
Output: 1
Explanation: 1 has no prime factors, therefore all of its prime factors are limited to 2, 3, and 5.

Constraints:
1 <= n <= 1690
"""
# prime number can be broke down itself or 1
# Solution 1: the Nth sequence number----> heap
# solution 2: Ugly number = 2^x * 3^y * 5^z (x, y ,z ====> 3 pointers)


# Approach 1: three pointers (x, y, z)
# Time complexity: O(n)
# space complexity: O(n)
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        two_postion, three_postion, five_position = 0, 0, 0
        nums = [1]
        while len(nums) < n:
            by2 = nums[two_postion] * 2
            by3 = nums[three_postion] * 3
            by5 = nums[five_position] * 5

            min_num = min(by2, by3, by5)
            nums.append(min_num)

            if min_num == by2:
                two_postion += 1

            if min_num == by3:
                three_postion += 1

            if min_num == by5:
                five_position += 1

        return nums[-1]

# Approach 2: heap
#todo list
