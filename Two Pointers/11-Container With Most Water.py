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
# How do we get 49? 7 * 7 ===> min(height[r], height[r]) * (r - l)
# Can't sort the array

# Appraoch Brute Force
# Time complexity: O(n^2)
class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_sum = 0
        for i in range(len(height)):
            for j in range(i + 1, len(height)):
                current_sum = (j - i) * min(height[i], height[j])
                max_sum = max(max_sum, current_sum)

        return max_sum

# Approach 2: Two Pointer Approach
# Find max(2sum)? ----> two pointers
# left = 0, right= len(height) - 1
# the key is when to move the pointers?
# since no matter moving left or right pointer, the width(right - left) is decreasing,
# so to optimize the result, we should move the pointer whoes height[] is smaller.
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

