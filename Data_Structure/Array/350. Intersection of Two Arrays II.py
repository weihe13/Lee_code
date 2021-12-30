# Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must
# appear as many times as it shows in both arrays and you may return the result in any order.

# Example 1:
# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2,2]
# Example 2:
# Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# Output: [4,9]
# Explanation: [9,4] is also accepted.

# Constraints:
# 1 <= nums1.length, nums2.length <= 1000
# 0 <= nums1[i], nums2[i] <= 1000

# Follow up:
# What if the given array is already sorted? How would you optimize your algorithm?
# What if nums1's size is small compared to nums2's size? Which algorithm is better?
# What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into
# the memory at once?

# 思路一：Hash Map: We collect numbers and their counts from one of the arrays into a hash map. Then, we iterate along the
# second array, and check if the number exists in the hash map and its count is positive. If so - add the number to
# the result and decrease its count in the hash map.
# 思路二：Sort: 1. Sort nums1 and nums2.
#              2. Initialize i, j and k with zero.
#              3. Move indices i along nums1, and j through nums2:
#              4. Increment i if nums1[i] is smaller.
#              5. Increment j if nums2[j] is smaller.
#              6. If numbers are the same, copy the number into nums1[k], and increment i, j and k.
#              7. Return first k elements of nums1.

# Follow-up Questions:
# What if the given array is already sorted? How would you optimize your algorithm?
# We can use either Approach 2 or Approach 3, dropping the sort of course. It will give us linear time and constant
# memory complexity.

# What if nums1's size is small compared to nums2's size? Which algorithm is better?
# Approach 1 is a good choice here as we use a hash map for the smaller array.

# What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into
# the memory at once?
# If nums1 fits into the memory, we can use Approach 1 to collect counts for nums1 into a hash
# map. Then, we can sequentially load and process nums2. If neither of the arrays fit into the memory, we can apply
# some partial processing strategies: Split the numeric range into subranges that fits into the memory. Modify
# Approach 1 to collect counts only within a given subrange, and call the method multiple times (for each subrange).
# Use an external sort for both arrays. Modify Approach 2 to load and process arrays sequentially.

class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """

        from collections import defaultdict, Counter
        res = []
        if len(nums1) > len(nums2):
            d = Counter(nums1)
            for num in nums2:
                if num in d and d[num] > 0:
                    res.append(num)
                    d[num] -= 1
        else:
            d = Counter(nums2)
            for num in nums1:
                if num in d and d[num] > 0:
                    res.append(num)
                    d[num] -= 1
        return res