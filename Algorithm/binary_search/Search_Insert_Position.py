# Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return
# the index where it would be if it were inserted in order.
# You must write an algorithm with O(log n) runtime complexity.

# Example 1:
# Input: nums = [1,3,5,6], target = 5
# Output: 2
# Example 2:

# Input: nums = [1,3,5,6], target = 2
# Output: 1
# Example 3:

# Input: nums = [1,3,5,6], target = 7
# Output: 4

# 这类binary search的题注意两点：
# 1. 判断是否继续循环的条件里含等号
# 2. 最后return left


class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0
        right = len(nums) - 1
        while left <= right:
            m = left + (right - left)//2
            if nums[m] < target:
                left = m + 1
            elif nums[m] > target:
                right = m - 1
            else:
                return m
        return left