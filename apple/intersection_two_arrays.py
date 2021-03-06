from collections import defaultdict
from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        s = set()

        for i in nums1:
            s.add(i)

        res = set()

        for j in nums2:
            if j in s:
                res.add(j)

        return list(res)




nums1 = [1,2,2,1]
nums2 = [2,2]
print(Solution().intersection(nums1, nums2))

nums1 = [4, 9, 5]
nums2 = [9, 4, 9, 8, 4]
print(Solution().intersection(nums1, nums2))