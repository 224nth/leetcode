from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        pass



board =[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

assert Solution().exist("ABCCED") == True
assert Solution().exist("SEE") == True
assert Solution().exist("ABCB") == False


