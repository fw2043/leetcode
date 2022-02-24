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

