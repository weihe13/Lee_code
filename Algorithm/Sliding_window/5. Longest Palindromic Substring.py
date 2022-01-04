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
#      4. 最好方法：按return的len是odd还是even两种情况讨论，速度快，容易理解。
#      5. helper函数return时，注意str的切片是左闭右开。

class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest_pal = ''
        if len(s) == 0:
            return ''
        if len(s) == 1:
            return s

        for i in range(0, len(s)):
            # odd case
            longest = self.helper(s, i, i)
            if len(longest) > len(longest_pal):
                longest_pal = longest

            # even case
            longest = self.helper(s, i, i + 1)
            if len(longest) > len(longest_pal):
                longest_pal = longest
        return longest_pal

    def helper(self, s, i, i2):
        # find longest palindrome starting from i and i2
        while i >= 0 and i2 < len(s):
            if s[i] == s[i2]:
                i -= 1
                i2 += 1
            else:
                break
        return s[i + 1:i2]  # 注意i2是取不到的

class Solution3: # 会超时
    def longestPalindrome(self, s: str) -> str:
        if s is "":
            return s
        res = ""
        dp = [[None for i in range(len(s))] for j in range(len(s))]
        for j in range(len(s)):
            for i in range(j+1):
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

        # 硬写的思路
        # m = ''  # Memory to remember a palindrome
        # for i in range(len(s)):  # i = start, O = n
        #     for j in range(len(s), i, -1):  # j = end, O = n^2
        #         if len(m) >= j-i:  # To reduce time
        #             break
        #         elif s[i:j] == s[i:j][::-1]:
        #             m = s[i:j]
        #             break
        # return m
