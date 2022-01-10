"""
You are given an m x n grid where each cell can have one of three values:

0 representing an empty cell,
1 representing a fresh orange, or
2 representing a rotten orange.
Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.

Example 1:
Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
Output: 4

Example 2:
Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.

Example 3:
Input: grid = [[0,2]]
Output: 0
Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.


Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 10
grid[i][j] is 0, 1, or 2.
"""
# Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.
# one minute by one minute, cell of graph = 1 problem
# Shortest path---> BFS
# The difference from normal shortest path from source to target like leetcode 1091:
# No fresh oranges, then return the path, so have to keep track fresh orange, go through the grid first!
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        q = deque()  # to store the current rotten oranges
        time, fresh = 0, 0  # track how many of fresh
        # Iterate the grid to find the rotten and fresh orange
        for r in range(m):  # O(N) running time
            for c in range(n):
                if grid[r][c] == 2:
                    q.append([r, c])  # to store all the rotten oragnes
                elif grid[r][c] == 1:
                    fresh += 1
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        while q and fresh > 0:
            size = len(q)
            for i in range(size):
                r, c = q.popleft()
                for i, j in directions:
                    new_r, new_c = r + i, c + j
                    # outbound or not fresh,we do not need to do anything
                    if (new_r < 0 or new_r == len(grid)) or (new_c < 0 or new_c == len(grid[0])) or grid[new_r][
                        new_c] != 1:
                        continue
                    grid[new_r][new_c] = 2
                    q.append([new_r, new_c])
                    fresh -= 1
            time += 1
        return time if fresh == 0 else -1