class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """

        if s == '':
            return True

        if s in wordDict:
            return True

        for i in range(1,len(s)):
            if s[0:i] in wordDict and self.wordBreak(s[i:], wordDict):
                return True

        return False



s = "leetcode"
wordDict = ["leet", "code"]
assert (Solution().wordBreak(s, wordDict) == True)

s = "applepenapple"
wordDict = ["apple", "pen"]
assert (Solution().wordBreak(s, wordDict) == True)

s = "catsandog"
wordDict = ["cats", "dog", "sand", "and", "cat"]
assert (Solution().wordBreak(s, wordDict) == False)