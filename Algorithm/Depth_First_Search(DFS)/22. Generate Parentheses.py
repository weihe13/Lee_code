# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
#
#
#
# Example 1:
#
# Input: n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]
# Example 2:
#
# Input: n = 1
# Output: ["()"]
#
#
# Constraints:
#
# 1 <= n <= 8

# 思路：1. dfs: if len == 2n, return. when dfs, consider add'(' first, then backtrack, consider add')'.
#      2. The key of the dfs function here is there are two times of recursion in one dfs function. if left < n,
#         recursion, then pop, then another recursion. 

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []

        def dfs(path, left, right):
            if len(path) == 2 * n:
                ans.append("".join(path))

            if left < n:
                path.append("(")
                dfs(path, left + 1, right)
                path.pop()

            if right < left:
                path.append(")")
                dfs(path, left, right + 1)
                path.pop()

        dfs([], 0, 0)
        return ans
