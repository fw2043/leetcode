"""
Given an m x n matrix board containing 'X' and 'O', capture all regions that are 4-directionally surrounded by 'X'.
A region is captured by flipping all 'O's into 'X's in that surrounded region.
"""
##############################
#  capture all regions that are 4-directionally surrounded by 'X':  4 Xs around

#TODO: NEED TO UPDATE DFS
"""
BFS:
simialar to leetcode 200: using BFS to mark the cells/grids/nodes that do not need to change (escape cases)
"""


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return

        row = len(board)
        col = len(board[0])

        # step 1: retrieve all boarder cell:
        for i in range(col):
            self.bfs(board, 0, i)
            self.bfs(board, row - 1, i)
        for j in range(row):
            self.bfs(board, j, 0)
            self.bfs(board, j, col - 1)

        # step 2: flip the captured cells ( 'O' ---> "X") AND escaped one ('E' ---> 'O')
        for r in range(0, row):
            for c in range(0, col):
                if board[r][c] == 'O':
                    board[r][c] = 'X'  # captured
                elif board[r][c] == 'E':
                    board[r][c] = 'O'  # escaped

    def bfs(self, board: List[List[str]], row: int, col: int):
        q = collections.deque([(row, col)])
        while q:
            m, n = q.popleft()
            if board[m][n] != "O":
                continue
            board[m][n] = "E"
            directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
            for dm, dn in directions:  # 4 Distions around the current grid have to be X, then we can assgin the current grid to "X"
                next_m, next_n = m + dm, n + dn
                if next_m < 0 or next_n < 0 or next_m >= len(board) or next_n >= len(board[0]):
                    continue
                q.append((next_m, next_n))



# class Solution:
#     def solve(self, board: List[List[str]]) -> None:
#         """
#         Do not return anything, modify board in-place instead.
#         """
#         if not board or not board[0]:
#             return
#
#         for m in range(len(board)):
#             for n in range(len(board[0])):
#                 # if the grid is "o", then go to BFS to check the grids around it:
#                 if board[m][n] == 'O':
#                     self.bfs(board, m, n)
#
#     def bfs(self, board: List[List[str]], m: int, n: int):
#         q = collections.deque([(m, n)])
#         while q:
#             m, n = q.popleft()
#             directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
#             for dm, dn in directions:  # 4 Distions around the current grid have to be X, then we can assgin the current grid to "X"
#                 m, n = m + dm, n + dn
#                 if m < 0 or n < 0 or m >= len(board) or n >= len(board[0]) or board[m][n] == "X":
#                     continue
#                 board[m][n] == 'X'
#                 q.append((m, n))