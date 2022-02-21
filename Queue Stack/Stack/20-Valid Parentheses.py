"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.

Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
"""
# we can start from many open parentheses like (((((,
# # but if we see  the first closing paratenese,
# then the one before it have to be a right opening parathese, pop then out
# check the next closing parathese

# Stack + hashmap
# Time complexity: O(n)
# Space complexity: O(n)

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        para = {'}': '{', ']': '[', ')': '('}

        for char in s:
            # closing parenthese
            if char in para:
                # stack is not empty and the last one is the related openning parenthese
                if stack and stack[-1] == para[char]:
                    stack.pop()
                else:
                    return False
            # open parenthese
            else:
                stack.append(char)
        # if stack is empty return true, else return false
        return True if not stack else False

