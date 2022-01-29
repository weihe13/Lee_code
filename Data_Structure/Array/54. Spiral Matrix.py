# Given an m x n matrix, return all elements of the matrix in spiral order.

# Example 1:
# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [1,2,3,6,9,8,7,4,5]
# Example 2:
# Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# Output: [1,2,3,4,8,12,11,10,9,5,6,7]

# Constraints:
# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 10
# -100 <= matrix[i][j] <= 100

# 思路：1. 每取完一个数，就把这个位置换成0，这样判断继续原方向会碰到0就转向；
#      2. 用di，dj来表示方向，最开始是0，1,表示向右，每次碰壁就向右转，di，dj=dj,-di

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        A = []
        i, j = 0, 0
        di, dj = 0, 1
        for k in range(m*n):
            A.append(matrix[i][j])
            matrix[i][j] = 0
            if not matrix[(i+di)%m][(j+dj)%n]:
                di, dj = dj, -di
            i += di
            j += dj
        return A