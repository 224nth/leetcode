

class Solution:
    def intToRoman(self, num: int) -> str:

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
        ans = ""
        i = 0
        while num:
            for _ in range(num // val[i]):
                ans += syb[i]
                num -= val[i]
            i += 1
        return ans





print(Solution().intToRoman(58))
print(Solution().intToRoman(1994))
