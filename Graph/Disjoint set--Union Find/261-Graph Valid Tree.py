"""
You have a graph of n nodes labeled from 0 to n - 1. You are given an integer n and a list of edges
where edges[i] = [ai, bi] indicates that there is an undirected edge between nodes ai and bi in the graph.

Return true if the edges of the given graph make up a valid tree, and false otherwise.

Example 1:
Input: n = 5, edges = [[0,1],[0,2],[0,3],[1,4]]
Output: true

Example 2:
Input: n = 5, edges = [[0,1],[1,2],[2,3],[1,3],[1,4]]
Output: false


Constraints:
1 <= n <= 2000
0 <= edges.length <= 5000
edges[i].length == 2
0 <= ai, bi < n
ai != bi
There are no self-loops or repeated edges.
"""
# what is a valid tree? Any connected graph without simple cycles is a tree
# how to identify cycle?
# Condition 1: The graph must contain n - 1 edges.
# Condition 2: The graph must contain a single connected component.

# DFS



# BFS











# UnionFind:
# TIme complexity: O(n), n is the number of vertices in the graph
# Space complexity: O(n)
class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]
        self.rank = [1] * size

    def find(self, x):
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]

    def union(self, x, y):
        # Check if A and B are already in the same set.
        rootx = self.find(x)
        rooty = self.find(y)
        if rootx == rooty:
            return False
        if rootx != rooty:
            if self.rank[rootx] > self.rank[rooty]:
                self.root[y] = rootx
            elif self.rank[rootx] < self.rank[rooty]:
                self.root[x] = rooty
            else:
                self.root[y] = rootx
                self.rank[rootx] += 1

        return True

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # condition 1: must contains n -1 edges:
        if len(edges) != n - 1:
            return False

        uf = UnionFind(n)
        # Add each edge. Check if a merge happened:
        for a, b in edges:
            if not uf.union(a, b):
                return False
        return True