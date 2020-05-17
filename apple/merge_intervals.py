import functools
from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        if not intervals:
            return intervals

        intervals.sort(key = lambda x:x[0])

        res = []
        res.append(intervals[0])
        for i in range(1,len(intervals)):
            if intervals[i][0] >  res[-1][1]:
                res.append(intervals[i])
            else:
                res[-1][1] = max(intervals[i][1], res[-1][1])

        return res


assert Solution().merge([[1,4],[0,4]]) == [[0,4]]
# assert Solution().merge([[1,3],[2,6],[8,10],[15,18]]) == [[1,6],[8,10],[15,18]]
# assert Solution().merge([[1,4],[4,5]]) == [[1,5]]