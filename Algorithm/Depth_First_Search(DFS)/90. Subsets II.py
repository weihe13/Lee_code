# Given an integer array nums that may contain duplicates, return all possible subsets (the power set).
# The solution set must not contain duplicate subsets. Return the solution in any order.

# Example 1:
# Input: nums = [1,2,2]
# Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
# Example 2:
# Input: nums = [0]
# Output: [[],[0]]

# Constraints:
#
# 1 <= nums.length <= 10
# -10 <= nums[i] <= 10

# 思路：1. DFS,关键是要通过sort去重，exclude duplicated case。自己一开始没想到sort，用seen(set)去重，每次调用recursion时输入一个新的
#         空的seen，保证对于[2,4,4,4,1,4], 每层循环内不会有重复case，比如[2,4,1]，只会有一个。因为第一个4加到本层的seen后，后面两个4不
#         会再形成新的[2,4,1]。并且因为调用下层recursion时，传入的的是一个新的seen，所以仍然能形成[2,4,4,1]，因为第二个4来自下层recursion。
#         但问题是这时还会形成[2,1,4],不符合条件。所以必须先sort，就能防止这种情况。
#      2. sort后去重也不再需要seen（虽然可以用），直接判断i>0时nums[i]!=nums[i-1]即可去重。
#      3. 时间复杂度：O(N*2^N), 空间复杂度：O(N).
#      4. 也可以DP，去重方法一样。

# 自己写法，seen去重，没必要
class Solution:
    def __init__(self):
        pass

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        nums.sort()  # 帮助去重
        seen = set()
        for i in range(len(nums)):  # 用seen去重的关键是每层要传入一个新的seen
            if nums[i] not in seen:
                seen.add(nums[i])
                self.dfs(nums[i + 1:], [nums[i]], res, set())
        return res

    def dfs(self, nums, curr, res, seen):
        res.append(curr)
        for i in range(len(nums)):
            if nums[i] not in seen:
                seen.add(nums[i])
                self.dfs(nums[i + 1:], curr + [nums[i]], res, set())


# 优化
class Solution2:
    def __init__(self):
        pass

    def subsetsWithDup(self, nums):
        ret = []
        self.dfs(sorted(nums), [], ret)
        return ret

    def dfs(self, nums, path, ret):
        ret.append(path)  # 注意这里dfs不需要终止条件，nums为空自然就结束返回了
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            self.dfs(nums[i + 1:], path + [nums[i]], ret)


# DP
class Solution3:
    def __init__(self):
        pass

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        nums.sort()

        for i in range(len(nums)):
            if i == 0 or nums[i] != nums[i - 1]:
                l = len(res)  # 关键是不相等时才更新l
            res += [res[j] + [nums[i]] for j in range(len(res) - l, len(res))] # 前面l个位置不更新，因为前一个相同的数已经加过了

        return res
