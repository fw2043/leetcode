"""
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.

Example 1:

Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true
Example 2:

Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false

Constraints:
m == matrix.length
n == matrix[i].length
1 <= m, n <= 100
-104 <= matrix[i][j], target <= 104
"""
##### Binary Search
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
        # step 1: check the midle row, [10,11,16,20] ---> is 3 between 10 and 20 ---> go top or bottom,
        # step 2: find the row, then binary search to find the item

        rows, cols = len(matrix), len(matrix[0])

        # find the right row: log(M)
        top, bott = 0, rows - 1
        while top <= bott:
            row = (top + bott) // 2  # row = 1: [10,11,16,20]
            if target > matrix[row][-1]:  # 3 > 20: false
                top = row + 1
            elif target < matrix[row][0]:  # 3 < 10: true
                bott = row - 1
            else:  # in this row, found the row
                break
        if not (top <= bott):  # not found the row, then couldn't find the number
            return False

        left, right = 0, cols - 1
        while left <= right:
            col = (left + right) // 2
            if target < matrix[row][col]:  # <
                right = col - 1
            elif target > matrix[row][col]:  # >
                left = col + 1
            else:  # ==
                return True

        return False



