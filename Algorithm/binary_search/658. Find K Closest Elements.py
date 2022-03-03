# Given a sorted integer array arr, two integers k and x, return the k closest integers to x in the array. The result
# should also be sorted in ascending order. An integer a is closer to x than an integer b if:

# |a - x| < |b - x|, or
# |a - x| == |b - x| and a < b

# Example 1:
# Input: arr = [1,2,3,4,5], k = 4, x = 3
# Output: [1,2,3,4]
# Example 2:
# Input: arr = [1,2,3,4,5], k = 4, x = -1
# Output: [1,2,3,4]

# Constraints:
# 1 <= k <= arr.length
# 1 <= arr.length <= 104
# arr is sorted in ascending order.
# -104 <= arr[i], x <= 104

# 思路：1. 找最接近target的数，想到二分法。OOOXXX模型，先找到第一个X(大于等于target的数)，在找k个最接近的
#      2. 要求是sorted result，而原数组就是sorted，所以先找index，然后直接return满足条件的index顺序的原数组。
#      3. 注意代码的可理解性，先用一个二分找到第一个X，再写主程序判断k个最接近的。判断最接近的数时，因为还要考虑index是否valid，以及left
#         right 哪个更接近，如果写在主程序中判断，也很长，所以再写一个单独的function去判断。

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        right = self.find_upper_closest(arr, x)  # 等于x或第一个大于x的数
        left = right - 1  # right-1一定就是小于x的最接近x的数

        for _ in range(k):
            if self.isleftcloser(arr, x, left, right):
                left -= 1
            else:
                right += 1
        return arr[left + 1:right]

    def find_upper_closest(self, arr, x):
        start, end = 0, len(arr) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if arr[mid] >= x:
                end = mid
            else:
                start = mid
        if arr[start] >= x:
            return start
        if arr[end] >= x:
            return end
        return len(arr)  # 因为return的要是第一个大于或等于target的值，这样right-1才小于target，所以
        # 如果end小于x，就要return end+1,就是len(arr)

    def isleftcloser(self, arr, x, left, right):
        if left < 0:
            return False   # 如果left<0,直接往右找
        if right >= len(arr):
            return True    # 如果right>=len,不用判断了（判断也报错），直接往左找
        return x - arr[left] <= arr[right] - x