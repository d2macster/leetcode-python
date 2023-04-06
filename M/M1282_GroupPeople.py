from typing import List
from collections import defaultdict
class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        if not groupSizes:
            return []
        result = []
        person_group_size = defaultdict(list)
        for pid, gs in enumerate(groupSizes):
            person_group_size[gs].append(pid)
        for gs, pids in person_group_size.items():
            for i in range(0, len(pids), gs):
                result.append(pids[i:i+gs])

        return result

if __name__ == "__main__":
    s = Solution()
    print(s.groupThePeople([3,3,3,3,3,1,3]))
    print(s.groupThePeople([2,1,3,3,3,2]))