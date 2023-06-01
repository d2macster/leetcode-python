from collections import defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t:
            return ""
        tc = defaultdict(int)
        for c in t:
            tc[c] += 1
        Ls = len(s)
        Lt = len(t)
        begin, end, counter  = 0, 0, Lt
        minS = ""

        while end < Ls:
            c = s[end]
            end += 1
            if c in tc:
                if tc[c] > 0:
                    counter -= 1
                tc[c] -= 1
            while counter == 0 and begin <= (end - Lt):
                if not minS:
                    minS = s[begin:end]
                if len(s[begin:end]) < len(minS):
                    minS = s[begin:end]
                c = s[begin]
                if c not in tc:
                    begin += 1
                    continue
                if tc[c] >= 0:
                    counter += 1
                tc[c] += 1
                begin += 1

        return minS


if __name__ == "__main__":
    s = Solution()
    print(s.minWindow("ADOBECODEBANC", "ABC"))
    print(s.minWindow("bba", "ab"))
    print(s.minWindow("a", "a"))
    print(s.minWindow("a", "aa"))