from typing import List
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        L = len(nums)
        if L == 0:
            return []
        result = [[nums[0]]]
        if L == 1:
            return result
        for l in range(1, L):
            new_result = []
            v = nums[l]
            for new_pos in range(l+1):
                for pr in result:
                    prc = pr.copy()
                    prc.insert(new_pos, v)
                    new_result.append(prc)
            result = new_result
        return result
    
if __name__ == "__main__":
    n1 = []
    n2 = [1]
    n3 = [1,2]
    n4 = [1,2,3]
    s = Solution()
    print(s.permute(n4))
