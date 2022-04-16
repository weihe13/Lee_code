# Given a binary array nums, return the maximum length of a contiguous subarray with an equal number of 0 and 1.

# Example 1:
#
# Input: nums = [0,1]
# Output: 2
# Explanation: [0, 1] is the longest contiguous subarray with an equal number of 0 and 1.
# Example 2:
#
# Input: nums = [0,1,0]
# Output: 2
# Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.
#
#
# Constraints:
# 1 <= nums.length <= 105
# nums[i] is either 0 or 1.

# 思路： 1. 因为1100，1010，1001 all meet the requirement. And the res can start from any index. So two pointer may not
#          work. The best way is regard 0 as -1. Then, if the pre sum of two index are same, that means the subarray
#          between them have equal number of 1 and 0. If a subarray have equal number of 1 and 0, its pre sum must be 0.


# My solution is record the presum of every index. Actually we only need to record the first element for each presum.
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        count = 0
        max_length = 0
        table = {0: 0}
        for index, num in enumerate(nums, 1):
            if num == 0:
                count -= 1
            else:
                count += 1

            if count in table:
                max_length = max(max_length, index - table[count])
            else:
                table[count] = index

        return max_length


import collections


class Solution2:  # my solution, waste some space
    def findMaxLength(self, nums: List[int]) -> int:
        dp = [0] * (len(nums) + 1)
        mapping = collections.defaultdict(list)
        mapping[0].append(-1)
        for i in range(len(nums)):
            if nums[i] == 0:
                dp[i + 1] = dp[i] - 1
            else:
                dp[i + 1] = dp[i] + 1
            mapping[dp[i + 1]].append(i)
        res = 0

        for i in mapping.keys():
            if len(mapping[i]) > 1:
                res = max(res, mapping[i][-1] - mapping[i][0])
        return res