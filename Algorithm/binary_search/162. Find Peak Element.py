# A peak element is an element that is strictly greater than its neighbors. Given an integer array nums, find a peak
# element, and return its index. If the array contains multiple peaks, return the index to any of the peaks. You may
# imagine that nums[-1] = nums[n] = -∞. You must write an algorithm that runs in O(log n) time.

# Example 1: Input: nums = [1,2,3,1] Output: 2 Explanation: 3 is a peak element and your function should return the
# index number 2. Example 2: Input: nums = [1,2,1,3,5,6,4] Output: 5 Explanation: Your function can return either
# index number 1 where the peak element is 2, or index number 5 where the peak element is 6.

# Constraints:
# 1 <= nums.length <= 1000
# -231 <= nums[i] <= 231 - 1
# nums[i] != nums[i + 1] for all valid i.

# 思路： 1. constrains 和 条件给了提示，相邻的数不相等，是可以用二分法
#       2. nums[-1], nums[n] 都是负无穷大，意味着-1 到 n个位置一定有一个peak，每次二分的时候也是判断mid处于上坡还是下坡，如果下坡则左边
#          一定有peak，如果上坡则右边一定有peak，如果左右都比mid小，则mid本身是peak。
#       3. 二分法的本质是找有解的部分

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left + 1 < right:
            mid = (left + right) // 2
            if nums[mid] < nums[mid - 1]:
                right = mid
            elif nums[mid] < nums[mid + 1]:
                left = mid
            else:
                return mid

        if nums[left] > nums[right]:
            return left
        return right

