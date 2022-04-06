# Given an array of n positive integers and a positive integer s, find the minimal length of a subarray of which the
# sum ≥ s. If there isn't one, return -1 instead.
#
# Example
# Example 1:
#
# Input: [2,3,1,2,4,3], s = 7
# Output: 2
# Explanation: The subarray [4,3] has the minimal length under the problem constraint.
# Example 2:
#
# Input: [1, 2, 3, 4, 5], s = 100
# Output: -1
# Challenge
# If you have figured out the O(nlog n) solution, try coding another solution of which the time complexity is O(n).

# 思路： 1. 双指针算法，右指针不回头，因为回头以后curr_sum更小，不可能找到答案
#       2. 时间复杂度：O(2N)=O(N)，外层循环O(N),内层也是O(N),不回头，相加关系
#          空间复杂度：O(1)

class Solution:
    """
    @param nums: an array of integers
    @param s: An integer
    @return: an integer representing the minimum size of subarray
    """

    def __init__(self):
        pass

    def minimum_size(self, nums: List[int], s: int) -> int:
        # write your code here
        if not nums:
            return -1

        res = float('inf')
        left, right = 0, 0
        curr = nums[left]
        while left <= len(nums) - 1:
            while curr < s:
                right += 1
                if right <= len(nums) - 1:
                    curr += nums[right]
                else:
                    break
            if curr >= s:
                curr_res = right - left + 1
                res = min(res, curr_res)
                curr -= nums[left]
                left += 1
            else:
                break

        if left == 0:
            return -1
        return res