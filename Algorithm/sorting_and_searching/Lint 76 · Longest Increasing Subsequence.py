# Given a sequence of integers, find the longest increasing subsequence (LIS).
# You code should return the length of the LIS.
# What's the definition of longest increasing subsequence?
# The longest increasing subsequence problem is to find a subsequence of a given sequence in which the subsequence's
# elements are in sorted order, lowest to highest, and in which the subsequence is as long as possible. This
# subsequence is not necessarily contiguous, or unique.
# https://en.wikipedia.org/wiki/Longest_increasing_subsequence
#
# Example
# Example 1:
# Input:
# nums = [5,4,1,2,3]
# Output:
# 3
# Explanation:
# LIS is [1,2,3]
# Example 2:
# Input:
# nums = [4,2,4,5,3,7]
# Output:
# 4
# Explanation:
# LIS is [2,4,5,7]
# Challenge
# Time complexity O(n^2) or O(nlogn)
# 思路： 1. logn想到binary search
#       2. 这种算法得到的lis不是真正的LIS，想track真正LIS的话需要额外用一个parent List记住每个添加的num的前一个num

class Solution:
    """
    @param nums: An integer array
    @return: The length of LIS (longest increasing subsequence)
    """

    def longest_increasing_subsequence(self, nums: List[int]) -> int:
        # write your code here
        if not nums:
            return 0

        lis = [nums[0]]
        for num in nums[1:]:
            if num > lis[-1]:
                lis.append(num)
            else:
                index = self.get_first_gt(lis, num)
                lis[index] = num  # 如果num比lis中一些值小，就用num替代第一个大于num的值，这样并不会改变num左侧nums的LIS长度，但是
                # 有可能在后面的循环中获得更长的LIS
        return len(lis)

    def get_first_gt(self, nums, target):
        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if nums[mid] > target:
                end = mid
            elif nums[mid] < target:
                start = mid
            else:
                return mid
        if nums[start] >= target:  # 注意这里不能用==，必须是>=, 因为nums[start]和nums[left]都有可能大于target
            return start
        return end