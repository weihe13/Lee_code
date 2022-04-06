# Given an array of integers nums, sort the array in ascending order.

# Example 1:
# Input: nums = [5,2,3,1]
# Output: [1,2,3,5]
# Example 2:
# Input: nums = [5,1,1,2,0,0]
# Output: [0,0,1,1,2,5]

# Constraints:
# 1 <= nums.length <= 5 * 104
# -5 * 104 <= nums[i] <= 5 * 104

# 思路： 普通quick sort和 merge sort见sort总结
#       1. 优化的quick sort：思路一样，把小于mid的数丢到左边，大于mid的数丢到右边，再recursion左边和右边的list。
#       2. i代表从左往右第一个大于mid的位置，j代表从右往左第一个小于mid的位置，当找到这两个位置后，如果i小于j，就交换两者位置，继续循环。
#          当i > j 时，i左边的都是小于等于mid的，j右边的都是大于等于mid的，所以i位置一定第一个大于mid的数，j位置一定是第一个小于mid的数，
#          这时把start位置和j互换，就能使得mid位置左边都小于它，右边都大于它。recursion下去，直到子list只有一个数。

# 记忆：left和right比较有等号，和qivot比较没有等号。
class Solution_:
    def sortArray(self, nums: List[int]) -> List[int]:
        self.quicksort(nums, 0, len(nums) - 1)
        return nums

    def quicksort(self, nums, start, end):
        if start >= end:
            return

        qivot = nums[(start + end) // 2]
        i = start
        j = end

        while i <= j: # 这里必须有等号，才能让结束循环的时候i > j, 否则结束的时候可能i==j，导致输入[1,2]，输出[1]和[1,2],无限循环
            while i <= j and nums[i] < qivot: # 这里第二个判断不能有=, 否则如果很多数相等则无法均分
                i += 1
            while i <= j and nums[j] > qivot:
                j -= 1
            if i <= j:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1

        self.quicksort(nums, start, j)  # 这里不是切片，j位置是能取到的，且j位置的数一定小于等于qivot
        self.quicksort(nums, i, end)  # i位置的数一定大于等于qivot


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        self.quicksort(nums, 0, len(nums) - 1)
        return nums

    def quicksort(self, nums, start, end):
        if start >= end:
            return

        mid = start + (end - start) // 2
        # 自己理解：如果原array大小完全随机，是否取mid没有影响。但如果原array是1-50000个数按顺序排好了，每次recusion需要遍历的元素个数
        # 就是n-1, n-2, n-3..时间复杂度还是O(n^2).quick sort关键是分成两个sub array后理想情况下每次需要遍历的元素直接减半，时间复杂
        # 度就是O(nlog(n)).
        nums[start], nums[mid] = nums[mid], nums[start]
        i = start + 1
        j = end

        while i <= j:
            while i <= j and nums[i] <= nums[start]: # 等于的情况既放左边也放右边，防止有大量相同的数时不能均分
                i += 1
            while i <= j and nums[j] >= nums[start]:
                j -= 1
            if i < j:   # 如果i小于j，互换i，j位置的值，继续循环。
                nums[i], nums[j] = nums[j], nums[i]

        nums[start], nums[j] = nums[j], nums[start]
        self.quicksort(nums, start, j - 1) # j位置（原mid的值）不用包含在内,包含在内会recursion limit使得堆栈溢出。
        self.quicksort(nums, j + 1, end)   # j位置（原mid的值）不用包含在内，包含在内会recursion limit使得堆栈溢出。
