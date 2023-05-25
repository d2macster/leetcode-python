from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        L = len(nums)
        if L <= 1:
            return L
        ip = 1
        prev_v = nums[0]
        count = 1
        for i in range(1,L):
            v = nums[i]
            if v == prev_v:
                count += 1
            if v > prev_v:
                prev_v = v
                count = 1
            if count <= 2:
                nums[ip] = v
                ip += 1
        return ip
    
if __name__ == "__main__":
    s = Solution()
    nums = [1,1,1,2,2,3]
    l = s.removeDuplicates(nums)
    print(f"{l} {nums}")

    nums = [0,0,1,1,1,1,2,3,3]
    l = s.removeDuplicates(nums)
    print(f"{l} {nums}")