"""
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1.
You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first
if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return the ordering of courses you should take to finish all courses. If there are many valid answers,
return any of them. If it is impossible to finish all courses, return an empty array.

Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: [0,1]
Explanation: There are a total of 2 courses to take. To take course 1 you should have finished course 0.
So the correct course order is [0,1].
Example 2:

Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
Output: [0,2,1,3]
Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both courses 1 and 2.
Both courses 1 and 2 should be taken after you finished course 0.
So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3].

Example 3:
Input: numCourses = 1, prerequisites = []
Output: [0]


Constraints:
1 <= numCourses <= 2000
0 <= prerequisites.length <= numCourses * (numCourses - 1)
prerequisites[i].length == 2
0 <= ai, bi < numCourses
ai != bi
All the pairs [ai, bi] are distinct.
"""

# DFS
# Build adjacent graph-----> FILO(stack),
# if you want to get the first course3 --->preq2 ---> preq1 --->preq0. so the output could be preq0, preq1, preq2
# Dfs for every singe node
# how to detect cycle? current path has cycle(use curr_path to store the
# end case: visited
# Time complexity: O(E+V)

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = {c: [] for c in range(numCourses)}
        for crs, prep in prerequisites:
            preMap[crs].append(prep)

        # if the crs has been added to the output
        visited = set()
        # the crs has been in the cycle: 0---> 1 --->2 --->0
        cycle = set()

        output = []
        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visited:
                return True
            cycle.add(crs)
            for prep in preMap[crs]:
                if not dfs(prep):
                    return False
            cycle.remove(crs)
            visited.add(crs)
            output.append(crs)
            return True

        for c in range(numCourses):
            if not dfs(c):
                return []
        return output





class Solution:

    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preq = collections.defaultdict(list)
        topological_order = []
        for crs, pre in prerequisites:
            preq[pre].append(crs)

        # there are 3 states for each node: visted(black, visiting(current recursion path), un-visited(white)
        color = ['white' for i in range(numCourses)]
        is_possible = True  # to identigy cycle

        def dfs(node):
            nonlocal is_possible
            if not is_possible:
                return
            # starting recursion
            color[node] = 'grey'
            # Treversave on neigboring vertices:
            if node in preq:
                for neibor in preq[node]:
                    if color[neibor] == 'white':
                        dfs(neibor)
                    elif color[neibor] == 'grey':
                        is_possible = False
            # recursion ends, we mark it as black
            color[node] = 'black'
            topological_order.append(node)

        for vertex in range(numCourses):
            # if we have not processed them yet
            if color[vertex] == 'white':
                dfs(vertex)
        # have to reverse the order
        return topological_order[::-1] if is_possible else []


# BFS
# Steps:
# 1. what are impossible cases to finish all courses(0 ---> 1, 1 --->0) and
# how to identify them: eventually in-degree for each node == 0 OR keep track the number of course you added
# 2. a grpah for search later
# 3. Count in-degree for each node
# 4. find the starting node
# 5. start to search the graph and update the in-degree, put zero in-degree to the queue
# 6. can't just return the result, have to have another condition: number of course you added or in-degree == 0 for all of them

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preq = collections.defaultdict(list)  # store the graph for search later
        in_degree = [0] * numCourses  # store in-degree for each node
        for u, v in prerequisites:
            preq[v].append(u)
            in_degree[u] += 1
            # print(preq)
        # print(in_degree)
        zero_indegree = deque()
        for i, degree in enumerate(in_degree):  # find the starting nodes whose in-degree == 0
            if degree == 0:
                zero_indegree.append(i)
        # print(zero_indegree)
        took = []
        while zero_indegree:
            course = zero_indegree.popleft()
            took.append(course)
            numCourses -= 1
            # print(took)
            for next_course in preq[course]:
                in_degree[next_course] -= 1
                if in_degree[next_course] == 0:
                    zero_indegree.append(next_course)

        return took if numCourses == 0 else []

# Kahn's alogorithm


