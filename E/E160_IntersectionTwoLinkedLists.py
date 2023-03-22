from typing import Optional, List
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def showList(self, head: ListNode) -> List[str]:
        result = []
        while head is not None:
            result.append(str(head.val))
            head = head.next
        return result
    

    def revertList(self, head: ListNode) -> ListNode:
        prev_head : Optional[ListNode] = None
        result = head
        while head is not None:
            result = head
            next_head = head.next
            head.next = prev_head
            prev_head = head
            head = next_head

        return result
        
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        headA = self.revertList(headA)
        headB = self.revertList(headB)
        print(self.showList(headA))
        print(self.showList(headB))
        iA = headA
        iB = headB
        hABi = None
        while iA is not None and iB is not None and iA.val == iB.val:
            hABi = iA
            iA = iA.next
            iB = iB.next
        headA = self.revertList(headA)
        headB = self.revertList(headB)
        print(self.showList(headA))
        print(self.showList(headB))
        return hABi
    
if __name__ == "__main__":
    nums1 = [4,1,8,4,5]
    nums2 = [5,6,1,8,4,5]
    hA = ListNode(nums1[0])
    hB = ListNode(nums2[0])

    headA = hA
    headB = hB

    for v in nums1[1:]:
        n = ListNode(v)
        hA.next = n
        hA = n

    for v in nums2[1:]:
        n = ListNode(v)
        hB.next = n
        hB = n

    s = Solution()
    s.getIntersectionNode(headA, headB)