class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        Ls = len(s)
        Lt = len(t)
        if Ls == 0:
            return True
        if Ls > Lt:
            return False
        if Lt == Ls:
            return s == t
        si = 0
        ti = 0
        while ti < Lt and si < Ls:
            if s[si] != t[ti]:
                ti += 1
                continue
            if si == Ls - 1:
                return True
            si += 1
            ti += 1
        return False
    
if __name__ == "__main__":
    s = Solution()
    print(s.isSubsequence("abc", "ahbgdc"))
    print(s.isSubsequence("ace", "abcde"))
    print(s.isSubsequence("aec", "abcde"))
    print(s.isSubsequence("axc", "ahbgdc"))
