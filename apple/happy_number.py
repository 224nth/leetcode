class Solution:
    def isHappy(self, n: int) -> bool:

        count = 0
        while count < 1000:
            res = 0

            for c in str(n):
                res += int(c) **2

            if res == 1:
                return True
            count += 1
            n= res

        return False

assert Solution().isHappy(19) == True