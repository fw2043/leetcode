"""
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1.
You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first
if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.

Example 1:
Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take.
To take course 1 you should have finished course 0. So it is possible.

Example 2:
Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take.
To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1.
So it is impossible.


Constraints:
1 <= numCourses <= 105
0 <= prerequisites.length <= 5000
prerequisites[i].length == 2
0 <= ai, bi < numCourses
All the pairs prerequisites[i] are unique.
"""
# Hint: This problem is equivalent to finding if a cycle exists in a directed graph.
# If a cycle exists, no topological ordering exists and therefore it will be impossible to take all courses.
# what if we have some disconnected graphs: no prerequisites ===> return True by default
###############################
# DFS
# how to build the graph? preqmap[crs].append(preq) or preqmap[preq).append(crs)
# in a dfs search, if 0 ----> 1 ----> 2 ----->0 (go to one of visited nodes again)
# what is the visited set: all courses along the current dfs path
# how to write dfs (return value: true /false, the base case: pre = [])
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # input: 5, 5
        # [[0,1],[0,2],[1,3],[1,4], [3,4]]
        preqMap = {i: [] for i in range(numCourses)} # can't use defaultdict in case there is any course is not included in
        for crs, pre in prerequisites:
            preqMap[crs].append(pre)
        # print('preqMap: ', preqMap)
        visited = set()  # all courses along the current dfs path

        def dfs(crs):
            # two base cases:
            if crs in visited:
                return False
            if preqMap[crs] == []:
                return True
            # starting recursion
            visited.add(crs)
            # print('starting recursion: ', visited)
            for neigbor in preqMap[crs]:
                if not dfs(neigbor):
                    return False
            # ending of recursion
            # print('ending recursion: ', visited)
            visited.remove(crs)  # to make sure if it include the couress in current path, for next path we start from empty
            preqMap[crs] = []
            return True

        # Call DFS for each courses
        for crs in range(numCourses):
            if not dfs(crs):
                return False
        # by default it is true, in case there are non-connected graph, no prerequisites
        return True
#########################
# BFS:
# edges and in-degree
# put nodes whose in-degree is 0 into queue, and then update the in degree
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        edges = {i: [] for i in range(numCourses)}
        in_degree = [0 for i in range(numCourses)]
        for crs, pre in prerequisites:
            edges[pre].append(crs)
            in_degree[crs] += 1

        # find the starting node whoese in-degree == 0
        zero_degree = deque([])
        count = 0
        for i in range(numCourses):
            if in_degree[i] == 0:
                zero_degree.append(i)

        while zero_degree:
            node = zero_degree.popleft()
            count += 1
            # update the relted in-degree
            for x in edges[node]:
                in_degree[x] -= 1
                if in_degree[x] == 0:
                    zero_degree.append(x)

        return count == numCourses








