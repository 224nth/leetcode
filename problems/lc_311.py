from typing import List


class Solution:
    def multiply(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        num_of_a_rows = len(A)
        num_of_a_cols = len(A[0])
        num_of_b_cols = len(B[0])

        result = [[0 for _ in range(num_of_b_cols)] for _ in range(num_of_a_rows)]
        for a_row in range(num_of_a_rows):
            for a_col in range(num_of_a_cols):
                if A[a_row][a_col]:
                    for b_col in range(num_of_b_cols):
                        if  B[a_col][b_col]:
                            result[a_row][b_col] += A[a_row][a_col] * B[a_col][b_col]

        return result



A = [
  [ 1, 0, 0],
  [-1, 0, 3]
]

B = [
  [ 7, 0, 0 ],
  [ 0, 0, 0 ],
  [ 0, 0, 1 ]
]

assert Solution().multiply(A, B) == [[7,0,0], [-7,0,3]]


