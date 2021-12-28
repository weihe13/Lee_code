class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # m = (left + right)//2 如果大于2**31-1，在C语言和java中会报错
        # 如果while left<right,：
        # 1. [5] 5, 会return -1
        # 2. 取不到list的最后一个数：4+(5-4)//2 == 4

        left = 0
        right = len(nums) - 1
        while left <= right:
            m = left + (right - left) // 2
            if nums[m] == target:
                return m
            elif nums[m] < target:
                left = m + 1
            elif nums[m] > target:
                right = m - 1
        return -1