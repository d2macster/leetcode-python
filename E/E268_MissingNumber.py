from typing import List
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums = sorted(nums)
        if nums[0] != 0:
            return 0
        prev_n = 0
        for n in nums:
            if n > prev_n + 1:
                return prev_n + 1
            prev_n = n
        return len(nums)