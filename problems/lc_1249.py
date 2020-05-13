


class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:


        def removeExtra(str, op, cl):

            string = [c for c in str]

            c,o = 0,0
            i = 0
            while i < len(string):
                if string[i] == cl:
                    c +=1
                elif string[i] == op:
                    o+=1
                if c > o:
                    string.pop(i)
                    c -= 1
                else:
                    i+=1

            return "".join(string)

        s = removeExtra(s, "(", ")")
        s = removeExtra(s[::-1],")","(")
        return s[::-1]



assert Solution().minRemoveToMakeValid("lee(t(c)o)de)") =="lee(t(c)o)de"
assert Solution().minRemoveToMakeValid("a)b(c)d") == "ab(c)d"
assert Solution().minRemoveToMakeValid("a)b(c)d") == "ab(c)d"
assert Solution().minRemoveToMakeValid( "))((") == ""