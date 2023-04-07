from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for r in range(9):
            s = set()
            for c in range(9):
                v = board[r][c]
                if v == ".":
                    continue
                if v in s:
                    return False
                s.add(v)

        for c in range(9):
            s = set()
            for r in range(9):
                v = board[r][c]
                if v == ".":
                    continue
                if v in s:
                    return False
                s.add(v)

        for r0 in range(0, 9, 3):
            for c0 in range(0, 9, 3):
                s = set()

                for r in range(r0, r0+3):
                    for c in range(c0, c0+3):
                        v = board[r][c]
                        if v == ".":
                            continue
                        if v in s:
                            return False
                        s.add(v)

        return True
    
if __name__ == "__main__":
    board1 = [["5","3",".",".","7",".",".",".","."]
        ,["6",".",".","1","9","5",".",".","."]
        ,[".","9","8",".",".",".",".","6","."]
        ,["8",".",".",".","6",".",".",".","3"]
        ,["4",".",".","8",".","3",".",".","1"]
        ,["7",".",".",".","2",".",".",".","6"]
        ,[".","6",".",".",".",".","2","8","."]
        ,[".",".",".","4","1","9",".",".","5"]
        ,[".",".",".",".","8",".",".","7","9"]]
    
    board2 = [["8","3",".",".","7",".",".",".","."]
        ,["6",".",".","1","9","5",".",".","."]
        ,[".","9","8",".",".",".",".","6","."]
        ,["8",".",".",".","6",".",".",".","3"]
        ,["4",".",".","8",".","3",".",".","1"]
        ,["7",".",".",".","2",".",".",".","6"]
        ,[".","6",".",".",".",".","2","8","."]
        ,[".",".",".","4","1","9",".",".","5"]
        ,[".",".",".",".","8",".",".","7","9"]]
    s = Solution()
    print(s.isValidSudoku(board1))
    print(s.isValidSudoku(board2))
