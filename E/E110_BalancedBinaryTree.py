from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        layer = [root]
        depth = 0
        depth_set = set()
        while layer:
            depth += 1
            new_layer = []
            for n in layer:
                if n.left is None and n.right is None:
                    depth_set.add(depth)

                if n.left is not None:
                    new_layer.append(n.left)
                if n.right is not None:
                    new_layer.append(n.right)
            L = len(depth_set)
            if L > 2:
                return False
            if L == 2:
                dl = list(depth_set)
                if abs(dl[0] - dl[1]) > 1:
                    return False
            
            layer = new_layer
        return True