from collections import defaultdict


class Solution:
    def firstUniqChar(self, s: str) -> int:

        if not s or s == "":
            return -1

        map = defaultdict(list)

        for i, c in enumerate(s):
            map[c].append(i)

        lowest = len(s)
        for key in map.keys():
            if len(map[key]) == 1 and map[key][0] < lowest:
                lowest = map[key][0]

        if lowest == len(s):
            return -1

        return lowest



print(Solution().firstUniqChar("leetcode"))
print(Solution().firstUniqChar("loveleetcode"))