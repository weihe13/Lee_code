# Given an integer array nums and an integer k, return the kth largest element in the array.
# Note that it is the kth largest element in the sorted order, not the kth distinct element.

# Example 1:
# Input: nums = [3,2,1,5,6,4], k = 2
# Output: 5
# Example 2:
# Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
# Output: 4

# Constraints:
# 1 <= k <= nums.length <= 104
# -104 <= nums[i] <= 104

# 思路： 1. heap
#       2. quick sort

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        res = self.find_kth_largest(nums, 0, len(nums) - 1, k - 1)
        return res

    def find_kth_largest(self, nums, start, end, k):
        if start >= end:
            return nums[k]

        left, right = start, end
        qivot = nums[(left + right) // 2]
        while left <= right:
            while left <= right and nums[left] > qivot:
                left += 1
            while left <= right and nums[right] < qivot:
                right -= 1
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        if k <= right:
            return self.find_kth_largest(nums, start, right, k)
        elif k >= left:
            return self.find_kth_largest(nums, left, end, k)
        return nums[k]

class Solution2:
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        return heapq.nlargest(k, nums)[-1]