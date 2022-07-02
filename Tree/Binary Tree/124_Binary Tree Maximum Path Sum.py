"""
A path in a binary tree is a sequence of nodes where each pair of adjacent nodes
in the sequence has an edge connecting them. A node can only appear in the sequence at most once.
Note that the path does not need to pass through the root.

The path sum of a path is the sum of the node's values in the path.

Given the root of a binary tree, return the maximum path sum of any non-empty path.

Example 1:
Input: root = [1,2,3]
Output: 6
Explanation: The optimal path is 2 -> 1 -> 3 with a path sum of 2 + 1 + 3 = 6.

Example 2:
Input: root = [-10,9,20,null,null,15,7]
Output: 42
Explanation: The optimal path is 15 -> 20 -> 7 with a path sum of 15 + 20 + 7 = 42.


Constraints:
The number of nodes in the tree is in the range [1, 3 * 104].
-1000 <= Node.val <= 1000
"""
# A node can only appear in the sequence at most once
# have to split at the subtrees 8--13 or 8--4,can not visit 8 twice.
"""
                          5
                         / \
                        4   8
                       /   / \
                      11  13  4
                     /  \    / \
                    7    2  5   1
"""
#  # global variable: res = root.val, nonlocal res
# Recursion:
# compute max path sum with split: split (15 + 20 + 7). need to check if we need to update res
# return root + either left or right: max(root+left, root+right) return to the parent

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # root = [-10,9,20,null,null,15,7]
        # global variable
        res = root.val

        # return max path sum without split
        def dfs(root):
            nonlocal res
            if not root:
                return 0

            leftMax = dfs(root.left)
            rightMax = dfs(root.right)

            # if negative value, then 0
            leftMax = max(leftMax, 0)
            rightMax = max(rightMax, 0)

            # compute max path sum with split: split (15 + 20 + 7)
            res = max(res, leftMax + root.val + rightMax)

            # return root + either left or right: max(root+left, root+right) return to the parent
            return root.val + max(leftMax, rightMax)

        dfs(root)
        return res


















