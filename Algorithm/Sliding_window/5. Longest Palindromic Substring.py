# Given a string s, return the longest palindromic substring in s.
# Example 1:
# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.
# Example 2:
# Input: s = "cbbd"
# Output: "bb"

# Constraints:
# 1 <= s.length <= 1000
# s consist of only digits and English letters.

# 思路：1. https://zkf85.github.io/2019/03/26/leetcode-005-longest-palindrome
#      2. j决定的是每次尝试的str结束的位置，所以j也要在range(len(s))循环，直接指定最末位置，前面所有情况都没有尝试。
#      3. 矩阵模式下，会超时，考虑改进：因为对于任意一行j，dp 只与前一行有关，与j-2之前的行都无关，所以记录之前的结果无意义，不需要记录矩阵

class Solution3: # 会超时
    def longestPalindrome(self, s: str) -> str:
        if s is "":
            return s
        res = ""
        dp = [[None for i in range(len(s))] for j in range(len(s))]
        for j in range(len(s)):
            for i in range(j+):
                if i == j:
                    dp[j][i] = True
                elif j == i+1:
                    dp[j][i] = (s[i] == s[j])
                else:
                    dp[j][i] = (dp[j-1][i+1] and s[i] == s[j])
                if dp[j][i] and j - i + 1 > len(res):
                    res = s[i:j+1]
        return res

class Solution3_2: # 不再记录整个矩阵，只记录array
    def longestPalindrome(self, s: str) -> str:
        if s is "":
            return s
        res = ""
        dp = [None for i in range(len(s))]
        for j in range(len(s)):
            for i in range(j+1):
                if i == j:
                    dp[i] = True
                elif j == i+1:
                    dp[i] = (s[i] == s[j])
                else:
                    dp[i] = (dp[i+1] and s[i] == s[j])
                if dp[i] and j - i + 1 > len(res):
                    res = s[i:j+1]
        return res
