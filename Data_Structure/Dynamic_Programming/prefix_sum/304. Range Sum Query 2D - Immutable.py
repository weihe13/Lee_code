# Given a 2D matrix matrix, handle multiple queries of the following type: Calculate the sum of the elements of
# matrix inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2,
# col2). Implement the NumMatrix class:
# NumMatrix(int[][] matrix) Initializes the object with the integer matrix matrix. int sumRegion(int row1, int col1,
# int row2, int col2) Returns the sum of the elements of matrix inside the rectangle defined by its upper left corner
# (row1, col1) and lower right corner (row2, col2).

# Example 1: Input ["NumMatrix", "sumRegion", "sumRegion", "sumRegion"] [[[[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2,
# 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]], [2, 1, 4, 3], [1, 1, 2, 2], [1, 2, 2, 4]] Output [null, 8, 11,
# 12] Explanation NumMatrix numMatrix = new NumMatrix([[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0,
# 1, 7], [1, 0, 3, 0, 5]]); numMatrix.sumRegion(2, 1, 4, 3); // return 8 (i.e sum of the red rectangle)
# numMatrix.sumRegion(1, 1, 2, 2); // return 11 (i.e sum of the green rectangle) numMatrix.sumRegion(1, 2, 2,
# 4); // return 12 (i.e sum of the blue rectangle)

# Constraints:
# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 200
# -105 <= matrix[i][j] <= 105
# 0 <= row1 <= row2 < m
# 0 <= col1 <= col2 < n
# At most 104 calls will be made to sumRegion.

# 思路：1. 如果用循环或者np.sum硬写，每次时间复杂度是m*n,如果重复k次，就是m*n*k。所以用一个新矩阵把每个位置的sum存下来，之后就不用重新算了，
#         时间复杂度应该是m*n+k
#      2. 形成新矩阵有两种方式，一是在原有矩阵上改，需要分情况讨论但不容易在idx上出错；另一种是新建一个矩阵，为了避免边界idx的分类讨论，
#         新矩阵是m+1*n+1，第一行第一列都是0。

# time complexity m*n*k
    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        sums = 0
        for i in range(row1,row2+1):
            for j in range(col1,col2+1):
                sums += self.matrix[i][j]
        return sums

# 新建一个矩阵
    def __init__(self, matrix: List[List[int]]):
        self.rows = len(matrix) + 1
        self.cols = len(matrix[0]) + 1
        self.prefsum = p = [[0] * self.cols for i in range(self.rows)]

        for i in range(1, self.rows):
            for j in range(1, self.cols):
                p[i][j] = p[i-1][j] + p[i][j-1] - p[i-1][j-1] + matrix[i-1][j-1]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        p = self.prefsum
        row2 += 1 # 注意：p是m+1*n+1，row2 col2 对应过来都要加1，row1 col1 因为就需要row-1，col-1，所以不做改变
        col2 += 1
        return p[row2][col2] - p[row2][col1] - p[row1][col2] + p[row1][col1]

# 直接改变原矩阵
    def __init__(self, matrix: List[List[int]]):
        row = len(matrix)
        col = len(matrix[0])
        for i in range(row):
            for j in range(col):
                if i == 0 and j == 0:
                    matrix[i][j] = matrix[i][j]
                elif i == 0:
                    matrix[i][j] += matrix[i][j - 1]
                elif j == 0:
                    matrix[i][j] += matrix[i - 1][j]
                else:
                    matrix[i][j] += matrix[i - 1][j] + matrix[i][j - 1] - matrix[i - 1][j - 1]
        self.matrix = matrix


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        res = self.matrix[row2][col2]
        # 注意：这里用row1,col1判断是否有sub矩阵可以减，
        #      用row2,col2判断不了，还要用row1,col1再次判断进行分类讨论，比如row2，col2大于0，但是row1=col1=0，这时其实没有矩阵可以
        #      减，如果仍然res -= self.matrix[row1 - 1][col2]，row1-1是-1，就减掉了row1col2最后一个数。
        if row1 > 0:
            res -= self.matrix[row1 - 1][col2]
        if col1 > 0:
            res -= self.matrix[row2][col1 - 1]
        if row1 > 0 and col1 > 0:
            res += self.matrix[row1 - 1][col1 - 1]
        return res

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
