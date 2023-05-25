from typing import List
class Solution:
    def trap(self, height: List[int]) -> int:
        L = len(height)
        if L <= 2:
            return 0
        left = [0] * L
        right = [0] * L
        mL = 0
        mR = 0
        for i in range(L):
            mL = max(mL,  height[i])
            left[i] = mL
        for j in range(L-1, -1, -1):
            mR = max(mR, height[j])
            right[j] = mR
        V = 0
        for i in range(L):
            V += max(0, min(left[i], right[i]) - height[i])
        return V
    
if __name__ == "__main__":
    s = Solution()
    print(s.trap([0,1,0,2,1,0,1,3,2,1,2,1]))
    print(s.trap([4,2,0,3,2,5]))