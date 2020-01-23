class TreeNode:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        def rec_helper(tree, depth):

            if not tree:  # Base case; if reached node
                return depth

            depth += 1

            # Gets depths of left and right branches
            if tree.left and tree.right:
                left_branch = rec_helper(tree.left, depth)
                right_branch = rec_helper(tree.right, depth)

            elif tree.left and not tree.right:
                left_branch = rec_helper(tree.left, depth)
                right_branch = depth

            elif not tree.left and tree.right:
                left_branch = depth
                right_branch = rec_helper(tree.right, depth)

            else:
                return depth

            # Compare depths of branches and return deeper branch
            if left_branch >= right_branch:
                return left_branch

            else:
                return right_branch

        return rec_helper(root, 0)
