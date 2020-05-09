import queue
from typing import List


class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:

        def dfs(n, c):
            m[n] = c
            for nn in graph[n]:
                if nn in m:
                    if m[nn] == c:
                        return False
                elif not dfs(nn, int(not c)):
                    return False
            return True

        m = {}
        for i in range(len(graph)):
            if not dfs(i, m.get(i, 1)):
                return False
        return True


assert Solution().isBipartite([[],[2,4,6],[1,4,8,9],[7,8],[1,2,8,9],[6,9],[1,5,7,8,9],[3,6,9],[2,3,4,6,9],[2,4,5,6,7,8]]) == False
assert Solution().isBipartite([[4],[],[4],[4],[0,2,3]]) == True
assert Solution().isBipartite([[3],[2,4],[1],[0,4],[1,3]]) == True
assert Solution().isBipartite([[1,3], [0,2], [1,3], [0,2]]) == True
assert Solution().isBipartite([[1,2,3], [0,2], [0,1,3], [0,2]]) == False