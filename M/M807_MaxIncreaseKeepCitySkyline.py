from typing import List
class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        L = len(grid)
        if L == 1:
            return 0
        maxRow = [0] * L
        maxCol = [0] * L
        for r in range(L):
            for c in range(L):
                maxRow[r] = max(maxRow[r], grid[r][c])
                maxCol[c] = max(maxCol[c], grid[r][c])

        result = 0
        for r in range(L):
            for c in range(L):
                U = min(maxRow[r], maxCol[c])
                result += (U - grid[r][c])

        return result
    
if __name__ == "__main__":
    grid = [[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]]
    s = Solution()
    print(s.maxIncreaseKeepingSkyline(grid))