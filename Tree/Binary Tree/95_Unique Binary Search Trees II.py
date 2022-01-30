"""
Given an integer n, return all the structurally unique BST's (binary search trees),
which has exactly n nodes of unique values from 1 to n. Return the answer in any order.

Example 1:
Input: n = 3
Output: [[1,null,2,null,3],[1,null,3,2],[2,1,3],[3,1,null,null,2],[3,2,null,1]]

Example 2:
Input: n = 1
Output: [[1]]

Constraints:

1 <= n <= 8
"""
# Similar to leetcode 96
# Time complexity: O(n^2)
# space complexity: O(n)

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        def generateBSF(start, end):
            if start > end:
                return [None, ]
            all_trees = []
            for i in range(start, end + 1):
                # left subtrees: start to i-1
                left_subtrees = generateBSF(start, i - 1)
                # right subtrees: i +1 to end
                right_subtrees = generateBSF(i + 1, end)

                # connect left and right subtree to the root i:
                for l in left_subtrees:
                    for r in right_subtrees:
                        curr_tree = TreeNode(i)
                        curr_tree.left = l
                        curr_tree.right = r
                        all_trees.append(curr_tree)

            return all_trees

        return generateBSF(1, n) if n else []
