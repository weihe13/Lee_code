# Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.
# In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

# Example 1:
# Input: rowIndex = 3
# Output: [1,3,3,1]
# Example 2:
# Input: rowIndex = 0
# Output: [1]
# Example 3:
# Input: rowIndex = 1
# Output: [1,1]

# Constraints:
# 0 <= rowIndex <= 33
# Follow up: Could you optimize your algorithm to use only O(rowIndex) extra space?

# 思路： 1. 关键是要找pattern，比如如果把每一行都左对齐，line[i][j]=line[i-1][j-1]+line[i-1][j]

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        triangle = []
        for row_num in range(rowIndex + 1):
            row = [0 for i in range(row_num + 1)]
            row[0], row[-1] = 1, 1
            for j in range(1, len(row) - 1):
                row[j] = triangle[row_num - 1][j - 1] + triangle[row_num - 1][j]
            triangle.append(row)
        return triangle[rowIndex]

class Solution2:
    def getRow(self, rowIndex: int) -> List[int]:
        res = [1]*(rowIndex+1)
        for i in range(2, rowIndex+1):
            prev = res[0]
            for j in range(1,i):
                tmp = res[j]
                res[j] = prev+res[j]
                prev = tmp
        return res