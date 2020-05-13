import re


class Solution:
    def maskPII(self, S: str) -> str:


        def maskEmail(s):
            if "@" not in s:
                return s
            parts =re.split("[@.]+",s)

            for i in range(len(parts)):
                parts[i] = parts[i].lower()
                if i == 0:
                    parts[i] = parts[i][0] +"*****" + parts[i][-1]

            return parts[0] +"@"+parts[1]+"."+parts[2]



        def maskPhone(s):
            if "@" in s:
                return s

            digits = re.findall(r'\d+', s)
            digits = "".join(digits)

            num=""
            if len(digits) == 11:
                num = "+*-"
            elif len(digits) == 12:
                num = "+**-"
            elif len(digits) == 13:
                num = "+***-"

            num = num+ "***-***-"+digits[len(digits)-4:]


            return  num

        S= maskEmail(S)
        S= maskPhone(S)

        return S


assert Solution().maskPII("LeetCode@LeetCode.com") == "l*****e@leetcode.com"
assert Solution().maskPII("AB@qq.com") == "a*****b@qq.com"
assert Solution().maskPII("1(234)567-890") == "***-***-7890"
assert Solution().maskPII("86-(10)12345678") ==  "+**-***-***-5678"

