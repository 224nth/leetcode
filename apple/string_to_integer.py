



class Solution:
    def myAtoi(self, str1: str) -> int:
        max_int = 2 ** 31 - 1
        min_int = -1 * 2 ** 31
        potential = ""
        sign = 1
        num_started = False
        for i in range(len(str1)):
            if not num_started and str1[i] == " ":
                continue
            elif not num_started and str1[i] == '-':
                num_started = True
                sign = -1

            elif not num_started and  str1[i] == "+":
                num_started = True
                sign = 1
            elif str1[i] >= "0" and str1[i] <= "9":
                num_started = True
                potential = potential + str(str1[i])
            elif num_started:
                break
            else:
                return 0

        num = 0

        for i in range(len(potential)):
            current = int(potential[i])

            if (max_int - current)/10 < num:
                if sign ==1:
                    return max_int
                return min_int

            num = num * 10 + current
        return sign * num


assert Solution().myAtoi("2147483646") == 2147483646
assert Solution().myAtoi("2147483648") == 2147483647
assert Solution().myAtoi("+-1") == 0
assert Solution().myAtoi("+1") == 1
assert Solution().myAtoi("-91283472332") == -2147483648
assert Solution().myAtoi("42") == 42
assert Solution().myAtoi("   -42") == -42
assert Solution().myAtoi("   42 with words") == 42
assert Solution().myAtoi("   42.234") == 42
