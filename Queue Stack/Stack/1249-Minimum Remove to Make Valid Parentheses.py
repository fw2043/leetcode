"""
Given a string s of '(' , ')' and lowercase English characters.

Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions ) so that the resulting parentheses string is valid and return any valid string.

Formally, a parentheses string is valid if and only if:

It is the empty string, contains only lowercase characters, or
It can be written as AB (A concatenated with B), where A and B are valid strings, or
It can be written as (A), where A is a valid string.


Example 1:
Input: s = "lee(t(c)o)de)"
Output: "lee(t(c)o)de"
Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.
Example 2:

Input: s = "a)b(c)d"
Output: "ab(c)d"
Example 3:

Input: s = "))(("
Output: ""
Explanation: An empty string is also valid.
"""
## Need to confirm:
# 1. the parenthese is only ( or )
# only lowcase english letter

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        # similar to valid parentheses problen: leetcode20
        # to keep track the nindex of opening parentheses,
        # when we go through string, find closing parenthese,
        # then pop this previous openning one
        # s = "lee(t(c)o)de)"
        stack = []
        N = len(s)
        # Strings are immutable, meaning they can't be modified
        S = list(s)  # need to modify invalid parenthese, so convert string to a list

        for i in range(N):
            if S[i] == '(':  # stack = [3,5]
                stack.append(i)  # keep tracking the index of open parentheses
            elif S[i] == ')':
                if stack:
                    stack.pop()
                else:  # it is invalid closing one, instead of removing it, then set it to empty
                    S[i] = ''

        # now check if stack still has opening parenthese need to replace to be '':
        for j in stack:
            S[j] = ''

        return ''.join(S)


