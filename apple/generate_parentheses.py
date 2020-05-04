from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        def gp(n):
            if n == 1:
                return {"()"}
            elif n ==0:
                return {}

            ans = gp(n-1)
            res = set()
            for a in ans:
                res.add("(" + a + ")")
                res.add("()"+a)
                res.add(a +"()")

            return res


        return list(gp(n))


    def generateParenthesis2(self, n: int) -> List[str]:

        ans = []

        def gp(n, o, c, current):
            if len(current) == 2*n:
                ans.append(current)
                return

            if o< n:
                gp(n,o+1, c, current+'(')
            if c<o:
                gp(n,o,c+1,current+')')

        gp(n, 0, 0, "")
        return ans




a =Solution().generateParenthesis(4)
b = Solution().generateParenthesis2(4)

print(a)
print(b)

print(set(b).symmetric_difference(set(a)))