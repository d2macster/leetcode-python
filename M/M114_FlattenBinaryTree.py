from typing import Optional, Tuple
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def walk(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
        l = root.left
        r = root.right
        root.left = None
        root.right = None
        R = root
        if l:
            le = self.walk(l)
            R.right = l
            R = le
        if r:
            re = self.walk(r)
            R.right = r
            R = re
        return R
    
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.walk(root)
        return root