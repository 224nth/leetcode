

class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:

        num = 0
        for c in S:
            if c in J:
                num +=1

        return num




assert Solution().numJewelsInStones(J = "aA", S = "aAAbbbb") == 3

assert Solution().numJewelsInStones(J = "z", S = "ZZ") == 0

