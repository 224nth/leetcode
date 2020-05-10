import sys


class Solution:
    def reverse(self, x: int) -> int:
        max_int = 2**31
        sign = 1

        if x < 0:
            sign = -1
            x = -1 * x


        res = 0

        while x > 0:
            if (max_int - (x%10))/ 10 < res:
                return  0

            res = res * 10 + x % 10
            x = x // 10

        return sign * res

assert Solution().reverse(1534236469) == 0
assert Solution().reverse(123) == 321
assert Solution().reverse(-123) == -321
assert Solution().reverse(120) == 21


