# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k,
# and j != k, and nums[i] + nums[j] + nums[k] == 0. Notice that the solution set must not contain duplicate triplets.

# Example 1:
# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# Example 2:
# Input: nums = []
# Output: []
# Example 3:
# Input: nums = [0]
# Output: []

# Constraints:
# 0 <= nums.length <= 3000
# -105<= nums[i] <= 105

# 思路： 1. 先sort，确定住第一个数以后，对i+1之后的nums用two sum的思路做。
#          关键是要注意不能有重复的list，所以move i 和move left之前都要先确定nums[i]!=nums[i+1]
#          还有一个细节是当sort以后当nums[i]大于0就不用再判断了，==0是要的，因为有可能是三个0
#       2. hashmap，不排序。为了防止加入重复组合，res设为set，加入的时候加入排序的组合，这样一样的组合不会重复加。

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if i == 0 or nums[i] != nums[i - 1]:  # 因为这里是for循环，i会自动+1，为了没有重复，需要比较i和i-1
                self.twosum(nums, i, res)
        return res

    def twosum(self, nums, i, res):
        left = i + 1
        right = len(nums) - 1

        while left < right:
            sums = nums[i] + nums[left] + nums[right]
            if sums > 0:
                right -= 1
            elif sums < 0:
                left += 1
            else:
                res.append([nums[i], nums[left], nums[right]])
                right -= 1
                left += 1
                while left < right and nums[left] == nums[left - 1]:
                    left += 1


# Time Complexity: O(n2). twoSumII is O(n), and we call it nn times. Sorting the array takes O(nlogn), so overall
# complexity is O(nlogn+n2). This is asymptotically equivalent to O(n2).
# Space Complexity: from O(logn) to O(n), depending on the implementation of the sorting algorithm. For the purpose
# of complexity analysis, we ignore the memory required for the output.

class Solution2:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res, dup = set(), set()
        seen = {}
        for i, val1 in enumerate(nums):
            if val1 not in dup:  # 同样的val1，后循环的不会有更多可能了，只要曾经循环过就跳过，否则3000个0的test过不了
                dup.add(val1)
                for j, val2 in enumerate(nums[i + 1:]):
                    complement = -val1 - val2
                    if complement in seen and seen[complement] == i:  # 说明i到j之间有complement，组合成功
                        res.add(tuple(sorted((val1, val2, complement))))  # tuple(sorted())防止add一样组合
                    seen[val2] = i  # 这步最关键，意思是如果complement不在seen里，就把val2在set中的value更新为i，意思是
                    # nums[i+1:]里含有val2，如果后面的complement在seen中对应的value是i，就说明组合成功。
        return res
