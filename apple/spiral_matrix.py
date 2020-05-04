from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return


        def spiral(rows, cols):

            s_row = 0
            s_col = 0

            res = []

            while s_row < rows and s_col < cols:

                for i in range(s_col, cols):
                    res.append(matrix[s_row][i])

                s_row += 1

                for i in range(s_row, rows):
                    res.append(matrix[i][cols-1])
                cols -=1

                if rows > s_row:
                    for i in range(cols-1, s_col-1, -1):
                        res.append(matrix[rows-1][i])

                    rows -= 1

                if cols > s_col:
                    for i in range(rows-1, s_row-1, -1):
                        res.append(matrix[i][s_col])

                    s_col +=1

            return res

        return spiral(len(matrix), len(matrix[0]))




a = [
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
#print(Solution().spiralOrder(a))

a =[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
print(Solution().spiralOrder(a))