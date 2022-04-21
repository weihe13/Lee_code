# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
#
# You must write an algorithm that runs in O(n) time.
#
#
#
# Example 1:
#
# Input: nums = [100,4,200,1,3,2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
# Example 2:
#
# Input: nums = [0,3,7,2,5,8,4,6,0,1]
# Output: 9
#
#
# Constraints:
#
# 0 <= nums.length <= 105
# -109 <= nums[i] <= 109

# Logic: 1. First intuition is sort the input array, then use a loop to iterate each index of the sorted array, if the
#           difference between previous number and current number is exactly 1, we will know it will form a consecutive
#           elements sequence and continue to check the next index. If the difference is bigger than one, that means
#           the current consecutive sequence is stopped, and we can start a new sequence. Some corner cases are if the
#           difference between the adjacent element are 0, we still can continue the consecutive sequence and check the
#           next index. (NlogN)
#        2. Use a hashset to store or the unique value in the input array. Then in the for loop, we just need to check
#           whether the num+1 is in the input array. (N+N~O(N))


class Solution1:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums_sorted = sorted(nums)
        res, curr = 1, 1
        for i in range(1, len(nums)):
            if nums_sorted[i] - nums_sorted[i-1] == 0:
                continue
            elif nums_sorted[i] - nums_sorted[i-1] == 1:
                curr += 1
                res = max(res, curr)
            else:
                curr = 1
        return res


class Solution2:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        nums_set = set(nums)

        for num in nums:
            if num - 1 not in nums_set:
                curr = 1
                curr_num = num
                while curr_num + 1 in nums_set:
                    curr += 1
                    curr_num = curr_num + 1
                res = max(res, curr)
        return res