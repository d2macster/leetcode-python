from typing import List
from collections import defaultdict
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        L = len(s)
        if L < 10:
            return []
        result = []
        cache = defaultdict(int)
        for i in range(0, L - 9):
            SS = s[i:i+10]
            cache[SS] += 1
        for k, v in cache.items():
            if v < 2:
                continue
            result.append(k)
        return result
