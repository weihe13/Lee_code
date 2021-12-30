# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero
# elements. Note that you must do this in-place without making a copy of the array.

# Example 1:
# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]
# Example 2:
# Input: nums = [0]
# Output: [0]
#
# Constraints:
# 1 <= nums.length <= 104
# -231 <= nums[i] <= 231 - 1

# Follow up: Could you minimize the total number of operations done?

# 思路：1. 如果不是0，就往前换
#      2. 活用pop
#      3. 自己思路：先加0，在去掉0
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # 不是0就往前换
        pos = 0

        for i in range(len(nums)):
            el = nums[i]
            if el != 0:
                nums[pos], nums[i] = nums[i], nums[pos]
                pos += 1

        #  My answer:
        # i = 0
        # for c in range(len(nums)):
        #     if nums[c] == 0:
        #         nums.append(0)
        #         i += 1
        # for j in range(i):
        #     nums.remove(0)

        # 用count去记录已经判断了多少个数，因为如果i位置是0，i不会变
        # i = count = 0
        # while count < len(nums):
        #     if nums[i] == 0:
        #         nums.append(nums.pop(i))
        #     else:
        #         i += 1
        #     count += 1
