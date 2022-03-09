# Given an integer x, return true if x is palindrome integer.
# An integer is a palindrome when it reads the same backward as forward.
# For example, 121 is a palindrome while 123 is not.

# Example 1:
# Input: x = 121
# Output: true
# Explanation: 121 reads as 121 from left to right and from right to left.
# Example 2:
# Input: x = -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
# Example 3:
# Input: x = 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

# Constraints:
# -2^31 <= x <= 2^31 - 1

# Follow up: Could you solve it without converting the integer to a string?

# 思路：1. 转成string，return s == s[::-1]
#      2. 把数字倒过来，但是有可能超过数字最大限制，integer overflow problem.
#      3. 把数字倒过来，但是只倒一半即可

class Solution1:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        s = str(x)

        return s == s[::-1]


class Solution2:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        copy = x
        digit = 0
        while copy // 10 >= 1:
            digit = digit * 10 + copy % 10
            copy //= 10
        digit = digit * 10 + copy % 10

        return digit == x


class Solution3:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        if x % 10 == 0 and x != 0:  # 不加这个判断，输入10，会return True
            return False

        reverse = 0
        while x > reverse:
            reverse = reverse * 10 + x % 10
            x //= 10

        return x == reverse or x == reverse // 10 # 奇数位或偶数位两种情况
