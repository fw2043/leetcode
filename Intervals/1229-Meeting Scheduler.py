"""
Given the availability time slots arrays slots1 and slots2 of two people and a meeting duration duration,
return the earliest time slot that works for both of them and is of duration duration.

If there is no common time slot that satisfies the requirements, return an empty array.

The format of a time slot is an array of two elements [start, end]
representing an inclusive time range from start to end.

It is guaranteed that no two availability slots of the same person intersect with each other.
That is, for any two time slots [start1, end1] and [start2, end2] of the same person, either start1 > end2 or start2 > end1.



Example 1:
Input: slots1 = [[10,50],[60,120],[140,210]], slots2 = [[0,15],[60,70]], duration = 8
Output: [60,68]

Example 2:
Input: slots1 = [[10,50],[60,120],[140,210]], slots2 = [[0,15],[60,70]], duration = 12
Output: []


Constraints:
1 <= slots1.length, slots2.length <= 104
slots1[i].length, slots2[i].length == 2
slots1[i][0] < slots1[i][1]
slots2[i][0] < slots2[i][1]
0 <= slots1[i][j], slots2[i][j] <= 109
1 <= duration <= 106
"""
# Two pointers to iterate each list
# sort the lists
# #  10------50, 60------------120, 140-210
#         # 0-----15,     60-------70
# firstly, sort the lists
# the intersetion is:  min(end of two time slot) - max(start of two time slot)
# if intersetion >= during: return [intersetion_start, intersetion_start+ durion]
# if intersection < during: move to next time slot, who should move? ===> the one ends first
# Time complexity: sort----> nlogn + mlogm

class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        #  10------50, 60------------120, 140-210
        # 0-----15,     60-------70
        slots1.sort()
        slots2.sort()
        p1, p2 = 0, 0
        while p1 < len(slots1) and p2 < len(slots2):
            intersetion_start = max(slots1[p1][0], slots2[p2][0])
            intersetion_end = min(slots1[p1][1], slots2[p2][1])

            if intersetion_end - intersetion_start >= duration:
                return (intersetion_start, intersetion_start + duration)
            # move the one end earlier:
            if slots1[p1][1] < slots2[p2][1]:
                p1 += 1

            else:
                p2 += 1
        return []











