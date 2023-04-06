from typing import List
dl = {"2": ["a", "b", "c"], 
              "3": ["d", "e", "f"], 
              "4": ["g", "h", "i"], 
              "5": ["j", "k", "l"], 
              "6": ["m", "n", "o"], 
              "7": ["p", "q", "r", "s"], 
              "8": ["t", "u", "v"], 
              "9": ["w", "x", "y", "z"]}
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        L = len(digits)
        if L == 0:
            return []
        if L == 1:
            return dl[digits[0]]
        result = []
        nc = self.letterCombinations(digits[1:])
        for l in dl[digits[0]]:
            for c in nc:
                ac = l+c
                result.append(ac)
        return result

if __name__ == "__main__":
    s = Solution()
    print(s.letterCombinations(""))
    print(s.letterCombinations("2"))
    print(s.letterCombinations("23"))

