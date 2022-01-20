# Given an integer n, return true if it is a power of two. Otherwise, return false.
# An integer n is a power of two, if there exists an integer x such that n == 2x.

# Example 1:
# Input: n = 1
# Output: true
# Explanation: 20 = 1
# Example 2:
# Input: n = 16
# Output: true
# Explanation: 24 = 16
# Example 3:
#
# Input: n = 3
# Output: false

# Constraints:
# -231 <= n <= 231 - 1

# 思路：1. 关键是要思考清楚，如果是2的幂，那么每次除以2后必须余数是0，最后一次的商一定是1。
#      2. 二进制的思路，~x可以对二进制数的每一位取反，比如
#         x: 000101
#         ~x: 111010
#         在python里对于int n，~n+1 = -n
#         找到的规律是 如果 n&(-n)==n,那么n就是2的power

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        while n % 2 == 0:
            n /= 2

        return n == 1

# 利用二进制的思路
class Solution2(object):
    def isPowerOfTwo(self, n):
        if n == 0:
            return False
        return n & (-n) == n
