# Given an array of strings strs, group the anagrams together. You can return the answer in any order. An Anagram is
# a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original
# letters exactly once.

# Example 1:
# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
# Example 2:
# Input: strs = [""]
# Output: [[""]]
# Example 3:
# Input: strs = ["a"]
# Output: [["a"]]

# Constraints:
# 1 <= strs.length <= 104
# 0 <= strs[i].length <= 100
# strs[i] consists of lowercase English letters.

# 思路： 1.分析：anagrams就是字母的count一样或者sort后一样。str不能做dict的key但tuple可以。考虑hashmap。
#       2.方法一，先sort再tuple，时间复杂度O(nklogk),因为遍历了一遍是n，每个str长度为k，排序是klogk。空间复杂度O(nk)为什么不是O(n)？
#       3.方法二，把str转化为数字，把count存入len为26的list，再tuple list作为key。好处是不用排序，时间复杂度优化为O(nk).


class Solution1:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = defaultdict(list)
        for s in strs:
            key = tuple(sorted(s))
            seen[key].append(s)
        return seen.values()

class Solution2:
    def groupAnagrams(self, strs):
        ans = collections.defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            ans[tuple(count)].append(s)
        return ans.values()