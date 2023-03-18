from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        result = []
        H = {}
        for nid, n in enumerate(nums):
            H[n] = nid
        L = len(nums)
        prev_n = nums[0]
        for ni in range(L):
            n = nums[ni]
            if ni > 0 and prev_n == n:
                continue
            prev_n = n
            for n1i in range(ni+1, L):
                n1 = nums[n1i]
                n2 = -(n + n1)
                if n2 < n1:
                    continue
                if n2 not in H:
                    continue
                n2i = H[n2]
                if n2i <= n1i:
                    continue
                r = [n, n1, n2]
                if result:
                    pr = result[-1]
                    inc_check = 0
                    for i in range(3):
                        if inc_check == 0 and r[i] > pr[i]:
                            inc_check = 1
                            break
                        if inc_check == 0 and r[i] < pr[i]:
                            inc_check = -1
                            break

                    if inc_check < 1:
                        continue
                result.append(r)

        return result
    
if __name__ == "__main__":
    d1 = [-1,0,1,2,-1,-4]
    d2 = [-4,-2,-2,-2,0,1,2,2,2,3,3,4,4,6,6]
    s = Solution()
    print(s.threeSum(d1))
    print(s.threeSum(d2))