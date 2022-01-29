# Write a function that takes an unsigned integer and returns the number of '1' bits it has (also known as the
# Hamming weight).

# Note: Note that in some languages, such as Java, there is no unsigned integer type. In this case, the input will be
# given as a signed integer type. It should not affect your implementation, as the integer's internal binary
# representation is the same, whether it is signed or unsigned. In Java, the compiler represents the signed integers
# using 2's complement notation. Therefore, in Example 3, the input represents the signed integer. -3.

# Example 1:
# Input: n = 00000000000000000000000000001011
# Output: 3
# Explanation: The input binary string 00000000000000000000000000001011 has a total of three '1' bits.
# Example 2:
# Input: n = 00000000000000000000000010000000
# Output: 1
# Explanation: The input binary string 00000000000000000000000010000000 has a total of one '1' bit.
# Example 3:
# Input: n = 11111111111111111111111111111101
# Output: 31
# Explanation: The input binary string 11111111111111111111111111111101 has a total of thirty one '1' bits.

# Constraints:
# The input must be a binary string of length 32.
# Follow up: If this function is called many times, how would you optimize it?

# 思路：1. in python, bin() can change a int to binary. In this question, input n is binary. For example:
#         print(n): 11
#         bin(n): '00000000000000000000000000001011' or '0b1011'
#         bin(n).count('1'): 3  It can return the answer, but may not what the interviewer want.
#         int('00000000000000000000000000001011', 2): 11
#      2. From Elements of Programming Interviews in Python, n &= n - 1 deletes the last 1 bit in n.
#         For example, n = 0b1010, then (注意：n &= n-1 等价于 n = n & (n-1))
#         0b1010 & 0b1010 - 0b0001
#         = 0b1010 & 0b1001
#         = 0b1000
#         And you repeat this until there are no ones left. Time complexity is O(k) where k is the
#         number of ones in the binary representation.
#      3. n = 11, '0b1011'
#         n &= n-1, n -> 10, '0b1010'
#         n &= n-1, n -> 8, '0b1000'
#         n &= n-1, n -> 0, '0b0'
#      4. 可以自己推算，二进制里：
#         0001 -> 1
#         0010 -> 2    2^1
#         0011 -> 3
#         0100 -> 4    2^2
#         0101 -> 5
#         0110 -> 6
#         0111 -> 7
#         1000 -> 8    2^3
#         每前进一位1，代表2的高次幂。
#      5. int & int， return二进制下重合的1会表示数字几，比如
#         n = 10, 1010
#         m = 9,  1001
#         n & m -> 8, 1000


def hammingWeight(self, n: int) -> int:
    count = 0
    while n:  # 只要n不是0就继续
        count += 1
        n &= n - 1
    return count

# 也可以不用二进制做
class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        while n > 0:
            n, r = divmod(n,2)
            if r == 1:
                count += 1
        return count
