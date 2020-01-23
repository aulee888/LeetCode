class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        p = root
        q = root

        def rec_helper(p, q):
            if p and q:
                print(p.val, q.val)

            if not p and not q:
                print(None, None)
                return True

            if p and not q:
                return False

            if not p and q:
                return False

            if p.val == q.val:
                return rec_helper(p.left, q.right) and \
                       rec_helper(p.right, q.left)

            return False

        return rec_helper(p, q)
