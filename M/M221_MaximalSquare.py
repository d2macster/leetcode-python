from typing import List
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        R = len(matrix)
        if R == 0:
            return 0
        C = len(matrix[0])
        if C == 0:
            return 0
        counts = []

        for r in range(R):
            cnt = 0
            cnt_row = []
            for c in range(C):
                if matrix[r][c] == "1":
                    cnt += 1
                else:
                    cnt = 0
                cnt_row.append(cnt)
            counts.append(cnt_row)
        MSS = 0
        for c in range(C):
            cnt = 0
            for r in range(R):
                if matrix[r][c] == "1":
                    cnt += 1
                    MSS = 1
                else:
                    cnt = 0
                counts[r][c] = min(cnt, counts[r][c])

        for r in range(1,R):
            for c in range(1, C):
                counts[r][c] = min(counts[r][c], counts[r-1][c-1] + 1)
                MSS = max(MSS, counts[r][c] * counts[r][c])

        
        return MSS

if __name__ == "__main__":
    matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
    s = Solution()
    print(s.maximalSquare(matrix))
