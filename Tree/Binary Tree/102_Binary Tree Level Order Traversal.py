"""
Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).
Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]
"""
##############################################################################
#######################################
"""
Method 1:BFS
"""
## THe output format is List of List: [[3],[9,20],[15,7]]

# Time complexity: O(n)
# Space complexity: O(n)
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        # create a queue
        q = collections.deque()
        # initialize to root
        q.append(root)

        while q:
            # print(len(q), q)
            qLen = len(q)  # for each iteration, the length will be 1, 2, 4, 4 as it is appending more values
            # 1: 3
            # 2: 9, 20
            # 4: null, null, 15,7
            # 4: null,null,null,null
            level = []
            for i in range(qLen):
                node = q.popleft()
                # print(i, node)

                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            # print(level)
            if level:
                res.append(level)

        return res

# Method: DFS
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        levels = []

        def helper(node, level):
            if len(levels) == level:
                levels.append([])
            levels[level].append(node.val)
            if node.left:
                helper(node.left, level + 1)
            if node.right:
                helper(node.right, level + 1)

        helper(root, 0)
        return levels