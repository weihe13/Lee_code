# Given a string s containing an out-of-order English representation of digits 0-9, return the digits in ascending
# order.

# Example 1:
# Input: s = "owoztneoer"
# Output: "012"
# Example 2:
# Input: s = "fviefuro"
# Output: "45"

# Constraints:
# 1 <= s.length <= 105
# s[i] is one of the characters ["e","g","f","i","h","o","n","s","r","u","t","w","v","x","z"].
# s is guaranteed to be valid.

# 思路: 1. 分析字母和数字的关系，比如有几个z就代表有几个0

# Time complexity : O(N) where N is a number of characters in the input string. O(N) time
# is needed to compute hashmap count "letter -> its frequency in the input string". Then we deal with a data
# structure out which contains 10 elements only and all operations are done in a constant time.

# Space complexity : O(1). count contains constant number of elements since input string contains only lowercase English
# letters, and out contains not more than 10 elements.

class Solution:
    def originalDigits(self, s: str) -> str:
        count = collections.Counter(s)
        res = dict()

        res['0'] = count['z']
        res['2'] = count['w']
        res['6'] = count['x']
        res['8'] = count['g']
        res['3'] = count['h'] - res['8']
        res['7'] = count['s'] - res['6']
        res['5'] = count['v'] - res['7']
        res['4'] = count['r'] - res['3'] - res['0']
        res['1'] = count['o'] - res['0'] - res['2'] - res['4']
        res['9'] = count['i'] - res['5'] - res['8'] - res['6']

        output = [k * res[k] for k in sorted(res.keys())]
        return "".join(output)