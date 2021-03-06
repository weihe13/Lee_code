# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much
# water it can trap after raining.

# Example 1: Input: height = [0,1,0,2,1,0,1,3,2,1,2,1] Output: 6 Explanation: The above elevation map (black section)
# is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being
# trapped.
# Example 2:
# Input: height = [4,2,0,3,2,5]
# Output: 9

# Constraints:
# n == height.length
# 1 <= n <= 2 * 104
# 0 <= height[i] <= 105

# 思路：
# 1. For each element in the array, we find the maximum level of water it can trap after the rain, which is equal
# to the minimum of maximum height of bars on both the sides minus its own height.

# 2. Using two pointers. As long as
# the height[left] is bigger than height right, the water trapped depends on the right_max. So, we can say that if
# there is a larger bar at one end (say right), we are assured that the water trapped would be dependant on height of
# bar in current direction (from left to right). As soon as we find the bar at reverse_string end (right) is smaller,
# we start iterating in opposite direction (from right to left). We must maintain \text{left\_max}left_max and \text{
# right\_max}right_max during the iteration, but now we can do it in one iteration using 2 pointers,
# switching between the two.

# 3. 注意这种算法下，固定的那一边一定是当前最高的bar。当左边移动时，说明此时最高的是height[r]，所以water trapped可以直接用
#    left_max - height[l],因为可以确认left_max没有height[r]高，否则固定的应该是left_max所在位置。
# 4. Further understanding based on 3: The current maximum height must be the height of index left or index right, so
#    the outer if condition should compare the height of index left and right to find the current maximum value and fix
#    left or right. Then move the other side, and use the previous maximum height of that side minus current height to
#    get the water that can be trapped.

# 5. presum, 用两个list. Need to pay attention that the maximum value of left side and right side should include the
#    height of the current index. In this way, if the maximum value is the height of current index, the number of water
#    add to res will be 0. Otherwise, the number of water added to the res could be negative.

class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        area = 0
        max_left = max_right = 0
        l = 0
        r = len(height) - 1
        while l < r:
            if height[l] < height[r]:    # 注意外层判断比较的是left和right所在位置的值，使得固定位置是当前最高值，如果比leftmax和
                # rightmax会滞后（自己猜测，因为leftmax的更新在内层判断，答案不对）
                if height[l] > max_left:
                    max_left = height[l]
                else:
                    area += max_left - height[l]
                l += 1
            else:
                if height[r] > max_right:
                    max_right = height[r]
                else:
                    area += max_right - height[r]
                r -= 1

        return area


class Solution2:
    def trap(self, height: List[int]) -> int:
        left = [0] * len(height)
        right = [0] * len(height)
        left_max = right_max = 0

        for i in range(len(height)):
            left_max = max(left_max, height[i])
            left[i] = left_max

        for i in range(len(height) - 1, -1, -1):
            right_max = max(right_max, height[i])
            right[i] = right_max

        res = 0
        for i in range(len(height)):
            h = min(left[i], right[i])
            res += h - height[i]
        return res
