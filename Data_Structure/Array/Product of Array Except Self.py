# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements
# of nums except nums[i].
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
# You must write an algorithm that runs in O(n) time and without using the division operation.

# Example 1:
# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]

# Example 2:
# Input: nums = [-1,1,0,-3,3]
# Output: [0,0,9,0,0]

# Constraints:
# 2 <= nums.length <= 105
# -30 <= nums[i] <= 30
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

# Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space
# for space complexity analysis.)

# 思路：
# 1. set two lists to record the product of prefix and product suffix of each position in nums.
# 2. the product of prefix and suffix of the same position is the answer for the position.
# 注意：set L 和 R两个lists时，因为第一个元素是1，所以for循环的range是（1, n）和reverse(range(n-1)

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # The length of the input array
        length = len(nums)

        # The left and right arrays as described in the algorithm
        L, R, answer = [0] * length, [0] * length, [0] * length

        # L[i] contains the product of all the elements to the left
        # Note: for the element at index '0', there are no elements to the left,
        # so the L[0] would be 1
        L[0] = 1
        for i in range(1, length):
            # L[i - 1] already contains the product of elements to the left of 'i - 1'
            # Simply multiplying it with nums[i - 1] would give the product of all
            # elements to the left of index 'i'
            L[i] = nums[i - 1] * L[i - 1]

        # R[i] contains the product of all the elements to the right
        # Note: for the element at index 'length - 1', there are no elements to the right,
        # so the R[length - 1] would be 1
        R[length - 1] = 1
        for i in reversed(range(length - 1)):
            # R[i + 1] already contains the product of elements to the right of 'i + 1'
            # Simply multiplying it with nums[i + 1] would give the product of all
            # elements to the right of index 'i'
            R[i] = nums[i + 1] * R[i + 1]

        # Constructing the answer array
        for i in range(length):
            # For the first element, R[i] would be product except self
            # For the last element of the array, product except self would be L[i]
            # Else, multiple product of all elements to the left and to the right
            answer[i] = L[i] * R[i]

        return answer

#         L = [1]
#         R = [1]
#         l = 1
#         r = 1
#         n = len(nums)

#         for i in range(1, n):
#             l *= nums[i-1]
#             L.append(l)

#         for i in range(1, n):
#             r *= nums[n-i]
#             R.append(r)
#         R.reverse()

#         res = []
#         for i in range(n):
#             prob = L[i]*R[i]
#             res.append(prob)

#         return res

# 自己方法，硬做，速度慢，空间大
# import numpy as np
# res = []
# diction = {}
# for i in range(len(nums)):
#     num = nums.pop(i)
#     if num in diction:
#         res.append(diction[num])
#     else:
#         p = np.prod(nums)
#         res.append(p)
#         diction[num] = p
#     nums.insert(i, num)
# return res