# Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of
# islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
# You may assume all four edges of the grid are all surrounded by water.

# Example 1:
# Input: grid = [
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]
# Output: 1
# Example 2:
# Input: grid = [
#   ["1","1","0","0","0"],
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]
# ]
# Output: 3

# Constraints:
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 300
# grid[i][j] is '0' or '1'

# 思路：1. BFS 或者 DFS都可以，关键是只寻找trigger 1，找到一个trigger1后要把连着的1都变成0，再继续循环

class Solution1: #DFS
    def numIslands(self, grid: List[List[str]]) -> int:
        nr = len(grid)
        nc = len(grid[0])
        count = 0
        # grid_ = grid.copy()  加上这步可以不改变原grid
        for i in range(nr):
            for j in range(nc):
                if grid[i][j] == '1':
                    count += 1
                    self.dfs(grid, i, j)
        return count

    def dfs(self, grid, row, col):
        nr = len(grid)
        nc = len(grid[0])

        if 0 <= row <= nr - 1 and 0 <= col <= nc - 1 and grid[row][col] == '1':
            grid[row][col] = '0'
            self.dfs(grid, row - 1, col)
            self.dfs(grid, row + 1, col)
            self.dfs(grid, row, col - 1)
            self.dfs(grid, row, col + 1)
        else:
            return


class Solution:   #BFS
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        nr, nc = len(grid), len(grid[0])
        count = 0

        for r in range(nr):
            for c in range(nc):
                if grid[r][c] == '1':
                    count += 1
                    grid[r][c] = '0'
                    queue = deque()
                    queue.append([r, c])
                    while queue:
                        row, col = queue.popleft()
                        if row - 1 >= 0 and grid[row - 1][col] == '1':
                            queue.append([row - 1, col])
                            grid[row - 1][col] = '0'
                        if col - 1 >= 0 and grid[row][col - 1] == '1':
                            queue.append([row, col - 1])
                            grid[row][col - 1] = '0'
                        if row + 1 < nr and grid[row + 1][col] == '1':
                            queue.append([row + 1, col])
                            grid[row + 1][col] = '0'
                        if col + 1 < nc and grid[row][col + 1] == '1':
                            queue.append([row, col + 1])
                            grid[row][col + 1] = '0'
        return count