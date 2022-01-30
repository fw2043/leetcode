"""
Given the roots of two binary trees p and q, write a function to check if they are the same or not.
Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

Example 1:
Input: p = [1,2,3], q = [1,2,3]
Output: true

Example 2:
Input: p = [1,2], q = [1,null,2]
Output: false

Example 3:
Input: p = [1,2,1], q = [1,1,2]
Output: false

Constraints:
The number of nodes in both trees is in the range [0, 100].
-104 <= Node.val <= 104
"""
#if they are structurally identical, and the nodes have the same value
# Recursion:
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not q or not p:
            return False
        if p.val != q.val:
            return False

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
# Iteration
# use a queue to store each pair of nodes in both of trees:
# check each node in a pair
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        def check(p, q):
            if not p and not q:
                return True
            if not q or not p:
                return False
            if p.val != q.val:
                return False
            return True

        deq = collections.deque([(p, q), ])
        while deq:
            pnode, qnode = deq.popleft()
            if not check(pnode, qnode):
                return False
            if pnode:
                deq.append((pnode.left, qnode.left))
                deq.append((pnode.right, qnode.right))

        return True

# Time complexity: O(N) since each node is visited exactly once.
# Space complexity : O(log(N)) in the best case of completely balanced tree
# and O(N) in the worst case of completely unbalanced tree, to keep a deque.
