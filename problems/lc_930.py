from typing import List


class Solution:
    def numSubarraysWithSum(self, A: List[int], S: int) -> int:

        if not A:
            return 0

        pre = []
        post = []

        csum = 0
        for i in range(len(A) -1):
            csum += A[i]
            pre[i] = csum


        csum = 0
        for i in range(len(A)-1, -1, -1):
            post[i] = csum
            csum += A[i]

        for i in range(len(A)//2):
            if pre[i]+[]











print(Solution().numSubarraysWithSum([1,0,1,0,1],2))