from collections import defaultdict
class Solution:
    def equalFrequency(self, word: str) -> bool:
        L = len(word)
        if L == 0:
            return False
        if L == 1:
            return True
        counter = [0 for _ in range(32)]
        OA = ord('a')
        for c in word:
            counter[ord(c) - OA] += 1

        oc = defaultdict(int)
        for c in counter:
            if c == 0:
                continue
            oc[c] += 1
        ockeys = sorted(oc.keys())
        LOC = len(ockeys)
        if LOC > 2:
            return False
        if LOC == 1:
            if ockeys[0] == 1:
                return True
            return oc[ockeys[0]] == 1

        if ockeys[0] == 1 and oc[ockeys[0]] == 1:
            return True
        if ockeys[1] == (ockeys[0] + 1) and oc[ockeys[1]] == 1:
            return True

        return False

if __name__ == "__main__":
    s = Solution()
    print(s.equalFrequency("abcc"))
    print(s.equalFrequency("abbcc"))
    print(s.equalFrequency("bac"))