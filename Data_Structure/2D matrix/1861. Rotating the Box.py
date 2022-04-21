# You are given an m x n matrix of characters box representing a side-view of a box. Each cell of the box is one of
# the following:
#
# A stone '#' A stationary obstacle '*' Empty '.' The box is rotated 90 degrees clockwise, causing some of the stones
# to fall due to gravity. Each stone falls down until it lands on an obstacle, another stone, or the bottom of the
# box. Gravity does not affect the obstacles' positions, and the inertia from the box's rotation does not affect the
# stones' horizontal positions.
# It is guaranteed that each stone in box rests on an obstacle, another stone, or the bottom of the box.
# Return an n x m matrix representing the box after the rotation described above.

# Example 1:
# Input: box = [["#",".","#"]]
# Output: [["."],
#          ["#"],
#          ["#"]]
# Example 2:
# Input: box = [["#",".","*","."],
#               ["#","#","*","."]]
# Output: [["#","."],
#          ["#","#"],
#          ["*","*"],
#          [".","."]]
# Example 3:
# Input: box = [["#","#","*",".","*","."],
#               ["#","#","#","*",".","."],
#               ["#","#","#",".","#","."]]
# Output: [[".","#","#"],
#          [".","#","#"],
#          ["#","#","*"],
#          ["#","*","."],
#          ["#",".","*"],
#          ["#",".","."]]

# Constraints:
#
# m == box.length
# n == box[i].length
# 1 <= m, n <= 500
# box[i][j] is either '#', '*', or '.'.

# Logic：1. First thought is rotate the matrix, then find which indexes should change. But the second step is difficult.
#        2. each row in input array is independent and can be processed separately
#         how to process each row:
#         we need to move stones ("#") to empty spaces (".") from left to right
#         since it's only move from left to right, we can iterate from the end of the row
#         and keep in memory the last non-obstacle space where we can move stones
#         and at the end we just need to rotate array.

class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        if not box:
            return []
        m, n = len(box), len(box[0])

        for row in box:
            move_to = n - 1
            for i in range(n - 1, -1, -1):
                if row[i] == '*':
                    move_to = i - 1
                elif row[i] == '#':
                    row[i], row[move_to] = row[move_to], row[i]
                    move_to -= 1

        return list(zip(*box[::-1]))    # Firstly, reverse the rows of the matrix, then zip all the rows.
        # https://stackoverflow.com/questions/8421337/rotating-a-two-dimensional-array-in-python

        # rotate:
        # rotated = []
        # for i in range(n):   # The first column will become first row after rotation, second column will become second
        #                      # row, etc.
        #     rotated.append([])
        #     for j in range(m-1, -1, -1):  # The last row will become first column, second last row will become second
        #                                   # column. So the for loop should iterate from m-1 to 0.
        #         rotated[i].append(box[j][i])
        # return rotated
