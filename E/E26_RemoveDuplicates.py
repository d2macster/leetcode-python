from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        L = len(nums)
        O = -1000
        prev = O
        for i in range(L):
            if nums[i] > prev:
                prev = nums[i]
                continue
            nums[i] = O
        next_id = 1
        for i in range(1,L):
            if nums[i] == O:
                continue
            n = nums[i]
            nums[next_id] = n
            next_id += 1


        return next_id
    
if __name__ == "__main__":
    nums = [0,0,1,1,1,2,2,3,3,4]
    s = Solution()
    s.removeDuplicates(nums)
    print(nums)