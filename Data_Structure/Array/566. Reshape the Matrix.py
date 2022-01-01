# In MATLAB, there is a handy function called reshape which can reshape an m x n matrix into a new one with a
# different size r x c keeping its original data. You are given an m x n matrix mat and two integers r and c
# representing the number of rows and the number of columns of the wanted reshaped matrix. The reshaped matrix should
# be filled with all the elements of the original matrix in the same row-traversing order as they were. If the
# reshape operation with given parameters is possible and legal, output the new reshaped matrix; Otherwise,
# output the original matrix.

# Example 1:
# Input: mat = [[1,2],[3,4]], r = 1, c = 4
# Output: [[1,2,3,4]]
# Example 2:
# Input: mat = [[1,2],[3,4]], r = 2, c = 4
# Output: [[1,2],[3,4]]

# Constraints:
# m == mat.length
# n == mat[i].length
# 1 <= m, n <= 100
# -1000 <= mat[i][j] <= 1000
# 1 <= r, c <= 300

# 注意： 1. 自己的思路是没问题的，但是速度很慢，import了numpy
#       2. 学习别人flatten list的写法

class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:

        A = [x for row in mat for x in row]
        if r * c == len(A):
            return [A[i * c: (i + 1) * c] for i in range(r)]
        else:
            return mat

        # 自己的写法 很慢
        # import numpy as np
        # old_row = len(mat)
        # old_column = len(mat[0])
        # res = []
        # if old_row * old_column != r * c:
        #     return mat
        # mat = list(np.concatenate(mat).flat)
        # for i in range(r):
        #     element = mat[i * c:(i + 1) * c]
        #     res.append(element)
        # return res
