# Given an integer array nums, return the number of triplets chosen from the array that can make triangles if we take
# them as side lengths of a triangle.

# Example 1:
#
# Input: nums = [2,2,3,4]
# Output: 3
# Explanation: Valid combinations are:
# 2,3,4 (using the first 2)
# 2,3,4 (using the second 2)
# 2,2,3
# Example 2:
#
# Input: nums = [4,2,3,4]
# Output: 4
#
#
# Constraints:
#
# 1 <= nums.length <= 1000
# 0 <= nums[i] <= 1000

# 思路：1. 这题如果要列举所有可能的组合，那时间复杂度不能低于O(n3)，因为如果array全是1，那满足条件的组合是n个数里取三个，有多少取法就有多少
#         满足条件，所以满足条件的组合就有n*(n-1)*(n-2)/6个，就是O(n3)的时间复杂度。
#      2. 这题要求是数有多少个，那么可以达到更快的时间复杂度，先sort，那么找到一个满足条件的left和right后，left往右一直到right-1位置都
#         可以和right位置组成满足条件的组合，先加上right-left个满足条件的情况后，再将right向左移动。需要注意这时left不用再从头开始，就从
#         当前位置开始判断就可以了。因为left左边的数更小，它们+right位置的数都无法大于第三个数，加right-1位置更不可能。
#      3. 时间复杂度，n^2, 空间复杂度 logn，因为sort takes logn space.

# 注意比较下面两种写法的不同，推荐第一种
class Solution1:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        count = 0
        for i in range(2, len(nums)):
            left, right = 0, i - 1
            while left < right:
                if nums[left] + nums[right] <= nums[i]: # 这里不用考虑下标越界问题，因为left<right才进入循环，每次只+1
                    left += 1
                else:
                    count += right - left
                    right -= 1
        return count


class Solution2:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        count = 0
        for i in range(2, len(nums)):
            left, right = 0, i - 1
            while left < right:
                # 内层循环也要判断left<right，否则会出现left>right,count加上一个负数
                while left < right and nums[left] + nums[right] <= nums[i]:
                    left += 1

                # if left < right: 因为上面的内层也判断了left<right,因此这里不需要了
                count += right - left
                right -= 1
        return count