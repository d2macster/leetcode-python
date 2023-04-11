from typing import List
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows < 1:
            return []
        prev_elements = [1]
        result = [prev_elements]
        for row in range(2, numRows+1):
            elements = [1 for _ in range(row)]
            for c in range(1, row-1):
                elements[c] = prev_elements[c-1] + prev_elements[c]
            result.append(elements)
            prev_elements = elements
        return result
