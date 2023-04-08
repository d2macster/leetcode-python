from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        h1 = head
        h2 = head
        l = 1
        while h2 is not None:
            h1 = h1.next
            h2 = h2.next
            l += 1
            if h2 is not None:
                h2 = h2.next
                l += 1
        
        if l % 2 == 1:
            return h1
        else:
            return h1.next
