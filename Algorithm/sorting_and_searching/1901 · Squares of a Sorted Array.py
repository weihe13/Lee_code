# lintcode
# Given an array of integers A sorted in non-decreasing order, return an array of the squares of
# each number, also in sorted non-decreasing order.

# Example
# Example 1
# Input:
# [-4,-1,0,3,10]
# Output:
# [0,1,9,16,100]
# Example 2
# Input:
# [-7,-3,2,3,11]
# Output:
# [4,9,9,49,121]

# 思路：1. 先算平方，再sort
#      2. 分析：two pointers, 因为最大的平方数只可能由最大正数或者最小负数得到，所以由两边往中间从大往小找，加到list时从len(n)-1到0逆序
#         往里加。

class solution():
    def square_array(self, nums: List[int]) -> List[int]:
        left = 0
        right = len(nums) - 1
        res = [0] * len(nums)   # 这里如果直接res=[]，下面会index out of range
        for i in range(len(nums)-1, -1, -1):
            if abs(nums[left]) <= abs(nums[right]):
                square = nums[right]
                right -= 1
            else:
                square = nums[left]
                left += 1
            sqr = square * square
            res[i] = sqr
        return res