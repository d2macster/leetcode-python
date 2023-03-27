from typing import List
class Solution:
    def maxArea(self, height: List[int]) -> int:
        L = len(height)
        if L < 2:
            return 0
        l = 0
        r = L-1
        maxA = (r - l) * min(height[l], height[r])

        while l < r:
            lh = height[l]
            rh = height[r]
            if lh <= rh:
                while l < r and height[l] <= lh:
                    l += 1
                A = (r - l) * min(height[l], height[r])
                maxA = max(maxA, A)
                continue
            while l < r and height[r] <= rh:
                r -= 1
            A = (r - l) * min(height[l], height[r])
            maxA = max(maxA, A)

        return maxA
    
if __name__ == "__main__":
    h1 = [1,8,6,2,5,4,8,3,7]
    h2 = [1,1]
    h3 = [2,3,10,5,7,8,9]
    s = Solution()
    print(s.maxArea(h1))

