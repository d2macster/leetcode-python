from typing import List
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        counter = [0, 0, 0]
        for n in nums:
            counter[n] += 1
        i = 0
        for k in [0, 1, 2]:
            for j in range(counter[k]):
                nums[i + j] = k
            i += counter[k]
