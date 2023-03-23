from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        prev_h = head
        h = head.next
        prev_h.next = None

        while h is not None:
            if h.val > prev_h.val:
                prev_h.next = h
                prev_h = h
            h = h.next
            prev_h.next = None
        return head