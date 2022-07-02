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
#### Approach 1:
# Top-down recursion: Time complexity: O(nlogn)
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
# Time complexity: O(n), space: O(n)
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            if not root:
                return (True, -1)
            left, right = dfs(root.left), dfs(root.right)
            balanced = (left[0] and right[0] and abs(left[1] - right[1]) <= 1)
            return (balanced, max(left[1], right[1]) + 1)

        return dfs(root)[0]

