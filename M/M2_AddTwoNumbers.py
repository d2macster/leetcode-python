from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        sum = ListNode(l1.val + l2.val)
        carrier = int(sum.val / 10)
        sum.val = sum.val % 10
        s = sum
        l1 = l1.next
        l2 = l2.next
        while l1 is not None or l2 is not None:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            n = ListNode(v1 + v2 + carrier)
            carrier = int(n.val / 10)
            n.val = n.val % 10
            s.next = n
            s = n

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        if carrier:
            n = ListNode(1)
            s.next = n
            s = n

        return sum 