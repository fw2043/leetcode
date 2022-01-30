"""
Given the root of a binary tree, return its maximum depth.
A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: 3

Example 2:
Input: root = [1,null,2]
Output: 2


Constraints:
The number of nodes in the tree is in the range [0, 104].
-100 <= Node.val <= 100
"""
# Iteration
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # empty node:
        if not root:
            return 0
        stack = [(1, root)]
        depth = 0
        while stack:
            curr_depth, node = stack.pop()
            if node:
                depth = max(depth, curr_depth)
                stack.append((curr_depth + 1, node.left))
                stack.append((curr_depth + 1, node.right))

        return depth


# Recursion
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # empty node:
        if not root:
            return 0
        children = [root.left, root.right]
        # leaf node:
        if not any(children):
            return 1
        max_depth = float('-inf')
        for c in children:
            if c:
                max_depth = max(self.maxDepth(c), max_depth)

        return max_depth + 1
