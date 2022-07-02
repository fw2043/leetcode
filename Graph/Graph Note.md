## Dijkstra’s algorithm: https://www.youtube.com/watch?v=XB4MIexjvY0
1. solves the “single-source shortest path” problem in a weighted directed graph with **non-negative weights**.
2. could be directed or non-directed graph
3. greedy method
4. relaxation: if (d[u] + c(u,v) < d[v]): d[v] = d[u] + c(u,v), start --> u --->v
5. worst case: n * n = n^2(for each vertix, have to relax all the connected vertices, the worst case is it is connected to all of them )
6. drawbacks: may work or may not work for negative weights graph
## Implemention:
1. minHeap & BFS: 

        heapq.heapify(list)
       
        heapq.heappop(list)
2. Time complexity: E*logV
Module:

# 图类算法总结: https://blog.csdn.net/ntt5667781/article/details/52743342
