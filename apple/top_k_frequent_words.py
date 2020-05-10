from typing import List


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        pass




words =  ["i", "love", "leetcode", "i", "love", "coding"]
k = 2
assert Solution().topKFrequent(words, k) == ["i", "love"]



words = ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"]
k = 4
assert Solution().topKFrequent(words, k) == ["the", "is", "sunny", "day"]


