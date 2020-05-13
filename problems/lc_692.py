from collections import Counter
from queue import PriorityQueue
from typing import List


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:

        counts = Counter(words)

        q = PriorityQueue()

        for i in counts.keys():
            q.put((counts[i] * -1, i))

        lst = []
        for i in range(k):
            lst.append(q.get()[1])

        return lst


assert Solution().topKFrequent(["i", "love", "leetcode", "i", "love", "coding"], k = 2) ==  ["i", "love"]
assert Solution().topKFrequent(["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], k = 4) == ["the", "is", "sunny", "day"]