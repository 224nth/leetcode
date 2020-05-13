
from typing import List

class Solution:
    def isPossible(self, nums: List[int]) -> bool:

        from collections import Counter
        from collections import defaultdict

        counts = Counter(nums)
        store = defaultdict(int)


        for num in nums:
            if counts[num] == 0:
                continue
            elif counts.get(num) > 0 and  (num+1 in counts and counts.get(num+1) > 0) and ((num+2) in counts and counts.get(num+2) >0):
                store[num+2] += 1
                counts[num] -=1
                counts[num+1] -= 1
                counts[num+2] -= 1
            elif store.get(num-1) > 0 and counts.get(num) >0:
                store[num-1] -=1
                store[num] += 1
                counts[num] -=1
            else:
                return False

        return True








assert Solution().isPossible([1,2,3,3,4,5]) == True
assert Solution().isPossible([1,2,3,3,4,4,5,5]) == True
assert Solution().isPossible([1,2,3,4,4,5]) == False
