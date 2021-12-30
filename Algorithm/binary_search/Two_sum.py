# 注意： 用two pointers 时，nums_copy = nums.copy()可能说没有这个attribution，这时可以用nums[:].



class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        # hashmap = {}
        # for i in range(len(nums)):
        #     hashmap[nums[i]] = i
        # for i in range(len(nums)):
        #     complement = target - nums[i]
        #     if complement in hashmap and hashmap[complement] != i:
        #         return [i, hashmap[complement]]
        # 有相同元素时，hashmap匹配了最后一个的index，第二次循环时再看i和hashmap[complement]是否为同一个。


        numscopy = nums[:]
        nums.sort()
        left = 0
        right = len(nums) - 1
        result = []
        while True:
            if nums[left] + nums[right] == target:
                break
            elif nums[left] + nums[right] > target:
                right -= 1
            else:
                left += 1
        if nums[left] != nums[right]:
            result.append(numscopy.index(nums[left]))
            result.append(numscopy.index(nums[right]))
        else:
            indices = [i for i, x in enumerate(numscopy) if x == nums[left]]
            result = indices[:2]
        return result
