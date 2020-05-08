
from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        store = [False for i in range(len(s))]
        if s[0] in wordDict:
            store[0] = True

        for i in range(1, len(s)):
            if s[0:i+1] in wordDict:
                store[i] = True
                continue

            for j in range(i):
                if (store[j] and s[j+1:i+1] in wordDict):
                    store[i] = True
                    break


        return store[-1]


assert Solution().wordBreak(s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]) == False
assert Solution().wordBreak(s = "ab", wordDict = ["a", "b"]) == True
assert Solution().wordBreak(s = "leetcode", wordDict = ["leet", "code"]) == True

assert Solution().wordBreak(s = "leetcodee", wordDict = ["leet", "code"]) == False

assert Solution().wordBreak( s = "applepenapple", wordDict = ["apple", "pen"]) == True
