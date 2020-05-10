
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        sortedList = []
        resList = []
        for s in strs:
            s_sorted = ''.join(sorted(s))


            found = False
            for i in range(len(resList)):
                if s_sorted == sortedList[i]:
                    resList[i].append(s)
                    found = True
                    break

            if not found:
                sortedList.append(''.join(sorted(s)))
                resList.append([s])

        return resList


assert Solution().groupAnagrams(['eat', 'tea', 'tan', 'ate', 'nat', 'bat']) == [
  ['ate','eat','tea'],
  ['nat','tan'],
  ['bat']
]