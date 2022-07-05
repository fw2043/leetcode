"""
Given an array of integers temperatures represents the daily temperatures,
return an array answer such that answer[i] is the number of days you have to wait after the ith day
to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.

Example 1:
Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]

Example 2:
Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]

Example 3:
Input: temperatures = [30,60,90]
Output: [1,1,0]


Constraints:
1 <= temperatures.length <= 105
30 <= temperatures[i] <= 100
"""
# Brute Force
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        answer = [0] * n
        for day in range(n):
            for future_day in range(day + 1, n):
                if temperatures[future_day] > temperatures[day]:
                    answer[day] = future_day - day
                    break

        return answer
# Stack

