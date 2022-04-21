# Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every
# character in t (including duplicates) is included in the window. If there is no such substring, return the empty
# string "".

# The testcases will be generated such that the answer is unique.
# A substring is a contiguous sequence of characters within the string.

# Example 1:
#
# Input: s = "ADOBECODEBANC", t = "ABC"
# Output: "BANC"
# Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
# Example 2:
#
# Input: s = "a", t = "a"
# Output: "a"
# Explanation: The entire string s is the minimum window.
# Example 3:
#
# Input: s = "a", t = "aa"
# Output: ""
# Explanation: Both 'a's from t must be included in the window.
# Since the largest window of s only has one 'a', return empty string.
#
#
# Constraints:
#
# m == s.length
# n == t.length
# 1 <= m, n <= 105
# s and t consist of uppercase and lowercase English letters.
#
#
# Follow up: Could you find an algorithm that runs in O(m + n) time?

# 思路：1. two pointers，用一个matchedchars记录目前满足要求的字母个数

# 自己写法

import collections


class Solution:
    def minWindow(self, source: str, target: str) -> str:
        left, right = 0, 0
        counts = collections.Counter(target)
        require = len(counts)
        curr = 0
        curr_count = collections.defaultdict(int)
        res, ret = float('inf'), ""

        while left <= len(source) - len(target):
            while right <= len(source) - 1 and curr < require:
                curr_count[source[right]] += 1  # 不论souce[right]是否在target中，都加进去，这样移动left时才有的减
                if curr_count[source[right]] == counts.get(source[right], -1):
                    curr += 1
                right += 1

            if curr == require:
                if right - left + 1 < res:
                    ret = source[left:right]
                    res = right - left + 1
            else:
                break

            curr_count[source[left]] -= 1
            if curr_count[source[left]] < counts[source[left]]:
                curr -= 1
            left += 1
            # left一次只移动一位，再写一个while太容易出错了
            # while left <= len(source)-len(target) and curr == require:
            #     curr_count[source[left]] -= 1
            #     if curr_count[source[left]] < counts.get(source[left], -1):
            #         curr -= 1
            #     elif right-left < res:
            #         ret = source[left+1:right]
            #         res = right - left
            #     left += 1

        return ret

# 自己写法，稍微有点乱，主要是初始的count+1不在循环里
class Solution:
    def minWindow(self, source: str, target: str) -> str:
        if not source or not target or len(source) < len(target):
            return ''

        left, right, res = 0, 0, float('inf')
        target_dict = collections.Counter(target)
        t = len(target_dict)
        count = 0
        seen = collections.defaultdict(int)
        seen[source[left]] += 1
        ret = []
        if seen[source[left]] == target_dict[source[left]]:
            count += 1

        while left <= len(source) - len(target):
            while count < t and right < len(source) - 1:
                right += 1
                seen[source[right]] += 1
                if seen[source[right]] == target_dict.get(source[right], -1):
                    count += 1
            if count == t:
                curr = right - left + 1
                if curr < res:
                    ret = [left, right]
                    res = curr
            else:
                break
            seen[source[left]] -= 1
            if seen[source[left]] < target_dict[source[left]]:
                count -= 1
            left += 1

        if ret:
            return source[ret[0]:ret[1] + 1]
        return ""


# 答案写法，没按九章模板写，不建议
class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if not s or not t:
            return ''

        from collections import Counter
        target = Counter(t)
        current_window = {}
        require = len(target)
        ans = float('inf'), None, None
        formed = 0

        l = r = 0
        while r < len(s):
            character = s[r]
            current_window[character] = current_window.get(character, 0) + 1
            if character in t and current_window[character] == target[character]:
                formed += 1

            while l <= r and formed == require:
                if r - l + 1 < ans[0]:
                    ans = (r - l + 1, l, r)
                character = s[l]
                current_window[character] -= 1
                if character in t and current_window[character] < target[character]:
                    formed -= 1
                l += 1

            r += 1

        return '' if ans[0] == float('inf') else s[ans[1]:ans[2] + 1]
