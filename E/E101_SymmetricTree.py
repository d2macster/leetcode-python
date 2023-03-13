class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import List, Optional
class Solution:
    def isLayerSymmetric(self, nodes: List[Optional[TreeNode]]) -> bool:
        L = len(nodes)
        if L <= 1:
            return True
        for i in range(int(L/2)):
            n1 = nodes[i]
            n2 = nodes[L-1-i]
            if n1 is None and n2 is None:
                continue
            if n1 is None and n2 is not None:
                return False
            if n1 is not None and n2 is None:
                return False
            if n1.val != n2.val:
                return False
        return True    

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        layer = [root]
        while layer:
            new_layer = []
            for node in layer:
                if node is None:
                    continue
                new_layer.append(node.left)
                new_layer.append(node.right)
            if not self.isLayerSymmetric(new_layer):
                return False
            layer = new_layer
        return True
Console
