from typing import List
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        R = len(grid)
        C = len(grid[0])
        if C == 0:
            return 0
        path_sum = [100000 for _ in range(C)]
        path_sum[0] = 0
        new_path_sum = [0 for _ in range(C)]
        for r in range(R):
            new_path_sum[0] = path_sum[0] + grid[r][0]
            for c in range(1, C):
                new_path_sum[c] = min(path_sum[c], new_path_sum[c-1]) + grid[r][c]
            path_sum = new_path_sum[:]

        return path_sum[-1]
