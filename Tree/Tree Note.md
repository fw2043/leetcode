# Definition of a tree:
1. there are n-1 edges for tree with n nodes
2. there is no cycle
# Spanning tree of a graph
1. Mininum spanning tree qeustion,  it can be solved using either Kruskal or Prim's algorithm
2. Prim's algorithm,  takes O(NlgN) but the whole solution is dominated by O(N*N) due to graph creation (nested loop)