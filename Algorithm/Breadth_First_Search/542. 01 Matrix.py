# Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.
# The distance between two adjacent cells is 1.

# Example 1:
# Input: mat = [[0,0,0],[0,1,0],[0,0,0]]
# Output: [[0,0,0],[0,1,0],[0,0,0]]
# Example 2:
# Input: mat = [[0,0,0],[0,1,0],[1,1,1]]
# Output: [[0,0,0],[0,1,0],[1,2,1]]

# Constraints:
# m == mat.length
# n == mat[i].length
# 1 <= m, n <= 104
# 1 <= m * n <= 104
# mat[i][j] is either 0 or 1.
# There is at least one 0 in mat.

# 思路： 1. BFS: 核心是一层一层找，先找距离为0的点，再找距离为1的点，再找距离为2的点，以此类推

class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        m, n = len(matrix), len(matrix[0])
        queue = collections.deque()
        res = [[-1 for _ in range(n)] for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    # The distance to itself is 0 and add all sources here to queue
                    res[i][j] = 0
                    queue.append((i, j))

        # Now we start our BFS
        while queue:
            curI, curJ = queue.popleft()
            for i, j in dirs:
                neighBorI, neighBorJ = curI + i, curJ + j
                # Validate all the neighbors and validate the distance as well
                if 0 <= neighBorI < m and 0 <= neighBorJ < n and res[neighBorI][neighBorJ] == -1:
                    res[neighBorI][neighBorJ] = res[curI][curJ] + 1
                    queue.append((neighBorI, neighBorJ))
        return res