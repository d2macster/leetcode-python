from typing import List
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0
        nums = sorted(nums)
        return (nums[-1] - 1) * (nums[-2] - 1)