# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum
# and return its sum. A subarray is a contiguous part of an array.

# Example 1:
# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.
# Example 2:

# Input: nums = [1]
# Output: 1
# Example 3:

# Input: nums = [5,4,-1,7,8]
# Output: 23

#Constraints:
# 1 <= nums.length <= 105
# -104 <= nums[i] <= 104

# Follow up: If you have figured out the O(n) solution, try coding another solution using the divide and conquer
# approach, which is more subtle.

# 思路一：Dynamic Programming, Kadane's Algorithm. Whenever you see a question that asks for the maximum or minimum of
# something, consider Dynamic Programming as a possibility. The difficult part of this problem is figuring out when a
# negative number is "worth" keeping in a subarray. As expected, any subarray whose sum is positive is worth keeping.
# Let's start with an empty array, and iterate through the input, adding numbers to our array as we go along.
# Whenever the sum of the array is negative, we know the entire array is not worth keeping, so we'll reset it back to
# an empty array. (A special case is [-2, -1]. We need to keep -1 which is negative.)

# 思路二：Divide and Conquer (recursion)
# Define a helper function that we will use for recursion. This function will take an input
# left and right, which defines the bounds of the array. The return value of this function will be the best possible
# subarray for the array that fits between left and right. If left > right, we have an empty array. Return negative
# infinity. Find the midpoint of our array. This is (left + right) / 2, rounded down. Using this midpoint,
# find the best possible subarray that uses elements from both sides of the array with the algorithm detailed in the
# animation above. The best subarray using elements from both sides is only 1 of 3 possibilities. We still need to
# find the best subarray using only the left or right halves. So, call this function again, once with the left half,
# and once with the right half. Return the largest of the 3 values - the best left half sum, the best right half sum,
# and the best combined sum. Call our helper function with the entire input array (left = 0, right = length - 1).
# This is our final answer, so return it.

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        current_sum = max_sum = nums[0]

        for num in nums[1:]:
            current_sum = max(num, current_sum + num)
            max_sum = max(max_sum, current_sum)
        return max_sum


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        def findBestSubarray(nums, left, right):
            # Base case - empty array.
            if left > right:
                return -math.inf

            mid = (left + right) // 2
            curr = best_left_sum = best_right_sum = 0

            # Iterate from the middle to the beginning.
            for i in range(mid - 1, left - 1, -1):
                curr += nums[i]
                best_left_sum = max(best_left_sum, curr)

            # Reset curr and iterate from the middle to the end.
            curr = 0
            for i in range(mid + 1, right + 1):
                curr += nums[i]
                best_right_sum = max(best_right_sum, curr)

            # The best_combined_sum uses the middle element and
            # the best possible sum from each half.
            best_combined_sum = nums[mid] + best_left_sum + best_right_sum

            # Find the best subarray possible from both halves.
            left_half = findBestSubarray(nums, left, mid - 1)
            right_half = findBestSubarray(nums, mid + 1, right)

            # The largest of the 3 is the answer for any given input array.
            return max(best_combined_sum, left_half, right_half)

        # Our helper function is designed to solve this problem for
        # any array - so just call it using the entire input!
        return findBestSubarray(nums, 0, len(nums) - 1)

