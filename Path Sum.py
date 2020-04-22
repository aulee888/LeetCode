class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __str__(self):
        return f'P: {self.val}\nL: {self.left.val} R: {self.right.val}'


class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:

        def helper(curr, total):
            total += curr.val

            if curr.left:
                if helper(curr.left, total):
                    return True

            if curr.right:
                if helper(curr.right, total):
                    return True

            if not curr.left and not curr.right and total == sum:
                return True

            else:
                return False

        if not root:  # Corner case; None is root.
            return False
        else:
            return helper(root, 0)
