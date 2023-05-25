class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        Lh = len(haystack)
        Ln = len(needle)
        if Ln == 0 or Ln > Lh:
            return -1
        for i in range(Lh):
            if Lh - i < Ln:
                break
            notMatched = False
            for j in range(Ln):
                if needle[j] != haystack[i+j]:
                    notMatched = True
                    break
            if notMatched:
                i += 1
                continue
            return i
        return -1