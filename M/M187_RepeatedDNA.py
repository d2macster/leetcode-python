from typing import List
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        L = len(s)
        if L < 10:
            return []
        result = set()
        seen = set()
        for i in range(0, L - 9):
            SS = s[i:i+10]
            if SS in seen:
                result.add(SS)
                continue
            seen.add(SS)
        return list(result)
