# Given a pattern and a string s, find if s follows the same pattern.
# Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.

# Example 1:
# Input: pattern = "abba", s = "dog cat cat dog"
# Output: true
# Example 2:
# Input: pattern = "abba", s = "dog cat cat fish"
# Output: false
# Example 3:
# Input: pattern = "aaaa", s = "dog cat cat dog"
# Output: false

# Constraints:
# 1 <= pattern.length <= 300
# pattern contains only lower-case English letters.
# 1 <= s.length <= 3000
# s contains only lowercase English letters and spaces ' '.
# s does not contain any leading or trailing spaces.
# All the words in s are separated by a single space.

# 思路： 1. 能想到用dictionary，如果key在dictionary中但value和word不匹配则return false。
#       2. 但要注意abba -> cat cat cat cat的情况，就是不仅key value要匹配，不同key的value不能一样。

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split(' ')
        if len(s) != len(pattern):
            return False
        match = {}
        for i in range(len(s)): # 自己本来写法：if pattern[i] in match and match[pattern[i]]==s[i]:continue，没有意义直接删
            if pattern[i] not in match:
                if s[i] in match.values():
                    return False
                else:
                    match[pattern[i]] = s[i]
            else:
                if match[pattern[i]] != s[i]:
                    return False
        return True