from collections import defaultdict


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:


        map = defaultdict(lambda :0)

        for i in s:
            map[i] +=1

        for i in t:
            map[i] -= 1

        for key in map.keys():
            if map[key] != 0:
                return False
        return True

print(Solution().isAnagram(s = "anagram", t = "nagaram"))