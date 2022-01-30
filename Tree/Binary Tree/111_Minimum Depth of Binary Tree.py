"""
Given a binary tree, find its minimum depth.
The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
Note: A leaf is a node with no children.

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: 2

Example 2:
Input: root = [2,null,3,null,4,null,5,null,6]
Output: 5

Constraints:

The number of nodes in the tree is in the range [0, 105].
-1000 <= Node.val <= 1000
"""
# Note: A leaf is a node with no children.
# DFS Iteration:
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        stack = [(1, root)]
        min_depth = float('inf')
        while stack:
            curr_depth, node = stack.pop()
            children = [node.left, node.right]
            if not any(children):
                min_depth = min(curr_depth, min_depth)
            for c in children:
                if c:
                    stack.append((curr_depth + 1, c))
        return min_depth

# BFS iteration
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        q = collections.deque([(1, root)])
        while q:
            depth, node = q.popleft()
            children = [node.left, node.right]
            if not any(children):
                return depth
            for c in children:
                if c:
                    q.append((depth + 1, c))
