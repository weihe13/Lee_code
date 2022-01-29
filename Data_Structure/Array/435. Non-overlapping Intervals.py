# 和56一起看
# Given an array of intervals intervals where intervals[i] = [starti, endi], return the minimum number of
# intervals you need to remove to make the rest of the intervals non-overlapping.

# Example 1:
# Input: intervals = [[1,2],[2,3],[3,4],[1,3]]
# Output: 1
# Explanation: [1,3] can be removed and the rest of the intervals are non-overlapping.
# Example 2:
# Input: intervals = [[1,2],[1,2],[1,2]]
# Output: 2
# Explanation: You need to remove two [1,2] to make the rest of the intervals non-overlapping.
# Example 3:
# Input: intervals = [[1,2],[2,3]]
# Output: 0
# Explanation: You don't need to remove any of the intervals since they're already non-overlapping.

# Constraints:
# 1 <= intervals.length <= 105
# intervals[i].length == 2
# -5 * 104 <= starti < endi <= 5 * 104

# 思路： 1. 按interval的end排序，排序后如果遇到overlap，就把后一个(当前)interval删掉。理由：后一个interval的end大于前一个interval的
#          end，因此排查后续interval时当前interval可能产生更多的overlap(只要和前一个interval overlap的一定和当前interval overlap)
#          因为当前interval的end值更大。
#       2. 如何用算法体现剔除当前interval的操作呢？设置end变量，当不存在overlap时，更新end到当前interval的end，因为不剔除当前interval，
#          需要更新end。如果存在overlap，则不更新end，意思是假装这个interval被剔除了，因此不用更新end。
#       3. 56题是让合并interval，这时按start排序。

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        intervals.sort(key = lambda x: x[1])
        count = 0
        end = -float("inf")
        for i in range(len(intervals)):
            if intervals[i][0] >= end:
                end = intervals[i][1]
                count += 1
        return len(intervals)-count