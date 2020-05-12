from collections import defaultdict


class Solution:
    def minWindow(self, s: str, t: str) -> str:


        map = defaultdict(int)

        length = [[0] * len(t)]
        current = 0
        end = len(s)
        start = -1

        min_so_far = 1000

        while current < len(t):
            found = False
            for i in range(len(s)):
                if s[i] == t[current]:

                    length[current] = i 
                    found= True

                    break
            if found:
                current +=1
            else:
                return False

        return s[start:end+1]







S = "ADOBECODEBANC"
T = "ABC"

assert Solution().minWindow(S, T) == "BANC"