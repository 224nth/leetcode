import queue
import string
from typing import List

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        words = set()

        for word in wordList:
            words.add(word)

        q = queue.Queue()
        q.put((1,beginWord))

        while not q.empty():

            count, word = q.get()
            if word == endWord:
                return count
            for i in range(len(word)):
                for c in string.ascii_lowercase:
                    if c != word[i]:
                        newc = word[:i]+c+word[i+1:]

                        if newc in words:
                            words.discard(newc)
                            q.put((count+1, newc))

        return 0




assert  Solution().ladderLength(beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]) == 5

assert Solution().ladderLength(beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log"]) == 0