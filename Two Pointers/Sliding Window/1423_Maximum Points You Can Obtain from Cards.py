"""
There are several cards arranged in a row, and each card has an associated number of points.
The points are given in the integer array cardPoints.

In one step, you can take one card from the beginning or from the end of the row.
You have to take exactly k cards.

Your score is the sum of the points of the cards you have taken.

Given the integer array cardPoints and the integer k, return the maximum score you can obtain.


Example 1:

Input: cardPoints = [1,2,3,4,5,6,1], k = 3
Output: 12
Explanation: After the first step, your score will always be 1. However,
choosing the rightmost card first will maximize your total score. The optimal strategy is to take the three cards on the right,
giving a final score of 1 + 6 + 5 = 12.

Example 2:
Input: cardPoints = [2,2,2], k = 2
Output: 4
Explanation: Regardless of which two cards you take, your score will always be 4.

Example 3:
Input: cardPoints = [9,7,7,9,7,7,9], k = 7
Output: 55
Explanation: You have to take all the cards. Your score is the sum of points of all cards.


Constraints:

1 <= cardPoints.length <= 105
1 <= cardPoints[i] <= 104
1 <= k <= cardPoints.length
"""
# edge cases:  if k <= len(cardPoints):
# Brute Force: Either take all from left/right or some of left and some of right,
# but the length of the ones left(always length - k)----->Sliding window
# Input: cardPoints = [1,2,3,4,5,6,1], k = 3
# Initial sliding window: [1,2,3,4], [5,6,1] are out of window
# Time complexity: O(K + K)
# Space complexity: O(1)

class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        if k >= len(cardPoints):
            return sum(cardPoints)

        i, j = 0, len(cardPoints) - k
        max_sum = total = sum(cardPoints[j:])
        while j < len(cardPoints):
            total += cardPoints[i] - cardPoints[j]
            max_sum = max(max_sum, total)
            i += 1
            j += 1
        return max_sum