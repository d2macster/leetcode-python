from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        result = head
        lr = head
        h = head.next
        head.next = None
        while h is not None:
            ch = h
            h = h.next
            ch.next = None

            if ch.val <= result.val:
                ch.next = result
                result = ch
                continue
            if ch.val >= lr.val:
                lr.next = ch
                lr = ch
                continue
            r = result
            
            while r.val < ch.val:
                rn = r.next
                if rn.val >= ch.val:
                    r.next = ch
                    ch.next = rn
                    break
                r = r.next


        return result