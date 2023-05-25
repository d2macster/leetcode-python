from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return
        h = head
        L = 0
        while h:
            L += 1
            h = h.next
        L2 = int(L/2) + L % 2
        i = 1
        h = head
        while i < L2:
            h = h.next
            i += 1
        next = h.next
        h.next = None
        #revert the list
        h = next
        prev = None
        last = h
        while h:
            last = h
            next = h.next
            h.next = prev
            prev = h
            h = next
        h = head
        while h:
            next = h.next
            h.next = last
            h = next
            if last:
                ln = last.next
                last.next = next
                last = ln

if __name__ == "__main__":
    s = Solution()
    head = None
    prev = None
    for n in [1,2,3,4]:
        node = ListNode(val=n)
        if prev is None:
            prev = node
            head = node
        else:
            prev.next = node
            prev = node
    h = head
    # while h:
    #     print(h.val)
    #     h = h.next
    s.reorderList(head)
    
    h = head
    while h:
        print(h.val)
        h = h.next