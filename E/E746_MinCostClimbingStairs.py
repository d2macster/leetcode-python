from typing import List
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        L = len(cost)
        if L == 0:
            return 0
        if L == 1:
            return cost[0]
        cache = [0 for _ in range(L)]
        cache[0] = cost[0]
        cache[1] = min(0, cost[0]) + cost[1] 
        for i in range(2, L):
            cache[i] = min(cache[i-1], cache[i-2]) + cost[i]
        return min(cache[-1], cache[-2])
