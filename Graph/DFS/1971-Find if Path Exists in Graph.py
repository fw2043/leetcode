"""
There is a bi-directional graph with n vertices, where each vertex is labeled from 0 to n - 1 (inclusive).
The edges in the graph are represented as a 2D integer array edges, where each edges[i] = [ui, vi]
denotes a bi-directional edge between vertex ui and vertex vi. Every vertex pair is connected by at most one edge,
and no vertex has an edge to itself.

You want to determine if there is a valid path that exists from vertex start to vertex end.

Given edges and the integers n, start, and end, return true if there is a valid path from start to end, or false otherwise.


Example 1:
Input: n = 3, edges = [[0,1],[1,2],[2,0]], start = 0, end = 2
Output: true
Explanation: There are two paths from vertex 0 to vertex 2:
- 0 → 1 → 2
- 0 → 2

Example 2:
Input: n = 6, edges = [[0,1],[0,2],[3,5],[5,4],[4,3]], start = 0, end = 5
Output: false
Explanation: There is no path from vertex 0 to vertex 5.


Constraints:

1 <= n <= 2 * 105
0 <= edges.length <= 2 * 105
edges[i].length == 2
0 <= ui, vi <= n - 1
ui != vi
0 <= start, end <= n - 1
There are no duplicate edges.
There are no self edges.
"""
# DFS:
# Recursion without stack
class Solution:
    def validPath(self, n: int, edges: List[List[int]], start: int, end: int) -> bool:
        # n = 3, edges = [[0,1],[1,2],[2,0]], start = 0, end = 2
        #
        g = defaultdict(list[int])  # g = {0: [1, 2], 1: [0], 2: [0]....}
        for s, e in edges:  # bi-directional
            g[s].append(e)
            g[e].append(s)

        seen = set()

        def dfs(s, e):
            if s == e:
                return True
            seen.add(s)
            for i in g[s]:
                if i not in seen and dfs(i, e):
                    return True
            return False

        return dfs(start, end)

# Stack solution:
class Solution:
    def validPath(self, n: int, edges: List[List[int]], start: int, end: int) -> bool:

        adjacency_list = [[] for _ in range(n)]
        for a, b in edges:
            adjacency_list[a].append(b)
            adjacency_list[b].append(a)

        stack = [start]
        seen = set()

        while stack:
            # Get the current node.
            node = stack.pop()

            # Check if we have reached the target node.
            if node == end:
                return True

            # Check if we've already visited this node.
            if node in seen:
                continue
            seen.add(node)

            # Add all neighbors to the stack.
            for neighbor in adjacency_list[node]:
                stack.append(neighbor)

        # Our stack is empty and we did not reach the end node.
        return False