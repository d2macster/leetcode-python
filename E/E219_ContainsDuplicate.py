from typing import List

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if len(nums) < 2:
            return False
        HASH = {}
        for nid, n in enumerate(nums):
            prev_id = HASH.get(n)
            if prev_id is not None:
                if nid - prev_id <= k:
                    return True
            HASH[n] = nid
        return False