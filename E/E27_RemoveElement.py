from typing import List
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        L = len(nums)
        newL = 0
        j = 0
        for i in range(L):
            if nums[i] == val:
                continue
            if i != j:
                nums[j] = nums[i]
            j += 1
            i += 1
            newL += 1
        return newL