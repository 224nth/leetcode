from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if (word == "" or word == None):
            return True
        if board == None or len(board) == 0:
            return False

        self.X = len(board)
        self.Y = len(board[0])

        for i in range(len(board)):
            for j in range(len(board[0])):
                if (board[i][j] == word[0]):
                    self.visited = set()
                    self.visited.add((i, j))
                    if self.dfs(board, i, j, word, 0):
                        return True

    def dfs(self, board, x, y, word, index):
        if (index == len(word) - 1):
            return True

        if (x > 0) and (x - 1, y) not in self.visited and board[x - 1][y] == word[index + 1]:
            self.visited.add((x - 1, y))
            b1 = self.dfs(board, x - 1, y, word, index + 1)
            if (b1):
                return True
            else:
                self.visited.remove((x - 1, y))

        if (x < self.X - 1) and (x + 1, y) not in self.visited and board[x + 1][y] == word[index + 1]:
            self.visited.add((x + 1, y))
            b1 = self.dfs(board, x + 1, y, word, index + 1)
            if (b1):
                return True
            else:
                self.visited.remove((x + 1, y))

        if (y > 0) and (x, y - 1) not in self.visited and board[x][y - 1] == word[index + 1]:
            self.visited.add((x, y - 1))
            b1 = self.dfs(board, x, y - 1, word, index + 1)
            if (b1):
                return True
            else:
                self.visited.remove((x, y - 1))

        if (y < self.Y - 1) and (x, y + 1) not in self.visited and board[x][y + 1] == word[index + 1]:
            self.visited.add((x, y + 1))
            b1 = self.dfs(board, x, y + 1, word, index + 1)
            if (b1):
                return True
            else:
                self.visited.remove((x, y + 1))

        return False


assert Solution().exist([["A","B","C","E"],["S","F","E","S"],["A","D","E","E"]],"ABCESEEEFS") == True


board =[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]




board1 = [['a','b'],['c','d']]
assert Solution().exist(board1, "abdc") == True
assert Solution().exist(board, "ABCCED") == True

assert Solution().exist(board, "SEE") == True
assert Solution().exist(board, "ABCB") == False


