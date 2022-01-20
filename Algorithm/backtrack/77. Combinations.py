# Given two integers n and k, return all possible combinations of k numbers out of the range [1, n].
# You may return the answer in any order.

# Example 1:
# Input: n = 4, k = 2
# Output:
# [
#   [2,4],
#   [3,4],
#   [2,3],
#   [1,2],
#   [1,3],
#   [1,4],
# ]
# Example 2:
# Input: n = 1, k = 1
# Output: [[1]]

# Constraints:
# 1 <= n <= 20
# 1 <= k <= n

# 思路： Backtracking is an algorithm for finding all solutions by exploring all potential candidates. If the solution
# candidate turns to be not a solution (or at least not the last one), backtracking algorithm discards it by making
# some changes on the previous step, i.e. backtracks and then try again.

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def backtrack(first=1, curr=[]):
            # if the combination is done
            if len(curr) == k:
                output.append(curr[:]) # 注意，这里如果append(curr)会加空list
            for i in range(first, n + 1):
                # add i into the current combination
                curr.append(i)
                # use next integers to complete the combination
                backtrack(i + 1, curr)
                # backtrack
                curr.pop() # 这里指拿走了一位数字（当前循环的i），不是整个combination

        output = []
        backtrack()
        return output
