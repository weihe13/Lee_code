# Given an array of integers nums and an integer k, return the total number of continuous subarrays whose sum equals
# to k.

# Example 1:
# Input: nums = [1,1,1], k = 2
# Output: 2
# Example 2:
# Input: nums = [1,2,3], k = 3
# Output: 2

# Constraints:
# 1 <= nums.length <= 2 * 104
# -1000 <= nums[i] <= 1000
# -107 <= k <= 107

# 思路：1. 用dict记录对于每一个i，nums[0:i]的和。这样对于任何一个满足条件的subarrays = nums[i:j],一定可以用nums[:j] - nums[:i]找到。
#         比如[3,-1,1,1,1,1,2], k=3. 对于i=5位置，sum(nums[:i]) = 6,diff = 6-3 = 3。这时就找前面有几个presum等于3的就行，有两个
#         就说明有两个满足条件的subarray。
#      2. 因为只循环了一遍，时间复杂度就是O(n), 额外建了一个dictionary，空间复杂度也是O(n).

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        seen = {0: 1}
        res = 0
        currsum = 0

        for num in nums:
            currsum += num
            diff = currsum - k
            if diff in seen:
                res += seen[diff]
            seen[currsum] = seen.get(currsum, 0) + 1

        return res
