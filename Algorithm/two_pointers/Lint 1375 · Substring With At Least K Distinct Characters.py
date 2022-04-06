# Given a string S with only lowercase characters.
#
# Return the number of substrings that contains at least k distinct characters.
#
# 10 ≤ length(S) ≤ 1,000,00010≤length(S)≤1,000,000
# 1 ≤ k ≤ 261≤k≤26
# Example
# Example 1:
#
# Input: S = "abcabcabca", k = 4
# Output: 0
# Explanation: There are only three distinct characters in the string.
# Example 2:
#
# Input: S = "abcabcabcabc", k = 3
# Output: 55
# Explanation: Any substring whose length is not smaller than 3 contains a, b, c.
#     For example, there are 10 substrings whose length are 3, "abc", "bca", "cab" ... "abc"
#     There are 9 substrings whose length are 4, "abca", "bcab", "cabc" ... "cabc"
#     ...
#     There is 1 substring whose length is 12, "abcabcabcabc"
#     So the answer is 1 + 2 + ... + 10 = 55.

# 思路：1. 双指针，同时要用hashmap记录当前字母数量
#      2. 时间复杂度：O(N),空间复杂度：O(1)

import collections


class Solution:
    """
    @param s: a string
    @param k: an integer
    @return: the number of substrings there are that contain at least k distinct characters
    """

    def __init__(self):
        pass

    def k_distinct_characters(self, s: str, k: int) -> int:
        # Write your code here
        res = 0
        right, left = 0, 0
        seen = collections.defaultdict(int)
        seen[s[left]] += 1
        while left <= len(s) - k:
            while len(seen) < k and right < len(s) - 1:
                right += 1
                seen[s[right]] += 1
            if len(seen) >= k:
                res += len(s) - right
            else:
                break
            seen[s[left]] -= 1
            if seen[s[left]] == 0:  # 这个判断不能忘
                del seen[s[left]]
            left += 1
        return res
