"""
Given an m x n matrix, return all elements of the matrix in spiral order.
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]

Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]

Constraints:
m == matrix.length
n == matrix[i].length
1 <= m, n <= 10
-100 <= matrix[i][j] <= 100
"""
"""
Given that we are at (row, col), where row is the row index, and col is the column index.
move right: (row, col + 1)
move downwards: (row + 1, col)
move left: (row, col - 1)
move upwards: (row - 1, col)
"""

# Remember that we don't include the output array in the space complexity.
# input matrix = [[1,2,3],[4,5,6],[7,8,9]]
# go 1 ->2 ->3, reach out to right boundary could not have anymore,
#  change direction, 3 -> 6 -> 9, reach out to the bottom boundary,
# change direction, 9 can only go to 8, 8 -->7, reach out to left boundary
# 7--> 4, then 1 is visited, so change direction
# so from the example above:
# we have to change left, right, bottom, top boundaries--->chop out the boundaries, narrow down the size
# need to check the condition: left < right and top < bottom
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        left, right = 0, len(matrix[0])
        top, bottom = 0, len(matrix)

        while left < right and top < bottom:
            # get every i in the top row:
            for i in range(left, right):
                res.append(matrix[top][i])
            top += 1

            # get every i in right col:
            for i in range(top, bottom):
                res.append(matrix[i][right - 1])
            right -= 1

            if not (left < right and top < bottom):
                break

            # get every i in bottom row:
            # traverse from right to left, so set -1(decrease i from right until left)
            for i in range(right - 1, left - 1, -1):
                res.append(matrix[bottom - 1][i])
            bottom -= 1

            # get every i in left col:
            for i in range(bottom - 1, top - 1, -1):
                res.append(matrix[i][left])
            left += 1

        return res

# Time complexity: O(M⋅N). This is because we visit each element once.
# Space complexity: O(1), This is because we don't use other data structures.