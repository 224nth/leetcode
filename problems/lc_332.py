import collections
from queue import PriorityQueue
from typing import List


class Solution:

    result = []
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:

        map = collections.defaultdict()

        for ticket in tickets:
            if ticket[0] not in map:
                q = PriorityQueue()
                q.put(ticket[1])
                map[ticket[0]] = q
            else:
                q = map[ticket[0]]
                q.put(ticket[1])

        self._recurse("JFK", map)
        return self.result[::-1]

    def _recurse(self, next, map):
        q = map.get(next)

        while(q != None and not q.empty()):
            self._recurse(q.get(), map)

        self.result.append(next)

    def findItinerary2(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        graph = collections.defaultdict(list)
        ans = []

        for scr, dep in tickets:
            graph[scr].append(dep)
        for key in graph:
            graph[key].sort()

        def dfs(node):
            arr = graph[node]
            while arr:
                dfs(arr.pop(0))
            ans.append(node)

        dfs("JFK")
        return ans[::-1]


#arr = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
#print(Solution().findItinerary(arr))

#arr =[["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
#print(Solution().findItinerary(arr))

arr =[["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
print(Solution().findItinerary(arr))

# arr = [["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]]
#print(Solution().findItinerary(arr))

