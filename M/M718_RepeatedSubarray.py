from typing import List
class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        L1 = len(nums1)
        L2 = len(nums2)
        if L1 == 0 or L2 == 0:
            return 0
        cache = [0 for _ in range(L2)]
        M = 0
        for i1 in range(L1):
            new_cache = [0 for _ in range(L2)]
            for i2 in range(L2):
                if nums1[i1] != nums2[i2]:
                    continue
                prev = cache[i2-1] if i2 > 0 else 0
                new_cache[i2] = prev + 1
            cache = new_cache
            M = max(M, max(cache))

        return M
    
if __name__ == "__main__":
    s = Solution()
    print(s.findLength([1,2,3,2,1], [3,2,1,4,7]))
    print(s.findLength([0,0,0,0,0], [0,0,0,0,0]))
    print(s.findLength([0,1,1,1,1], [1,0,1,0,1]))
    print(s.findLength([0,0,0,0,1], [1,0,0,0,0]))