"""
Given an array of meeting time intervals intervals where intervals[i] = [starti, endi],
return the minimum number of conference rooms required.

Example 1:
Input: intervals = [[0,30],[5,10],[15,20]]
Output: 2

Example 2:
Input: intervals = [[7,10],[2,4]]
Output: 1


Constraints:
1 <= intervals.length <= 104
0 <= starti < endi <= 106
"""
# Leetcode 252 meeting room

# Intervals: sort them and then linear search or binary search
# put starts and ends into two lists and sort them
# check the different scenario to increase the count?

# Time complexity: O(nlogn) + O(n)
# Space complexity: O(n)

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        # put the starts and ends into two lists and sort them
        start = sorted([i[0] for i in intervals])
        end = sorted(i[-1] for i in intervals)
        # res to store the result, count to track the number at each point
        res, count = 0, 0
        s, e = 0, 0
        # start will be done iterating first
        while s < len(intervals):
            if start[s] < end[e]:
                # there is a meeting starts before a meeting ends
                count += 1
                s += 1
            else:  # there is a meetind end
                count -= 1
                e += 1
            res = max(res, count)

        return res

# Heap solution:


