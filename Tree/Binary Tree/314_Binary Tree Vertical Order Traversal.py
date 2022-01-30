"""
Given the root of a binary tree, return the vertical order traversal of its nodes' values.
(i.e., from top to bottom, column by column).

If two nodes are in the same row and column, the order should be from left to right.

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: [[9],[3,15],[20],[7]]

Example 2:
Input: root = [3,9,8,4,0,1,7]
Output: [[4],[9],[3,0,1],[8],[7]]

Example 3:
Input: root = [3,9,8,4,0,1,7,null,null,null,2,5]
Output: [[4],[9,5],[3,0,1],[8,2],[7]]


Constraints:

The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100
"""
# Vertical traversal:
# for root, hd = 0
# for left child, hd = parent_hd - 1
# for right child, hd = parent_hd + 1
# Time complexity: O(nlogn) for sorted(), O(n) for BFS
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        q = collections.deque([(root, 0)])
        hashTable = defaultdict(list)

        while q:
            qlen = len(q)
            for i in range(qlen):
                node, hd = q.popleft()
                if node:
                    hashTable[hd].append(node.val)
                    q.append((node.left, hd - 1))
                    q.append((node.right, hd + 1))

        return [hashTable[x] for x in sorted(hashTable.keys())]

















