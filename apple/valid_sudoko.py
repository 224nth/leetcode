from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        for i in range(9):
            current = set()
            for j in range(9):
                if board[i][j] != '.':
                    if board[i][j] in current:
                        return False
                    else:
                        current.add(board[i][j])

        for i in range(9):
            current = set()
            for j in range(9):
                if board[j][i] != '.':
                    if board[j][i] in current:
                        return False
                    else:
                        current.add(board[j][i])

        for i in range(3):
            for j in range(3):

                current = set()
                for p in range(3):
                    for q in range(3):
                        if board[i*3+p][j*3+q] != '.':
                            if board[i*3+p][j*3+q] in current:
                                return False
                            else:
                                current.add(board[i*3+p][j*3+q])

        return True




assert Solution().isValidSudoku([
  ["8","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]) == False

assert Solution().isValidSudoku([
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]) == True
