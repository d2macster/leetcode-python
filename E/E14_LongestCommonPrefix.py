from typing import List
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        L = len(strs)
        if L == 0:
            return ""
        prefix = strs[0]
        if L == 1:
            return prefix
        pl = len(prefix)
        for si in range(1, L):
            pl = min(pl, len(strs[si]))
        if pl == 0:
            return ""

        for si in range(1, L):
            if pl == 0:
                return ""
            new_pl = 0
            for pli in range(pl):
                if prefix[pli] != strs[si][pli]:
                    break
                new_pl = pli + 1
            pl = new_pl

        if pl == 0:
            return ""
        return prefix[0:pl]
    
if __name__ == "__main__":
    strs = ["flower","flow","flight"]
    s = Solution()
    print(s.longestCommonPrefix(strs))
