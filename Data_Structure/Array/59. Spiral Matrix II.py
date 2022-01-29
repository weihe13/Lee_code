# Given a positive integer n, generate an n x n matrix filled with elements from 1 to n2 in spiral order.

# Example 1:
# Input: n = 3
# Output: [[1,2,3],[8,9,4],[7,6,5]]
# Example 2:
# Input: n = 1
# Output: [[1]]

# Constraints:
# 1 <= n <= 20

# 思路：1. 判断继续原方向会碰到非0数就转向；
#      2. 用di，dj来表示方向，最开始是0，1,表示向右，每次碰壁就向右转，di，dj=dj,-di
#      3. 巧妙在于用(i+di)除以行数的余数，和(j+dj)除以列数的余数来判断下一个位置，这样如果本层完毕了会循环到第一个位置。


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        A = [[0]*n for _ in range(n)]
        i, j = 0, 0
        di, dj = 0, 1
        for k in range(n*n):
            A[i][j] = k+1
            if A[(i+di)%n][(j+dj)%n]:
                di, dj = dj, -di
            i += di
            j += dj
        return A