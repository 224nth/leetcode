from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        inedges = dict()
        inedges_count = [0] * numCourses
        for i in range(numCourses):
            inedges[i] = []
        for edge in prerequisites:
            inedges[edge[0]].append(edge[1])
            inedges_count[edge[1]] += 1
        zero = set()
        for i in range(numCourses):
            if inedges_count[i] == 0:
                zero.add(i)
        for i in range(numCourses):
            if (len(zero) == 0):
                return False
            course = zero.pop()
            for outedge in inedges[course]:
                inedges_count[outedge] -= 1
                if inedges_count[outedge] == 0:
                    zero.add(outedge)
        return True


assert Solution().canFinish(numCourses = 2, prerequisites = [[1,0]]) == True
assert Solution().canFinish(numCourses = 2, prerequisites = [[1,0],[0,1]]) == False
