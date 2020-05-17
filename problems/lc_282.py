from typing import List


class Solution:

    def addOperators(self, num: str, target: int) -> List[str]:

        res = []
        def find(num, target, ce, idx):

            if idx == len(num):
                if target == eval(ce):
                    res.append(ce)
                    return
                else:
                    return

            for i in range(idx, len(num)):
                if num[idx] == "0" and i > idx:
                    continue
                if idx == 0:
                    find(num, target,  str(num[idx:i+1]), i+1)
                else:
                    find(num, target,  ce + "+" + num[idx:i+1], i+1)
                    find(num, target, ce + "-" + num[idx: i + 1], i + 1)
                    find(num, target,  ce + "*" + num[idx :i + 1], i + 1)



        find(num, target, "", 0)
        return res


#print(Solution().addOperators("123", 6))
#assert Solution().addOperators("123", 6) == ["1+2+3", "1*2*3"]
print(Solution().addOperators("105", 5))
assert Solution().addOperators("105", 5) == ["1*0+5","10-5"]