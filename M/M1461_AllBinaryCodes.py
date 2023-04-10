class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        if k < 1:
            return False
        L = len(s)
        if L < k:
            return False
        ACC = pow(2, k)
        if L - k + 1 < ACC:
            return False
        CC = set()
        for i in range(0, L - k + 1):
            CC.add(s[i:i+k])
        return len(CC) == ACC

if __name__ == "__main__":
    s = Solution()
    print(s.hasAllCodes("00110110", 2))
    print(s.hasAllCodes("0110", 2))
    print(s.hasAllCodes("0110", 1))
    print(s.hasAllCodes("00110", 2))