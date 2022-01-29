# Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix. This matrix has
# the following properties: Integers in each row are sorted in ascending from left to right. Integers in each column
# are sorted in ascending from top to bottom.

# Example 1:
# Input: matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 5
# Output: true
# Example 2:
# Input: matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 20
# Output: false

# Constraints:
# m == matrix.length
# n == matrix[i].length
# 1 <= n, m <= 300
# -109 <= matrix[i][j] <= 109
# All the integers in each row are sorted in ascending order.
# All the integers in each column are sorted in ascending order.
# -109 <= target <= 109

# 思路：1. 硬找，利用if target in row 一行行判断
#      2. 从坐下角开始，如果大于target就row-1，因为右边的一定更大；如果小于target就col+1,因为左边的一定更小。巧妙之处在于如果从0，0位置
#         开始，无法判断是row+1还是col+1，从左下角开始，能固定下一步。但是前提是从左到右从上到下从小变大。

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix:
            if target in row:
                return True
        return False


# Time complexity : O(nm) Becase we perform a constant time operation for each element of an n\times mn×m element
# matrix, the overall time complexity is equal to the size of the matrix.
#
# Space complexity : O(1) The brute force approach does not allocate more additional space than a handful of
# pointers, so the memory footprint is constant.

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # an empty matrix obviously does not contain `target` (make this check
        # because we want to cache `width` for efficiency's sake)
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        # cache these, as they won't change.
        height = len(matrix)
        width = len(matrix[0])
        # start our "pointer" in the bottom-left
        row = height - 1
        col = 0
        while col < width and row >= 0:
            if matrix[row][col] > target:
                row -= 1
            elif matrix[row][col] < target:
                col += 1
            else:  # found it
                return True
        return False
# Time: O(m+n) The key to the time complexity analysis is noticing that, on every iteration (during which we do not
# return true) either row or col is is decremented/incremented exactly once. Because row can only be decremented mm
# times and col can only be incremented nn times before causing the while loop to terminate, the loop cannot run for
# more than n+mn+m iterations. Because all other work is constant, the overall time complexity is linear in the sum
# of the dimensions of the matrix.
# Space complexity : O(1)
# Because this approach only manipulates a few pointers, its memory footprint is constant.
