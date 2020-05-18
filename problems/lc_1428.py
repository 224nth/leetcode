
#class BinaryMatrix(object):
#    def get(self, row: int, col: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:

        ans = -1
        [rows, cols] = binaryMatrix.dimensions()
        for i in range(len(rows)):
            for j in range(len(cols)):
                if binaryMatrix.get(i, j) == 1:
                    ans = j
                    break

        return ans

assert Solution().leftMostColumnWithOne([[0,0],[1,1]]) == 0
assert Solution().leftMostColumnWithOne([[0,0],[0,1]]) == 1
assert Solution().leftMostColumnWithOne([[0,0],[0,0]]) == -1