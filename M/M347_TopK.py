from typing import List
from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if k <= 0:
            return 0
        counter = defaultdict(int)
        for n in nums:
            counter[n] += 1
        summary = [(k, v) for k, v in counter.items()]
        summary = sorted(summary, key=lambda t: t[1], reverse=True)
        return [t[0] for t in summary[0:k]]
    
if __name__ == "__main__":
    s = Solution()
    print(s.topKFrequent([1,1,1,2,2,3], 2))
    print(s.topKFrequent([1], 1))