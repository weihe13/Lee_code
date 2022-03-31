# Given an array of distinct integers candidates and a target integer target, return a list of all unique
# combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.
# The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the
# frequency of at least one of the chosen numbers is different. It is guaranteed that the number of unique
# combinations that sum up to target is less than 150 combinations for the given input.

# Example 1:
# Input: candidates = [2,3,6,7], target = 7
# Output: [[2,2,3],[7]]
# Explanation:
# 2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
# 7 is a candidate, and 7 = 7.
# These are the only two combinations.
# Example 2:
# Input: candidates = [2,3,5], target = 8
# Output: [[2,2,2,2],[2,3,3],[3,5]]
# Example 3:
# Input: candidates = [2], target = 1
# Output: []

# Constraints:
# 1 <= candidates.length <= 30
# 1 <= candidates[i] <= 200
# All elements of candidates are distinct.
# 1 <= target <= 500

# 思路： 1. 找所有可能组合，想到DFS
#       2. 不能有重复组合，要先排序，recursion完一个数字，跳到下一个数字时，如果一样就continue
#       3. 因为一个数可以使用多次，向下层recursion输入参数时不能剔除本层新加的数字，但也不能包含之前已经实验过的数字，否则会重复，所以向
#       下层输入的参数时candidates[i:]，即包含本层新加的数，但不包含之前已经实验过的数。

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        self.dfs(candidates, target, [], res)
        return res

    def dfs(self, candidates, target, combination, res):
        if target == 0:
            res.append(combination)
            return

        if target < 0:
            return

        for i in range(len(candidates)):
            if i > 0 and candidates[i] == candidates[i - 1]:
                continue
            self.dfs(candidates[i:], target - candidates[i], combination + [candidates[i]], res)

# 优化：先去重再sort，recursion时如果target已经小于当前num就可以break了。
class Solution2:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates_sorted = sorted(list(set(candidates)))
        self.dfs(candidates_sorted, target, [], res)
        return res

    def dfs(self, candidates, target, combination, res):
        if target == 0:
            res.append(combination)
            return

        if target < 0:
            return

        for i in range(len(candidates)):
            if target < candidates[i]:
                break
            self.dfs(candidates[i:], target - candidates[i], combination + [candidates[i]], res)