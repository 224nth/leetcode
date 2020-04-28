class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        state = [['.'] * n for i in range(n)]
        self._place_queen(0, 0, state, n)
        self._place_queen(0, 1, state, n)
        self._place_queen(1, 0, state, n)
        self._place_queen(0, 1, state, n)


    def _check_move(self, i, j, state, n):

        if state[i][j] == 'Q':
            return False
        elif i-1 >=0  and state[i-1][j] == 'Q':
            return False
        elif j - 1 >= 0 and state[i][j-1] == 'Q':
            return False

        elif i + 1 <n and state[i + 1][j] == 'Q':
            return False
        elif j + 1 < n and state[i][j + 1] == 'Q':
            return False

        elif i - 1 >= 0 and j-1 >= 0 and state[i - 1][j-1] == 'Q':
            return False
        elif i + 1 <n and j+1 < n and state[i + 1][j+1] == 'Q':
            return False

        elif i - 1 >= 0 and j+1 < n and state[i - 1][j + 1] == 'Q':
            return False

        elif i + 1 >= 0 and j-1 >= 0 and state[i + 1][j-1] == 'Q':
            return False

        return True


    def _place_queen(self, i, j, state, n):

        state[i][j] = 'Q'
        n=n-1

        if n == 0:
            print(state)
            return

        if i+2 < n and self._check_move(i+2, j , state, n):
            self._place_queen(i+2, j, state, n)
        elif j+2 < n and self._check_move(i, j+2, state, n):
            self._place_queen(i, j+2, state, n)

        elif j-2 >=0 and self._check_move(i, j-2 , state, n):
            self._place_queen(i, j-2, state, n)
        elif i-2 >=0 and self._check_move(i-2, j , state, n):
            self._place_queen(i-2, j, state, n)

        elif j+2 < n and i+2 <n and self._check_move(i+2, j+2 , state, n):
            self._place_queen(i+2, j+2, state, n)

        elif j+2 < n and i-2>=0 and self._check_move(i-2, j+2 , state, n):
            self._place_queen(i-2, j+2, state,n)

        elif j-2 >=0 and i-2>=0 and self._check_move(i-2, j-2, state, n):
            self._place_queen(i-2, j-2, state,n)

        elif j-2 >=0 and i+2 <n  and self._check_move(i+2, j-2 , state, n):
            self._place_queen(i+2, j-2, state, n)

        state[i][j]= '.'
        n=n+1



Solution().solveNQueens(4)