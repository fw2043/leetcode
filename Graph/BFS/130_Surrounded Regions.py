"""
Given an m x n matrix board containing 'X' and 'O', capture all regions that are 4-directionally surrounded by 'X'.
A region is captured by flipping all 'O's into 'X's in that surrounded region.
"""
##############################
# A region is captured by flipping all 'O's into 'X's in that surrounded region.
# Reverse Thinking
# surrounded regions: everything except un-surrounded regions(connect to the boarder)
# 1. capture unsurrounded regions( O--> T)-----> DFS or BFS
# 2. capature surrounded regions(O ---> X)
# 3. Uncapture unsurrounded regions( T --> O)
# DFS
# Time Complexity O(n*m)
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return
        rows, cols = len(board), len(board[0])

        def capture(r, c):
            if (r < 0 or c < 0 or r == rows or c == cols or board[r][c] != "O"):  # stop searching
                return
            board[r][c] = "T"
            capture(r + 1, c)
            capture(r - 1, c)
            capture(r, c + 1)
            capture(r, c - 1)

        # 1. capture unsurrounded regions( O--> T)-----> DFS
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O" and (r in [0, rows - 1] or c in [0, cols - 1]):
                    capture(r, c)
        # 2. capature surrounded regions(O ---> X)
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"

                    # 3. Uncapture unsurrounded regions( T --> O)
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "T":
                    board[r][c] = "O"
# BFS
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return
        rows, cols = len(board), len(board[0])

        def capture(r, c):
            direct = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            q = deque([(r, c)])
            while q:
                r, c = q.popleft()
                if board[r][c] != "O":
                    continue
                board[r][c] = "T"
                # mark neighor:
                if c < len(board[0]) - 1: q.append((r, c + 1))
                if r < len(board) - 1: q.append((r + 1, c))
                if c > 0: q.append((r, c - 1))
                if r > 0: q.append((r - 1, c))

        # 1. capture unsurrounded regions( O--> T)-----> DFS
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O" and (r in [0, rows - 1] or c in [0, cols - 1]):
                    capture(r, c)
        # 2. capature surrounded regions(O ---> X)
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"

                    # 3. Uncapture unsurrounded regions( T --> O)
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "T":
                    board[r][c] = "O"