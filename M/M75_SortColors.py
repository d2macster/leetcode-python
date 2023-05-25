from typing import List
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        L = len(nums)
        if L < 2:
            return
        i0 = 0
        i2 = L-1
        i = 0
        while i <= i2:
            while i0 <= i2 and nums[i0] == 0:
                i0 += 1
                i = i0
            while i2 >= i0 and nums[i2] == 2:
                i2 -= 1
            if i > i2:
                break
            if nums[i] == 1:
                i+= 1
                continue
            if nums[i] == 2:
                nums[i] = nums[i2]
                nums[i2] = 2
                i2 -= 1
                continue
            if nums[i] == 0:
                nums[i] = nums[i0]
                nums[i0] = 0
                i0 += 1


if __name__ == "__main__":
    s = Solution()
    nums = [2,0,2,1,1,0]
    s.sortColors(nums)
    print(nums)
    nums = [2,0,1]
    s.sortColors(nums)
    print(nums)

    nums = [0,0]
    s.sortColors(nums)
    print(nums)