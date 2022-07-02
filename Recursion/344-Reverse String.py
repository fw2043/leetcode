"""
Write a function that reverses a string. The input string is given as an array of characters s.

You must do this by modifying the input array in-place with O(1) extra memory.


Example 1:

Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
Example 2:

Input: s = ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]


Constraints:
1 <= s.length <= 105
s[i] is a printable ascii character.
"""
# don't use s.reverse()

# Two pointers:
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        n = len(s) - 1
        i = 0
        while i < n :
            s[n], s[i] = s[i], s[n]
            i += 1
            n -= 1
        return s

# recursive: change the while loop in the solution above to recursion
# while i < n ====> base case
# i += 1 and n -= 1   ====> recursion

class Solution:
    def reverseString(self, s: List[str]) -> None:
        def helper(left, right):
            if left >= right:
                return
            s[left], s[right] = s[right], s[left]
            helper(left + 1, right - 1)

        helper(0, len(s) - 1)

        return s
