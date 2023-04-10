from typing import List
from collections import defaultdict
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        if not citations:
            return 0

        counter = defaultdict(int)
        for c in citations:
            counter[c] += 1
        cv = sorted(counter.keys(), reverse=True)
        result = 0
        L = len(cv)

        alreadyCounted = 0
        for c in cv:
            alreadyCounted += counter[c]
            result = max(result, min(c, alreadyCounted))
        return result

if __name__ == "__main__":
    s = Solution()
    print(s.hIndex([3,0,6,1,5]))
    print(s.hIndex([1,3,1]))