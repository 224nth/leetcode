
from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return 0

        def binarySearch(list, target, start, end):

            if end == start and list[end] != target:
                return False

            mid = start+ (end - start)//2
            if list[mid] ==target:
                return True

            if target < list[mid]:
                return binarySearch(list, target, start, mid)
            else:
                return binarySearch(list, target, mid+1, end)
        main = []
        for i in matrix:
            if not i:
                return 0
            main = main + i

        return binarySearch(main, target,0 ,len(main))


assert Solution().searchMatrix([[]], 1) == False
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 3
assert Solution().searchMatrix(matrix, target) == True


matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 13
assert Solution().searchMatrix(matrix, target) ==False