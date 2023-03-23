from typing import Optional
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        check_p = p is None
        check_q = q is None
        if check_p and check_q:
            return True
        if check_p ^ check_q:
            return False
        pq = deque()
        qq = deque()
        pq.appendleft(p)
        qq.appendleft(q)
        
        while pq or qq:
            if len(pq) != len(qq):
                return False
            epq = pq.popleft()
            eqq = qq.popleft()
            if epq.val != eqq.val:
                return False
            check_epq_left = epq.left is None
            check_epq_right = epq.right is None
            check_eqq_left = eqq.left is None
            check_eqq_right = eqq.right is None
            if check_epq_left ^ check_eqq_left:
                return False
            if check_epq_right ^ check_eqq_right:
                return False
            if epq.left is not None:
                pq.appendleft(epq.left)
            if epq.right is not None:
                pq.appendleft(epq.right)

            if eqq.left is not None:
                qq.appendleft(eqq.left)
            if eqq.right is not None:
                qq.appendleft(eqq.right)
            
        return True
