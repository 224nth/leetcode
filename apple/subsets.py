
from typing import List
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        lst = [[]]


        for i in nums:

            for j in range(len(lst)):

                each = lst[j].copy()
                each.append(i)
                lst.append(each)

        return lst

def checkEqual(L1, L2):
    return len(L1) == len(L2) and sorted(L1) == sorted(L2)





assert checkEqual(Solution().subsets([1,2,3]), [
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
])
