# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        """Length of path between two nodes is number of edges b/w them"""
        self.diameter = 0

        def counter(node):
            # Corner Case; if root is not given
            # Also base case; if root has no left/right
            if not node:
                return 0

            left_count = counter(node.left)
            right_count = counter(node.right)

            # Path of diameter
            if self.diameter < (left_count + right_count):
                self.diameter = left_count + right_count

            # Depth of node
            if left_count > right_count:
                return left_count + 1
            else:
                return right_count + 1

        counter(root)

        return self.diameter

t = TreeNode(1)
t.left = TreeNode(2)
t.left.left = TreeNode(4)
t.left.left.left = TreeNode(6)
t.left.left.right = TreeNode(7)
t.left.right = TreeNode(5)
t.left.right.left = TreeNode(8)
t.left.right.right = TreeNode(9)
t.left.right.right.right = TreeNode(10)

t.right = TreeNode(3)

print(Solution().diameterOfBinaryTree(t.left))
