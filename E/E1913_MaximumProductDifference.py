from typing import List
class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        max1 = nums[0]
        max2 = nums[1]
        if max2 > max1:
            max1, max2 = max2, max1
        
        for n in nums[2:]:
            if n <= max2:
                continue
            max2 = max1
            max1 = n
            if max2 > max1:
                max1, max2 = max2, max1

        min1 = nums[0]
        min2 = nums[1]
        if min2 < min1:
            min1, min2 = min2, min1

        for n in nums[2:]:
            if n >= min2:
                continue
            min2 = min1
            min1 = n
            if min2 < min1:
                min1, min2 = min2, min1

        return max1 * max2 - min1 * min2