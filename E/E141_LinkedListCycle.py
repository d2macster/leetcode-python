from typing import Optional
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False
        if head.next is None:
            return False
        if head.next == head:
            return True
        
        hl = head.next
        head.next = None
        while hl is not None:
            if hl.next == head:
                return True
            p = hl
            hl = hl.next
            p.next = head
        return False