# A parentheses string is valid if and only if:
#
# It is the empty string,
# It can be written as AB (A concatenated with B), where A and B are valid strings, or
# It can be written as (A), where A is a valid string.
# You are given a parentheses string s. In one move, you can insert a parenthesis at any position of the string.
#
# For example, if s = "()))", you can insert an opening parenthesis to be "(()))" or a closing parenthesis to be "(
# ))))". Return the minimum number of moves required to make s valid.

# Example 1:
# Input: s = "())"
# Output: 1
# Example 2:
#
# Input: s = "((("
# Output: 3

# Constraints:
#
# 1 <= s.length <= 1000
# s[i] is either '(' or ')'

# 思路：1. The key is finding out in what situation we need to add new bracket or in what situation we do not add new
#         bracket. Does equal number of left bracket and left bracket guarantee that the input is valid? No, consider
#         the case that ')))((('. So the order matter. We need to iterate from the most left index. Then if it is a (,
#         that means we have one more ( to use. If it is a ), and currently we do not have additional ( to use, we will
#         need to add a (.
#      2. So the first thought is using a stack to store the left ( we have. If we encounter a ), pop a ( from the
#      stack. we can improve this by using a int to count the left ( we have cumulatively. The trick is when the count
#      of ( is -1, add 1 to both count of ( and the answer, which means we definitely need to add a ( in this case, then
#      we can continue. So the number of ( will not smaller than -1.

class Solution1:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        res = 0

        for i in range(len(s)):
            if s[i] == '(':
                stack.append(s[i])
            else:
                if not stack:
                    res += 1
                else:
                    stack.pop()
        return res + len(stack)


class Solution2:
    def minAddToMakeValid(self, s: str) -> int:
        res, count = 0, 0
        for cha in s:
            if cha == "(":
                count += 1
            else:
                count -= 1
            if count == -1:
                count += 1
                res += 1
        return res+count


