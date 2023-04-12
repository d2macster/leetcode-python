class Solution:
    def helper(self, s: str, t: str, si: int, ti: int, Ls: int, Lt: int) -> int:
        diff = 0
        counter = 0
        while si < Ls and ti < Lt:
            if s[si] != t[ti]:
                diff += 1
            if diff > 1:
                break
            if diff == 1:
                counter += 1
            si += 1
            ti += 1
        return counter
    
    def countSubstrings(self, s: str, t: str) -> int:
        Ls = len(s)
        Lt = len(t)
        if Ls == 0:
            return 0
        if Lt == 0:
            return 0
        counter = 0
        for si in range(Ls):
            for ti in range(Lt):
                counter += self.helper(s, t, si, ti, Ls, Lt)
        return counter
if __name__ == "__main__":
    s = Solution()
    print(s.countSubstrings("aba", "baba"))
    print(s.countSubstrings("ab", "bb"))