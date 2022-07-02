"""
You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Example 1:
Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Example 2:
Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step


Constraints:
1 <= n <= 45
"""
# the number of distinct ways to stair n: stair[n] = stair[n-1] + stair[n-2] ====> which is Fibonacci numbers
# but stair(2) = 2
# Recursion with Memoization
# Time complexity : O(n). Size of recursion tree can go upto nn.
# Space complexity : O(n). The depth of recursion tree can go upto nn
class Solution:
    def climbStairs(self, n: int) -> int:
        # the number of distinct ways to stair n: stair[n] = stair[n-1] + stair[n-2] ====> which is Fibonacci numbers
        cache = {}

        def recursive_fib(n):
            if n in cache:
                return cache[n]
            # n = 2: return 2, a little different from Fabonacci number
            if n <= 2:
                result = n
            else:
                result = recursive_fib(n - 1) + recursive_fib(n - 2)

            cache[n] = result
            return result

        return recursive_fib(n)

