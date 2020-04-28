import string


class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """

        self._ladderLength(beginWord, endWord, wordList, 0)


    def _ladderLength(self, beginWord, endWord, wordList, pos):

        if beginWord == endWord:
            return len
        elif pos >= len(endWord):
            return 0

        for i in string.ascii_lowercase:
            pre = beginWord[pos]
            length = self._ladderLength(beginWord, endWord, wordList, i+1)
            if length:
                return length


beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]
print(Solution().ladderLength(beginWord, endWord, wordList))