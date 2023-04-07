from typing import List
from collections import defaultdict
import heapq
class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        q = []
        lq = 0
        for nid, n in enumerate(nums):
            heapq.heappush(q, (n, nid))
            lq += 1
            if lq > k:
                heapq.heappop(q)
                lq -= 1

        q = sorted(q, key=lambda t: t[1])
        return [e[0] for e in q]
    
if __name__ == "__main__":
    s = Solution()
    print(s.maxSubsequence([2,1,3,3], 2))
    print(s.maxSubsequence([-1,-2,3,4], 3))
    print(s.maxSubsequence([3,4,3,3], 2))