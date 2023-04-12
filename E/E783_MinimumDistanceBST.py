from typing import Optional, Tuple
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def __init__(self) -> None:
        self.InorderData = []
    def inorder(self, root: Optional[TreeNode]) -> None:
        if not root:
            return
        self.inorder(root.left)
        self.InorderData.append(root.val)
        self.inorder(root.right)
    
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        self.inorder(root)
        minD = float('inf')
        for i in range(1, len(self.InorderData)):
            minD = min(minD, self.InorderData[i] - self.InorderData[i-1])
        return minD