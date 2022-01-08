"""
Given an n x n binary matrix grid, return the length of the shortest clear path in the matrix.
If there is no clear path, return -1.

A clear path in a binary matrix is a path from the top-left cell (i.e., (0, 0)) to the bottom-right cell (i.e., (n - 1, n - 1))
such that:

All the visited cells of the path are 0.
All the adjacent cells of the path are 8-directionally connected (i.e., they are different and they share an edge or a corner).
The length of a clear path is the number of visited cells of this path.

Example 1:
Input: grid = [[0,1],[1,0]]
Output: 2

Example 2:
Input: grid = [[0,0,0],[1,1,0],[1,1,0]]
Output: 4

Example 3:
Input: grid = [[1,0,0],[1,1,0],[1,1,0]]
Output: -1


Constraints:

n == grid.length
n == grid[i].length
1 <= n <= 100
grid[i][j] is 0 or 1
"""
# The length of a clear path is the number of visited cells of this path
# Not the path, the queue to store the current cells and steps
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] != 0:
            return -1
        m, n = len(grid), len(grid[0])
        q = deque() # to store the current cells to vistit and the current steps
        q.append([(0,0), 1])
        grid[0][0] == 1 # either mark the vistied to 1 or use a set to store the visited cells
        directions = [(0, 1), (0, -1), (1, 1), (-1, 1), (1, 0), (-1, 0), (-1, -1), (1, -1)]
        while q:
            size = len(q)
            for i in range(size):
                cell, steps = q.popleft()
                r, c = cell[0], cell[1]
                if r == m -1 and c == n -1:
                    return steps
                for i, j in directions:
                    new_r, new_c = r + i, c + j
                    if new_r >= 0 and new_r < m and new_c >= 0 and new_c < n and grid[new_r][new_c] == 0:
                        q.append([(new_r, new_c), steps + 1])
                        grid[new_r][new_c] = 1 # mark it vistied
        return -1
