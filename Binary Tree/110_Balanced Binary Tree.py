"""
Given a binary tree, determine if it is height-balanced.
For this problem, a height-balanced binary tree is defined as:
a binary tree in which the left and right subtrees of every node differ in height by no more than 1.
"""
"""
Constraints:
The number of nodes in the tree is in the range [0, 5000].
-104 <= Node.val <= 104
"""
################################################################################
#### Approach 1: Top-down recursion:
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # approach 1: top-down

        if not root:
            return True

        # check if subtrees have height within 1. If they do, check if the subtrees are balanced

        return abs(self.height(root.left) - self.height(root.right)) < 2 \
               and self.isBalanced(root.left) \
               and self.isBalanced(root.right)

    def height(self, root: TreeNode):
        if not root:
            return -1
        return 1 + max(self.height(root.left), self.height(root.right))


##########################################################################################
# Bottom-up recursion
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # Bottom-up recursion
        return self.isBalancedHelper(root)[0]

    def isBalancedHelper(self, root: TreeNode) -> (bool, int):
        # An empty tree is balanced and has height -1
        if not root:
            return True, -1

        # Check subtrees to see if they are balanced:
        leftIsBalanced, leftHeight = self.isBalancedHelper(root.left)
        if not leftIsBalanced:
            return False, 0

        rightIsBalanced, rightHeight = self.isBalancedHelper(root.right)
        if not rightIsBalanced:
            return False, 0
        # If the subtrees are balanced, check if the current tree is balanced using their height:
        return (abs(leftHeight - rightHeight) < 2), 1 + max(leftHeight, rightHeight)



