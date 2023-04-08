from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k <= 0:
            return head
        if head is None:
            return head
        l = 0
        h = head
        while h is not None:
            h = h.next
            l += 1
        if l == 1:
            return head
        k %= l
        if k == 0:
            return head
        h = head
        for _ in range(1, (l - k)):
            h = h.next
        new_head = h.next
        h.next = None
        h = new_head
        while h.next is not None:
            h = h.next
        h.next = head
        return new_head