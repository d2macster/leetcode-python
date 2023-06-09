from typing import List
import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        q = nums[0:k]
        heapq.heapify(q)
        ql = k
        evicted = min(q)
        for n in nums[k:]:
            if n < evicted:
                continue
            heapq.heappush(q, n)
            ql += 1
            if ql > k:
                evicted = heapq.heappop(q)
                ql -= 1
        return min(q)
    
if __name__ == "__main__":
    s = Solution()
    print(s.findKthLargest([3,2,1,5,6,4], 2))
    print(s.findKthLargest([3,2,3,1,2,4,5,5,6], 4))