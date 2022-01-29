# similar to 435 and 56, but totally different thought.
# Given an array of meeting time intervals intervals where
# intervals[i] = [starti, endi], return the minimum number of conference rooms required.
#
# Example 1:
# Input: intervals = [[0,30],[5,10],[15,20]]
# Output: 2
# Example 2:
# Input: intervals = [[7,10],[2,4]]
# Output: 1

# Constraints:
# 1 <= intervals.length <= 104
# 0 <= starti < endi <= 106

# 思路：1. 就和现实中找会议室一样，每次都是先看哪个会议室最先空，就用哪个，这就是思路，问题是如何用code实现
#      2. 通过heapq实现Priority Queues，存储当前的会议最早结束的时间，用这个和下一个会议开始时间比较。如果小于，则更新当前会议
#         最早结束时间。

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        # If there is no meeting to schedule then no room needs to be allocated.
        if not intervals:
            return 0
        # The heap initialization
        free_rooms = []
        # Sort the meetings in increasing order of their start time.
        intervals.sort(key=lambda x: x[0])
        # Add the first meeting. We have to give a new room to the first meeting.
        heapq.heappush(free_rooms, intervals[0][1])
        # For all the remaining meeting rooms
        for i in intervals[1:]:
            # If the room due to free up the earliest is free, assign that room to this meeting.
            if free_rooms[0] <= i[0]:
                heapq.heappop(free_rooms)
            # If a new room is to be assigned, then also we add to the heap,
            # If an old room is allocated, then also we have to add to the heap with updated end time.
            heapq.heappush(free_rooms, i[1])
        # The size of the heap tells us the minimum rooms required for all the meetings.
        return len(free_rooms)