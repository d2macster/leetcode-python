from typing import List
from collections import defaultdict
from sortedcontainers import SortedSet
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if k == 1:
            return nums
        L = len(nums)
        result = []
        
        if k == 2:
            for i in range(1, L):
                result.append(max(nums[i-1], nums[i]))
            return result
        
        counter = defaultdict(int)
        s = SortedSet()
        M = nums[0]
        for i in range(0, k):
            n = nums[i]
            M = max(M, n)
            counter[n] += 1
            s.add(n)
        result.append(M)

        for i in range(k, L):
            n = nums[i]
            s.add(n)
            M = max(M, n)
            ne = nums[i-k]
            counter[n] += 1
            counter[ne] -= 1
            if counter[ne] <= 0:
                counter.pop(ne)
                s.discard(ne)
                if ne == M:
                    M = s.__getitem__(-1)
            result.append(M)
        return result
    
if __name__ == "__main__":
    s = Solution()
    print(s.maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3))
    print(s.maxSlidingWindow([1,3,1,2,0,5], 3))

