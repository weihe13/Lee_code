# Description
# Given an array of integers, find a contiguous subarray which has the largest sum.
#
# The subarray should contain at least one number.
#
# Example
# Example 1:
#
# Input:
#
# nums = [−2,2,−3,4,−1,2,1,−5,3]
# Output:
#
# 6
# Explanation:
#
# the contiguous subarray [4,−1,2,1] has the largest sum = 6.
# Example 2:
#
# Input:
#
# nums = [1,2,3,4]
# Output:
#
# 10
# Explanation:
#
# the contiguous subarray [1,2,3,4] has the largest sum = 10.
#
# Challenge
# Can you do it in time complexity O(n)?

# Logic: 1. All the subarray can be represent as the subarray from 0 index to current index exclude a pre_subarray. So
#           we only need to update the minimum sum of pre_subarray and use the sum of current subarray from index 0 to
#           current index to minus minimum presum,to get the currmax. Then compare the currmax and the global max and
#           update the global max.（对subarray的选择就体现在pre_sum-minimum, 因为减的是minimum，等于选择的是以minmum 后的那个
#           index为起始位置的subarray，意思是以当前index结尾的最大subarray）
#        2. DP

class Solution:
    """
    @param nums: A list of integers
    @return: A integer indicate the sum of max subarray
    """

    def max_sub_array(self, nums: List[int]) -> int:
        # write your code here
        maximum = pre_sum = nums[0]
        minimum = min(nums[0], 0)  # 这里要注意，如果nums[0]为正，minimum就是不选nums[0],就是0

        for num in nums[1:]:
            pre_sum += num
            maximum = max(maximum, pre_sum - minimum)
            minimum = min(minimum, pre_sum)

        return maximum


class Solution:
    """
    @param nums: A list of integers
    @return: A integer indicate the sum of max subarray
    """

    def max_sub_array(self, nums: List[int]) -> int:
        # write your code here
        maximum = curr = nums[0]
        for num in nums[1:]:
            curr = max(num, num + curr)
            maximum = max(maximum, curr)

        return maximum
