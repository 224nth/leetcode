from typing import List, Set


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:


        res = []
        def _permute(nums, s):
            if len(s) == len(nums):
                res.append(s.copy())
            else:
                for i in nums:
                    if i not in s:
                        s.append(i)
                        _permute(nums, s)
                        s.pop()


        _permute(nums, [])

        return res

assert Solution().permute([1,2,3]) == [
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]


