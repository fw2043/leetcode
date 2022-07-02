# disjoint set: the “union-find” data structure
The primary use of disjoint sets is to address **the connectivity between the components of a network**. 
The “network“ here can be a computer network or a social network. For instance, we can use a disjoint set to determine 
if two people share a common ancestor.
## Union: union by rank
## Find: path compression optimization
## Optimized “disjoint set” with Path Compression and Union by Rank:  understand and memorize the implementation below
## Find: O(logn)
## Union: O(logn)
## Connected: O(logn)

            # UnionFind class
        class UnionFind:
            def __init__(self, size):
                self.root = [i for i in range(size)]
                # Use a rank array to record the height of each vertex, i.e., the "rank" of each vertex.
                # The initial "rank" of each vertex is 1, because each of them is
                # a standalone vertex with no connection to other vertices.
                self.rank = [1] * size
            
            # A basic implementation of the find function:
            def find(self, x):
                while x != self.root[x]:
                    x = self.root[x]
                return x
                    
            # The find function here is the same as that in the disjoint set with path compression.
            def find(self, x):
                if x == self.root[x]:
                    return x
                self.root[x] = self.find(self.root[x])
                return self.root[x]
                
             # A basic implementation of the union function:
             def union(self, x, y):
                rootX = self.find(x)
                rootY = self.find(y)
                if rootX != rootY:
                    self.root[rootY] = rootX
                         
            # The union function with union by rank
            def union(self, x, y):
                rootX = self.find(x)
                rootY = self.find(y)
                if rootX != rootY:
                    if self.rank[rootX] > self.rank[rootY]:
                        self.root[rootY] = rootX
                    elif self.rank[rootX] < self.rank[rootY]:
                        self.root[rootX] = rootY
                    else:
                        self.root[rootY] = rootX
                        self.rank[rootX] += 1
        
            def connected(self, x, y):
                return self.find(x) == self.find(y)



### Note: 

First, Data structure for this algorithm:
1. uses a list to record the root (representative) of each component: leetcode 547, 323
2. dict: initialzie key, value are themselves, leetcode 721
3. the index/key will represent themselves and the valu will represent the parent/root
Second, when to union? when they are connected!
