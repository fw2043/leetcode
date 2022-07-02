"""
Given a directed acyclic graph (DAG) of n nodes labeled from 0 to n - 1,
find all possible paths from node 0 to node n - 1 and return them in any order.
The graph is given as follows: graph[i] is a list of all nodes you can visit from node i
(i.e., there is a directed edge from node i to node graph[i][j]).


Example 1:
Input: graph = [[1,2],[3],[3],[]]
Output: [[0,1,3],[0,2,3]]
Explanation: There are two paths: 0 -> 1 -> 3 and 0 -> 2 -> 3.

Example 2:
Input: graph = [[4,3,1],[3,2,4],[3],[4],[]]
Output: [[0,4],[0,3,4],[0,1,3,4],[0,1,2,3,4],[0,1,4]]


Constraints:

n == graph.length
2 <= n <= 15
0 <= graph[i][j] < n
graph[i][j] != i (i.e., there will be no self-loops).
All the elements of graph[i] are unique.
The input graph is guaranteed to be a DAG.
"""
# The input graph is guaranteed to be a DAG.

# Todo: Dp solution
# Todo: Backtracking solution

# DFS Solution
# after check all the paths of the node, have to pop it out so that we can go back to the previous one (after dfs(node), path.pop())
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        # directed graph, we don't need to mark visited node (seen list)
        if not graph or len(graph) == 0:
            return

        def dfs(node):
            # path: 0, 1
            path.append(node)
            if node == len(graph) - 1:
                paths.append(path.copy()) # Returns a shallow copy of a list. A shallow copy means any modification in the new list won’t be reflected in the original list.
                return
            next_nodes = graph[node]  # [1,2]
            for next_node in next_nodes:
                dfs(next_node)
                path.pop()  # have to pop 3 from path, so the path will be [0,1], back to 1, then pop 1,back to 0, then path = 0,2,3

        paths, path = [], []
        dfs(0)
        return paths




