from typing import Optional, List
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:        
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        ha = headA
        hb = headB
        La = 1
        Lb = 1
        while ha.next is not None:
            La += 1
            ha = ha.next
        while hb.next is not None:
            Lb += 1
            hb = hb.next
        # no common path
        if ha != hb:
            return None
        
        ha = headA
        hb = headB
        for _ in range(La - Lb):
            ha = ha.next
        for _ in range(Lb - La):
            hb = hb.next
        while ha is not None:
            if ha == hb:
                return ha
            ha = ha.next
            hb = hb.next

        return headA

    
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