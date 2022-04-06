# Given an integer array nums of unique elements, return all possible subsets (the power set).
# The solution set must not contain duplicate subsets. Return the solution in any order.

# Example 1:
# Input: nums = [1,2,3]
# Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
# Example 2:
# Input: nums = [0]
# Output: [[],[0]]
# Constraints:
# 1 <= nums.length <= 10
# -10 <= nums[i] <= 10
# All the numbers of nums are unique.

# 思路： 1. DFS：自己写法有added，其实不需要。总结是要把DFS的每个变量代表的意义想清楚，才能思路清晰不容易出错。
#       2. 答案中的DFS(backtrack)：写在一个函数里，更简单
#          时间复杂度：O(N*2^N),方案总数2^N，每次需要O(N)时间把方案copy到res中
#          空间复杂度：O(N)，用O(N)space去maintain curr。
#       3. DP：时间复杂度：O(N*2^N)，空间复杂度：O(N*2^N)。
#          每次都是在当前res中已有subset的基础上，每一个subset加上下一个num得到新的subset

class Solution1:
    def __init__(self):
        pass

    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.dfs(nums, [], res)
        return res

    def dfs(self, nums, curr, res):  # i表示以i位置的数开始的subset，nums表示i==0对应的nums，curr是加上i位置后的subset
        # 不用考虑baseline，nums为空自动就停了
        res.append(curr)
        # list is not hashable，要变成tuple才能判断是否重复
        # 因为每次recursion都是以i开头的不同len的subset，因此不存在重复情况，不用加visited
        for i in range(len(nums)):
            self.dfs(nums[i+1:], curr+[nums[i]], res)  # next nums是不包含nums[i]的


class Solution2:
    def __init__(self):
        pass

    def subsets(self, nums: List[int]) -> List[List[int]]:
        def dfs(start, curr):  # curr是当前要加到res中的subset，start是本次循环的开始位置
            res.append(curr)
            for j in range(start, n):
                dfs(j + 1, curr + [nums[j]])  # 注意下次recusion要加的是curr+[nums[start]], 下次start是j+1

        n = len(nums)
        res = []
        dfs(0, [])
        return res


class Solution3:
    def __init__(self):
        pass

    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]

        for num in nums:
            res += [subset + [num] for subset in res]

        return res


