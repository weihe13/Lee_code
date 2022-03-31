# You are given an array of variable pairs equations and an array of real numbers values, where equations[i] = [Ai,
# Bi] and values[i] represent the equation Ai / Bi = values[i]. Each Ai or Bi is a string that represents a single
# variable. You are also given some queries, where queries[j] = [Cj, Dj] represents the jth query where you must find
# the answer for Cj / Dj = ?. Return the answers to all queries. If a single answer cannot be determined, return -1.0.

# Note: The input is always valid. You may assume that evaluating the queries will not result in division by zero and
# that there is no contradiction.

# Example 1:
# Input: equations = [["a","b"],["b","c"]], values = [2.0,3.0], queries = [["a","c"],["b","a"],["a","e"],["a","a"],
# ["x","x"]]
# Output: [6.00000,0.50000,-1.00000,1.00000,-1.00000]
# Explanation:
# Given: a / b = 2.0, b / c = 3.0
# queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ?
# return: [6.0, 0.5, -1.0, 1.0, -1.0 ]
# Example 2:
# Input: equations = [["a","b"],["b","c"],["bc","cd"]], values = [1.5,2.5,5.0], queries = [["a","c"],["c","b"],
# ["bc","cd"],["cd","bc"]]
# Output: [3.75000,0.40000,5.00000,0.20000]
# Example 3:
# Input: equations = [["a","b"]], values = [0.5], queries = [["a","b"],["b","a"],["a","c"],["x","y"]]
# Output: [0.50000,2.00000,-1.00000,-1.00000]

# Constraints:
# 1 <= equations.length <= 20
# equations[i].length == 2
# 1 <= Ai.length, Bi.length <= 5
# values.length == equations.length
# 0.0 < values[i] <= 20.0
# 1 <= queries.length <= 20
# queries[i].length == 2
# 1 <= Cj.length, Dj.length <= 5
# Ai, Bi, Cj, Dj consist of lower case English letters and digits.

# 思路： 1. 想到DFS，难想到的是先构建一张图，然后在图上DFS
#       2. 构建图的方式：graph = defaultdict(defaultdict),key代表node，value代表weight

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(defaultdict)
        # 1. 造图
        for (divident, divisor), value in zip(equations, values):
            graph[divident][divisor] = value
            graph[divisor][divident] = 1 / value

        # 2. DFS
        res = []
        for (divident, divisor) in queries:
            if divident not in graph or divisor not in graph:
                ret = -1.0
            elif divident == divisor:
                ret = 1.0
            else:
                visited = set()
                ret = self.dfs(graph, divident, divisor, 1, visited)
            res.append(ret)
        return res

    def dfs(self, graph, currnode, targetnode, acc_value, visited):
        visited.add(currnode)
        ret = -1.0
        if targetnode in graph[currnode]:
            ret = acc_value * graph[currnode][targetnode]
        else:
            for neighbor in graph[currnode]:
                if neighbor in visited:
                    continue
                ret = self.dfs(graph, neighbor, targetnode, acc_value * graph[currnode][neighbor], visited)
                if ret != -1.0:
                    break
        visited.remove(currnode)
        return ret