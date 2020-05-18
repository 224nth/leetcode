import collections
from collections import defaultdict


class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if len(s) < len(t):
            return ""

        hashmap = collections.Counter(t)
        missing = len(t)
        min_window = ""
        start = 0

        for end in range(len(s)):
            if hashmap[s[end]] > 0:
                missing -= 1
            hashmap[s[end]] -= 1

            while missing == 0:
                length = end - start + 1

                if not min_window or len(min_window) > length:
                    min_window = s[start:end + 1]

                hashmap[s[start]] += 1

                if hashmap[s[start]] > 0:
                    missing += 1

                start += 1
        return min_window


S = "ADOBECODEBANC"
T = "ABC"

ans =  Solution().minWindow(S, T)
print(ans)
assert ans == "BANC"