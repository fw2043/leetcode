"""
You have a graph of n nodes. You are given an integer n and an array edges where edges[i] = [ai, bi]
indicates that there is an edge between ai and bi in the graph.

Return the number of connected components in the graph.

Example 1:
Input: n = 5, edges = [[0,1],[1,2],[3,4]]
Output: 2

Example 2:
Input: n = 5, edges = [[0,1],[1,2],[2,3],[3,4]]
Output: 1

Constraints:

1 <= n <= 2000
1 <= edges.length <= 5000
edges[i].length == 2
0 <= ai <= bi < n
ai != bi
There are no repeated edges.
"""
# Todo
# This is Disjoint set ===> unionFind
#



# DFS
# find a connected components and mark them(set), then when find it again,
# Time complexity: O(E) edges
# Space complexity: O(E + N)
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        pair = collections.defaultdict(set)
        for u, v in edges:
            pair[u].add(v)
            pair[v].add(u)

        # print(pair): defaultdict(<class 'set'>, {0: {1}, 1: {0, 2}, 2: {1}, 3: {4}, 4: {3}})
        def helper(u):
            if u in pair:
                for v in pair[u]:
                    if v not in visited:
                        visited.add(v)
                        helper(v)

        visited = set()
        count = 0
        for i in range(n):
            if i not in visited:
                visited.add(i)
                helper(i)
                count += 1

        return count







