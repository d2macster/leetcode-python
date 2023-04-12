from typing import List
import bisect

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        Ls = len(searchWord)
        if Ls == 0:
            return []
        result = []
        products = sorted(products)
        for i in range(Ls):
            prefix = searchWord[0:i+1]
            pi = bisect.bisect_left(products, prefix)
            result.append([p for p in products[pi:pi+3] if p.startswith(prefix)])
        return result
    
if __name__ == "__main__":
    s = Solution()
    s.suggestedProducts(["mobile","mouse","moneypot","monitor","mousepad"], "mouse")