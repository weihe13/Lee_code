# Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following
# rules: Each row must contain the digits 1-9 without repetition. Each column must contain the digits 1-9 without
# repetition. Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition. Note: A
# Sudoku board (partially filled) could be valid but is not necessarily solvable. Only the filled cells need to be
# validated according to the mentioned rules.

# Example 1: Input: board = [["5","3",".",".","7",".",".",".","."] ,["6",".",".","1","9","5",".",".","."] ,[".","9",
# "8",".",".",".",".","6","."] ,["8",".",".",".","6",".",".",".","3"] ,["4",".",".","8",".","3",".",".","1"] ,["7",
# ".",".",".","2",".",".",".","6"] ,[".","6",".",".",".",".","2","8","."] ,[".",".",".","4","1","9",".",".","5"] ,
# [".",".",".",".","8",".",".","7","9"]] Output: true
#
# Example 2: Input: board = [["8","3",".",".","7",".",".",".",
# "."] ,["6",".",".","1","9","5",".",".","."] ,[".","9","8",".",".",".",".","6","."] ,["8",".",".",".","6",".",".",
# ".","3"] ,["4",".",".","8",".","3",".",".","1"] ,["7",".",".",".","2",".",".",".","6"] ,[".","6",".",".",".",".",
# "2","8","."] ,[".",".",".","4","1","9",".",".","5"] ,[".",".",".",".","8",".",".","7","9"]] Output: false
# Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. Since there are two
# 8's in the top left 3x3 sub-box, it is invalid.

# Constraints:
# board.length == 9
# board[i].length == 9
# board[i][j] is a digit 1-9 or '.'.

# 思路： 1. 判断一行或者一列是否有重复数字出现，第一时间想到hashmap
#       2. 关键是每个3*3的九宫格里也不能有重复数字，这里代表每个九宫格的算法是r//3*3+c//3

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        N = 9

        # Use hash set to record the status
        rows = [set() for _ in range(N)]
        cols = [set() for _ in range(N)]
        boxes = [set() for _ in range(N)]

        for r in range(N):
            for c in range(N):
                val = board[r][c]
                # Check if the position is filled with number
                if val == ".":
                    continue

                # Check the row
                if val in rows[r]:
                    return False
                rows[r].add(val)

                # Check the column
                if val in cols[c]:
                    return False
                cols[c].add(val)

                # Check the box
                idx = (r // 3) * 3 + c // 3
                if val in boxes[idx]:
                    return False
                boxes[idx].add(val)

        return True

# 因为一共9个数，行列和九宫格都是9个位置，所以如果一个数出现过就给该位置赋值1，否则是0，大原理其实一样，了解下这种思路。
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        N = 9

        # Use an array to record the status
        rows = [[0] * N for _ in range(N)]
        cols = [[0] * N for _ in range(N)]
        boxes = [[0] * N for _ in range(N)]

        for r in range(N):
            for c in range(N):
                # Check if the position is filled with number
                if board[r][c] == ".":
                    continue

                pos = int(board[r][c]) - 1

                # Check the row
                if rows[r][pos] == 1:
                    return False
                rows[r][pos] = 1

                # Check the column
                if cols[c][pos] == 1:
                    return False
                cols[c][pos] = 1

                # Check the box
                idx = (r // 3) * 3 + c // 3
                if boxes[idx][pos] == 1:
                    return False
                boxes[idx][pos] = 1

        return True
