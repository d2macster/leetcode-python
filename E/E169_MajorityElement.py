from typing import List
from collections import defaultdict
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if not nums:
            return 0
        counter = defaultdict(int)
        for n in nums:
            counter[n] += 1
        best_count = 0
        best_e = 0
        for e, c in counter.items():
            if c > best_count:
                best_count = c
                best_e = e
        return best_e