from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if not root:
            return 0
        s = 0
        if root.val >= low and root.val <= high:
            s += root.val
        if root.left and low < root.val:
            s += self.rangeSumBST(root.left, low, high)
        if root.right and high > root.val:
            s += self.rangeSumBST(root.right, low, high)
        return s
