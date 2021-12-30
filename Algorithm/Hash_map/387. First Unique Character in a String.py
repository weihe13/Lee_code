# Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

# Example 1:
# Input: s = "leetcode"
# Output: 0
# Example 2:
# Input: s = "loveleetcode"
# Output: 2
# Example 3:
# Input: s = "aabb"
# Output: -1

# Constraints:
# 1 <= s.length <= 105
# s consists of only lowercase English letters.

# 思路： 1. 因为要看是否重复，所以必须遍历每一个element。所以想到hashmap；
#       2. 自己写法是硬写，不容易读，答案用了Counter和enumerate，简化了很多。

class Solution:
    def firstUniqChar(self, s: str) -> int:
        """
        :type s: str
        :rtype: int
        """
        # build hash map : character and how often it appears
        count = collections.Counter(s)

        # find the index
        for idx, ch in enumerate(s):
            if count[ch] == 1:
                return idx
        return -1


class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = {}
        for i in range(len(s)):
            if s[i] not in d:
                d[s[i]] = 1
            else:
                d[s[i]] = d.get(s[i]) + 1
        ans = []
        for k, v in d.items():
            if v == 1:
                ans.append(s.index(k))
        ans.sort()
        if len(ans) != 0:
            return ans[0]
        else:
            return -1



