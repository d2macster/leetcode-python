from typing import List
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n < 1:
            return []
        result = ["()"]
        if n == 1:
            return result
        for _ in range(1, n):
            next_result = set()
            for prev_el in result:
                next_result.add(f"(){prev_el}")
                next_result.add(f"({prev_el})")
                next_result.add(f"{prev_el}()")
                Lpe = len(prev_el)
                c = 0
                for pei in range(Lpe):
                    if prev_el[pei] == '(':
                        c += 1
                    else:
                        c -= 1
                    if c > 0:
                        next_result.add(f"{prev_el[0:pei+1]})({prev_el[pei+1:]}")
            result = list(next_result)
        return result
    
if __name__ == "__main__":
    s = Solution()
    for i in range(1,5):
        print(s.generateParenthesis(i))