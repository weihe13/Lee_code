# Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an
# array of the non-overlapping intervals that cover all the intervals in the input.

# Example 1:
# Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
# Example 2:
# Input: intervals = [[1,4],[4,5]]
# Output: [[1,5]]
# Explanation: Intervals [1,4] and [4,5] are considered overlapping.

# Constraints:
# 1 <= intervals.length <= 104
# intervals[i].length == 2
# 0 <= starti <= endi <= 104

# 思路：1. 问题在于连续两个interval之间的大小关系有很多种情况，讨论起来很复杂，所以先按interval[0]排序，这样只比较interval[1]就行了。
#      2. 熟练list按第一个元素sort的写法。
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        merged = []
        for interval in intervals:
            # if the list of merged intervals is empty or if the current
            # interval does not overlap with the previous, simply append it.
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
            # otherwise, there is overlap, so we merge the current and previous
            # intervals.
                merged[-1][1] = max(merged[-1][1], interval[1])
        return merged

# Time complexity : O(nlogn). Other than the sort invocation, we do a simple linear scan of the list, so the runtime
# is dominated by the O(nlogn) complexity of sorting.

# Space complexity : O(logN) (or O(n)). If we can sort intervals in place, we do not need more than constant
# additional space, although the sorting itself takes O(logn) space. Otherwise, we must allocate linear space to
# store a copy of intervals and sort that.