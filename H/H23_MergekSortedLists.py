from typing import List, Optional
import heapq
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        L = len(lists)
        if L == 0:
            return None
        if L == 1:
            return lists[0]
        q = []
        for i in range(L):
            if not lists[i]:
                continue
            heapq.heappush(q, (lists[i].val, i))

        result : Optional[ListNode] = None
        re : Optional[ListNode] = None
        
        while q:
            t = heapq.heappop(q)
            i = t[1]
            min_n = lists[i]
            if result is None:
                result = min_n
                re = min_n
            else:
                re.next = min_n
                re = min_n
            lists[i] = lists[i].next
            min_n.next = None
            if lists[i]:
                heapq.heappush(q, (lists[i].val, i))

        return result
        