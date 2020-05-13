from math import sqrt
from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:

        from queue import PriorityQueue

        def findDistance(point):
            return sqrt((point[0]) ** 2+ (point[1]) ** 2)

        q = PriorityQueue(maxsize=K)

        for point in points:
            d = -1*findDistance(point)
            if q.full():
                a = q.queue[0]
                if d < a[0]:
                    continue
                else:
                    q.get()

            q.put((d, point))

        res = []
        while not q.empty():
            res.append(q.get()[1])

        return res

# assert Solution().kClosest(points = [[1,3],[-2,2]], K = 1) == [[-2,2]]
# assert Solution().kClosest( points = [[3,3],[5,-1],[-2,4]], K = 2) == [[3,3],[-2,4]] or Solution().kClosest( points = [[3,3],[5,-1],[-2,4]], K = 2) == [[-2,4], [3,3]]

print( Solution().kClosest([[-95,76],[17,7],[-55,-58],[53,20],[-69,-8],[-57,87],[-2,-42],[-10,-87],[-36,-57],[97,-39],[97,49]], 5))