"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

Example 1:
Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]

Example 2:
Input: n = 1
Output: ["()"]


Constraints:
1 <= n <= 8
"""
# BackTracking
# The conditions are:
# 1. the number of opening parentheses == the number of closing parentheses
# 2. only add opening parentheses if the number of opening < n
# 3. only add closing closing parentheses if the number of closing < the number of opening

###########################Note Note Notr
# if you use list to store the progress, you need to call list.pop(0 to return back to the previous step(back track)
########################################


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []

        def backTracking(openN, closeN):
            if openN == closeN == n:
                res.append(''.join(stack))
                return
            if openN < n:
                stack.append('(')
                backTracking(openN + 1, closeN)
                stack.pop()
            if closeN < openN:
                stack.append(')')
                backTracking(openN, closeN + 1)
                stack.pop()

        backTracking(0, 0)
        return res

# using a internal parameter to store the current S, then don't need to pop:
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtracking(openN, closeN, S):
            #
            # base population
            if openN == closeN == n:
                res.append(S)
                return
            if openN < n:
                backtracking(openN + 1, closeN, S + "(")
            if closeN < openN:
                backtracking(openN, closeN + 1, S + ")")

        backtracking(0, 0, '')
        return res
