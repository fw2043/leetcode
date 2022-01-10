"""
Given a directed acyclic graph (DAG) of n nodes labeled from 0 to n - 1, find all possible paths from node 0 to node n - 1
and return them in any order.

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
# Bad Solution
# put the current path to the queue and track the last node in the current path to find the next node
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        # use a dictionay to store {node: [node1, node3]}
        paths = []
        if not graph or len(graph) == 0:
            return paths

        queue = deque() # can't do:  queue = deque([0]), it will be a list of int
        queue.append([0]) # list of list

        while queue:
            current_path = queue.popleft()
            node = current_path[-1]
            for next_node in graph[node]:
                temp_path = current_path.copy()
                temp_path.append(next_node)

                if next_node == len(graph) - 1:
                    paths.append(temp_path)
                else:
                    queue.append(temp_path)
        return paths