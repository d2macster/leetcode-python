from typing import List
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums = sorted(nums) 
        result = nums[0] + nums[1] + nums[2]
        diff = abs(result - target)
        L = len(nums)
        for i1 in range(L-2):
            n1 = nums[i1]
            i2 = i1 + 1
            i3 = L-1
            while i2 < i3:
                r = n1 + nums[i2] + nums[i3]
                D = abs(r - target)
                if D < diff:
                    result = r
                    diff = D
                if r == target:
                    return r
                if r < target:
                    i2 += 1
                if r > target:
                    i3 -= 1
        return result
    
if __name__ == "__main__":
    s = Solution()
    d1 = [-1,2,1,-4]
    d2 = [0,0,0]
    d3 = [1,1,1,0]
    print(s.threeSumClosest(d1, 1))
    print(s.threeSumClosest(d2, 1))
    print(s.threeSumClosest(d3, -100))