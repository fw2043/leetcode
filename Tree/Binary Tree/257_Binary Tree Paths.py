"""
Given the root of a binary tree, return all root-to-leaf paths in any order.
A leaf is a node with no children.
Input: root = [1,2,3,null,5]
Output: ["1->2->5","1->3"]
"""
"""
Constraints:
The number of nodes in the tree is in the range [1, 100].
-100 <= Node.val <= 100
"""
##################
# Recursive
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        result, path = [], []
        self.findPaths(root, path, result)
        return result

    def findPaths(self, node, path, result):
        # stop case
        if node is None:
            return
        # leaf node--base case
        if node.left is None and node.right is None:
            current_path = ""
            for n in path:
                current_path += str(n.val) + "->"
            result.append(current_path + str(node.val))

        if node.left:
            path.append(node)
            self.findPaths(node.left, path, result)
            path.pop()  # Backtracking for alternative paths

        if node.right:
            path.append(node)
            self.findPaths(node.right, path, result)
            path.pop()  # Backtracking for alternative paths

#### Non recursive: Stack
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if not root:
            return

        result, stack = [], [(root, "")]

        while stack:
            node, ls = stack.pop()
            # leaf node
            if not node.left and not node.right:
                result.append(ls + str(node.val))
            if node.left:
                stack.append((node.left, ls + str(node.val) + "->"))
            if node.right:
                stack.append((node.right, ls + str(node.val) + "->"))

        return result



