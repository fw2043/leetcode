"""
Given a list of the scores of different students, items, where items[i] = [IDi, scorei] represents one score
from a student with IDi, calculate each student's top five average.

Return the answer as an array of pairs result, where result[j] = [IDj, topFiveAveragej] represents the student
with IDj and their top five average. Sort result by IDj in increasing order.

A student's top five average is calculated by taking the sum of their top five scores and dividing it by 5
using integer division.



Example 1:
Input: items = [[1,91],[1,92],[2,93],[2,97],[1,60],[2,77],[1,65],[1,87],[1,100],[2,100],[2,76]]
Output: [[1,87],[2,88]]
Explanation:
The student with ID = 1 got scores 91, 92, 60, 65, 87, and 100. Their top five average is (100 + 92 + 91 + 87 + 65) / 5 = 87.
The student with ID = 2 got scores 93, 97, 77, 100, and 76. Their top five average is (100 + 97 + 93 + 77 + 76) / 5 = 88.6, but with integer division their average converts to 88.

Example 2:
Input: items = [[1,100],[7,100],[1,100],[7,100],[1,100],[7,100],[1,100],[7,100],[1,100],[7,100]]
Output: [[1,100],[7,100]]


Constraints:
1 <= items.length <= 1000
items[i].length == 2
1 <= IDi <= 1000
0 <= scorei <= 100
For each IDi, there will be at least five scores.
"""


# edge case: the number of scores are less then 5?
# Thoughts:
# get all the scores for each student: map/dict
# sort
# heap or sort

# Approach 1: map and sort
# step1: map
# step2: sort
class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        students = {}
        res = []
        for item in items:
            id, score = item[0], item[1]
            if id not in students:
                students[id] = [score]
            else:
                students[id].append(score)

        for id, scores in students.items():
            scores.sort(reverse=True)
            avg = sum(scores[:5]) // 5
            res.append([id, avg])

        return sorted(res)
# Time complexity: O(n*logn)
# space complexity: O(n)

# Approach 2: min-heap ---->  -score to represent max-heap
# to get the min-heap for each student is O(logn), for
class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        students = collections.defaultdict(list)
        res = []
        for item in items:
            id, score = item[0], item[1]
            heapq.heappush(students[id], -score)

        for id in students:
            avg = sum(-heapq.heappop(students[id]) for i in range(5)) // 5

            res.append([id, avg])
        return sorted(res)

# to push and pop an element: O(logn)
# time complexity: O(nlogn)