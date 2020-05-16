from collections import defaultdict
from typing import List


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:


        parent = [0 for i in range(len(edges) + 1)]

        def findParent(index):
            if parent[index] == 0:
                return index
            return findParent(parent[index])


        for i in range(len(edges)):
            a = findParent(edges[i][0])
            b = findParent(edges[i][1])
            if a == b:
                return edges[i]
            parent[b]= a

        return []




#assert Solution().findRedundantConnection([[1,2], [1,3], [2,3]]) == [2,3]
#assert Solution().findRedundantConnection([[1,2], [2,3], [3,4], [1,4], [1,5]]) == [1,4]
assert Solution().findRedundantConnection([[1,4],[3,4],[1,3],[1,2],[4,5]]) == [1,3]