class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """


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


        for i in range(len(matrix)):
            if matrix[i] and matrix[i][0] <= target and matrix[i][-1] >=target:
                found = binarySearch(matrix[i], target, 0, len(matrix[i]))
                if found:
                    return True
        return False

assert Solution().searchMatrix([[]], 1) == False
a = [
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
assert Solution().searchMatrix(a, 5) == True
assert Solution().searchMatrix(a, 20) == False