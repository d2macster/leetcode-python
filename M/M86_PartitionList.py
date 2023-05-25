from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if not head:
            return head
        new_head: Optional[ListNode] = None
        new_head_last: Optional[ListNode] = None
        new_tail: Optional[ListNode] = None
        new_tail_last: Optional[ListNode] = None
        h = head
        while h is not None:
            next = h.next
            if h.val < x:
                if not new_head_last:
                    new_head = h
                    new_head_last = h
                    new_head_last.next = None
                else:
                    new_head_last.next = h
                    new_head_last = h
                    new_head_last.next = None
            else:
                if not new_tail_last:
                    new_tail = h
                    new_tail_last = h
                    new_tail_last.next = None
                else:
                    new_tail_last.next = h
                    new_tail_last = h
                    new_tail_last.next = None
            h = next
        
        if not new_head:
            return new_tail
        if not new_tail:
            return new_head
        
        new_head_last.next = new_tail
        return new_head