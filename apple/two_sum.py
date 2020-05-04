from collections import defaultdict
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        if not nums:
            return []

        map = defaultdict(set)

        for i, num in enumerate(nums):
            if (target - num) in map:
                return [map[target-num].pop(), i]

            map[num].add(i)





print(Solution().twoSum([3,3], 6))
