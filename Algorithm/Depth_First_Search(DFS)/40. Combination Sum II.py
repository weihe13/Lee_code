# Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in
# candidates where the candidate numbers sum to target. Each number in candidates may only be used once in the
# combination.

# Note: The solution set must not contain duplicate combinations.
# Example 1:
# Input: candidates = [10,1,2,7,6,1,5], target = 8
# Output:
# [
# [1,1,6],
# [1,2,5],
# [1,7],
# [2,6]
# ]
# Example 2:
# Input: candidates = [2,5,2,1,2], target = 5
# Output:
# [
# [1,2,2],
# [5]
# ]

# Constraints:
# 1 <= candidates.length <= 100
# 1 <= candidates[i] <= 50
# 1 <= target <= 30

# 思路： 1. 要求找到所有可能combination，想到DFS
#       2. 由于不能有重复，考虑到有可能有相同的数字形成相同组合，先sort，遇到重复数字就continue

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        self.dfs(candidates, target, [], res)
        return res

    def dfs(self, candidates, target, combination, res):
        if target == 0:
            res.append(combination)  # 如果用backtrack的写法，这里要append(combination.copy())
            return

        if target < 0:
            return

        for i in range(len(candidates)):
            if i > 0 and candidates[i] == candidates[i - 1]:
                continue
            candidates_left = candidates[i + 1:]
            # combination.append(candidates[i])
            self.dfs(candidates_left, target - candidates[i], combination + [candidates[i]], res)
            # combination.pop()
