from typing import List
class Solution:        
    def sortArray(self, nums: List[int]) -> List[int]:
        L = len(nums)
        if L <= 1:
            return nums
        if L == 2:
            if nums[0] > nums[1]:
                nums[0], nums[1] = nums[1], nums[0]
            return nums
        result = [0 for _ in range(L)]
        l2 = int(L/2)
        n1 = self.sortArray(nums[0:l2])
        n2 = self.sortArray(nums[l2:])
        i = 0
        i1 = 0
        i2 = 0
        l1 = len(n1)
        l2 = len(n2)
        while i1 < l1 or i2 < l2:
            if i1 == l1:
                result[i] = n2[i2]
                i2 += 1
                i += 1
                continue
            if i2 == l2:
                result[i] = n1[i1]
                i1 += 1
                i += 1
                continue
            if n1[i1] <= n2[i2]:
                result[i] = n1[i1]
                i += 1
                i1 += 1
                continue
            else:
                result[i] = n2[i2]
                i += 1
                i2 += 1

        return result
