# You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of
# your product fails the quality check. Since each version is developed based on the previous version, all the versions
# after a bad version are also bad.

# Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following
# ones to be bad.

# You are given an API bool isBadVersion(version) which returns whether version is bad. Implement a function to find
# the first bad version. You should minimize the number of calls to the API.

# Example 1:

# Input: n = 5, bad = 4
# Output: 4
# Explanation:
# call isBadVersion(3) -> false
# call isBadVersion(5) -> true
# call isBadVersion(4) -> true
# Then 4 is the first bad version.


# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 因为每次是用m-1和m+1重新赋值，m一定在left和right之间，不可能等于（m等于left时就是left和right相等）
        # 所以最后一定会形成left==right, 然后：
        # 1. 若该位置为True，则right = m-1<left, 才会停止循环，所以return的是left
        # 2. 若该位置为False，则left = m+1>right, 停止循环，所以依然return left

        left = 0
        right = n

        while left <= right:
            m = left + (right - left) // 2

            if isBadVersion(m):
                right = m - 1
            else:
                left = m + 1
        return left


