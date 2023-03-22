# Definition for singly-linked list.
from typing import List, Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1
        head : Optional[ListNode] = None
        prev_node: Optional[ListNode] = None
        if list1.val <= list2.val:
            head = list1
            prev_node = head
            list1 = list1.next
        else:
            head = list2
            prev_node = head
            list2 = list2.next
        

        while list1 is not None or list2 is not None:
            if list1 is None:
                prev_node.next = list2
                prev_node = list2
                list2 = list2.next
                continue
            if list2 is None:
                prev_node.next = list1
                prev_node = list1
                list1 = list1.next
                continue
            if list1.val <= list2.val:
                prev_node.next = list1
                prev_node = list1
                list1 = list1.next
            else:
                prev_node.next = list2
                prev_node = list2
                list2 = list2.next
        
        return head
if __name__ == "__main__":
    L1 = [1,2,4]
    L2 = [1,3,4]
    head1 = ListNode(L1[0])
    prev1 = head1
    head2 = ListNode(L2[0])
    prev2 = head2

    for v in L1[1:]:
        n = ListNode(v)
        prev1.next = n
        prev1 = n
    
    for v in L2[1:]:
        n = ListNode(v)
        prev2.next = n
        prev2 = n

    s = Solution()
    hm = s.mergeTwoLists(head1, head2)
    while hm is not None:
        print(hm.val)
        hm = hm.next