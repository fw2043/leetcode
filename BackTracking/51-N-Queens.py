"""
The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle.
You may return the answer in any order.

Each solution contains a distinct board configuration of the n-queens' placement,
where 'Q' and '.' both indicate a queen and an empty space, respectively.



Example 1:

Input: n = 4
Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above

Example 2:
Input: n = 1
Output: [["Q"]]


Constraints:

1 <= n <= 9
"""
# Backtracking
"""
# first iterate each row, for each row: iterate through columns at the curent row,
                def backtrack_nqueen(row = 0, count = 0):
                    for col in range(n):
                        # iterate through columns at the curent row.
                        if is_not_under_attack(row, col):
                            # explore this partial candidate solution, and mark the attacking zone
                            place_queen(row, col)
                            if row + 1 == n:
                                # we reach the bottom, i.e. we find a solution!
                                count += 1
                            else:
                                # we move on to the next row
                                count = backtrack_nqueen(row + 1, count)
                            # backtrack, i.e. remove the queen and remove the attacking zone.
                            remove_queen(row, col)
                    return count
"""
# each queen has to be in separate different row/ column
# each queen has to be in separate different postive/ negative diagonal

# Backtracking
# since for each queen only have n rows options, only need to go through each row
# place each queen in each row for every row iteration until we reach to the bottom row = n -1
# only need to track column position for the previous queen
# for same diagonal, (row-colum) is same

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # 3 set to track colum, postive and negative diagonals where the queen is at each row
        col = set()
        postive_diag = set()
        negative_diag = set()

        # initialize the board:
        board = [['.'] * n for i in range(n)]
        res = []

        def dfs(r):
            # if r = n, then reach out to the bottom row, can return
            if r == n:
                # change the data format to string
                copy_board = [''.join(row) for row in board]
                res.append(copy_board)

            for c in range(n):
                if c in col or (r + c) in postive_diag or (r - c) in negative_diag:
                    continue

                # place the queen
                col.add(c)
                postive_diag.add(r + c)
                negative_diag.add(r - c)
                board[r][c] = 'Q'

                # backtracking:
                dfs(r + 1)

                # clean up to back track to the previous step
                col.remove(c)
                postive_diag.remove(r + c)
                negative_diag.remove(r - c)
                board[r][c] = '.'

        dfs(0)
        return res

