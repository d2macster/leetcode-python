from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        l = 0
        h = head
        while h is not None:
            l += 1
            h = h.next
        m = int(l/2) + 1
        
        l = 0
        h = head
        while h is not None:
            l += 1
            if l == m:
                return h
            h = h.next
        return None
