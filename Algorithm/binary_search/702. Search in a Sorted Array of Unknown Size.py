# This is an interactive problem. You have a sorted array of unique elements and an unknown size. You do not have an
# access to the array but you can use the ArrayReader interface to access it. You can call ArrayReader.get(i) that:
# returns the value at the ith index (0-indexed) of the secret array (i.e., secret[i]), or returns 231 - 1 if the i
# is out of the boundary of the array. You are also given an integer target. Return the index k of the hidden array
# where secret[k] == target or return -1 otherwise.

# You must write an algorithm with O(log n) runtime complexity.

# Example 1:
# Input: secret = [-1,0,3,5,9,12], target = 9
# Output: 4
# Explanation: 9 exists in secret and its index is 4.
# Example 2:
# Input: secret = [-1,0,3,5,9,12], target = 2
# Output: -1
# Explanation: 2 does not exist in secret so return -1.

# Constraints:
# 1 <= secret.length <= 104
# -104 <= secret[i], target <= 104
# secret is sorted in a strictly increasing order.

# 思路：1. 要求time complexity O(logn),想到二分法。
#      2. 先用第一次类似反二分法找到包含target的array，也就是right一开始的值
#      3. 然后就套用二分法模版即可！

class Solution:
    def search(self, reader: 'ArrayReader', target: int) -> int:
        right = self.get_upper_index(reader, target)

        left = 0
        while left + 1 < right:
            mid = (left + right) // 2
            if reader.get(mid) >= target:
                right = mid
            else:
                left = mid
        if reader.get(left) == target:
            return left
        if reader.get(right) == target:
            return right
        return -1

    def get_upper_index(self, reader, target):
        right = 1
        while reader.get(right) < target:
            right *= 2
        return right