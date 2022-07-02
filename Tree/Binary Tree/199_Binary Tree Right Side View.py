"""
Given the root of a binary tree, imagine yourself standing on the right side of it,
return the values of the nodes you can see ordered from top to bottom.

Example 1:
Input: root = [1,2,3,null,5,null,4]
Output: [1,3,4]

Example 2:
Input: root = [1,null,3]
Output: [1,3]

Example 3:
Input: root = []
Output: []


Constraints:
The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100
"""
# Level traversal: BFS
# at same level, traval from left to right, so the end of the level, rightside = node ===> will be the most right node
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        q = deque([root])
        res = []
        while q:
            rightSide = None
            size = len(q)
            for i in range(size):
                node = q.popleft()
                if node:
                    rightSide = node
                    # travel from left to right
                    q.append(node.left)
                    q.append(node.right)
            # at the end of each level, rightside will be the most right node at the level
            if rightSide:
                res.append(rightSide.val)
        return res