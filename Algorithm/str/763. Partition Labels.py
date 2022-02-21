# You are given a string s. We want to partition the string into as many parts as possible so that each letter
# appears in at most one part. Note that the partition is done so that after concatenating all the parts in order,
# the resultant string should be s.
#
# Return a list of integers representing the size of these parts.

# Example 1:
# Input: s = "ababcbacadefegdehijhklij"
# Output: [9,7,8]
# Explanation:
# The partition is "ababcbaca", "defegde", "hijhklij".
# This is a partition so that each letter appears in at most one part.
# A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits s into less parts.
# Example 2:
# Input: s = "eccbbbbdec"
# Output: [10]

# Constraints:
# 1 <= s.length <= 500
# s consists of lowercase English letters.

# 思路：1. Greedy 算法：第一次遍历，用一个dictionary记录每个字母出现的最后位置，第二次遍历，不断更新见过的字母的最后位置，当当前位置i和当
#         前所有见过的字母出现的最后位置相等时，意味着可以partition。
#      2. 第一次遍历，记录每个字母的开始和结束位置，sort并pop没有出现的字母后（这点要注意，要pop掉没出现的字母），有overlap就merge。
#      3. 第一种方法时间复杂度O(n),遍历了2次，空间复杂度O(1), keep data structure last of not more than 26 characters.
#      4. 第二种方法时间复杂度O(n),遍历了1次，空间复杂度O(1)

# 难想但写法简单不容易出错
class Solution(object):
    def partitionLabels(self, S):
        last = {c: i for i, c in enumerate(S)}
        j = anchor = 0
        ans = []
        for i, c in enumerate(S):
            j = max(j, last[c])
            if i == j:
                ans.append(i - anchor + 1)  # 注意长度是index相减再加1
                anchor = i + 1
        return ans

# 容易理解但写的时候要注意的点不少
class Solution1:
    def partitionLabels(self, s: str) -> List[int]:
        length = [[0, 0, 0] for i in range(26)] #用第三个位置记录是否见过该字母
        for i in range(len(s)):
            idx = ord(s[i]) - ord('a')
            length[idx][1] = i     # 第二个位置表示end肯定要更新
            if length[idx][2] == 0:  # 第一个位置表示start没见过时更新
                length[idx][0] = i
                length[idx][2] = 1
            else:
                continue

        length = sorted(length)  # 按第一个位置从小到大排序
        res = []
        for interval in length:
            if interval[2] != 0: # 向res里增加见过的字母
                res.append(interval)

        i = 0
        while i < len(res) - 1:  # 注意到len(res)-1, 不是len(res)， 防止index out of range
            if res[i + 1][0] < res[i][1]:
                res[i][1] = max(res[i + 1][1], res[i][1]) # 这里一定要注意！！要更新的是两个结束位置的max。
                res.pop(i + 1)   # 这里要注意，pop掉i+1，i不能变，继续比下一个
            else:
                i += 1     # 不overlap时，才改变i
        # 注意，每次pop后，i保持不变，且判断条件中的len(res)跟新了，所以虽然res变短了，也不会index out of range
        # 判断len(res)-1位置时，已经和len(res)位置做了比较，如果overlap就merge，否则就不变，这样len(res)位置相当于也处理过了。这就是
        # 直接在res中改的好处。如果新建一个list往里加区间，更麻烦而且最后一个位置不好处理。因为之前的位置即使没有overlap，也要和后面的位置
        # 继续比较，但最后一个位置可以直接加，要单独写一个判断条件。

        return [res[i][1] - res[i][0] + 1 for i in range(len(res))]  # 注意长度是index相减再加1


