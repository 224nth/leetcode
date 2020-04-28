class Solution(object):


    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        memo = [-1] * len(s)
        return self.wordBreak(s, wordDict, memo)

    def _wordBreak(self,s,wordDict, memo):

        n = len(s)

        if s == '':
            return True

        if memo[n] == -1:
            memo[n] = 0
            for i in range(1,len(s)):
                if s[0:i] in wordDict and self.wordBreak(s[i:], wordDict):
                    memo[n] = 1

        return memo[n]





s = "leetcode"
wordDict = ["leet", "code"]
assert (Solution().wordBreak(s, wordDict) == True)

s = "applepenapple"
wordDict = ["apple", "pen"]
assert (Solution().wordBreak(s, wordDict) == True)

s = "catsandog"
wordDict = ["cats", "dog", "sand", "and", "cat"]
assert (Solution().wordBreak(s, wordDict) == False)