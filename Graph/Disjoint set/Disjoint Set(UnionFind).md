# disjoint set: the “union-find” data structure
The primary use of disjoint sets is to address the connectivity between the components of a network. 
The “network“ here can be a computer network or a social network. For instance, we can use a disjoint set to determine 
if two people share a common ancestor.
## Union: union by rank
## Find: path compression optimization
## Optimized “disjoint set” with Path Compression and Union by Rank:  understand and memorize the implementation below

    # UnionFind class
class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]
        # Use a rank array to record the height of each vertex, i.e., the "rank" of each vertex.
        # The initial "rank" of each vertex is 1, because each of them is
        # a standalone vertex with no connection to other vertices.
        self.rank = [1] * size

    # The find function here is the same as that in the disjoint set with path compression.
    def find(self, x):
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]

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


# Test Case
uf = UnionFind(10)
# 1-2-5-6-7 3-8-9 4
uf.union(1, 2)

uf.union(2, 5)

uf.union(5, 6)

uf.union(6, 7)

uf.union(3, 8)

uf.union(8, 9)

print(uf.connected(1, 5))  # true

print(uf.connected(5, 7))  # true

print(uf.connected(4, 9))  # false

# 1-2-5-6-7 3-8-9-4
uf.union(9, 4)

print(uf.connected(4, 9))  # true