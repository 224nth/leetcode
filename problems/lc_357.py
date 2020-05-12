from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        from queue import PriorityQueue
        counts = Counter(nums)

        q = PriorityQueue()

        for i in counts.keys():
            q.put((counts[i]*-1, i))


        lst = []
        for i in range(k):
            lst.append(q.get()[1])

        return lst


assert Solution().topKFrequent(nums = [1,1,1,2,2,3], k = 2) == [1,2]
assert Solution().topKFrequent(nums = [1], k = 1) == [1]