from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        L = len(nums)
        if L <= 1:
            return L
        s = set(nums)
        result = 0
        for n in nums:
            if n not in s:
                continue
            l = 1
            s.remove(n)
            np = n+1
            nm = n-1
            while np in s:
                l+= 1
                s.remove(np)
                np += 1
            while nm in s:
                l += 1
                s.remove(nm)
                nm -= 1
            result = max(result, l)
        return result
    
if __name__ == "__main__":
    nums1 = [100,4,200,1,3,2]
    nums2 = [0,3,7,2,5,8,4,6,0,1]
    s = Solution()
    print(s.longestConsecutive(nums1))
    print(s.longestConsecutive(nums2))