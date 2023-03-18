from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        H = {}
        for nid, n in enumerate(nums):
            if n in H and 2*n == target:
                return [nid, H[n]]
            tn = target - n
            if tn in H:
                return[nid, H]
            H[n] = nid

        return [-1, -1]
