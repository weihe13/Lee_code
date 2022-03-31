# A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words
# beginWord -> s1 -> s2 -> ... -> sk such that: Every adjacent pair of words differs by a single letter. Every si for
# 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList. sk == endWord Given two words,
# beginWord and endWord, and a dictionary wordList, return the number of words in the shortest transformation
# sequence from beginWord to endWord, or 0 if no such sequence exists.

# Example 1:
# Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
# Output: 5
# Explanation: One shortest transformation sequence is "hit" -> "hot" -> "dot" -> "dog" -> cog", which is 5 words long.
# Example 2:
# Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
# Output: 0
# Explanation: The endWord "cog" is not in wordList, therefore there is no valid transformation sequence.

# Constraints:
# 1 <= beginWord.length <= 10
# endWord.length == beginWord.length
# 1 <= wordList.length <= 5000
# wordList[i].length == beginWord.length
# beginWord, endWord, and wordList[i] consist of lowercase English letters.
# beginWord != endWord
# All the words in wordList are unique.

# 思路：1. 最短路径想到BFS，首先要构建解空间，两种构建思路：
#        1）word 对应每一个只改动一个的词，后面再判断这些改变后词是否在wordlist中，时间复杂度26(nl^2)
#        2) 把每个word改动一个字母用word[:i]+'*'+word[i+1:]表示，以改动后的为key，改动前的word为value，时间复杂度nl^2,但空间占用更多


class Solution1:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        queue = collections.deque([beginWord])
        distance = {beginWord: 1}
        while queue:
            for _ in range(len(queue)):
                word = queue.popleft()
                if word == endWord:
                    return distance[word]
                for next_word in self.get_next_word(word, wordList):
                    if next_word in distance:
                        continue
                    queue.append(next_word)
                    distance[next_word] = distance[word] + 1
        return 0

    def get_next_word(self, word, wordlist):
        wordlist = set(wordlist)
        next_words = []
        for i in range(len(word)):
            word_left, word_right = word[:i], word[i + 1:]
            for char in 'abcdefghijklmnopqrstuvwxyz':
                if word[i] == char:
                    continue
                new_word = word_left + char + word_right
                if new_word in wordlist:
                    next_words.append(new_word)
        return next_words


class Solution2:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        all_possible_words = self.build_map(endWord, wordList)

        queue = collections.deque([beginWord])
        visited = {beginWord: 1}
        while queue:
            currword = queue.popleft()
            if currword == endWord:
                return visited[currword]
            for i in range(len(endWord)):
                intermediate_word = currword[:i] + "*" + currword[i + 1:]
                for word in all_possible_words[intermediate_word]:
                    if word in visited:
                        continue
                    queue.append(word)
                    visited[word] = visited[currword] + 1
        return 0

    def build_map(self, endWord, wordList):
        L = len(endWord)
        all_possible_words = defaultdict(list)
        for word in wordList:
            for i in range(L):
                all_possible_words[word[:i] + '*' + word[i + 1:]].append(word)
        return all_possible_words
