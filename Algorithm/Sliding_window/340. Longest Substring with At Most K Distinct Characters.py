# Given a string s and an integer k, return the length of the longest substring of s that contains at most k distinct
# characters.

# Example 1:
# Input: s = "eceba", k = 2
# Output: 3
# Explanation: The substring is "ece" with length 3.
# Example 2:
# Input: s = "aa", k = 1
# Output: 2
# Explanation: The substring is "aa" with length 2.

# Constraints:
# 1 <= s.length <= 5 * 104
# 0 <= k <= 50

# 思路 ： 1. 用sliding window，注意len < k 时也需要记录max length，因为k是允许的最大数量，有可能达不到k
#        2. Approach 2: Sliding Window + Ordered Dictionary.(Achieve O(N) time complexity)

class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        length = 0
        left = right = 0
        count = {}
        while left <= right <= len(s) - 1:
            count[s[right]] = count.setdefault(s[right], 0) + 1
            if len(count) <= k:
                current = right - left + 1
                length = max(length, current)

            while len(count) > k:
                if count[s[left]] == 1:
                    count.pop(s[left])
                else:
                    count[s[left]] -= 1
                left += 1
            right += 1
        return length

        # n = len(s)
        # if k == 0 or n == 0:
        #     return 0
        #
        # # sliding window left and right pointers
        # left, right = 0, 0
        # # hashmap character -> its rightmost position
        # # in the sliding window
        # hashmap = OrderedDict()
        #
        # max_len = 1
        #
        # while right < n:
        #     character = s[right]
        #     # if character is already in the hashmap -
        #     # delete it, so that after insert it becomes
        #     # the rightmost element in the hashmap
        #     if character in hashmap:
        #         del hashmap[character]
        #     hashmap[character] = right
        #     right += 1
        #
        #     # slidewindow contains k + 1 characters
        #     if len(hashmap) == k + 1:
        #         # delete the leftmost character
        #         _, del_idx = hashmap.popitem(last=False)
        #         # move left pointer of the slidewindow
        #         left = del_idx + 1
        #
        #     max_len = max(max_len, right - left)
        #
        # return max_len