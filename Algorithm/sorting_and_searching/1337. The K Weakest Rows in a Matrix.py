# You are given an m x n binary matrix mat of 1's (representing soldiers) and 0's (representing civilians). The
# soldiers are positioned in front of the civilians. That is, all the 1's will appear to the left of all the 0's in
# each row.
#
# A row i is weaker than a row j if one of the following is true:
# The number of soldiers in row i is less than the number of soldiers in row j.
# Both rows have the same number of soldiers and i < j.
# Return the indices of the k weakest rows in the matrix ordered from weakest to strongest.

# Example 1:
# Input: mat =
# [[1,1,0,0,0],
#  [1,1,1,1,0],
#  [1,0,0,0,0],
#  [1,1,0,0,0],
#  [1,1,1,1,1]],
# k = 3
# Output: [2,0,3]
# Explanation:
# The number of soldiers in each row is:
# - Row 0: 2
# - Row 1: 4
# - Row 2: 1
# - Row 3: 2
# - Row 4: 5
# The rows ordered from weakest to strongest are [2,0,3,1,4].
# Example 2:
# Input: mat =
# [[1,0,0,0],
#  [1,1,1,1],
#  [1,0,0,0],
#  [1,0,0,0]],
# k = 2
# Output: [0,2]
# Explanation:
# The number of soldiers in each row is:
# - Row 0: 1
# - Row 1: 4
# - Row 2: 1
# - Row 3: 1
# The rows ordered from weakest to strongest are [0,2,3,1].

# Constraints:
#
# m == mat.length
# n == mat[i].length
# 2 <= n, m <= 100
# 1 <= k <= m
# matrix[i][j] is either 0 or 1.

# 思路: 1. First thought is, calculate the sum for each row, then add sum, row pairs into res, then sort res in ascending
#         order. It will sorted with the sum from lowest to highest. If the sum is same, then compare row index.
#      2. The time complexity will be O(MN+NlogN), because sum() for each row takes O(m), n rows.
#      3. improve: use a for loop to check each column, if we meet 0, add the row index into the res. Because the inner
#         loop is from row index 0 to row index n-1, so if two rows both meet 0, smaller row index will add first.
#      4. The time complexity will be O(nk). But one thing we need to pay attention, if k == n, or several rows do not
#         have 0, then the length of res may smaller than k. In is case, we need use another for loop to check if a row
#         is in res. If not, add it to the res. Similar as before, smaller row index will add first.

class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        res = []
        for row in range(len(mat)):
            num_soldier = sum(mat[row])
            res.append((num_soldier, row))
        res = [i[1] for i in sorted(res)]
        return res[:k]


class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        seen = set()
        weakest = []
        i = 0
        while i < len(mat[0]):
            for j in range(len(mat)):
                # if len(seen) == k:  # for the loop in column i, also need to check whether already added k element.
                #     break           # Otherwise, we need to extract the first k element in weakest.
                if mat[j][i] == 0 and j not in seen:
                    weakest.append((i, j))
                    seen.add(j)
            if len(seen) >= k:
                weakest = weakest[:k]
                break
            i += 1

        while len(weakest) < k:
            for i in range(len(mat)):
                if i not in seen and len(weakest) < k:
                    weakest.append((sum(mat[i]), i))
        return [row[1] for row in weakest]