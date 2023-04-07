class Solution:
    def partitionString(self, s: str) -> int:
        if not s:
            return 1
        seen = set()
        counter = 0
        for c in s:
            if c in seen:
                counter += 1
                seen.clear()
            seen.add(c)
        counter += 1
        return counter
    
if __name__ == "__main__":
    s = Solution()
    print(s.partitionString("abacaba"))
    print(s.partitionString("ssssss"))
    print(s.partitionString("hdklqkcssgxlvehva"))