

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []

        map_bracket = {')':'(','}':'{',']':'['}
        for i in s:
            if i in ['(', '{', '[']:
                stack.append(i)
            elif map_bracket[i] == stack[-1]:
                stack.pop()
            else:
                return False

        return len(stack) == 0


assert (Solution().isValid('[(()){}]') == True)


assert (Solution().isValid('(())') == True)
assert (Solution().isValid('(()){}') == True)

assert (Solution().isValid('[(()){}](') == False)
assert (Solution().isValid('') == True)