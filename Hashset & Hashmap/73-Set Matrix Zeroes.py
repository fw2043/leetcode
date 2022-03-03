"""
Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's, and return the matrix.
You must do it in place.

Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]

Constraints:
m == matrix.length
n == matrix[0].length
1 <= m, n <= 200
-231 <= matrix[i][j] <= 231 - 1
"""
# In Place
# Can you provide a constant space solution?

# Approach 1: Additional memory
"""
Time Complexity: O(M×N) where M and N are the number of rows and columns respectively.
Space Complexity: O(M+N).
"""
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # First find all the cells location(rows, cols) with zero value
        # Then go through this matrix to set them to zero

        row_len = len(matrix)
        col_len = len(matrix[0])
        row_set, col_set = set(), set()

        for r in range(row_len):
            for c in range(col_len):
                if matrix[r][c] == 0:
                    row_set.add(r)
                    col_set.add(c)

        for r in range(row_len):
            for c in range(col_len):
                if r in row_set or c in col_set:
                    matrix[r][c] = 0

# Approach 2: O(1) Space, Efficient Solution
# The idea is that we can use the first cell of every row and column as a flag.
# This flag would determine whether a row or column has been set to zero.
# This means for every cell instead of going to M+N cells and setting it to zero we just set the flag in two cells.
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows, cols = len(matrix), len(matrix[0])

        # determine which row/col need to be zero, also check if the first row and first col should be zero or not?
        row_flag = col_flag = False
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    if i == 0:
                        row_flag = True
                    if j == 0:
                        col_flag = True

                    elif i != 0 and j != 0:
                        matrix[i][0] = 0
                        matrix[0][j] = 0

        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        if row_flag:  # the first row should be zero
            matrix[0] = [0] * cols

        if col_flag: # the first col should be zero
            for r in range(rows):
                matrix[r][0] = 0