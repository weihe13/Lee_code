# Reverse bits of a given 32 bits unsigned integer.

# Note: Note that in some languages, such as Java, there is no unsigned integer type. In this case, both input and
# output will be given as a signed integer type. They should not affect your implementation, as the integer's
# internal binary representation is the same, whether it is signed or unsigned. In Java, the compiler represents the
# signed integers using 2's complement notation. Therefore, in Example 2 above, the input represents the signed
# integer -3 and the output represents the signed integer -1073741825.

# Example 1: Input: n = 00000010100101000001111010011100 Output:    964176192 (00111001011110000010100101000000)
# Explanation: The input binary string 00000010100101000001111010011100 represents the unsigned integer 43261596,
# so return 964176192 which its binary representation is 00111001011110000010100101000000.
# Example 2: Input: n =
# 11111111111111111111111111111101 Output:   3221225471 (10111111111111111111111111111111) Explanation: The input
# binary string 11111111111111111111111111111101 represents the unsigned integer 4294967293, so return 3221225471
# which its binary representation is 10111111111111111111111111111111.

# Constraints:
# The input must be a binary string of length 32

# Follow up: If this function is called many times, how would you optimize it?

# 思路： 1. reverse the bits one by one.注意二进制是可以和十进制一样进行加减运算的。比如：
#       111 + 11 = 1010
#        7  +  3 =  10
#       2. >> 表示往右移一定位数，右边的移动的位数直接删掉了(相当于从左侧推入0, <<表示从右侧推入0)。比如：
#        10 >> 2 = 2
#       1010 >> 2 = 10
#       3. 对于二进制数，从右往左每一位的位置序号就表示2的几次方，比如：
#        1, 2的0次方； 10, 2的1次方， 100，2的2次方...
#       4. to retrieve the right-most bit in an integer n, one could either apply the modulo operation (i.e. n % 2)
#       or the bit AND operation (i.e. n & 1).Another example would be that in order to combine the results of reversed
#       bits (e.g. 2^a, 2^b), one could either use the addition operation (i.e. 2^a + 2^b2 ) or again the bit OR
#       operation (i.e. 2^a | 2^b2).
#       5. x & y是二进制下都是1的位置返回1，其他返回0。 x|y是二进制下每个位置只要有1个1就返回1，相当于十进制的加法(有反例，31 47不行)。

class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        ret, power = 0, 31
        while n:
            ret += (n & 1) << power
            n = n >> 1
            power -= 1
        return ret
# follow up question：
class Solution2:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        ret, power = 0, 24
        cache = dict()
        while n:
            ret += self.reverseByte(n & 0xff, cache) << power
            n = n >> 8
            power -= 8
        return ret

    def reverseByte(self, byte, cache):
        if byte not in cache:
            cache[byte] = (byte * 0x0202020202 & 0x010884422010) % 1023
        return cache[byte]