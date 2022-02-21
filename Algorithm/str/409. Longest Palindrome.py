# Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that
# can be built with those letters. Letters are case sensitive, for example, "Aa" is not considered a palindrome here.

# Example 1:
# Input: s = "abccccdd"
# Output: 7
# Explanation:
# One longest palindrome that can be built is "dccaccd", whose length is 7.
# Example 2:
# Input: s = "a"
# Output: 1
# Example 3:
# Input: s = "bb"
# Output: 2

# Constraints:
# 1 <= s.length <= 2000
# s consists of lowercase and/or uppercase English letters only.

# 思路：1. 要理解对题目意思，如果某个str是奇数个，也可以拿n-1个它来形成palindrome。
#      2. 答案思路和我一样，但code简化了很多。

class Solution:
    def longestPalindrome(self, s: str) -> int:
        s_count = collections.Counter(s)
        res = 0
        found_odd = False
        for key in s_count:
            if s_count[key] % 2 == 0:
                res += s_count[key]
            else:
                found_odd = True
                res += s_count[key] - 1

        if found_odd:
            res += 1
        return res


class Solution2:
    def longestPalindrome(self, s):
        ans = 0
        for v in collections.Counter(s).itervalues():
            ans += v / 2 * 2
            if ans % 2 == 0 and v % 2 == 1:
                ans += 1
        return ans

# Time Complexity: O(N), where NN is the length of s. We need to count each letter.
# Space Complexity: O(1), the space for our count, as the alphabet size of s is fixed. We should also consider
# that in a bit complexity model, technically we need O(logN) bits to store the count values.
