from typing import List
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations = sorted(citations)
        L = len(citations)
        result = 0
        for i in range(L):
            c = min(citations[i], L - i)
            result = max(result, c)
            if result >= (L-i):
                break
        return result

if __name__ == "__main__":
    s = Solution()
    print(s.hIndex([3,0,6,1,5]))
    print(s.hIndex([1,3,1]))