# There are n gas stations along a circular route, where the amount of gas at the ith station is gas[i].
# You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from the ith station to its next (i
# + 1)th station. You begin the journey with an empty tank at one of the gas stations.
# Given two integer arrays gas and cost, return the starting gas station's index if you can travel around the circuit
# once in the clockwise direction, otherwise return -1. If there exists a solution, it is guaranteed to be unique

# Example 1:
# Input: gas = [1,2,3,4,5], cost = [3,4,5,1,2]
# Output: 3
# Explanation:
# Start at station 3 (index 3) and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
# Travel to station 4. Your tank = 4 - 1 + 5 = 8
# Travel to station 0. Your tank = 8 - 2 + 1 = 7
# Travel to station 1. Your tank = 7 - 3 + 2 = 6
# Travel to station 2. Your tank = 6 - 4 + 3 = 5
# Travel to station 3. The cost is 5. Your gas is just enough to travel back to station 3.
# Therefore, return 3 as the starting index.
# Example 2:
# Input: gas = [2,3,4], cost = [3,4,3]
# Output: -1
# Explanation:
# You can't start at station 0 or 1, as there is not enough gas to travel to the next station.
# Let's start at station 2 and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
# Travel to station 0. Your tank = 4 - 3 + 2 = 3
# Travel to station 1. Your tank = 3 - 3 + 3 = 3
# You cannot travel back to station 2, as it requires 4 unit of gas but you only have 3.
# Therefore, you can't travel around the circuit once no matter where you start.

# Constraints:
#
# n == gas.length == cost.length
# 1 <= n <= 105
# 0 <= gas[i], cost[i] <= 104

# 思路： 1. Considering at each index if the gas > cost, means we are gaining some extra gas, otherwise we are losing
# some gas. If the starting point exists, it must start from the position where we lose the most of the gas,
# so that it can start to gain gas first to gather all the gas we need before we start losing.

# Take an example like (here the number refers to the value gas[i] - cost[i])
# [3,4,-12,4,-5,6]
#
# The minimum tank value will happen at index 4, where the value is -5, because at there our tank is at the minimum
# value -6, which means if the result exists, it must start to gather gas at index 5 so that we can cover all the gas
# loss before we reach index 4.
# The algorithm is simple, find the minimum tank value and its index, and then use the next index as the starting point.
#       2. 写的时候注意，并不需要一个list 去记录整个pre_sum的值，只要跟踪当前累积的pre_sum并更新min_sum就行。
class Solution:
    def __init__(self):
        pass

    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        pre_sum = gas[0] - cost[0]
        min_tank = pre_sum
        end = 0

        for i in range(1, n):
            pre_sum += gas[i] - cost[i]
            if pre_sum < min_tank:
                min_tank = pre_sum
                end = i

        if pre_sum >= 0:
            return end + 1 if end != n - 1 else 0
        return -1
