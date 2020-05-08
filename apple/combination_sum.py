

from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        arr = []

        def cSum(candidates,  target, current):
            if sum(current) == target:
                res = current.copy()
                res.sort()
                if res not in arr:
                    arr.append(res)
                return
            elif sum(current) > target:
                return
            else:
                for i in candidates:
                    current.append(i)
                    cSum(candidates, target, current)
                    current.pop()

        cSum(candidates, target, [])
        return arr


def checkEqual(L1, L2):


    assert len(L1) == len(L2)
    for i in range(len(L1)):
        assert L1[i] == L2[i]

    return True





assert checkEqual( Solution().combinationSum(
candidates = [2,3,5], target = 8),[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]
)