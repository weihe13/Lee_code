# A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and retrieve keys in
# a dataset of strings. There are various applications of this data structure, such as autocomplete and spellchecker.

# Implement the Trie class:
# Trie() Initializes the trie object. void insert(String word) Inserts the string word into
# the trie. boolean search(String word) Returns true if the string word is in the trie (i.e., was inserted before),
# and false otherwise. boolean startsWith(String prefix) Returns true if there is a previously inserted string word
# that has the prefix prefix, and false otherwise.

# Example 1:
# Input
# ["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
# [[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
# Output
# [null, null, true, false, true, null, true]
# Explanation
# Trie trie = new Trie();
# trie.insert("apple");
# trie.search("apple");   // return True
# trie.search("app");     // return False
# trie.startsWith("app"); // return True
# trie.insert("app");
# trie.search("app");     // return True

# Constraints:
# 1 <= word.length, prefix.length <= 2000
# word and prefix consist only of lowercase English letters.
# At most 3 * 104 calls in total will be made to insert, search, and startsWith.

# 思路：1. 按Terence的思路，add和search的method都加上参数i，用recursion去做，当i==len(word)时return
#      2. 只输入参数word，对word进行一次for循环，所以recursion的本质是一种优雅的不确定循环层数的循环。

class TrieNode:
    def __init__(self):
        self.isword = False
        self.edges = {}

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        p = self.root  # insert search starsWith每一个都是先从root开始
        for letter in word:
            if letter not in p.edges:
                p.edges[letter] = TrieNode()
            p = p.edges[letter]
        p.isword = True   # 表示这个word存在

    def search(self, word: str) -> bool:
        p = self.root
        for letter in word:
            if letter not in p.edges:
                return False
            else:
                p = p.edges[letter]
        return p.isword   # 循环完不代表这个word一定存在，可能是prefix

    def startsWith(self, prefix: str) -> bool:
        p = self.root
        for letter in prefix:
            if letter not in p.edges:
                return False
            else:
                p = p.edges[letter]
        return True      # 只要循环完了，就说明是startwith


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)