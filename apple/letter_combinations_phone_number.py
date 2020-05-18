from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []

        map = {
            "2": "abc",
            "3" :"def",
            "4" : "ghi",
            "5" :"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz",
        }

        comb = []
        def getCombination(digits, current):

            if digits == "":
                comb.append(current)
                return

            for i in map.get(digits[0]):
                getCombination(digits[1:], current+i)


        getCombination(digits, "")
        return comb


assert Solution().letterCombinations("23") == ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
