from typing import List
from collections import defaultdict
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        L = len(nums)
        if L <= 1:
            return nums
        counter = defaultdict(int)
        for n in nums:
            counter[n] += 1
        i = 0
        for k in sorted(counter.keys()):
            for _ in range(counter[k]):
                nums[i] = k
                i += 1
        return nums
