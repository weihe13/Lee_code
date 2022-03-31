# Description
# Given n unique postive integers, number k (1<=k<=n1<=k<=n) and target.
# Find all possible k integers where their sum is target.

# Example
# Example 1:
# Input:
# array = [1,2,3,4]
# k = 2
# target = 5
# Output:
# [[1,4],[2,3]]
# Explanation:
# 1+4=5,2+3=5
# Example 2:
# Input:
# array = [1,3,4,6]
# k = 3
# target = 8
# Output:
# [[1,3,4]]
# Explanation:
# 1+3+4=8

# 思路：1. 找combination，想到DFS， unique，不用考虑会重复的情况
#      2. 往res中加找到的combination时，要用deep copy, not shallow copy. 否则加进去的reference会一直变。
#      3. 如果用combination+[a[i]]的方式给下层recursion输入combination，则不需要深引用，因为其实combination一直没变
class Solution:
    """
    @param a: an integer array
    @param k: a postive integer <= length(A)
    @param target: an integer
    @return: A list of lists of integer
    """

    def k_sum_i_i(self, a: List[int], k: int, target: int) -> List[List[int]]:
        # write your code here
        res = []
        self.dfs(a, k, target, [], res)
        return res

    def dfs(self, a, k, target, combination, res):
        if k == 0:
            if target == 0:
                res.append(combination.copy()) # 注意要用deep copy
            return

        if target < 0:
            return

        for i in range(len(a)):
            combination.append(a[i])
            a_left = a[i + 1:]
            self.dfs(a_left, k - 1, target - a[i], combination, res)
            combination.pop()


class Solution2:
    """
    @param a: an integer array
    @param k: a postive integer <= length(A)
    @param target: an integer
    @return: A list of lists of integer
    """

    def k_sum_i_i(self, a: List[int], k: int, target: int) -> List[List[int]]:
        # write your code here
        res = []
        self.dfs(a, k, target, [], res)
        return res

    def dfs(self, a, k, target, combination, res):
        if k == 0:
            if target == 0:
                res.append(combination)  # 这里不用deep copy
            return

        if target < 0:
            return

        for i in range(len(a)):
            a_left = a[i + 1:]
            self.dfs(a_left, k - 1, target - a[i], combination + [a[i]], res)