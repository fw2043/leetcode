# Depth First Search Algorithms in Graph(DFS)
1. is mainly used to 
    1. Traverse all vertices in a “graph”/tree;
    2. Traverse all paths between any two vertices in a “graph”/tree
    3. The longest path
    4. Permutations
2. Implement: Stack(First In Last Out, Last In First Out) & Recursive call(Recursive Stack)
3. Time complexity: O(V + E),  We need to check every vertex and traverse through every edge in the graph.
4. Space complexity: O(V)
5. Steps:
    
    1. start from a starting node if you know start, otherwise check each node to go through dfs
    2. dfs: find the ending case( if something return True or....)
    3. initialize a node as the first node, put it to stack
    4. recursive call the stack: 
    pop from the stack, check either it is vistied or not, if not visited, then marked as visited,  
    put all the connected nodes(including the visited one) to stack, do something, pop one from stack, then follow the same thing 
    
6. data structure: 
    1. adjacency list: {1: [2, 5,6], 5: [1, 3, 2] }
    2. list: seen
    3. stack
 
 基于图的DFS: 无向图和BFS一样一般需要一个set来记录访问过的节点，避免重复访问造成死循环; 有向图 则不需要记录（797）
  Word XXX 系列面试中非常常见，例如word break，word ladder，word pattern，word search。  
    
    
 