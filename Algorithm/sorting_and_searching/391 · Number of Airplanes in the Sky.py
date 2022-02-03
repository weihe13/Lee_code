# Given an list interval, which are taking off and landing time of the flight. How many airplanes are there at most
# at the same time in the sky?

# If landing and taking off of different planes happen at the same time, we consider landing should happen at first.
# Example
# Example 1:
# Input: [(1, 10), (2, 3), (5, 8), (4, 7)]
# Output: 3
# Explanation:
# The first airplane takes off at 1 and lands at 10.
# The second ariplane takes off at 2 and lands at 3.
# The third ariplane takes off at 5 and lands at 8.
# The forth ariplane takes off at 4 and lands at 7.
# During 5 to 6, there are three airplanes in the sky.
# Example 2:
# Input: [(1, 2), (2, 3), (3, 4)]
# Output: 1
# Explanation: Landing happen before taking off.

# 思路：
# 算法一 前缀和
# 在开始时间位置+1架飞机，在结束时间-1架飞机，求一遍前缀和，就是对应时间飞机的数量,
# 前缀和算法涉及到了对时间离散化，所以这里更推荐扫描线
# 算法二 扫描线
# 扫描线，把飞机按开始时间从小到大排序，如果开始时间相同，结束时间小的在前，
# 扫描一遍，当扫描到开始时间，就会多一架飞机,飞机数+1，当扫描到结束时间就少一架飞机，飞机数-1
# 答案取扫描过程中的最大飞机数
#
# 复杂度分析
# 时间复杂度
# 算法一 前缀和
# 前缀和 O(Time)O(Time) Time表示最大时间
# 算法二 扫描线
# 扫描线 O(NlogN)O(NlogN) N是飞机数量
# 空间复杂度
# 算法一 前缀和
# 前缀和 O(Time)O(Time) Time表示最大时间
# 算法二 扫描线
# 扫描线 O(N)O(N) N是飞机数量

class Solution:
    """
    @param airplanes: an array of meeting time airplanes
    @return: the minimum number of conference rooms required
    """

    def countOfAirplanes(self, airplanes):
        # Write your code here
        room = []
        # 加入开始时间和结束时间，1是房间+1，-1是房间-1
        for i in airplanes:
            room.append((i.start, 1))
            room.append((i.end, -1))
        tmp = 0
        ans = 0
        # 排序
        room = sorted(room)  # 核心在于sort，如果时间一样按第二个元素从小到大排序，这样就考虑了先落地再起飞的设定，
        # 同时，这样也保证了当同一个时间有多架飞机降落或起飞时，最大值一定在扫描完该时间所有起飞飞机后得到，不会出现在中间，因此tmp可以简单累计
        # 扫描一遍
        for idx, cost in room:
            tmp += cost
            ans = max(ans, tmp)
        return ans

class Solution2:
    """
    @param airplanes: an array of meeting time airplanes
    @return: the minimum number of conference rooms required
    """
    def countOfAirplanes(self, airplanes):
        # Write your code here
        # 前缀和数组
        room = {}
        # 开始时间+1，结束时间-1
        for i in airplanes:
            room[i.start] = room.get(i.start, 0) + 1
            room[i.end] = room.get(i.end, 0) - 1
        ans = 0
        tmp = 0
        for i in sorted(room.keys()):
            tmp = tmp + room[i]
            ans = max(ans, tmp)
        return ans
