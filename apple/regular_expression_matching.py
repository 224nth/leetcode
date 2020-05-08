class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        pass



assert Solution().isMatch(s = "aa",p = "a") == False
assert Solution().isMatch(s = "aab",p = "c*a*b") == True
assert Solution().isMatch(s = "mississippi",p = "mis*is*p*.") == False
assert Solution().isMatch(s = "ab",p = ".*") == True
assert Solution().isMatch(s = "aa",p = ".*") == True
