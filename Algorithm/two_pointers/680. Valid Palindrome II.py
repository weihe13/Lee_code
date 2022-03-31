# Given a string s, return true if the s can be palindrome after deleting at most one character from it.

# Example 1:
# Input: s = "aba"
# Output: true
# Example 2:
# Input: s = "abca"
# Output: true
# Explanation: You could delete the character 'c'.
# Example 3:
# Input: s = "abc"
# Output: false

# Constraints:
# 1 <= s.length <= 105
# s consists of lowercase English letters.

# 思路：1. 想到比较s和s[::-1],要注意的是找到不想等的位置后，删除的位置有两种情况

class Solution:
    def validPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1
        while i < j:
            if s[i] != s[j]:
                delete_i = s[i + 1:j + 1]
                delete_j = s[i:j]
                return self._isPalindrome(delete_i) or self._isPalindrome(delete_j)
            i += 1
            j -= 1
        return True

    def _isPalindrome(self, s):
        return s == s[::-1]