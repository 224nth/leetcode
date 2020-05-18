from typing import List

class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        alen = len(A)
        res = [0] * alen
        st = 0
        end = alen - 1
        pt = alen - 1
        while st <= end:
            if abs(A[end]) > abs(A[st]):
                res[pt] = A[end] ** 2
                end -= 1
            else:
                res[pt] = A[st] ** 2
                st += 1
            pt -= 1
        return res

assert Solution().sortedSquares([-4,-1,0,3,10]) == [0,1,9,16,100]
assert Solution().sortedSquares([-7,-3,2,3,11]) == [4,9,9,49,121]