class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """

        tracker =[[0 for x in range(len(board[0]))] for y in range(len(board))]

        for i in range(len(board)):
            for j in range(len(board[0])):
                if word[0] == board[i][j]:
                    tracker[i][j] =1
                    if self.__exist(i, j, board, tracker, word[1:]):
                        return True
                    tracker[i][j] =0

        return False

    def __exist(self, i, j, board, tracker, word):
        if word == '':
            return True

        if i+1 < len(board) and board[i+1][j] == word[0] and tracker[i+1][j]==0:
            tracker[i+1][j] = 1
            if len(word) == 1: return True
            if self.__exist(i+1, j, board, tracker, word[1:]):
                return True
            tracker[i + 1][j] = 0

        if j + 1 < len(board[0]) and board[i][j+1] == word[0] and tracker[i][j+1] == 0:
            if len(word) == 1: return True
            tracker[i][j+1] = 1
            if self.__exist(i, j+1, board, tracker, word[1:]):
                return True
            tracker[i][j+1] = 0

        if j - 1 >=0 and board[i][j-1] == word[0] and tracker[i][j-1] == 0:
            if len(word) == 1: return True
            tracker[i][j-1] = 1
            if self.__exist(i, j-1, board, tracker, word[1:]):
                return True
            tracker[i][j-1] = 0

        if i-1 >= 0 and board[i-1][j] == word[0] and tracker[i-1][j] ==0:
            if len(word) == 1: return True
            tracker[i-1][j] = 1
            if self.__exist(i-1, j, board, tracker, word[1:]):
                return True
            tracker[i -1][j] = 0

        return  False


board =[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

word1= 'ABCCED'
word2 = 'ABCB'


assert(Solution().exist(board, word1) == True)
assert(Solution().exist(board, word2) == False)
