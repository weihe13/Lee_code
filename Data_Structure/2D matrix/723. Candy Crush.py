# This question is about implementing a basic elimination algorithm for Candy Crush.
#
# Given an m x n integer array board representing the grid of candy where board[i][j] represents the type of candy. A
# value of board[i][j] == 0 represents that the cell is empty.
#
# The given board represents the state of the game following the player's move. Now, you need to restore the board to
# a stable state by crushing candies according to the following rules:
#
# If three or more candies of the same type are adjacent vertically or horizontally, crush them all at the same time
# - these positions become empty. After crushing all candies simultaneously, if an empty space on the board has
# candies on top of itself, then these candies will drop until they hit a candy or bottom at the same time. No new
# candies will drop outside the top boundary. After the above steps, there may exist more candies that can be
# crushed. If so, you need to repeat the above steps. If there does not exist more candies that can be crushed (i.e.,
# the board is stable), then return the current board. You need to perform the above rules until the board becomes
# stable, then return the stable board.

# Example 1:

# Input: board = [[110,5,112,113,114],[210,211,5,213,214],[310,311,3,313,314],[410,411,412,5,414],[5,1,512,3,3],[610,
# 4,1,613,614],[710,1,2,713,714],[810,1,2,1,1],[1,1,2,2,2],[4,1,4,4,1014]] Output: [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,
# 0],[110,0,0,0,114],[210,0,0,0,214],[310,0,0,113,314],[410,0,0,213,414],[610,211,112,313,614],[710,311,412,613,714],
# [810,411,512,713,1014]] Example 2:
#
# Input: board = [[1,3,5,5,2],[3,4,3,3,1],[3,2,4,5,2],[2,4,4,5,5],[1,4,4,1,1]]
# Output: [[1,3,0,0,0],[3,4,0,5,2],[3,2,0,3,1],[2,4,0,5,2],[1,4,3,1,1]]
#
#
# Constraints:
#
# m == board.length
# n == board[i].length
# 3 <= m, n <= 50
# 1 <= board[i][j] <= 2000

# Logic: 1. First intuition is DFS+fall down, then recursion call the function. Seems work, but cannot pass some corner
#           case.
#        2. iterate to find the cells need to eliminate. Then fall down. Trick is check the abs value
#        3. In the fall down function, can use two pointers: One pointer point at the index that wait to set a new
#        value, the other pointer is finding the next non-zero value to add.

class Solution:
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        res = []
        seen = set()
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] != 0 and (i, j) not in seen:
                    seen.add((i, j))
                    for x, y in directions:
                        self.dfs(board, i, j, x, y, [(i, j)], board[i][j], res, seen)

        # set new 0:
        for adjacent in res:
            for x, y in adjacent:
                board[x][y] = 0

        # fall down the elements(two pointers)
        m, n = len(board), len(board[0])
        for j in range(n):
            row_index = m - 1
            for i in range(m - 1, -1, -1):
                if board[i][j] > 0:
                    board[row_index][j] = board[i][j]
                    row_index -= 1
            while row_index >= 0:
                board[row_index][j] = 0
                row_index -= 1
        if res != []:
            self.candyCrush(board)
        return board

    def dfs(self, board, i, j, x, y, curr, target, res, seen):
        new_x, new_y = i + x, j + y
        if 0 <= new_x < len(board) and 0 <= new_y < len(board[0]) and board[new_x][new_y] == target:
            self.dfs(board, new_x, new_y, x, y, curr + [(new_x, new_y)], target, res, seen)
        else:
            if len(curr) >= 3:
                res.append(curr[:])
                for cell in curr:
                    seen.add(cell)


class Solution2:
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        m, n = len(board), len(board[0])
        crushed = False
        # horizontal crushed
        for i in range(m):
            for j in range(n - 2):
                if board[i][j] == 0:
                    continue
                v = abs(board[i][j])
                if v == abs(board[i][j + 1]) == abs(board[i][j + 2]):
                    board[i][j] = board[i][j + 1] = board[i][j + 2] = -v
                    crushed = True
        # vertical crushed
        for i in range(m - 2):
            for j in range(n):
                if board[i][j] == 0:
                    continue
                v = abs(board[i][j])
                if v == abs(board[i + 1][j]) == abs(board[i + 2][j]):
                    board[i][j] = board[i + 1][j] = board[i + 2][j] = -v
                    crushed = True
        # gravity
        if crushed:
            for j in range(n):
                row_index = m - 1  # set move_to before inner loop
                for i in range(m - 1, -1, -1):
                    if board[i][j] > 0:
                        board[row_index][j] = board[i][j]
                        row_index -= 1
                while row_index >= 0:
                    board[row_index][j] = 0
                    row_index -= 1
        return self.candyCrush(board) if crushed else board
