"""
Given the root of a binary tree, return the zigzag level order traversal of its nodes' values.
(i.e., from left to right, then right to left for the next level and alternate between).

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: [[3],[20,9],[15,7]]

Example 2:
Input: root = [1]
Output: [[1]]

Example 3:
Input: root = []
Output: []

Constraints:

The number of nodes in the tree is in the range [0, 2000].
-100 <= Node.val <= 100
"""
# Check the output format: [[3],[20,9],[15,7]]
# the relationship between the index number of sublist in output and level of node in the tree
# Need to track the level for reverse the sublist
# How to use level information to append node value to result: new level or already went to this level:
# result.append or result[level-1].append

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []

        results = []
        q = [(root, 1)]
        while q != []:
            node, level = q.pop(0)
            if node.left != None:
                q.append((node.left, level + 1))
            if node.right != None:
                q.append((node.right, level + 1))

            if level == len(results):
                results[level - 1].append(node.val)
            else:
                results.append([node.val])

        for i in range(len(results)):
            if i % 2 == 1:
                results[i] = results[i][::-1]
        return results


# DFS, recursion
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
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

        for i in range(len(levels)):
            if i % 2 == 1:
                levels[i] = levels[i][::-1]

        return levels