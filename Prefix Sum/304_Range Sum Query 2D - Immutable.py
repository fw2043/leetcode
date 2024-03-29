"""
Given a 2D matrix matrix, handle multiple queries of the following type:

Calculate the sum of the elements of matrix inside the rectangle defined by its upper left corner (row1, col1)
and lower right corner (row2, col2).
Implement the NumMatrix class:

NumMatrix(int[][] matrix) Initializes the object with the integer matrix matrix.
int sumRegion(int row1, int col1, int row2, int col2)
Returns the sum of the elements of matrix inside the rectangle defined by its upper left corner (row1, col1)
and lower right corner (row2, col2).


Example 1:


Input
["NumMatrix", "sumRegion", "sumRegion", "sumRegion"]
[[[[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7],
[1, 0, 3, 0, 5]]], [2, 1, 4, 3], [1, 1, 2, 2], [1, 2, 2, 4]]
Output
[null, 8, 11, 12]

Explanation
NumMatrix numMatrix = new NumMatrix([[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5],
[4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]);
numMatrix.sumRegion(2, 1, 4, 3); // return 8 (i.e sum of the red rectangle)
numMatrix.sumRegion(1, 1, 2, 2); // return 11 (i.e sum of the green rectangle)
numMatrix.sumRegion(1, 2, 2, 4); // return 12 (i.e sum of the blue rectangle)

Constraints:
m == matrix.length
n == matrix[i].length
1 <= m, n <= 200
-105 <= matrix[i][j] <= 105
0 <= row1 <= row2 < m
0 <= col1 <= col2 < n
At most 104 calls will be made to sumRegion.
"""

# Brute Force algorithm: O(n^m)
def prefixSum(row1, row2, col1, col2, matrix):
    sum = 0
    for i in range(row1, row2 + 1):
        for j in range(col1, col2 + 1):
            sum += matrix[i][j]
    return sum


# An idea is to build on top of  prefix sum: O(n * m)
# Similar to 221, p
# prefix sum to prepare: always start with matrix[0][0], and save the prefix at the right buttom(matrix[r][j]
# edge case: to calculate the first row and left columnm, it will be out of boundary, to fix it, we create a large matrix:
# extra row and extra col with 0 values
# initialize: sumMat = [[0] * (col + 1) for r in range(rows + 1)]

# prefix sum = s[x2, x2] - s[x1-1, y2] - s[x2, y1-1] +s[x1-1, y1-1]
# SumRange(x1, y1, x2, y2) = s[x2,y2] - s[x-1, y2] - s[x2, y1-1] + s[x1-1, y1-1]
# Complexity
# Constructor: Time & Space: O(m*n), where m is the number of rows, n is the number of columns in the grid
# sumRegion: Time & Space: O(1)

class NumMatrix(object):

    def __init__(self, matrix):
        rows, cols = len(matrix), len(matrix[0])
        self.sumMatrix = [[0] * (cols + 1) for r in range(0, rows + 1)]

        for r in range(rows):
            prefixsum = 0
            for c in range(cols):
                # sum of all columns at the current row
                prefixsum += matrix[r][c]
                above = self.sumMatrix[r][c + 1]
                self.sumMatrix[r + 1][c + 1] = prefixsum + above

    def sumRegion(self, row1, col1, row2, col2):
        row1, col1, row2, col2 = row1 + 1, col1 + 1, row2 + 1, col2 + 1
        bottomRight = self.sumMatrix[row2][col2]
        above = self.sumMatrix[row1 - 1][col2]
        left = self.sumMatrix[row2][col1 - 1]
        topLeft = self.sumMatrix[row1 - 1][col1 - 1]
        return bottomRight - above - left + topLeft

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)



