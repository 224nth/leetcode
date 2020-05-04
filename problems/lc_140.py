from collections import defaultdict
from typing import List


class Solution:




    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:

        if not s or not wordDict:
            return

        wordDict = set(wordDict)

        memo = {}
        m = len(s)

        def dfs(s):
            if s in memo:
                return memo[s]

            res = []
            for i in range(1, len(s) +1):
                if s[:i] in wordDict:
                    if i == len(s):
                        res.append(s[:i])
                    else:
                        remain = dfs(s[i:])
                        for each in remain:
                            res.append(s[:i] + ' ' + each)

            memo[s] = res

            return res

        return dfs(s)





s = "catdog"
wordDict = ["cat", "cats", "and", "sand", "dog"]

print(Solution().wordBreak(s, wordDict))

s = "catsanddog"
wordDict = ["cat", "cats", "and", "sand", "dog"]

print(Solution().wordBreak(s, wordDict))

s = "pineapplepenapple"
wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
print(Solution().wordBreak(s, wordDict))



s = "catsandog"
wordDict = ["cats", "dog", "sand", "and", "cat"]

print(Solution().wordBreak(s, wordDict))