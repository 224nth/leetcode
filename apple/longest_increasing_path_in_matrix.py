
from typing import List

class Solution:
    max_so_far = 0
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:

        store = [[1 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]

        def markAll(i, j):

            if store[i][j] > 1:
                return store[i][j]

            if i + 1 < len(matrix) and  matrix[i + 1][j] > matrix[i][j]:
                store[i][j] = max(store[i][j],1+ markAll(i + 1, j))
            if i - 1 >= 0 and  matrix[i - 1][j] > matrix[i][j]:
                store[i][j] = max(store[i][j], 1+markAll(i - 1, j))
            if j + 1 < len(matrix[0]) and matrix[i][j + 1] > matrix[i][j]:
                store[i][j] =max(store[i][j],1+markAll(i, j + 1))
            if j - 1 >= 0  and matrix[i][j - 1] > matrix[i][j]:
                store[i][j] =max(store[i][j],1+markAll(i, j - 1))
            return store[i][j]

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                store[i][j] = markAll(i, j)
                if store[i][j] > self.max_so_far:
                    self.max_so_far = store[i][j]
        return self.max_so_far

assert Solution().longestIncreasingPath([
  []
]) == 0
assert Solution().longestIncreasingPath([
  [9,9,4],
  [6,6,8],
  [2,1,1]
]) == 4

assert Solution().longestIncreasingPath([
  [3,4,5],
  [3,2,6],
  [2,2,1]
]) == 4


assert Solution().longestIncreasingPath([
  [1]
]) == 1
