# Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace
# and initial word order.

# Example 1:
# Input: s = "Let's take LeetCode contest"
# Output: "s'teL ekat edoCteeL tsetnoc"
# Example 2:
# Input: s = "God Ding"
# Output: "doG gniD"

# Constraints:
# 1 <= s.length <= 5 * 104
# s contains printable ASCII characters.
# s does not contain any leading or trailing spaces.
# There is at least one word in s.
# All the words in s are separated by a single space.

# 注意：1. 用 for word in s: word = word[::-1]时，无法改变s中的元素。
#      2. 如果不用split，该怎么做？

class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split()
        for i in range(len(s)):
            s[i] = s[i][::-1]
        s = ' '.join(s)
        return s
