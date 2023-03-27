from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head is None:
            return head
        if n <= 0:
            return head
        L = 0
        h = head
        while h is not None:
            L += 1
            h = h.next
        if n > L:
            return head
        if n == L:
            return head.next
        
        parent = head
        cur_node = head.next
        cur_n = L-1
        while cur_n > n:
            cur_n -= 1
            parent = cur_node
            cur_node = cur_node.next
        parent.next = cur_node.next
        return head