from typing import List
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        if not nums:
            return -1
        nums = sorted(set(nums))
        if len(nums) < 3:
            return nums[-1]
        return nums[-3]