"""
We are given an array asteroids of integers representing asteroids in a row.

For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right, negative meaning left). Each asteroid moves at the same speed.

Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.


Example 1:

Input: asteroids = [5,10,-5]
Output: [5,10]
Explanation: The 10 and -5 collide resulting in 10. The 5 and 10 never collide.
Example 2:

Input: asteroids = [8,-8]
Output: []
Explanation: The 8 and -8 collide exploding each other.
Example 3:

Input: asteroids = [10,2,-5]
Output: [10]
Explanation: The 2 and -5 collide resulting in -5. The 10 and -5 collide resulting in 10.


Constraints:
2 <= asteroids.length <= 104
-1000 <= asteroids[i] <= 1000
asteroids[i] != 0
"""
# Each asteroid moves at the same speed---> that is they can collide
# Confirm if the element could be 0? No
# use stack
# need to consider when we should append to stack, when we should pop from stack
# 1. first to identify the cases of collisions is the key
# the collision happens when:
# stack[-1] -----> (go right, positive), the asteroids[i] <------(go left, negative)
# 2. when collision happens, what we should do? > 0, < 0, ==0
# when to break the loop, when to continue the loop
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for new in asteroids:
            # while collision:
            while stack and new < 0 and stack[-1] > 0:
                # if stack[-1] + new > 0: new explode, don't need to append
                if stack[-1] + new < 0:
                    # stack[-1] explode, add new into stack
                    stack.pop()
                    continue

                elif stack[-1] + new == 0:
                    # both of them explode, pop, but don't need to compare, don't need to add new---> break
                    stack.pop()
                    break
                elif stack[-1] + new > 0:
                    # new explode, don't need to pop, don't need to add new---> break
                    break

            else:
                stack.append(new)

        return stack