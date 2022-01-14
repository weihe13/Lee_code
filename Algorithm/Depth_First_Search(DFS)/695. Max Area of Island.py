# You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally
# (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water. The area of an island
# is the number of cells with a value 1 in the island.
# Return the maximum area of an island in grid. If there is no island, return 0.

# Example 1:
# Input: grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],
# [0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],
# [0,0,0,0,0,0,0,1,1,0,0,0,0]]
# Output: 6
# Explanation: The answer is not 11, because the island must be connected 4-directionally.
# Example 2:
# Input: grid = [[0,0,0,0,0,0,0,0]]
# Output: 0

# Constraints:
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 50
# grid[i][j] is either 0 or 1.

# 思路：1. 这种题recuresion肯定可以做，问题是思路
#      2. set, dict, list 三种类型变量在外部函数，被内部函数修改时，改动会保留。可以用此特性标记已经到过的点，防止重复计算。
#      3. 可以用for 循环+ pop 实现iteration。

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        def dfs(i, j):
            if 0 <= i < m and 0 <= j < n and grid[i][j]:
                grid[i][j] = 0
                return 1 + dfs(i - 1, j) + dfs(i, j + 1) + dfs(i + 1, j) + dfs(i, j - 1)
            return 0

        # 这种先append再max的写法，比每次都用max（）比较大小要快
        areas = [dfs(i, j) for i in range(m) for j in range(n) if grid[i][j]]
        return max(areas) if areas else 0

        # iteration
        rows, cols = len(grid), len(grid[0])
        res = []
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] != 1:
                    continue
                stack = [(r, c)]
                land = 0
                while stack:
                    t_r, t_c = stack.pop()
                    if 0 <= t_r < rows and 0 <= t_c < cols:
                        if grid[t_r][t_c] == 1:
                            land += 1
                            grid[t_r][t_c] = 0
                            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                                stack.append((t_r + dr, t_c + dc))
                res.append(land)
        return max(res) if res else 0