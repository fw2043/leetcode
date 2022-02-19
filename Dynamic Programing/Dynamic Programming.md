https://leetcode.com/explore/learn/card/dynamic-programming/631/strategy-for-solving-dp-problems/4096/

## What is Dynamic Programming?
1. The problem can be broken down into "**overlapping subproblems**" - smaller versions of the original problem that are re-used multiple times.

2. The problem has an "**optimal substructure**" - an optimal solution can be formed from optimal solutions to the overlapping subproblems of the original problem.

## Two ways to implement a DP algorithm:
1. Bottom-up, also known as tabulation: uses **iteration**

         Pseudocode example for bottom-up
        F = array of length (n + 1)
        F[0] = 0
        F[1] = 1
        for i from 2 to n:
            F[i] = F[i - 1] + F[i - 2]
            
2. Top-down, also known as memoization: uses **recursion**

        // Pseudocode example for top-down
        
        memo = hashmap
        Function F(integer i):
            if i is 0 or 1: 
                return i
            if i doesn't exist in memo:
                memo[i] = F(i - 1) + F(i - 2)
            return memo[i]

## When to Use DP
**The first characteristic** that is common in DP problems is that the problem will ask for the optimum value (maximum or minimum) of something, or the number of ways there are to do something. For example:

* What is the minimum cost of doing...
* What is the maximum profit from...
* How many ways are there to do...
* What is the longest possible...
* Is it possible to reach a certain point...

**The second characteristic** that is common in DP problems is that future "decisions" depend on earlier decisions.
## Framework for DP Problems
1. A function or data structure that will compute/contain the answer to the problem for every given state.

2. A recurrence relation to transition between states.

3. Base cases, so that our recurrence relation doesn't go on infinitely.















