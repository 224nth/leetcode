from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if not tokens:
            return 0
        stack =  []

        for token in tokens:
            if token not in ["-","+","*","/"]:
                stack.append(token)
            else:
                second = stack.pop()
                first = stack.pop()
                ans = int(eval(first+token+second))
                stack.append(str(ans))
        return int(stack[-1])

#assert Solution().evalRPN(["2", "1", "+", "3", "*"]) == 9
#assert Solution().evalRPN(["4", "13", "5", "/", "+"]) == 6
assert Solution().evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]) == 22
