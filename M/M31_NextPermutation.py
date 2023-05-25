from typing import List
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        L = len(nums)
        if L < 2:
            return
        curMax = nums[L-1]
        curMaxId = L-1
        swapped = False
        i = L - 2
        while i >= 0:
            v = nums[i]

            if v >= curMax:
                curMax = v
                curMaxId = i
                i -= 1
                continue
            swapped = True
            break

        if not swapped:
            n = sorted(nums)
            nums[:] = n[:]
            return

        v = nums[i]
        tail = nums[i:]
        for j in range(i+1,L):
            if nums[j] < curMax and nums[j] > v:
                curMax = nums[j]
                curMaxId = j
        nums[i] = curMax
        nums[curMaxId] = v

        tail = sorted(nums[i+1:])
        nums[i+1:] = tail

if __name__ == "__main__":
    s = Solution()
    # n = [1,2,3]
    # s.nextPermutation(n)
    # print(n)
    # n = [3,2,1]
    # s.nextPermutation(n)
    # print(n)

    # n = [1,2]
    # s.nextPermutation(n)

    n = [16,27,25,23,25,16,12,9,1,2,7,20,19,23,16,0,6,22,16,11,8,27,9,2,20,2,13,7,25,29,12,12,18,29,27,13,16,1,22,9,3,21,29,14,7,8,14,5,0,23,16,1,20]
    print(n)
    s.nextPermutation(n)
    print(n)