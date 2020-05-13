
class Solution:
    def frequencySort(self, s: str) -> str:
        from collections import Counter
        from queue import PriorityQueue
        counts = Counter(s)

        q = PriorityQueue()
        for i in counts.keys():
            q.put((counts[i] * -1, i))

        lst = []
        while not q.empty():
            current = q.get()
            for i in range(current[0]*-1):
                lst.append(current[1])

        return "".join(lst)



assert Solution().frequencySort("tree") == "eert"
assert Solution().frequencySort("cccaaa") == "cccaaa" or Solution().frequencySort("cccaaa") == "aaaccc"
assert Solution().frequencySort("Aabb") == "bbAa" or Solution().frequencySort("Aabb") == "bbaA"