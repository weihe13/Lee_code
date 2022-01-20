# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

# Example 1:
# Input: nums = [1,2,3,1]
# Output: true
# Example 2:
# Input: nums = [1,2,3,4]
# Output: false
# Example 3:

# Input: nums = [1,1,1,3,3,4,3,2,4,2]
# Output: true

# 思路： 1. set 后比长度
#       2. hashmap

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # hashmap = {}
        # for num in nums:
        #     if num in hashmap:
        #         return True
        #     hashmap[num] = hashmap.get(num, 0) + 1
        # return False

        distinct = set(nums)
        if len(distinct) != len(nums):
            return True
        else:
            return False