from typing import List
import heapq
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if k == 1:
            return nums
        L = len(nums)
        result = []
        q = []
        for i in range(0, k):
            heapq.heappush(q, (-nums[i], i))
        result.append(-q[0][0])
        for i in range(k, L):
            heapq.heappush(q, (-nums[i], i))
            while q[0][1] <= i - k:
                heapq.heappop(q)
            result.append(-q[0][0])

            
        return result
    
if __name__ == "__main__":
    s = Solution()
    print(s.maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3))
    print(s.maxSlidingWindow([1,3,1,2,0,5], 3))

