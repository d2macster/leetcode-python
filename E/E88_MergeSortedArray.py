from typing import List
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        r = [0] * (m + n)
        i1 = 0
        i2 = 0
        ir = 0
        while i1 < m or i2 < n:
            if i1 >= m:
                r[ir] = nums2[i2]
                i2+=1
                ir += 1
                continue
            if i2 >= n:
                r[ir] = nums1[i1]
                i1 += 1
                ir += 1
                continue
            if nums1[i1] <= nums2[i2]:
                r[ir] = nums1[i1]
                i1 += 1
                ir += 1
            else:
                r[ir] = nums2[i2]
                i2+=1
                ir += 1
        nums1[:] = r



if __name__ == "__main__":
    s = Solution()
    nums1 = [1,2,3,0,0,0]
    s.merge(nums1, 3, [2,5,6], 3)
    print(nums1)