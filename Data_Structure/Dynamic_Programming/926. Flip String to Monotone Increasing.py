# A binary string is monotone increasing if it consists of some number of 0's (possibly none), followed by some
# number of 1's (also possibly none).
# You are given a binary string s. You can flip s[i] changing it from 0 to 1 or from 1 to 0.
# Return the minimum number of flips to make s monotone increasing.

# Example 1:
# Input: s = "00110"
# Output: 1
# Explanation: We flip the last digit to get 00111.
# Example 2:
# Input: s = "010110"
# Output: 2
# Explanation: We flip to get 011111, or alternatively 000111.
# Example 3:
# Input: s = "00011000"
# Output: 2
# Explanation: We flip to get 00000000.

# Constraints:
#
# 1 <= s.length <= 105
# s[i] is either '0' or '1'.

# 思路：1. What we actually need to determine is which index to start with 1. So the first choice is no 1, that means all
#         the index to be 0. Then iterate from the zero index, check if it is 1, then how many times do we need to flip.
#         for each index, that answer is the number of 1 on the left plus the number of 0 on the right.
#      2. recursion: For each index, if it is zero, then continue. If it is 1, we have two choices, flip it or not. If
#         not flip it, the total number we need to flip is the number of 0 on the right plus the times we already
#         flipped. If flip it, plus 1 to the times of count we already done, and continue.

class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        right_0 = s.count('0')
        left_1 = 0
        res = len(s) - right_0

        for i in range(len(s)):
            if s[i] == '0':
                right_0 -= 1
            else:
                res = min(res, left_1 + right_0)
                left_1 += 1
        return res


class Solution2:
    def __init__(self):
        pass

    def minFlipsMonoIncr(self, s: str) -> int:
        right_0 = s.count('0')

        def helper(s, i, count, right_0):
            if i >= len(s):
                return count  # all value to be 0
            if s[i] == '0':
                right_0 -= 1
                return helper(s, i + 1, count, right_0)
            if s[i] == '1':
                return min(count + right_0, helper(s, i + 1, count + 1, right_0))

        return helper(s, 0, 0, right_0)


