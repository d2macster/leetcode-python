from typing import List
from collections import defaultdict
import heapq
class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        q = []
        lq = 0
        positions = defaultdict(list)
        for nid, n in enumerate(nums):
            positions[n].append(nid)
            heapq.heappush(q, n)
            lq += 1
            if lq > k:
                np = heapq.heappop(q)
                lq -= 1
                positions[np].pop(0)

        survivors = []
        for n in q:
            nid = positions[n].pop(0)
            survivors.append((n, nid))
        survivors = sorted(survivors, key=lambda t: t[1])
        return [s[0] for s in survivors]
    
if __name__ == "__main__":
    s = Solution()
    print(s.maxSubsequence([2,1,3,3], 2))
    print(s.maxSubsequence([-1,-2,3,4], 3))