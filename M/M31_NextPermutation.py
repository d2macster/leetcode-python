from typing import List
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        L = len(nums)
        if L < 2:
            return
        i = L-1
        cache = {}
        cache[nums[i]] = i
        sorted_cache_keys = [nums[i]]
        i-= 1
        swapped = False
        while i >= 0:
            v = nums[i]

            for k in sorted_cache_keys:
                if k <= v:
                    continue
                vpi = cache[k]
                nums[i] = k
                nums[vpi] = v
                swapped = True
                break

            if swapped:
                break

            if v not in cache:
                cache[v] = i
                sorted_cache_keys.append(v)
                sorted_cache_keys = sorted(sorted_cache_keys)
            i-= 1

        if swapped:
            tail = sorted(nums[i+1:])
            nums[i+1:] = tail
            return
        
        n = sorted(nums)
        nums[:] = n[:]

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