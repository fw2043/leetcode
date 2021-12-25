"""
Given two integer arrays pushed and popped each with distinct values,
return true if this could have been the result of a sequence of push and pop operations on an initially empty stack,
or false otherwise.



Example 1:
Input: pushed = [1,2,3,4,5], popped = [4,5,3,2,1]
Output: true
Explanation: We might do the following sequence:
push(1), push(2), push(3), push(4),
pop() -> 4,
push(5),
pop() -> 5, pop() -> 3, pop() -> 2, pop() -> 1

Example 2:
Input: pushed = [1,2,3,4,5], popped = [4,3,5,1,2]
Output: false
Explanation: 1 cannot be popped before 2.


Constraints:

1 <= pushed.length <= 1000
0 <= pushed[i] <= 1000
All the elements of pushed are unique.
popped.length == pushed.length
popped is a permutation of pushed.
"""
# Unique value?
# Same length? If not---> edge case
class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        # Input: pushed = [1,2,3,4,5], popped = [4,5,3,2,1]
        # mimic stack process
        stack = []
        N = len(popped)
        i = 0
        for p in pushed:
            stack.append(p)
            while stack and i < N and stack[-1] == popped[i]:
                i += 1
                stack.pop()

        return stack == []

"""
Time Complexity: O(N), where NN is the length of pushed and popped.
Space Complexity: O(N).
"""