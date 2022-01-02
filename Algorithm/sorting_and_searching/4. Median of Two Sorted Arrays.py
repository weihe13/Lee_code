# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
# The overall run time complexity should be O(log (m+n)).

# Example 1:
# Input: nums1 = [1,3], nums2 = [2]
# Output: 2.00000
# Explanation: merged array = [1,2,3] and median is 2.
# Example 2:
# Input: nums1 = [1,2], nums2 = [3,4]
# Output: 2.50000
# Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

# Constraints:
# nums1.length == m
# nums2.length == n
# 0 <= m <= 1000
# 0 <= n <= 1000
# 1 <= m + n <= 2000
# -106 <= nums1[i], nums2[i] <= 106

# 思路： 1. 在merge sorted array的基础上算media，但不知是否满足time complexity
#       2. 用list的extend和sort的function，但不知能不能用

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        l1, l2 = len(nums1), len(nums2)
        nums1[l1:l1 + l2] = [0 for i in range(l2)]

        p1 = l1 - 1
        p2 = l2 - 1

        # And move p backwards through the array, each time writing
        # the smallest value pointed at by p1 or p2.
        for p in range(l1 + l2 - 1, -1, -1):
            if p2 < 0:
                break
            if p1 >= 0 and nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
        l = l1 + l2
        if l % 2 == 0:
            return (nums1[l // 2 - 1] + nums1[l // 2]) / 2
        else:
            return nums1[(l - 1) // 2]

#         nums1.extend(nums2) #this is now the merged array of size M + N
#         nums1.sort() #this will take M+N*log(M+N) Time
#         size = len(nums1)

# 		#if the size of the merged array is odd
#         if size % 2 != 0:
#             mid = size // 2
#             return float(nums1[mid])

# 		#if the size of merged array is even
#         else:
#             mid = size // 2
#             return (nums1[mid] + nums1[mid-1]) / 2


