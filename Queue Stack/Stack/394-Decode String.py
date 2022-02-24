"""
Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times.
Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; there are no extra white spaces, square brackets are well-formed, etc.

Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers,k.
For example, there will not be input like 3a or 2[4].

Example 1:
Input: s = "3[a]2[bc]"
Output: "aaabcbc"
Example 2:

Input: s = "3[a2[c]]"
Output: "accaccacc"
Example 3:

Input: s = "2[abc]3[cd]ef"
Output: "abcabccdcdcdef"


Constraints:
1 <= s.length <= 30
s consists of lowercase English letters, digits, and square brackets '[]'.
s is guaranteed to be a valid input.
All the integers in s are in the range [1, 300].
"""
# All the integers in s are in the range [1, 300].
# could be nested brackets
# Use a stack
# when we should pop the characters?
# put all the characters and digit to stack
# if it is ], then pop all the characters until stack[-1] is '[', then pop all the digits
# then process the substing, put it back to stack

class Solution:
    def decodeString(self, s: str) -> str:
        # input: 54[ab3[cd]]
        stack = []
        for i in range(len(s)):
            if s[i] != ']':  # stack = [5,4,'[',a, b,3, '[', c,d]
                stack.append(s[i])
            else:  #
                substr = ''
                while stack[-1] != '[':
                    substr = stack.pop() + substr  # put the new pop character at the beginning
                    # substr = [cd]
                # pop opening bracket'[' out:
                stack.pop()
                # get the digits:
                k = ''
                while stack and stack[-1].isdigit():
                    k = stack.pop() + k
                # add the new substr k times to stack
                stack.append(int(k) * substr)

        return ''.join(stack)