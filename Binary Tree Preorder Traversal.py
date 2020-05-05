class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderTraversal(self, root):
        ans = []

        def helper(curr):
            if curr:
                ans.append(curr.val)

                helper(curr.left)
                helper(curr.right)
        helper(root)
        return ans
