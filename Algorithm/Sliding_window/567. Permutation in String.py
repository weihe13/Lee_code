# Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.
# In other words, return true if one of s1's permutations is the substring of s2.

# Example 1:
# Input: s1 = "ab", s2 = "eidbaooo"
# Output: true
# Explanation: s2 contains one permutation of s1 ("ba").
# Example 2:
# Input: s1 = "ab", s2 = "eidboaoo"
# Output: false

# Constraints:
# 1 <= s1.length, s2.length <= 104
# s1 and s2 consist of lowercase English letters.

# 思路：1. 判断permutation of s1的方式：counter一样，sort后一样。每次移动后都sort会超时，这里考虑counter
#      2. 直接用counter也可以，但是很慢，虽然能接受但是体现不了思路，考虑自己用类似hashmap的思路。这里用list来存次数，就不用pop了。
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        dict1 = [0] * 26
        dict2 = [0] * 26
        for i in range(len(s1)):
            dict1[ord(s1[i]) - ord('a')] += 1
            dict2[ord(s2[i]) - ord('a')] += 1
        if dict1 == dict2:
            return True
        l1 = len(s1)
        l2 = len(s2)
        for i in range(l2 - l1):
            dict2[ord(s2[i]) - ord('a')] -= 1
            dict2[ord(s2[l1 + i]) - ord('a')] += 1
            if dict2 == dict1:
                return True
        return False
        #         from collections import Counter
        #         gap = len(s1)
        #         left = 0
        #         right = left + gap
        #         l2 = len(s2)
        #         target = Counter(s1)

        #         while right <= l2:
        #             if Counter(s2[left:right]) == target:
        #                 return True
        #             else:
        #                 left += 1
        #                 right += 1
        #         return False
