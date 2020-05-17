from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        visited = [[False for _  in range(len(grid[0]))] for _ in range(len(grid))]
        count = 0


        def markAll(i,j, visited):
            visited[i][j] = True

            if i +1 < len(grid) and not visited[i+1][j] and grid[i+1][j] =="1":
                markAll(i+1, j, visited)
            if i-1 >=0 and not visited[i-1][j] and grid[i-1][j]  == "1":
                markAll(i-1, j, visited)
            if j +1 < len(grid[0]) and not visited[i][j+1] and grid[i][j+1] =="1":
                markAll(i, j+1, visited)
            if j-1 >=0 and not visited[i][j-1] and grid[i][j-1]  == "1":
                markAll(i, j-1, visited)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] =="1" and not visited[i][j]:
                    count +=1
                    markAll(i, j, visited)

        return count


grid = [["1","1","1"],["0","1","0"],["0","1","0"]]
assert Solution().numIslands(grid) ==1

# grid = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
# assert Solution().numIslands(grid) ==1


# grid = [[1,0,0]]
# assert Solution().numIslands(grid) ==1
#
# grid= [[1,0,0],
#     [0,1,0],
#     [0,0,1]]
# assert Solution().numIslands(grid) ==3