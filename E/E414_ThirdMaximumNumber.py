from typing import List
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        if not nums:
            return -1
        s = set()
        s.add(nums[0])
        min_s = nums[0]
        Ls = 1
        for n in nums[1:]:
            if Ls == 3 and n <= min_s:
                continue
            if n in s:
                continue
            s.add(n)
            Ls = len(s)
            if Ls <= 3:
                continue
            ss = sorted(s)
            s.discard(ss[0])
            Ls = 3
            min_s = ss[1]
        ss = sorted(s)
        if len(ss) < 3:
            return ss[-1]
        else:
            return ss[-3]
        
if __name__ == "__main__":
    nums1 = [3,2,1]
    nums2 = [2,2,3,1]
    nums3 = [3,4,5,1,2,4,4,4,8,6,1,2,3,4]
    s = Solution()
    print(s.thirdMax(nums3))