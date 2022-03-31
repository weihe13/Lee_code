# The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each
# other. Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the answer in any
# order. Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both
# indicate a queen and an empty space, respectively.

# Example 1:
# Input: n = 4
# Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
# Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above
# Example 2:
# Input: n = 1
# Output: [["Q"]]
#
# Constraints:
# 1 <= n <= 9

# 思路：1. 这是一个排列问题，return的[[".Q..","...Q","Q...","..Q."]]实际上是[2,4,1,3]，表示每行的Q应该出现在哪一列，想到DFS
#      2. 时间复杂度：九章：O(M*N^2)，M是方案数，因为每个方案要搜索N^2个位置, N^2是构造方案（也就是画棋盘）的时间
#                   自己理解以及leecode：O(N!)，因为每次搜索时类似一个方案数，可选择的位置是N,N-2,N-4
#         空间复杂度: O(N^2)


class Solution:
    def __init__(self):
        pass

    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        self.search(n, [], res)
        return res

    def search(self, n, cols, res):  # cols表示目前已经记录的每一行的Q的col index
        row = len(cols)
        if row == n:
            self.add_to_res(n, cols, res)
            return
        else:
            for col in range(n):
                if not self.isvalid(n, cols, row, col):
                    continue
                self.search(n, cols + [col], res)

    def isvalid(self, n, cols, row, col):
        for r, c in enumerate(cols):
            if c == col:
                return False
            elif r - row == c - col or r + c == row + col:  # 分别表示做对角线和右对角线
                return False
        return True

    def add_to_res(self, n, cols, res):
        board = []
        for i, col in enumerate(cols):
            add_row = ["Q" if j == col else "." for j in range(n)]  # 生成每一行的str
            board.append("".join(add_row))
        res.append(board)