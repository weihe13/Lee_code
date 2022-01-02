# Given an integer numRows, return the first numRows of Pascal's triangle.
# In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

# Example 1:
# Input: numRows = 5
# Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
# Example 2:
# Input: numRows = 1
# Output: [[1]]

# Constraints:
# 1 <= numRows <= 30

# 思路：1. 看成一个dynamic_programming 的问题，有：
#         base case: The value at the beginning or end of a row is always 1;
#         Recurrence relationL: each number is the sum of the two numbers directly above it.
#      2. 写的时候注意：1) 把每一行左对齐，去思考上一行index和下一行的关系：
#                     row[j] = triangle[row_num-1][j-1] + triangle[row_num-1][j]
#                     2) row_num starts from 0，while len(row) start from 1.
#                     3) row 只是其中一行， triangle才是整个三角，别想岔了
#                     4） row = [0 for i in range(row_num+1)] also works.

class Solution:
    def generate(self, num_rows: int) -> List[List[int]]:
        triangle = []

        for row_num in range(num_rows):
            # The first and last row elements are always 1.
            row = [None for _ in range(row_num + 1)]
            row[0], row[-1] = 1, 1

            # Each triangle element is equal to the sum of the elements
            # above-and-to-the-left and above-and-to-the-right.
            for j in range(1, len(row) - 1):
                row[j] = triangle[row_num - 1][j - 1] + triangle[row_num - 1][j]

            triangle.append(row)

        return triangle
