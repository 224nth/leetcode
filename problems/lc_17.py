import itertools


class Solution(object):
    map = {"1": "", "2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """

        digits =str(digits)
        lst = list(self.map[digits[len((digits))-1]])

        for c in range(len(digits)-2, -1,-1):
            a = list(self.map[digits[c]])
            lst = [x+y for x in a for y in lst]
        return lst



a=['a','b']
d=['e','f']
c = list(itertools.product(a, d))

print(c)

print(Solution().letterCombinations(23))