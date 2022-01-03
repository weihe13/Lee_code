# Given an integer array nums and an integer k, return the number of good subarrays of nums.
# A good array is an array where the number of different integers in that array is exactly k.
# For example, [1,2,3,1,2] has 3 different integers: 1, 2, and 3. A subarray is a contiguous part of an array.

# Example 1: Input: nums = [1,2,1,2,3], k = 2 Output: 7 Explanation: Subarrays formed with exactly 2 different
# integers: [1,2], [2,1], [1,2], [2,3], [1,2,1], [2,1,2], [1,2,1,2]
# Example 2:
# Input: nums = [1,2,1,3,4], k = 3
# Output: 3
# Explanation: Sub arrays formed with exactly 3 different integers: [1,2,1,3], [2,1,3], [1,3,4].

# Constraints:
# 1 <= nums.length <= 2 * 104
# 1 <= nums[i], k <= nums.length
#
#
# 思路：1. The idea is: we maintain two pointers left, right which point to the start and end of the shortest good array
#         ends on right. we maintain the number of good arrays ends on right. On right+1, there's two situation:
#         3.1. By appending the element to the shortest good array ends on right, it is still good. This means we can
#              safely extend all good arrays ends on right with the element on right+1.
#         3.2 By appending the element to the shortest good array ends on right, it is not good. We don't extend any
#              of the previous in this case.
#         Now we've handled all cases by extending previous good arrays, we then keep moving left to get the new
#         shortest good array. In this process, any arrays encountered are always good. In the worst case, we process
#         every element two times, thus the worst time complexity is O(n) where n is the number of elements.
#      2. 关键是，要maintain the number of good array ends on the right. 当达到len == k，每实现一次left += 1, 意味着增加一个
#         good array. 所以把所有以这个right结尾的good array的数量用 prev_good记录下来，当right再次移动一位并且len仍然满足要求时，
#         意味着之前prev_good个array加上新num后仍然good，另外每次left移动一次，会形成一个新的left-right组合，所以会单独增加1个array，
#         因此left每成功移动一次，合计增加prev_good+1个good array.
#      3. 两种情况：1）当right移动后len == k，就是第二点所说情况。2）当right移动后len>k，因为此时counter[nums[left]]一定等于1，否则
#         第一种情况的while会继续循环，所以left+1一定会形成一个新的good array，但不一定是最短，所以可以同理移动left。
#      4. 在没有第一次实现len == k之前prev_good是0，实现后prev_good很可能大于1，所以不管是第一次实现len==k(第一次找到新的数字组合),
#         还是之后每一次找到新的数字组合，都要重新赋值prev_good为1，意为一个新的数字组合找到了。
#      5. 注意每次right往右移动都有可能仍然 len == k，但只有最开始第一次需要prev_good = 1, 之后每次都需要累计prev_good. 所以
#         if prev_good == 0的条件判断很重要。

class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        ret = 0
        prev_good = 0
        counter = dict()
        left, right = 0, 0

        # keep moving right
        for right in range(len(nums)):
            counter[nums[right]] = counter.setdefault(nums[right], 0) + 1

            # now we have k distinct
            if len(counter.keys()) == k:
                # the first time we meet k distinct
                if prev_good == 0:
                    prev_good = 1

                # we can move left to find the shortest good to get new good
                while counter[nums[left]] > 1:
                    counter[nums[left]] -= 1
                    left += 1
                    prev_good += 1
            # now we have more than k distinct
            elif len(counter.keys()) > k:
                # we remove the first of previous shortest good and appending the right
                # to get a new good
                prev_good = 1
                counter.pop(nums[left])
                left += 1

                # we can move left to reach the shortest good to get new good
                while counter[nums[left]] > 1:
                    counter[nums[left]] -= 1
                    left += 1
                    prev_good += 1
            ret += prev_good
        return ret