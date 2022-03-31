# Given an m x n board of characters and a list of strings words, return all words on the board. Each word must be
# constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically
# neighboring. The same letter cell may not be used more than once in a word.

# Example 1: Input: board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]],
# words = ["oath","pea","eat","rain"] Output: ["eat","oath"] Example 2: Input: board = [["a","b"],["c","d"]],
# words = ["abcb"] Output: []

# Constraints:
# m == board.length
# n == board[i].length
# 1 <= m, n <= 12
# board[i][j] is a lowercase English letter.
# 1 <= words.length <= 3 * 104
# 1 <= words[i].length <= 10
# words[i] consists of lowercase English letters.
# All the strings of words are unique.

# 思路： 1. 看到图，很容易想到DFS和backtrack结合
#       2. 核心是优化time complexity，每次搜索时，不需要把整个图遍历一遍，当初始点不是words中单词的prefix时就可以跳过了，因此想到建立
#       一个辅助数据结构来帮助判断是否继续搜索。最简单的是set，但set难以进一步优化。
#       3. prefix的问题，想到trie。trie比set好在，如果找到了apple，而e下面没有children了，就可以把e删掉，同理找到appl后l也可能删掉，
#       最后prefix的集合会越来越小，跳过的搜索点就越来越多。如果用set，找到app后不能删除app，因为可能有apple还没找到，如果把'app'删了，
#       之后搜索时形成app后发现不在prefix中，会跳过，就找不到apple了。但保留app，在找到一次app后还会继续找app，会做很多无用功。
#       4. 另一个细节是利用IS_WORD的标记去重，找到一个word后就把'$'删掉，后面在找到该word也不会append到res中。

class Solution1:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        if not board or len(board[0]) == 0:
            return []

        IS_WORD = '$'
        trie = {}
        for word in words:
            node = trie
            for letter in word:
                node = node.setdefault(letter, {}) # node指向trie['letter']对应的children {}，
                # 或者新建trie['letter']并对应{}, 将node指向该新建{}所在位置。
            node[IS_WORD] = word   # 将'$' word pairs保存在该word最后一个字母的children {}中

        res = []
        n_row, n_col = len(board), len(board[0])
        for i in range(n_row):
            for j in range(n_col):
                if board[i][j] in trie:
                    self.search(i, j, board, trie, res)
        return res

    def search(self, r, c, board, node, res):
        IS_WORD = '$'
        letter = board[r][c]            # letter和node同时前进，currNode是当前letter在node中对应的children node
        currNode = node[letter]
        if IS_WORD in currNode:
            res.append(currNode[IS_WORD])
            currNode.pop(IS_WORD)  # 防止加重复的word
        if not currNode:  # 如果找到的是prefix，currNode除了$还有其他东西
            node.pop(letter)
            return

        board[r][c] = '#'
        for delta_x, delta_y in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            new_r, new_c = r + delta_x, c + delta_y
            if self.in_board(new_r, new_c, board) and board[new_r][new_c] in currNode:
                self.search(new_r, new_c, board, currNode, res)
        board[r][c] = letter

    def in_board(self, r, c, board):
        return 0 <= r < len(board) and 0 <= c < len(board[0])

# trie 例子：
# trie = {}
# words=['hewei','heweiye','apple']
# for word in words:
#     node = trie
#     for letter in word:
#                 # retrieve the next node; If not found, create a empty node.
#         node = node.setdefault(letter, {})
#     node['$'] = word
# 结果:
# node : {'$': 'apple'}
# trie: {'h': {'e': {'w': {'e': {'i': {'$': 'hewei', 'y': {'e': {'$': 'heweiye'}}}}}}},
#  'a': {'p': {'p': {'l': {'e': {'$': 'apple'}}}}}}


# 答案写法：
class Solution2:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        WORD_KEY = '$'

        trie = {}
        for word in words:
            node = trie # node指向trie指向的位置
            for letter in word:
                # retrieve the next node; If not found, create a empty node.
                node = node.setdefault(letter, {})  # node指向trie['letter']对应的children {}，
                # 或者新建trie['letter']并对应{}, 将node指向该新建{}所在位置。
            # mark the existence of a word in trie node
            node[WORD_KEY] = word

        rowNum = len(board)
        colNum = len(board[0])

        matchedWords = []

        def backtracking(row, col, parent):

            letter = board[row][col]    # letter和node同时前进
            currNode = parent[letter]

            # check if we find a match of word
            word_match = currNode.pop(WORD_KEY, False) # 这步pop很重要，防止加入重复答案
            if word_match:
                # also we removed the matched word to avoid duplicates,
                #   as well as avoiding using set() for results.
                matchedWords.append(word_match)

            # Before the EXPLORATION, mark the cell as visited
            board[row][col] = '#'

            # Explore the neighbors in 4 directions, i.e. up, right, down, left
            for (rowOffset, colOffset) in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                newRow, newCol = row + rowOffset, col + colOffset
                if newRow < 0 or newRow >= rowNum or newCol < 0 or newCol >= colNum:
                    continue
                if not board[newRow][newCol] in currNode:
                    continue
                backtracking(newRow, newCol, currNode)

            # End of EXPLORATION, we restore the cell
            board[row][col] = letter

            # Optimization: incrementally remove the matched leaf node in Trie.
            if not currNode:       # 如果pop('$')后currNode是{},说明已经是leaf node，可以pop掉了，提升time complexity
                parent.pop(letter)

        for row in range(rowNum):
            for col in range(colNum):
                # starting from each of the cells
                if board[row][col] in trie:
                    backtracking(row, col, trie)

        return matchedWords