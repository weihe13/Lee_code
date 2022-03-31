# Description
# Given an array of integers, find two non-overlapping subarrays which have the largest sum.
# The number in each subarray should be contiguous.
# Return the largest sum.
# The subarray should contain at least one number

# Example
# Example 1:
# Input:
# nums = [1, 3, -1, 2, -1, 2]
# Output:
# 7
# Explanation:
# the two subarrays are [1, 3] and [2, -1, 2] or [1, 3, -1, 2] and [2].
# Example 2:
# Input:
# nums = [5,4]
# Output:
# 9
# Explanation:
# the two subarrays are [5] and [4].
# Challenge
# Can you do it in time complexity O(n) ?

# 思路：1. 用leecode 53题的思路，左右各走一遍，对每一个位置i，记录nums[:i]和nums[i+1:]的最大sum

class Solution:
    """
    @param nums: A list of integers
    @return: An integer denotes the sum of max two non-overlapping subarrays
    """

    def max_two_sub_arrays(self, nums: List[int]) -> int:
        # write your code here
        if not nums:
            return 0
        n = len(nums)
        left_max, right_max = [0] * n, [0] * n
        curr_left_sum, curr_right_sum = nums[0], nums[-1]
        left_max[0], right_max[-1] = nums[0], nums[-1]

        max_up_to_now = nums[0]  # 0到i位置的目前最大值
        for i in range(1, n):
            curr_left_sum = max(curr_left_sum + nums[i], nums[i])
            max_up_to_now = max(curr_left_sum, max_up_to_now)
            left_max[i] = max_up_to_now

        max_up_to_now = nums[-1]  # n-1 到i 位置的目前最大值
        for i in range(n - 2, -1, -1):
            curr_right_sum = max(curr_right_sum + nums[i], nums[i])
            max_up_to_now = max(curr_right_sum, max_up_to_now)
            right_max[i] = max_up_to_now

        res = -float('inf')
        for i in range(n - 1): # 注意右list最少得有一个数，所以i不能取到len(nums)-1
            res = max(res, left_max[i] + right_max[i + 1])
        return res