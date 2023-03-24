from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.depth_helper(root) != -1
    
    def depth_helper(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        ld = self.depth_helper(root.left)
        if ld == -1:
            return -1
        rd = self.depth_helper(root.right)
        if rd == -1:
            return -1
        if abs(ld - rd) > 1:
            return -1
        return 1 + max(ld, rd)