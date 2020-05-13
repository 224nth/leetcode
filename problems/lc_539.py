

from typing import List
import functools
import sys

class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:

        def mysort(a,b):
            a = a.split(":")
            b = b.split(":")

            if a[0] == b[0]:
                return int(a[1]) - int(b[1])
            else:
                return int(a[0]) - int(b[0])

        def getdiff(a, b):

            a = a.split(":")
            b = b.split(":")

            diff = int(a[0]) * 60 + int(a[1]) - int(b[0]) * 60 - int(b[1])
            return diff


        def fortwo(a,b, lowest):
            diff = abs(getdiff(a, b))
            c_min = min(diff, 24 * 60 - diff)
            if c_min < lowest:
                lowest = c_min

            return lowest
        timePoints = sorted(timePoints, key=functools.cmp_to_key(mysort))

        lowest = sys.maxsize
        for i in range(len(timePoints) -1):
            lowest = fortwo(timePoints[i], timePoints[i+1], lowest)

        lowest = fortwo(timePoints[-1], timePoints[0], lowest)


        return lowest





assert Solution().findMinDifference(["23:59","00:00"]) == 1
assert Solution().findMinDifference(["00:00","23:59","00:00"]) == 0
assert Solution().findMinDifference(["05:31","22:08","00:35"]) == 147