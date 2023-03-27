from typing import List, Optional
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        L = len(nums)
        if L == 0:
            return 0
        majority_count = 1
        majority_e = nums[0]
        for n in nums[1:]:
            if n == majority_e:
                majority_count += 1
            else:
                majority_count -= 1
            if majority_count > int(L/2):
                return majority_e
            
            if majority_count == 0:
                majority_count = 1
                majority_e = n
        return majority_e