graph = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D', 'E'],
    'D': ['B', 'C', 'E', 'F'],
    'E': ['C', 'D'],
    'F': ['D']
}

# Traversing all Vertices of graph
def dfs(graph, s):
    stack = []
    stack.append(s)
    seen = []
    seen.append(s)
    while stack:
        vertex = stack.pop()
        nodes = graph[vertex]
        for node in nodes:
            if node not in seen:
                stack.append(node)
                seen.append(node)
        print(vertex)

# Traversing all paths between two vertices of bi-directional graph: leetcode 1971
def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
    adjacency = defaultdict(list)
    for u, v in edges:
        adjacency[u].append(v)
        adjacency[v].append(u)

    seen = set()
    stack = [source]

    while stack:
        node = stack.pop()
        # there are 3 possibilites
        if node == destination:
            return True
        if node in seen:
            continue
        seen.add(node)
        for neighbor in adjacency[node]:
            stack.append(neighbor)
    return False

#All Paths From Source to Target in a directed acyclic graph (DAG): 797

# Backtrack
# Time Complexity: O(2^N * N)

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        result = []
        target = len(graph) - 1
        def backtrack(currNode, path):
            # if we reach the target, no need to explore further.
            if currNode == target:
                result.append(path.copy())
                return
             # all posibilities: explore the neighbor nodes one after another.
            for nextNode in graph[currNode]:
                path.append(nextNode)
                backtrack(nextNode, path)
                path.pop()
        # kick of the backtracking, starting from the source node (0).
        path = [0]
        backtrack(0, path)
        return result

# Stack
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        result = []
        target = len(graph) - 1
        # (node, path): (0, [0])
        stack = [(0, [0])]
        while stack:
            node, path = stack.pop()
            if node == target:
                result.append(path.copy())
            for child in graph[node]:
                stack.append((child, path + [child]))

        return result

# recursion:
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        self.result = []
        target = len(graph) - 1

        def helper(node,path):
            if node == target:
                self.result.append(path)
            else:
                for nextNode in graph[node]:
                    helper(nextNode, path+[nextNode])
        helper(0, [0])
        return self.result

# The longest path: leetcode 329
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        dp = {}  # (r,c): LIP( Longest Increasing Path) to avoid deplicate computation
        # for a specific node, the steps need to do:
        def dfs(r, c, prevVal):
            # stop points:
            if r >= rows or r < 0 or c >= cols or c < 0 or matrix[r][c] <= prevVal:
                return 0
            # if the node is already visited:
            if (r, c) in dp:
                return dp[(r, c)]
            # 4 directions check:
            res = 1
            res = max(res, 1 + dfs(r + 1, c, matrix[r][c]))
            res = max(res, 1 + dfs(r - 1, c, matrix[r][c]))
            res = max(res, 1 + dfs(r, c + 1, matrix[r][c]))
            res = max(res, 1 + dfs(r, c - 1, matrix[r][c]))
            dp[(r, c)] = res
            return res

        # for each node, do dfs:
        for r in range(rows):
            for c in range(cols):
                # the values > 0, so set the preval = -1
                dfs(r, c, -1)

        return max(dp.values())

# NUmber of islands problem:
# 2D grid


if __name__ == "__main__":
    dfs(graph, 'A')

"""
A
C
E
D
F
B
"""