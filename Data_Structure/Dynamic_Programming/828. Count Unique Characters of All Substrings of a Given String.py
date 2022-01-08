# Let's define a function countUniqueChars(s) that returns the number of unique characters on s. For example if s =
# "LEETCODE" then "L", "T", "C", "O", "D" are the unique characters since they appear only once in s,
# therefore countUniqueChars(s) = 5. Given a string s, return the sum of countUniqueChars(t) where t is a substring
# of s. Notice that some substrings can be repeated so in this case you have to count the repeated ones too.

# Example 1:
# Input: s = "ABC"
# Output: 10
# Explanation: All possible substrings are: "A","B","C","AB","BC" and "ABC".
# Evey substring is composed with only unique letters.
# Sum of lengths of all substring is 1 + 1 + 1 + 2 + 2 + 3 = 10
# Example 2:
# Input: s = "ABA"
# Output: 8
# Explanation: The same as example 1, except countUniqueChars("ABA") = 1.
# Example 3:
# Input: s = "LEETCODE"
# Output: 92

# 思路：Here I use 2 maps, map1 and map2, map1 records the last index for each letter, map2 records the second last
# index for each letter. They are both initialized as -1(means a letter hasn't shown up) .
# Then consider about introducing a new letter, it will contribute (i - last_ch_position) unique chars,
# and also decrease (last_ch_position - second_last_ch_position) unique chars.
#
# Take an example: ABCBB
# i = 0, ch = A, substring = A. A hasn't shown up, so cur += 1, map1:{A:0}, map2:{}
# i = 1, ch = B, substring = AB, B. B hasn't shown up, so cur += 2, map1: {A:0, B:1}, map2:{}
# i = 2, ch = C, substring = ABC, BC, C. cur+= 3, map1:{A:0, B:1, C:2}, map2:{}
# i = 3. ch = B, sustring = ABCB, BCB, CB, B. last_b_position = 1, so it only contributes unique char to the index
# after last_b_position, which is i-map1[B] = 2, ie CB, B. It also decreases unique char in ABCB and BCB,
# which is map1[B] - map2[B] = 2, so cur+= 2-2, map1:{A:0, B:3, C:2}, map2:{B:1}
# i = 4, ch = B, substring = ABCBB, BCBB, CBB, BB, B. It increase one unique char which is "B" (i-map1[B]),
# but decreases 2 unique chars, which are "CBB, BB" (map1[B] - map2[B]), cur += 1 - 2, map1: {A:0, B:4, C:2}, map2:{B:3}

# 理解：1. 增加i位置的字母时，能增加i+1个substring；
#      2. 这新增的i+1个substring，有几个是合法的substring(没有重复字母),就能比之前额外加几个字母。比如上面i从1到2，在原有A，AB，B三个
#         substring的基础上会新增位置0-2，1-2，2三个substring，因为都没有重复字母，所以也会增加1+2+3个字母数。

def uniqueLetterString(self, s: str) -> int:
    map1 = collections.defaultdict(lambda: -1)  # last index for this letter
    map2 = collections.defaultdict(lambda: -1)  # second last index for this letter
    cur = 0
    res = 0

    for i, ch in enumerate(s):
        cur += (i - map1[ch]) - (map1[ch] - map2[ch])
        map2[ch] = map1[ch]
        map1[ch] = i
        res += cur
    return res