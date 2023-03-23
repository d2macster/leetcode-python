from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        q = [root]
        depth = 0
        while q:
            depth += 1
            next_q = []
            for n in q:
                if n.left is not None:
                    next_q.append(n.left)
                if n.right is not None:
                    next_q.append(n.right)
            q = next_q
        return depth
