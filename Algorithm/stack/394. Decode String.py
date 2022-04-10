# Given an encoded string, return its decoded string. The encoding rule is: k[encoded_string], where the
# encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a
# positive integer. You may assume that the input string is always valid; there are no extra white spaces,
# square brackets are well-formed, etc. Furthermore, you may assume that the original data does not contain any
# digits and that digits are only for those repeat numbers, k. For example, there will not be input like 3a or 2[4].

# Example 1:
# Input: s = "3[a]2[bc]"
# Output: "aaabcbc"
# Example 2:
# Input: s = "3[a2[c]]"
# Output: "accaccacc"
# Example 3:
# Input: s = "2[abc]3[cd]ef"
# Output: "abcabccdcdcdef"

# Constraints:
#
# 1 <= s.length <= 30
# s consists of lowercase English letters, digits, and square brackets '[]'.
# s is guaranteed to be a valid input.
# All the integers in s are in the range [1, 300]

# 思路： 1. think of stack
#       2. Must find the law for the calculation:
#          1) Each '[' means one number, so use stack to store the number in a last in first out order.
#          2) Because the left bracket and right bracket are paired, when we encounter a  right bracked, the last number
#             in the stack will definitely be the number related to this bracket.
#          3) If we do not encounter left bracket, then we need to continuously update the curr_string, 如果遇到[，就加到
#             stack里，加到stack现有数字之后，因为没有遇到和该数字对应的],说明还不应该执行。

class Solution:
    def decodeString(self, s: str) -> str:
        stack, curr_num, curr_string = [], 0, ''

        for i in range(len(s)):
            if s[i].isnumeric():
                curr_num = curr_num * 10 + int(s[i])
            elif s[i].isalpha():
                curr_string += s[i]
            elif s[i] == '[':
                stack.append(curr_string)
                stack.append(curr_num)
                curr_string = ''
                curr_num = 0
            else:
                num = stack.pop()
                pre_string = stack.pop()
                curr_string = pre_string + num * curr_string
        return curr_string