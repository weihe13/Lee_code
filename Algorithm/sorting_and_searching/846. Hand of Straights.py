# Alice has some number of cards and she wants to rearrange the cards into groups so that each group is of size
# groupSize, and consists of groupSize consecutive cards.
# Given an integer array hand where hand[i] is the value written on the ith card and an integer groupSize,
# return true if she can rearrange the cards, or false otherwise.

# Example 1:
# Input: hand = [1,2,3,6,2,3,4,7,8], groupSize = 3
# Output: true
# Explanation: Alice's hand can be rearranged as [1,2,3],[2,3,4],[6,7,8]
# Example 2:
# Input: hand = [1,2,3,4,5], groupSize = 4
# Output: false
# Explanation: Alice's hand can not be rearranged into groups of 4.

# Constraints:
#
# 1 <= hand.length <= 104
# 0 <= hand[i] <= 109
# 1 <= groupSize <= hand.length

# 思路： 1. 关键在于分析，什么样的情况才能返回True，核心的关键点是什么？是不是每个数字都要用到还是可以有多余数字？
#       2. 关键点是: 1) 对于每一个起始数字k，如果有m个k，那么从k+1到k+W,每一个数都至少要有m个。
#                   2) 对于方法二，如果有m个k，那么拆分的数组数量就至少是m个，如果当前只有m-l个数组，那么就要新建l个数组，如果当前数组数量
#                      大于m，则可以直接return False
#       3. 方法一time complexity：O(NlogN + NW) N is the number of different cards
#          方法二time complexity：O(NlogN)

import collections


class Solution:
    def __init__(self):
        pass

    def isNStraightHand(self, hand: List[int], W: int) -> bool:
        counts = collections.Counter(hand)
        for i in sorted(counts):
            if counts[i] > 0:  # counts[i] < 0 会返回false，所以counts[i]是可以等于0的，这个判断可以节约大量时间
                for j in range(W)[::-1]:
                    counts[i + j] -= counts[i]
                    if counts[i + j] < 0:
                        return False
        return True


import collections


class Solution2:
    def __init__(self):
        pass

    def isNStraightHand(self, hand: List[int], W: int) -> bool:
        counts = collections.Counter(hand)
        start = collections.deque()
        last_checked, opened = -1, 0

        for k in sorted(counts):
            if counts[k] < opened or opened > 0 and k > last_checked + 1:
                return False

            start.append(counts[k] - opened)
            last_checked, opened = k, counts[k]

            if len(start) == W:
                closing = start.popleft()
                opened -= closing

        return opened == 0
