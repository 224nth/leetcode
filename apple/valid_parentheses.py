


class Solution:
    def isValid(self, s: str) -> bool:

        if not s:
            return True

        stack = []
        for c in s:


            if c == ')' and stack and stack.pop() == '(':
                continue
            elif c == '}' and stack and stack.pop() == '{':
                continue
            elif c == ']' and stack and stack.pop() == '[':
                continue
            else:
                stack.append(c)


        return len(stack) == 0


print(Solution().isValid("(){}"))