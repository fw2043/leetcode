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

# connectivity of components
# disjoint set: union find
# initilaize: O(n)
# find: O(logn)
# union: O(logn)
class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]
        self.rank = [1] * size
        self.count = size

    def Find(self, x):
        if x == self.root[x]:
            return x
        self.root[x] = self.Find(self.root[x])
        return self.root[x]

    def Union(self, x, y):
        rootX = self.Find(x)
        rootY = self.Find(y)

        if rootY != rootX:
            if self.rank[rootX] > self.rank[rootY]:
                self.root[rootY] = rootX

            elif self.rank[rootY] > self.rank[rootX]:
                self.root[rootX] = rootY
            else:
                self.root[rootY] = rootX
                self.rank[rootX] += 1

            self.count -= 1

    def getCount(self):
        return self.count


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        uf = UnionFind(n)

        for e in edges:
            uf.Union(e[0], e[1])

        return uf.getCount()





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







