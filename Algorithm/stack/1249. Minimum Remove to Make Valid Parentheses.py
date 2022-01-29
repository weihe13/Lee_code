# Given a string s of '(' , ')' and lowercase English characters. Your task is to remove the minimum number of
# parentheses ( '(' or ')', in any positions ) so that the resulting parentheses string is valid and return any valid
# string. Formally, a parentheses string is valid if and only if:

# It is the empty string, contains only lowercase characters, or
# It can be written as AB (A concatenated with B), where A and B are valid strings, or
# It can be written as (A), where A is a valid string.

# Example 1:
# Input: s = "lee(t(c)o)de)"
# Output: "lee(t(c)o)de"
# Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.
# Example 2:
# Input: s = "a)b(c)d"
# Output: "ab(c)d"
# Example 3:
# Input: s = "))(("
# Output: ""
# Explanation: An empty string is also valid.

# Constraints:
# 1 <= s.length <= 105
# s[i] is either'(' , ')', or lowercase English letter.

# 思路： 1. valid的两个条件："("和")"数量一样；count("(")-count(")")>=0且最终等于0。
#       2. 哪些括号应该被remove？首先当一个右括号没有相匹配的左括号时，这个右括号一定要remove；其次最后剩下的左括号要remove。当然，当出现
#          右括号没有匹配的左括号时，也可以remove更早的右括号，但需要remove的括号数量不变。
#       3. 因为判断右括号是否valid时会判断和它最近的左括号，左括号是后进先出，所以想到stack。
#       4. build string时要注意：

# We need to be really careful with that "removal" step though, as it can be done in O(n), but there are many ways of
# accidentally making it O(n2). Making these mistakes (and not fixing them) in an interview won't look good. Here's
# some operations that are O(n)O(n) that people sometimes assume are O(1).

# Adding or removing (or even changing) just one character anywhere in a string is O(n), because strings are
# immutable. The entire string is rebuilt for every change.
# Adding or removing not from the end of a list, vector, or array is O(n) because the other items are moved up to
# make a gap or down to fill in the gap.
# Checking if an item is in a list, because this requires a linear search. Even if you use binary search, it'll still
# be O(logn), which is not ideal for this problem.

# A safe strategy is to iterate over the string and insert each character we want to keep into a list (Python) or
# StringBuilder (Java). Then once we have all the characters, it is a single O(n) step to convert them into a string.
# Recall that checking if an item is in a set is O(1). If all the indexes we need to remove are in a set, then we can
# iterate through each index in the string, check if the current index is in the set, and if it is not, then add the
# character at that index to the string builder.

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        index_to_remove = set()
        stack = []
        for i, c in enumerate(s):  #O(n)
            if c not in "()":
                continue
            elif c == '(':
                stack.append(i)
            elif not stack:
                index_to_remove.add(i)
            else:
                stack.pop() # stack是list因为需要pop（先进后出）

        index_to_remove = index_to_remove.union(set(stack)) # 判断in set 的操作是O(1)时间复杂度
        string_builder = []
        for i, c in enumerate(s):     # O(n)
            if i not in index_to_remove:
                string_builder.append(c)
        return "".join(string_builder)     # O(n)

# 时间复杂度：O(4n) so O(n).The second loop (hidden in library function calls for the Python code) pops each item from the
# stack and adds it to the set. Again, popping items from a stack is O(1), and there are at most nn characters on
# the stack, and so it too is O(n).
# 空间复杂度：O(n), where nn is the length of the input string. We are using a stack,
# set, and string builder, each of which could have up to n characters in them, and so require up to O(n) space.

# 优化思路：two_pass solution，第一次去掉invalid ),然后把str取反用同样算法去掉invalid(，这样时间复杂度虽然还是O(N)，但只pass两次。
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        def delete_invalid(s, open_symbol, close_symbol):
            balance = 0
            sb = []
            for c in s:
                if c == open_symbol:
                    balance += 1

                elif c == close_symbol:
                    if balance == 0:
                        continue
                    else:
                        balance -= 1
                sb.append(c)
            return "".join(sb)

        s1 = delete_invalid(s, '(', ')')
        s2 = delete_invalid(s1[::-1], ')', '(')
        return s2[::-1]
