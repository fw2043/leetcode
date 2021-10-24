"""
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.
An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
You may assume all four edges of the grid are all surrounded by water.
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
"""

"""
Method 1: BFS from Neetcode:
using an queue to traverse and a hashset to save visited node
"""


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        rows, cols = len(grid), len(grid[0])  # get the length of rows and cols
        visit = set()  # to track the visited islands
        islands = 0

        # BFS Approach: using an queue to tranverse the 4 neighbors and hashset to store the visited grids/nodes
        def bfs(r, c):  # inner function to update visited islands
            q = collections.deque()
            visit.add((r, c))
            q.append((r, c))  # append the current node
            # print("the first: ", q)
            while q:
                row, col = q.popleft()
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if (r in range(rows) and
                            c in range(cols) and
                            grid[r][c] == "1" and
                            (r, c) not in visit):
                        q.append((r, c))  # append the node
                        print(r, c, q)
                        visit.add((r, c))  # add it to the set
                # print("q: ", q)
                # print("visit: ", visit)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visit:  # find an island
                    print(r, c, visit)
                    bfs(r, c)
                    islands += 1
                    # print('islands: ', islands)

        return islands
