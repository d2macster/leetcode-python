from typing import List

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        Ls = len(searchWord)
        if Ls == 0:
            return []
        result = []
        for i in range(Ls):
            prefix = searchWord[0:i+1]
            cache = []
            for p in products:
                if not p.startswith(prefix):
                    continue
                cache.append(p)
            result.append(sorted(cache)[0:3])
        return result