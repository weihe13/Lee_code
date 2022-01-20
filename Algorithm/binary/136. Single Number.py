# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
# You must implement a solution with a linear runtime complexity and use only constant extra space.

# Example 1:
# Input: nums = [2,2,1]
# Output: 1
# Example 2:
# Input: nums = [4,1,2,1,2]
# Output: 4
# Example 3:
# Input: nums = [1]
# Output: 1

# Constraints:
# 1 <= nums.length <= 3 * 104
# -3 * 104 <= nums[i] <= 3 * 104
# Each element in the array appears twice except for one element which appears only once.

# 思路：1. sort再找单独的数字，但是空间复杂度应该不满足要求
#      2. 利用bit XOR运算的交换律。
#         If we take XOR of zero and some bit, it will return that bit
#          a ^ 0 = a, a ⊕ 0 = a
#         If we take XOR of two same bits, it will return 0
#          a ^ a = 0, a ⊕ a = 0
#          a ^ b ^ a = (a ^ a) ^ b = 0 ^ b = b, a ⊕ b ⊕ a = (a ⊕ a) ⊕ b = 0 ⊕ b = b

class Solution1:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(1, len(nums), 2):
            if nums[i] != nums[i-1]:
                return nums[i-1] #如果后一个和前一个不一样，return前一个
        return nums[-1] # 如果没有return，说明单独的是最后一个数（没有循环到最后一个数）

class Solution2(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = 0
        for i in nums:
            a ^= i
        return a