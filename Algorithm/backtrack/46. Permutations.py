# Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any
# order.

# Example 1:
# Input: nums = [1,2,3]
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
# Example 2:
# Input: nums = [0,1]
# Output: [[0,1],[1,0]]
# Example 3:
# Input: nums = [1]
# Output: [[1]]

# Constraints:
# 1 <= nums.length <= 6
# -10 <= nums[i] <= 10
# All the integers of nums are unique.

# 思路：1. Backtracking is an algorithm for finding all solutions by exploring all potential candidates.
#      2. 注意example里如果只有一个数字，也会输出一个listoflist，所以base case return的也是list of list，即[nums[:]].
#      3. base case return时，要return nums.copy()，因为nums是指向一个存储位置，后面会一直改变，要用nums.copy把当前结果保存下来
#         并return。同时注意nums[:]会比nums.copy()快
# (Because the list nums is being modified during the function calls. If you just append it to the output you append a
# reference (pointer) to nums not the actual list which means that after nums is modified from some other recursive
# function it will be "changed" in the output list that stores the reference to nums. In the end, output will contain
# pointers that will point to the same result (whatever was the last change in nums). So you need to make a deep copy
# of nums. I suggest you to look over list aliasing in Python.)
#      4. 用tree图能很好的帮助理解，刚开始先取第一个位置的数，最后返回时它会加到最后，这样循环中每次都取位置0的数，循环n次，保证每次取的数
#         不一样，并且正好能全部循环一遍。
#      5. 注意从树的底端往回走时，有两个地方要加回pop off的数字，一是下层recursion累积的permutation，每一个子list都要加回n；二是nums
#         要加回n，保证每次循环开始pop off 的数字在单次循环结束后加回去(虽然加了回去，但nums在循环的过程中在不断改变，所以每次循环开始
#         时都是pop(0)取第一个位置的数)。
#      6. 每一层recursion开始时，res = [],最后return的res是本层recursion得到的本层nums的permutation(list of list)。

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        # base case:
        if len(nums) == 1:
            return [nums[:]]

        for i in range(len(nums)):
            n = nums.pop(0)
            perms = self.permute(nums)
            for perm in perms:
                perm.append(n)
            nums.append(n)
            res.extend(perms)
        return res


