class Solution:
    def maxDepth(self, s: str) -> int:
        maxD = 0
        d = 0
        L = len(s)
        for i in range(L):
            if s[i] == '(':
                d += 1
                maxD = max(maxD, d)
            if s[i] == ')':
                d -= 1
        return maxD