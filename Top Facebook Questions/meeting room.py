# 252. Meeting Rooms
"""
Given an array of meeting time intervals where intervals[i] = [starti, endi], determine if a person could attend all meetings.
Example 1:

Input: intervals = [[0,30],[5,10],[15,20]]
Output: false
Example 2:

Input: intervals = [[7,10],[2,4]]
Output: true

Constraints:
0 <= intervals.length <= 104
intervals[i].length == 2
0 <= starti < endi <= 106
"""
class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort(key=lambda x: x[0])
        for i in range(1, len(intervals)):
            if intervals[i][0] < intervals[i-1][1]:
                return False
        return True


# 253. Meeting Rooms II
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        start = sorted(x[0] for x in intervals)
        end = sorted(x[1] for x in intervals)
        res, cnt = 0, 0
        s, e = 0, 0
        while s < len(intervals):
            if start[s] < end[e]:
                cnt += 1
                s += 1
            else:
                cnt -= 1
                e += 1
            res = max(res, cnt)

        return res

# Heap solution:
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[0])
        heap = []  # stores the end time of intervals
        for i in intervals:
            if heap and i[0] >= heap[0]:
            # means two intervals can use the same room
                heapq.heapreplace(heap, i[-1])
            else:
                # new room is located
                heapq.heappush(heap, i[-1])
        return len(heap)

# 56. Merge Intervals
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        res = [intervals[0]]
        for start, end in intervals[1:]:
            if start <= res[-1][1]:
                res[-1][1] = max(end, res[-1][1])
            else:
                res.append([start, end])

        return res