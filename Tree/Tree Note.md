# Summary:
1. https://www.cnblogs.com/love-yh/p/7248136.html
2. https://leetcode-solution-leetcode-pp.gitbook.io/leetcode-solution/thinkings/tree

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
4. Level-order Traversal: leetcode 102, 107, 103, min/max depth of binary tree: 
        
        标记层:
        class Solution:
        def bfs(k):
            # 使用双端队列，而不是数组。因为数组从头部删除元素的时间复杂度为 N，双端队列的底层实现其实是链表。
            queue = collections.deque([root])
            # 记录层数
            steps = 0
            # 需要返回的节点
            ans = []
            # 队列不空，生命不止！
            while queue:
                size = len(queue)
                # 遍历当前层的所有节点
                for _ in range(size):
                    node = queue.popleft()
                    if (step == k) ans.append(node)
                    if node.right:
                        queue.append(node.right)
                    if node.left:
                        queue.append(node.left)
                # 遍历完当前层所有的节点后 steps + 1
                steps += 1
            return ans
        
        
        
        不带层的模板: 
        class Solution:
            def bfs(k):
                # 使用双端队列，而不是数组。因为数组从头部删除元素的时间复杂度为 N，双端队列的底层实现其实是链表。
                queue = collections.deque([root])
                # 队列不空，生命不止！
                while queue:
                    node = queue.popleft()
                    # 由于没有记录 steps，因此我们肯定是不需要根据层的信息去判断的。否则就用带层的模板了。
                    if (node 是我们要找到的) return node
                    if node.right:
                        queue.append(node.right)
                    if node.left:
                        queue.append(node.left)
                return -1

5. Vertical traversal:Level-order Traversal + hash table, leetcode 314, 543
6. 所有搜索类的题目只要把握三个核心点，即开始点，结束点 和 目标即可。

DFS 搜索类的基本套路就是从入口开始做 dfs，然后在 dfs 内部判断是否是结束点，
这个结束点通常是叶子节点或空节点，关于结束这个话题我们放在七个技巧中的边界部分介绍，如果目标是一个基本值（比如数字）直接返回或者使用一个全局变量记录即可，如果是一个数组，则可以通过扩展参数的技巧来完成

        DFS 套路模板：
            # 其中 path 是树的路径， 如果需要就带上，不需要就不带
            def dfs(root, path):
                # 空节点
                if not root: return
                # 叶子节点
                if not root.left and not root.right: return
                path.append(root)
                # 逻辑可以写这里，此时是前序遍历
                dfs(root.left)
                dfs(root.right)
                # 需要弹出，不然会错误计算。
                # 比如对于如下树：
                """
                          5
                         / \
                        4   8
                       /   / \
                      11  13  4
                     /  \    / \
                    7    2  5   1
                """
                # 如果不 pop，那么 5 -> 4 -> 11 -> 2 这条路径会变成 5 -> 4 -> 11 -> 7 -> 2，其 7 被错误地添加到了 path
            
                path.pop()
                # 逻辑也可以写这里，此时是后序遍历
            
                return 你想返回的数据
            
 # Construct binary tree given two orders: leetcode 105, 106, 889:
 Key: determine the left, the length of all orders are same!
 
 #Sum: leetcode 129, 124, 112, 113, 437
        而有时候，我们需要 dfs 携带更多的有用信息。典型的有以下三种情况：
    携带父亲或者爷爷的信息。
        def dfs(root, parent):
            if not root: return
            dfs(root.left, root)
            dfs(root.right, root)
    携带路径信息，可以是路径和或者具体的路径数组等。
    路径和：
        def dfs(root, path_sum):
            if not root:
                # 这里可以拿到根到叶子的路径和
                return path_sum
            dfs(root.left, path_sum + root.val)
            dfs(root.right, path_sum + root.val)
    路径：
        def dfs(root, path):
            if not root:
                # 这里可以拿到根到叶子的路径
                return path
            path.append(root.val)
            dfs(root.left, path)
            dfs(root.right, path)
            # 撤销
            path.pop()
 
 # Populating/ Modification: 
 leetcode 116, 117
 # Special cases: 
 same tree(leetcode 100) and symmetric tree(leetcode 101)
 # Serialize and Deserialize Binary Tree:
 leetcode 297, 428, 449

 # Binaru search tree:
            












