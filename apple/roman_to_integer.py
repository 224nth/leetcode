

class Solution:
    def romanToInt(self, num: int) -> str:

        val = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4,
            1
        ]
        syb = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV",
            "I"
        ]

        ans = 0

        for i in range(len(syb)):
            while num.startswith(syb[i]):
                ans += val[i]
                num = num.replace(syb[i], "", 1)

        return ans


print(Solution().romanToInt("LVII"))

print(Solution().romanToInt("MCMXCIV"))