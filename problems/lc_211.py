import string


class Node:
    c = None
    children = [None for _ in range(26)]
    end = False

    def __init__(self, c, end = False):
        self.c = c
        self.end = end

    def add_children(self):
        self.children = [Node(c) for c in string.ascii_lowercase]


class WordDictionary:



    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.start = Node('-1')

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """

        temp = self.start
        for i in range(len(word)):
            if temp.children[ord(word[i])-ord('a')] is None:
                temp.add_children()

            temp = temp.children[ord(word[i])-ord('a')]
            if i+1 == len(word):
                temp.end = True





    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """

        temp = self.start

        for i in range(len(word)):
                       
            if temp.children[ord(word[i]) - ord('a')] is None:
                return False
            temp = temp.children[ord(word[i])-ord('a')]
            if i+1 == len(word) and temp.end == True:
                return True

        return False




d = WordDictionary()
d.addWord("bad")
d.addWord("dad")
d.addWord("mad")
print(d.search("pad"))
print(d.search("bad"))
print(d.search(".add"))