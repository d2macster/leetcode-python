from typing import List
from collections import defaultdict
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        if not nums1 or not nums2:
            return result
        counter = defaultdict(int)
        for n in nums1:
            counter[n] += 1
        for n in nums2:
            if n not in counter:
                continue
            result.append(n)
            counter[n] -= 1
            if counter[n] <= 0:
                counter.pop(n)
        return result