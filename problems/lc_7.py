class Solution:
    def reverse(self, x: int) -> int:

        if not x:
            return x

        not_negative = 1
        if x < 0:
            not_negative = -1


        x = abs(x)

        value = 0
        while x >=10:

            remainder = int(x%10)
            value = value * 10 + remainder
            x = int(x/10)
        value = value * 10 + x
        return not_negative* value



print(Solution().reverse(123))
print(Solution().reverse(-123))
print(Solution().reverse(120))