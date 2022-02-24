"""
You are given a string s and an integer k, a k duplicate removal consists of choosing k adjacent and equal letters from s and removing them, causing the left and the right side of the deleted substring to concatenate together.

We repeatedly make k duplicate removals on s until we no longer can.

Return the final string after all such duplicate removals have been made. It is guaranteed that the answer is unique.

Example 1:
Input: s = "abcd", k = 2
Output: "abcd"
Explanation: There's nothing to delete.

Example 2:
Input: s = "deeedbbcccbdaa", k = 3
Output: "aa"
Explanation:
First delete "eee" and "ccc", get "ddbbbdaa"
Then delete "bbb", get "dddaa"
Finally delete "ddd", get "aa"

Example 3:
Input: s = "pbbcggttciiippooaais", k = 2
Output: "ps"


Constraints:
1 <= s.length <= 105
2 <= k <= 104
s only contains lower case English letters.
"""
# Need to confirm, only lower case? YEs
# the range of k?

# Use a stack to store the characters, when there are k same characters, delete them.
# how to track the times each character we have seen?
# ---->use a pair to store the value and the count of each character.
# So instead of a normal stack list, we use list of list for the stack
# why stack.append([c, 1]), not stack.append((c,1))====> the tuples are immutable objects the lists are mutable.

class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        # instead of a normal stack, we use pair in stack:
        # stack = [['d', 1], ['e', 1]]
        stack = []
        # s = "deeedbbcccbdaa", k = 3
        for c in s:
            # if it is adjacent duplicate:
            if stack and stack[-1][0] == c:
                stack[-1][1] += 1
            else:
                stack.append([c, 1])

            # check if we need to pop
            if stack and stack[-1][1] == k:
                stack.pop()

        # return the string
        return "".join(c * n for c, n in stack)



