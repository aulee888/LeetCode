class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __str__(self):
        return f'P: {self.val}\nL: {self.left.val} R: {self.right.val}'


class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> list:

        def helper(curr, total, path):
            total -= curr.val
            path.append(curr.val)

            if not curr.left and not curr.right and total == 0:
                ans.append(path)

            if curr.left:
                helper(curr.left, total, path[:])

            if curr.right:
                helper(curr.right, total, path[:])

        if not root:  # Corner case; when root is None
            return []

        ans = []
        helper(root, sum, [])
        return ans
