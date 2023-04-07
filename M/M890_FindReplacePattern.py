from typing import List
class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        if not words or not pattern:
            return []
        
        result = []
        LP = len(pattern)
        for word in words:
            if len(word) != LP:
                continue
            forward = {}
            backward = {}
            i = 0
            while i < LP:
                w = word[i]
                p = pattern[i]
                if w in forward:
                    if forward[w] != p:
                        break
                if p in backward:
                    if backward[p] != w:
                        break
                forward[w] = p
                backward[p] = w
                i += 1
            if i == LP:
                result.append(word)

        return result
    
if __name__ == "__main__":
    s = Solution()
    print(s.findAndReplacePattern(["abc","deq","mee","aqq","dkd","ccc"], "abb"))
    print(s.findAndReplacePattern(["a","b","c"], "a"))