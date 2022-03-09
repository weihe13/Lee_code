# Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c],
# nums[d]] such that:

# 0 <= a, b, c, d < n
# a, b, c, and d are distinct.
# nums[a] + nums[b] + nums[c] + nums[d] == target
# You may return the answer in any order.

# Example 1:
# Input: nums = [1,0,-1,0,-2,2], target = 0
# Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
# Example 2:
# Input: nums = [2,2,2,2,2], target = 8
# Output: [[2,2,2,2]]

# 思路：1. 在3sum的基础上再写一层
#      2. 总结ksum

class Solution1:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            self.threeSum(nums, i, res, target)
        return res

    def threeSum(self, nums, first_idx, res, target):
        for j in range(first_idx + 1, len(nums)):
            if j > first_idx + 1 and nums[j] == nums[j - 1]:
                continue
            self.twoSum(nums, first_idx, j, res, target)

    def twoSum(self, nums, first_idx, second_idx, res, target):
        left, right = second_idx + 1, len(nums) - 1

        while left < right:  # 注意不能有等于号，否则如果left right相等时sums满足条件，同一个数会加两次
            sums = nums[first_idx] + nums[second_idx] + nums[left] + nums[right]
            if sums > target:
                right -= 1
            elif sums < target:
                left += 1
            else:
                res.append([nums[first_idx], nums[second_idx], nums[left], nums[right]])
                right -= 1
                left += 1
                while left <= len(nums) - 1 and nums[left] == nums[left - 1]:
                    left += 1



class Solution2:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()  # sort放在循环外
        res = self.kSum(nums, target, 4)
        return res

    def kSum(self, nums, target, k):
        res = []  # 每一步返回的res中的子list，都含有本层的k对应个数的数字

        if not nums:  # 这步很重要，如果len(nums)<k,循环下去子nums会变成空list，index out of range
            return res

        average = target // k
        if nums[0] > average or nums[-1] < average:
            return res

        if k == 2:
            return self.twoSum(nums, target)

        for i in range(len(nums)):
            if nums[i] > average:
                break
            if i == 0 or nums[i] != nums[i - 1]:
                for subset in self.kSum(nums[i + 1:], target - nums[i], k - 1):
                    res.append([nums[i]] + list(subset))
        return res

    def twoSum(self, nums, target):  # 注意要返回所有可能情况，又不能有重复，如果按原写法，同样的组合会计算两次，
        # 利用tuple+sort+set，去除重复的
        hashmap = {}
        res = set()
        for i in range(len(nums)):
            hashmap[nums[i]] = i
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap and hashmap[complement] != i:
                res.add(tuple(sorted([nums[i], complement])))
        return res