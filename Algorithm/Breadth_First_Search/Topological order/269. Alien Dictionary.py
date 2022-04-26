# There is a new alien language that uses the English alphabet. However, the order among the letters is unknown to
# you. You are given a list of strings words from the alien language's dictionary, where the strings in words are
# sorted lexicographically by the rules of this new language. Return a string of the unique letters in the new alien
# language sorted in lexicographically increasing order by the new language's rules. If there is no solution,
# return "". If there are multiple solutions, return any of them. A string s is lexicographically smaller than a
# string t if at the first letter where they differ, the letter in s comes before the letter in t in the alien
# language. If the first min(s.length, t.length) letters are the same, then s is smaller if and only if s.length <
# t.length.

# Example 1:
# Input: words = ["wrt","wrf","er","ett","rftt"]
# Output: "wertf"
# Example 2:
# Input: words = ["z","x"]
# Output: "zx"
# Example 3:
# Input: words = ["z","x","z"]
# Output: ""
# Explanation: The order is invalid, so return "".

# Constraints:
# 1 <= words.length <= 100
# 1 <= words[i].length <= 100
# words[i] consists of only lowercase English letters.

# 思路：1. 字母顺序是一个必须出现在另一个的前面，想到拓扑排序，这里难点是要自己通过words list构建有向图。
#      2. 拓扑排序要注意看是否所有元素都排进去了，如果循环完发现还有点没排进去，说明有circle或者两个点互为prerequest。
#      3. example 3 的情况我们不用做特殊处理，z和x的入度都无法减到0，不会进入循环，最后判断长度不一致return 空。

class Solution:
    def __init__(self):
        pass

    def alienOrder(self, words: List[str]) -> str:
        graph = self.build_graph(words)
        if not graph:  # 如果graph是None，说明words就是invalid
            return ""

        return self.BFS(words, graph)

    def build_graph(self, words):
        graph = {}
        for i in range(len(words)):
            for j in range(len(words[i])):
                if words[i][j] not in graph:
                    graph[words[i][j]] = set()
        # 初始graph的建立不能用defaultdict，否则in_degree的key不全（对于没有入度的点，defaultdict里没有对应的key）
        for i in range(len(words) - 1):
            for j in range(min(len(words[i]), len(words[i + 1]))):
                if words[i][j] != words[i + 1][j]:
                    graph[words[i][j]].add(words[i + 1][j])
                    break  # 找到第一个不相同的字母后，后面的都没有意义了，而且会混乱整个有向图
                # 下面这个判断一定要注意的是j==min-1而不是min，不能忘记len和index的-1关系
                if j == min(len(words[i]), len(words[i + 1])) - 1 and len(words[i]) > len(words[i + 1]):
                    return None
        return graph

    def BFS(self, graph):
        # 对graph中的每一个key，计算入度
        in_degrees = {node: 0 for node in graph}  # 对所有node建立入度，初始为0
        for letter in graph:
            for j in graph[letter]:
                in_degrees[j] += 1

        queue = [node for node in in_degrees if in_degrees[node] == 0]
        heapify(queue)
        res = []
        while queue:
            # 这里不需要分层，因为当取出curr后入度变为0的点，他们和queue中已经存在的点之间是没有pre request的关系的，对于他们先选谁出队
            # 都可以，所以要按照lexicographically的顺序取他们，分层反而会错。
            # 如果multiple solution，return 任意一个就可以，就可以不用heap
            curr = heappop(queue)
            res.append(curr)
            for next_node in graph[curr]:
                in_degrees[next_node] -= 1
                if in_degrees[next_node] == 0:
                    heappush(queue, next_node)

        return "".join(res) if len(res) == len(graph) else ""  # 需要判断是否有circle（非法排序）