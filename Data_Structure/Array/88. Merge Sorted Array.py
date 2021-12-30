# You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n,
# representing the number of elements in nums1 and nums2 respectively. Merge nums1 and nums2 into a single array
# sorted in non-decreasing order.The final sorted array should not be returned by the function, but instead be stored
# inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the
# elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

# Example 1:
# Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
# Output: [1,2,2,3,5,6]
# Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
# The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.
#
# Example 2:
# Input: nums1 = [1], m = 1, nums2 = [], n = 0
# Output: [1]
# Explanation: The arrays we are merging are [1] and [].
# The result of the merge is [1].
#
# Example 3: Input: nums1 = [0], m = 0, nums2 = [1], n = 1 Output: [1] Explanation: The arrays we are merging are []
# and [1]. The result of the merge is [1]. Note that because m = 0, there are no elements in nums1. The 0 is only
# there to ensure the merge result can fit in nums1.

# Constraints:
# nums1.length == m + n
# nums2.length == n
# 0 <= m, n <= 200
# 1 <= m + n <= 200
# -109 <= nums1[i], nums2[j] <= 109
#
# Follow up: Can you come up with an algorithm that runs in O(m + n) time?

# 思路：Three pointers(start from the end-为了避免overwriting) The algorithm is similar to before, except this time we set
# p1 to point at index m - 1 of nums1, p2 to point at index n - 1 of nums2, and p to point at index m + n - 1 of
# nums1. This way, it is guaranteed that once we start overwriting the first m values in nums1, we will have already
# written each into its new position. In this way, we can eliminate the additional space.
#
# Interview Tip: Whenever you're trying to solve an array problem in-place, always consider the possibility of
# iterating backwards instead of forwards through the array. It can completely change the problem, and make it a lot
# easier.

# 注意： 1. range到-1，是为了取到位置0，否则p取不到0
#       2. 第二个if的判断条件必须是p1 >= 0 and nums1[p1] > nums2[p2],
#          如果反过来，改为p2>=0 and nums1[p1]<nums2[2],else中就会包含p1<0的情况。
#          (不用担心p2小于0， 因为第一个if就是判断了p2小于0的情况)

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        # Set p1 and p2 to point to the end of their respective arrays.
        p1 = m - 1
        p2 = n - 1

        # And move p backwards through the array, each time writing
        # the smallest value pointed at by p1 or p2.
        for p in range(n + m - 1, -1, -1):
            if p2 < 0:
                break
            if p1 >= 0 and nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1

