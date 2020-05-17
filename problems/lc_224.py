class Solution:




    def calculate(self, s: str) -> int:


        stack = []
        index =0

        def get_next(self, s, index):
            res = ""
            index = index
            for i in range(index, len(s)):
                if s[i] == "":
                    continue
                elif s[i] == "(" or s[i] == ")" or s[i] == "+" or s[i] == "-":
                    res = s[i]
                    index = i + 1
                    break
                else:
                    res = res + s[i]
                    index = i + 1

            return res, index + 1

        next, index = get_next()
        while next != "":

            if next =="(":
                stack.append(next)
                next, index = get_next()

            if next == "+" or next == "-":
                next, index = get_next()

                val =









assert Solution().calculate("(1+(4+5+2)-3)+(6+8)")==23
assert Solution().calculate(" 2-1 + 2 ") ==3
