# Graph 
https://leetcode.com/explore/learn/card/graph/620/breadth-first-search-in-graph/3896/
## Definitions:
1. Vertex/vertices
2. Edges
3. directed and in-directed 
4. Degree of a vertex
5. In-degree and Out-degree
6. Weight

## Disjoint set: https://leetcode.com/explore/learn/card/graph/618/disjoint-set/3881/
1. Disjoint set could be used to  check if vertices are connected or not:

    if they are connected, then they are in same disjoint set which meeans they have same head.
    
    Quick Find: root[vertex] = root Vertex
    1. The find function finds the root node of a given vertex: O(1)
    
    2. The union function unions two vertices and makes their root nodes the same:O(n)
    
    Quick Union: root[vertex] = parent Vertex
    1.
## Data structure for graph and tree:
1. adjacent metrix: https://leetcode.com/explore/learn/card/graph/620/breadth-first-search-in-graph/3894/
   
       edges = [[0,1],[1,2],[2,0]] #: bi-directional
       
       graphdict = defualtdict(list[int])
       for s, e in edges: # bi-directional
            graphdict[s].append(e)
            graphdict[e].append(s)
        q = deque([start])
        seen = set()
        while q:
            node = q.popleft()
            if node == end:
                return True
            if node in seen:
                continue
            seen.add(node)
            for i in g[node]:
                q.append(i)    
## Breadth-First Search Algorithm Report Issue
In Graph theory, the primary use cases of the “breadth-first search” (“BFS”) algorithm are:
The first path is the shortest path from a to b vertex
1. Traversing all vertices in the “graph”;   
2. Finding the shortest path between two vertices in a graph where all edges have **equal and positive weights**.
3. Complexity Analysis
    Time Complexity: O(V+E). Here, V represents the number of vertices, and EE represents the number of edges. We need to check every vertex and traverse through every edge in the graph. The time complexity is the same as it was for the DFS approach.
    
    Space Complexity: O(V). Generally, we will check if a vertex has been visited before adding it to the queue, so the queue will use at most O(V) space. Keeping track of which vertices have been visited will also require O(V) space.
    
## When do we need BFS:
### 1. Level Order Traversal:
leetcode 102 & 103

### 2. Connected Component: leetcode 200, 994, 130

即由一个点，找出图中所有的点。比如给出无向连通图(Undirected Connected Graph)中的一个点，找到这个图里的所有点。(Undirected: mark visited)

### 3. Topological Sort:

Find a global order for all nodes in a DAG(directed acyclic graph)

### 4. Shortest Path in Simple Graph:

注意这里一定要是简单图，也就是图中每条边长度都是1（或边长都相同）。为什么呢? 因为宽搜可以理解为一层层进行的，就跟二叉树遍历一样。要是层和层之间，或每层的长度都不一样，宽搜就没法进行了。通常这里简单图求最短路径用到BFS的都是无向图，极少数是有向图
