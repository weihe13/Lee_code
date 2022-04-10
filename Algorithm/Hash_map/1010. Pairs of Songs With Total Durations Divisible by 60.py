# You are given a list of songs where the ith song has a duration of time[i] seconds. Return the number of pairs of
# songs for which their total duration in seconds is divisible by 60. Formally, we want the number of indices i,
# j such that i < j with (time[i] + time[j]) % 60 == 0.

# Example 1:
# Input: time = [30,20,150,100,40]
# Output: 3
# Explanation: Three pairs have a total duration divisible by 60:
# (time[0] = 30, time[2] = 150): total duration 180
# (time[1] = 20, time[3] = 100): total duration 120
# (time[1] = 20, time[4] = 40): total duration 60
# Example 2:
# Input: time = [60,60,60]
# Output: 3
# Explanation: All three pairs have a total duration of 120, which is divisible by 60.

# Constraints:
#
# 1 <= time.length <= 6 * 104
# 1 <= time[i] <= 500

# 思路：1. calculate the remainder of each song divided by 60 and count the number of each remainder
#      2. change the question to 2 sum
#      3. time complexity: O(n)

import collections


class Solution:
    def __init__(self):
        pass

    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        remainders = [t % 60 for t in time]
        counts = collections.Counter(remainders)
        res = 0
        for i in counts:
            if i == 0 or i == 30:
                count = counts[i]
                res += count * (count - 1) // 2
                counts[i] = 0
            else:
                target = 60 - i
                if target in counts:
                    count = counts[i] * counts[target]
                    res += count
                    counts[i] = 0
                    counts[target] = 0
        return res
