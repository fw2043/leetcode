"""
You are given an integer array height of length n.
There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
Example 2:

Input: height = [1,1]
Output: 1


Constraints:

n == height.length
2 <= n <= 105
0 <= height[i] <= 104
"""
# How do we get 49? 7 * 7 ===> height[r] * (r - l)
# Can't sort the array
# Find max(2sum)? ----> two pointers
# l = 0, r = len(height) - 1
# the key is why/when we need to update the pointers?
# which one is smaller(not desirable), then move it.
# Time complexity: O(n)
# Space complexity: O(1)
class Solution:
    def maxArea(self, height: List[int]) -> int:
        # brute force

        l, r = 0, len(height) - 1
        res = (r - l) * min(height[l], height[r])
        while l < r:
            area = (r - l) * min(height[l], height[r])
            res = max(res, area)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return res



# Brute Force
# Time complexity: O(n^2)
# Space complexity: O(n)
class Solution:
    def maxArea(self, height: List[int]) -> int:
        # brute force
        res = 0
        for i in range(len(height)):
            for j in range( i + 1, len(height)):
                area = (j - i) * min(height[i], height[j])
                res = max(area, res)
        return res
