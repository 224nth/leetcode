class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """

        if not s:
            return s

        s = s[::-1]

        s = s.split(" ")

        filtered = []
        for i in s:
            if i != " " and i != "":
                filtered.append(i[::-1])

        return " ".join(filtered)



    def reverseWords_inplace(self, s):
        """
        :type s: str
        :rtype: str
        """

        if not s:
            return s

        reverse = self.reverseWord(s)
        split = reverse.split(" ")

        filtered = []
        for i in split:
            if i != " " and i != "":
               filtered.append(self.reverseWord(i))

            return " ".join(filtered)

    def reverseWord(self,s):
        for i in range(int(len(s)/2)):
            temp = s[i]
            s[i]= s[len(s)-i-1]
            s[len(s) - i - 1] = temp


Solution().reverseWords("the sky is blue")
Solution().reverseWord("the")