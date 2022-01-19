"""
Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).
Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]
"""
##############################################################################
#######################################
import collections
from typing import List, Optional

"""
Method 1: using one queue: q
"""
## THe output format is List of List: [[3],[9,20],[15,7]]

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        # create a queue
        q = collections.deque()
        # initialize to root
        q.append(root)

        while q:
            # print(len(q), q)
            qLen = len(q)  # for each iteration, the length will be 1, 2, 4, 4 as it is appending more values
            # 1: 3
            # 2: 9, 20
            # 4: null, null, 15,7
            # 4: null,null,null,null
            level = []
            for i in range(qLen):
                node = q.popleft()
                # print(i, node)

                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            # print(level)
            if level:
                res.append(level)

        return res

"""
Method 2: using one queue: using the poped out node to get the next level and then append them to current_level
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []

        current_level = collections.deque([root])
        results = []
        while current_level:
            # print(current_level)
            # [3]
            res = []
            length_current_level = len(current_level)
            for i in range(length_current_level):

                # ######### using this poped out node to get the next level node and then append to current level
                node = current_level.popleft()  # delete/pop 3 from current level
                # print(i, current_level)  # empty []
                res.append(node.val)
                if node.left:
                    # [9]
                    current_level.append(node.left)
                if node.right:
                    # current level: [9,20]
                    current_level.append(node.right)
            # print(current_level)
            results.append(res)

        return results


""""
Method3: using two queue: current_level and next_level
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []

        current_level = [root]
        results = []
        while current_level:
            # save the values at the current level
            res = []
            # save the next level
            next_level = []
            for node in current_level:
                res.append(node.val)
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            # update the current level
            current_level = next_level
            results.append(res)

        return results


