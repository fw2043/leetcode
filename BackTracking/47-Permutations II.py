"""
Given a collection of numbers, nums, that might contain duplicates,
return all possible unique permutations in any order.

Example 1:
Input: nums = [1,1,2]
Output:
[[1,1,2],
 [1,2,1],
 [2,1,1]]

Example 2:
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]


Constraints:
1 <= nums.length <= 8
-10 <= nums[i] <= 10
"""
# the difference between leetcode 46 and 47 is: duplicates in the list
# use Counter to keep tracking the number of 1 still avaiable

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(counter, subset):
            if len(subset) == len(nums):
                res.append(subset[:])
                return

            for num in counter:
                # if this number still avaible
                if counter[num] > 0:
                    subset.append(num)
                    # update the count
                    counter[num] -= 1
                    backtrack(counter, subset)
                    # revert the choice for the next exploration
                    subset.pop()
                    counter[num] += 1

        counter = {}
        for num in nums:
            counter[num] = counter.get(num, 0) + 1
        backtrack(counter, [])
        return res
