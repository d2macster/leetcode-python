from typing import List
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        L = len(nums)
        if L < 2:
            return 0
        i = 0
        j = L-1
        result = (nums[i] - 1) * (nums[j] - 1)
        if nums[i] <= nums[j]:
            i += 1
        else:
            j -= 1
        while i < j:
            r = (nums[i] - 1) * (nums[j] - 1)
            result = max(r, result)
            if nums[i] <= nums[j]:
                i += 1
            else:
                j -= 1
        return result
