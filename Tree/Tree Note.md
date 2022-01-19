# Definition of a tree:
1. there are n-1 edges for tree with n nodes
2. there is no cycle
# Spanning tree of a graph
1. Mininum spanning tree qeustion,  it can be solved using either Kruskal or Prim's algorithm
2. Prim's algorithm,  takes O(NlgN) but the whole solution is dominated by O(N*N) due to graph creation (nested loop)
# Traverse a Tree
1. Pre-order Traversal: root, left, right
2. In-order Traversal: let, root, right ====> binary search tree
3. Post-order Traversal: left, right, root ====> delete node, mathematical expression(using stack)
4. Recursive or Iterative