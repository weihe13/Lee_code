# There is an integer array nums sorted in ascending order (with distinct values). Prior to being passed to your
# function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array
# is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,
# 7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2]. Given the array nums after the possible rotation
# and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

# You must write an algorithm with O(log n) runtime complexity.
# Example 1:
# Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4
# Example 2:
# Input: nums = [4,5,6,7,0,1,2], target = 3
# Output: -1
# Example 3:
# Input: nums = [1], target = 0
# Output: -1

# Constraints:
# 1 <= nums.length <= 5000
# -104 <= nums[i] <= 104
# All values of nums are unique.
# nums is an ascending array that is possibly rotated.
# -104 <= target <= 104

# 思路：1. 先通过binary search 找到rotate点，再通过binary search 找到target
#      2. one pass binary search，判断时要考虑的是左边是sorted array还是右边是sorted arrya。
#      3. 判断大小的时候，什么时候要含等于号？




class Solution2:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] >= nums[left]:  # 这里一定要含=，为什么？！猜测和//2向下取整有关
                if target >= nums[left] and target < nums[mid]:  # 如果target在左侧排好序的部分
                    right = mid - 1
                else:  # target在右侧混乱的部分
                    left = mid + 1
            else:
                if target > nums[mid] and target <= nums[right]:  # 如果target在右侧排好的部分
                    left = mid + 1
                else:  # target在左侧混乱的部分
                    right = mid - 1
        return -1