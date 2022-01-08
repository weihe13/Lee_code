# Given an m x n grid of characters board and a string word, return true if word exists in the grid. The word can be
# constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically
# neighboring. The same letter cell may not be used more than once.

# Example 1:
# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
# Output: true
# Example 2:
# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
# Output: true
# Example 3:
# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
# Output: false
#
#
# Constraints:
# m == board.length
# n = board[i].length
# 1 <= m, n <= 6
# 1 <= word.length <= 15
# board and word consists of only lowercase and uppercase English letters.
# Follow up: Could you use search pruning to make your solution faster with a larger board?

# 思路：因为不能重复用，所以每次找到一个就标记成不是alphabet的字符，保证不会搜索到，如果最后没找到再改回来。

class Solution: # 这个思路和leecode答案完全一样，但是快一些，不知原因
    def exist(self, board: List[List[str]], word: str) -> bool:

        if not board:
            return False

        def dfs(i, j, p):
            if p == len(word): # 如果p==len(word)，说明0到p-1都找到了
                return True
            if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]) or board[i][j] != word[p]:
                return False
            board[i][j] = "" # 没有return fasle，说明board[i][j] == word[p],标记成""防止重复使用
            if dfs(i + 1, j, p + 1) or dfs(i - 1, j, p + 1) or dfs(i, j + 1, p + 1) or dfs(i, j - 1, p + 1):
                return True
            board[i][j] = word[p] # 没找到全部，往回退的时候再改回来

        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i, j, 0):
                    return True
        return False