# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# Example 1:
# Input: s = "anagram", t = "nagaram"
# Output: true
# Example 2:
# Input: s = "rat", t = "car"
# Output: false

# Constraints:
# 1 <= s.length, t.length <= 5 * 104
# s and t consist of lowercase English letters.
# Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?
# 思路：1. 可以用hashmap，可以用any(dict.values())判断是不是所有value都是0，负数也会return True


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count_s = collections.Counter(s)
        count_t = collections.Counter(t)
        for k,v in count_s.items():
            if k in count_t and count_t[k]==v:
                count_t.pop(k)
            else:
                return False
        if len(count_t.keys())!=0:
            return False
        return True

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict = {}
        for ele in s:
            if ele not in dict:
                dict[ele] = 1
            else:
                dict[ele] += 1
        for ele in t:
            if ele not in dict:
                return False
            else:
                dict[ele] -= 1
        return False if any(dict.values()) else True