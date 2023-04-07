from typing import List
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        if not matrix:
            return
        R = len(matrix)
        if R == 0:
            return
        C = len(matrix[0])
        if C == 0:
            return
        rset = []
        cset = set()
        for r in range(R):
            for c in range(C):
                if matrix[r][c] == 0:
                    rset.append(r)
                    cset.add(c)

        
        for r in rset:
            for c in range(C):
                matrix[r][c] = 0
        for c in cset:
            for r in range(R):
                matrix[r][c] = 0