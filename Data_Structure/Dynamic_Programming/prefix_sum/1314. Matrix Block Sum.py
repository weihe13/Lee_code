# Given a m x n matrix mat and an integer k, return a matrix answer where each answer[i][j] is the sum of all
# elements mat[r][c] for: i - k <= r <= i + k, j - k <= c <= j + k, and (r, c) is a valid position in the matrix.

# Example 1:
# Input: mat = [[1,2,3],[4,5,6],[7,8,9]], k = 1
# Output: [[12,21,16],[27,45,33],[24,39,28]]
# Example 2:
# Input: mat = [[1,2,3],[4,5,6],[7,8,9]], k = 2
# Output: [[45,45,45],[45,45,45],[45,45,45]]

# Constraints:
# m == mat.length
# n == mat[i].length
# 1 <= m, n, k <= 100
# 1 <= mat[i][j] <= 100

# 思路： 1. 有了-k，+k的问题，需要用max(0, r-k),max(0, c-k)和min(r-1, i+k), max(c-1, j+k)去判断有没有超出边界。
#       2. 可以通过新变量s初始为0的方式，去新建一个persum矩阵，不改变mat原矩阵。
#       3. 熟悉lambda的写法。

fmax = lambda x, y: x if x > y else y  # 33% Faster than Python's Built-in MAX Function
fmin = lambda x, y: x if x < y else y  # Idem for MIN Function
inizero = lambda r, c: [[0] * c for _ in range(r)]


class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        r = len(mat)
        c = len(mat[0])

        presum = inizero(r, c)

        # first row
        s = 0
        for j in range(c):
            s += mat[0][j]
            presum[0][j] = s

        # first columns
        s = 0
        for i in range(r):
            s += mat[i][0]
            presum[i][0] = s

        # other points
        for i in range(1, r):
            for j in range(1, c):
                presum[i][j] = mat[i][j] + presum[i - 1][j] + presum[i][j - 1] - presum[i - 1][j - 1]

        res = inizero(r, c)
        for i in range(r):
            for j in range(c):
                r1, c1 = fmax(0, i - k), fmax(0, j - k)
                r2, c2 = fmin(r - 1, i + k), fmin(c - 1, j + k)

                val = presum[r2][c2]
                if r1 > 0:
                    val -= presum[r1 - 1][c2]
                    if c1 > 0:
                        val += presum[r1 - 1][c1 - 1]
                if c1 > 0:
                    val -= presum[r2][c1 - 1]
                res[i][j] = val
        return res
