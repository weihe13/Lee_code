# Winter is coming! During the contest, your first job is to design a standard heater with a fixed warm radius to
# warm all the houses.
#
# Every house can be warmed, as long as the house is within the heater's warm radius range.
#
# Given the positions of houses and heaters on a horizontal line, return the minimum radius standard of heaters so
# that those heaters could cover all houses.
#
# Notice that all the heaters follow your radius standard, and the warm radius will the same.

# Example 1: Input: houses = [1,2,3], heaters = [2] Output: 1 Explanation: The only heater was placed in the position
# 2, and if we use the radius 1 standard, then all the houses can be warmed.

# Example 2: Input: houses = [1,2,3,4], heaters = [1,4] Output: 1 Explanation: The two heater was placed in the
# position 1 and 4. We need to use radius 1 standard, then all the houses can be warmed. Example 3:
#
# Input: houses = [1,5], heaters = [2]
# Output: 3

# Constraints:
# 1 <= houses.length, heaters.length <= 3 * 104
# 1 <= houses[i], heaters[i] <= 109

# 思路： 1. two pointers, 其实思路和merge两个list很像，因为对于每个house，需要的半径只在和他相邻的两个加热器里选。所以两个指针都不会回头，
#          可以用双指针。可以优化的思路是从index 0 开始，需要比的只是当前加热器的距离和下一个加热器的距离。因为如果当前house已经是和下一个
#          加热器的距离更近了，后面的house值更大，一定也是和下一个加热器的距离更小，所以加热器index可以直接加1。
#       2. 需要注意的是原list没有保证是从小到大排序的，需要sort，最好用sorted，不改变原数组
#       3. binary search也可以用，只需要对加热器list排序，对每个house找到最近的加热器，更新所需半径。因为只需要对加热器list排序，时间
#          复杂度是O(mlogm)排序时间+O(nlogm)n次找的时间。

# 自己写法：可以优化的点，一是need list，二是循环过程中的逻辑可以优化，只需要从heater的index 0开始，一直比较当前heater和下一个heater到当前
#         house的距离。
class Solution:
    def __init__(self):
        pass

    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses = sorted(houses)
        heaters = sorted(heaters)
        need = [0] * len(houses)  # 这里是可以优化的，不需要额外list，用一个needed_index去记录当前最大值就行
        house, heater = 0, 0

        while house <= len(houses) - 1 and heater <= len(heaters) - 1:
            if houses[house] <= heaters[heater]:
                curr = heaters[heater] - houses[house]
                if heater > 0:
                    curr = min(curr, abs(heaters[heater - 1] - houses[house]))
                need[house] = curr
                house += 1
            # 如果heaters小，就heaters加1，保持curr house比curr heater小
            else:
                heater += 1
        # 如果结束是因为heater index 越界了，就说明后面的house 都比heater大，还没有算完，把剩下的算完
        while house <= len(houses) - 1:
            curr = houses[house] - heaters[heater - 1]  # 注意此时heater index 已经越界了
            need[house] = curr
            house += 1

        return max(need)


# 九章写法
class Solution:
    def __init__(self):
        pass

    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses = sorted(houses)
        heaters = sorted(heaters)
        n, m = len(houses), len(heaters)
        i, j = 0, 0
        heat_radius = 0

        while i < n and j < m:
            now_radius = abs(heaters[j] - houses[i])
            next_radius = float('inf')  # 这里很关键，当j==m-1后，now一定小于next，j不会再加一了，因此j不会越界，一定能把houses遍历完
            if j < m - 1:
                next_radius = abs(heaters[j + 1] - houses[i])
            if now_radius < next_radius:
                heat_radius = max(heat_radius, now_radius)
                i += 1
            else:
                j += 1
        return heat_radius


# binary search
class Solution:
    def __init__(self):
        pass

    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        heaters = sorted(heaters)
        res = 0
        for i in range(len(houses)):
            now_radius = self.get_radius(heaters, houses[i])
            res = max(now_radius, res)
        return res

    def get_radius(self, nums, target):
        left, right = 0, len(nums) - 1  # 注意二分法end从len(nums)-1开始，不是0，别粗心
        while left + 1 < right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid
            elif nums[mid] > target:
                right = mid
            else:
                return 0

        left_radius = abs(nums[left] - target)
        right_radius = abs(nums[right] - target)
        return min(left_radius, right_radius)

