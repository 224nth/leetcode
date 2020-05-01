from typing import List


class Solution:
    def longestWPI(self, hours: List[int]) -> int:

        prefix = 0
        d = {}
        res = 0
        for i, h in enumerate(hours):
            prefix += 1 if h > 8 else -1

            if prefix > 0:
                res = i + 1
            elif prefix - 1 in d:
                res = max(res, i - d[prefix - 1])

            if not prefix in d:
                d[prefix] = i

        return res





print(Solution().longestWPI([6,5,9,6,9,9,2]))



