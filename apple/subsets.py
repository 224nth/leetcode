
from typing import List
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        pass



assert Solution().subsets([1,2,3]) == [
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
