# Given a string s, find the length of the longest substring without repeating characters.

# Example 1:
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
# Example 2:
# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:
# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

# Constraints:
# 0 <= s.length <= 5 * 104
# s consists of English letters, digits, symbols and spaces.

# 思路：1. 看到找没有重复的substring，第一反应是two pointer和dict结合，right移动时用dict记录每一个str的idx，当有重复时直接把left
#         移动到dict中记录的该str之前的位置+1，形成新的substring继续移动right。
#      2. 一个重要细节是，当s[right]存在与dict中时不代表current substring中有该字母，要比较left和dict[s[right]]的大小，如果left
#         更大，说明不用移动left，可以继续移动right to extend the substring。

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = len(s)
        left = right = 0
        seen = {}
        res = 0
        while right <= l - 1:   # right开始移动后，left不可能大于right，所以不需要判断left是否<=right
            if s[right] not in seen or left > seen[s[right]]:
                seen[s[right]] = right
                length = right - left + 1
                res = max(length, res)
            else:
                left = seen[s[right]] + 1
                seen[s[right]] = right # 要移动left时，也要更新right的位置
            right += 1
        return res