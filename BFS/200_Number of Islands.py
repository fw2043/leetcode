"""
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.
An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.
Example 1:
Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

Example 2:
Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 300
grid[i][j] is '0' or '1'.
"""
"""
Method1: BFS
Time complexity: O(MN)===> max: 4*M*N
Space complexity: O(min(M, N))
"""


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0

        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    count += 1
                    self.bfs(grid, i, j)
        return count

    # Time complexity: O(MN)===> max: 4*M*N
    # Space complexity: O(min(M, N))
    def bfs(self, grid, i, j):
        q = collections.deque([(i, j)])
        grid[i][j] = '@'

        while q:
            i, j = q.popleft()
            # 4 directions
            for delta_i, delta_j in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                next_i = i + delta_i
                next_j = j + delta_j
                # edge case or they are water, go to next node
                if next_i < 0 or next_j < 0 or next_i >= len(grid) or next_j >= len(grid[0]) or grid[next_i][
                    next_j] != '1':
                    continue
                q.append((next_i, next_j))
                grid[next_i][next_j] = '@'
