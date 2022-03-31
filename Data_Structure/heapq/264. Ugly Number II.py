# An ugly number is a positive integer whose prime factors are limited to 2, 3, and 5.
# Given an integer n, return the nth ugly number.

# Example 1:
# Input: n = 10
# Output: 12
# Explanation: [1, 2, 3, 4, 5, 6, 8, 9, 10, 12] is the sequence of the first 10 ugly numbers.
# Example 2:
# Input: n = 1
# Output: 1
# Explanation: 1 has no prime factors, therefore all of its prime factors are limited to 2, 3, and 5.

# Constraints:
# 1 <= n <= 1690

# 思路： 1. 这题不能用三叉树tree做，因为大小关系不好判断，也存在重复
#       2. 取的是第n个最小的数，想到heapq

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        heap = [1]
        seen = set([1])

        for _ in range(n):
            smallest = heapq.heappop(heap)  # 这里第一次取最小的数不用heapify，因为只有一个数
            for prime in [2, 3, 5]:
                new_num = smallest * prime
                if new_num not in seen:
                    heapq.heappush(heap, new_num)
                    seen.add(new_num)   # 每往heap中加一个数就要记得往seen中add
        return smallest