# Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same
# color are adjacent, with the colors in the order red, white, and blue. We will use the integers 0, 1,
# and 2 to represent the color red, white, and blue, respectively. You must solve this problem without using the
# library's sort function.

# Example 1:
# Input: nums = [2,0,2,1,1,0]
# Output: [0,0,1,1,2,2]
# Example 2:
# Input: nums = [2,0,1]
# Output: [0,1,2]

# Constraints:
# n == nums.length
# 1 <= n <= 300
# nums[i] is either 0, 1, or 2.
# Follow up: Could you come up with a one-pass algorithm using only constant extra space?

# 思路： 1. 先count，再sort
#       2. 看到0就往前移，看到2就往后移，标记0和2的边界

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        p0 = curr = 0
        p2 = len(nums) - 1
        while curr <= p2:  # 注意p2的位置是没有判断过的，所以要一直判断到p2
            if nums[curr] == 0:
                nums[p0], nums[curr] = nums[curr], nums[p0]
                p0 += 1
                # 这里必须有curr += 1,否则如果第一个数就是0，会造成curr<p0，就完全乱套了。必须使得curr>=p0
                # 且如果第一个数是0，互换后p0 curr一起+1，如果第一个数是1，curr+1,p0不变，如果第一个数是2，互换后curr和p0都不变，
                # 无论哪种情况，curr一定会大于等于p0，从p0位置换到curr的数一定已经检查过了（curr==p0换过来的p0就是0，curr>p0换过来的
                # p0就是1，无论哪种情况都可以curr+=1，检查下一个）
                curr += 1
            elif nums[curr] == 2:    # 要注意必须用elif，为什么？
                nums[p2], nums[curr] = nums[curr], nums[p2]
                # curr += 1 注意：互换curr和p2后，curr不能+1，因为换过来的原p2位置的数没有检查过，可能还是2
                p2 -= 1
            else:
                curr += 1
        return nums
# 一样的思路，只是通过判断i和j的大小来避免p0超过curr
class Solution_1:
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i = 0
        k = len(nums)-1
        j = i
        while j <= k:
            if i < j and nums[j] == 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
            elif nums[j] == 2:
                nums[j], nums[k] = nums[k], nums[j]
                k -= 1
            else:
                j += 1
# Time complexity: O(N) since it's one pass along the array of length NN.
# Space complexity: O(1) since it's a constant space solution.

class Solution2:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = collections.Counter(nums)
        idx = 0
        for k in range(3):
            for i in range(count[k]):
                nums[idx] = k
                idx += 1
        return nums