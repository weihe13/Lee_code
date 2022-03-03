# There are n friends that are playing a game. The friends are sitting in a circle and are numbered from 1 to n in
# clockwise order. More formally, moving clockwise from the ith friend brings you to the (i+1)th friend for 1 <= i <
# n, and moving clockwise from the nth friend brings you to the 1st friend. The rules of the game are as follows:

# Start at the 1st friend. Count the next k friends in the clockwise direction including the friend you started at.
# The counting wraps around the circle and may count some friends more than once. The last friend you counted leaves
# the circle and loses the game. If there is still more than one friend in the circle, go back to step 2 starting
# from the friend immediately clockwise of the friend who just lost and repeat. Else, the last friend in the circle
# wins the game. Given the number of friends, n, and an integer k, return the winner of the game.

# Example 1:
# Input: n = 5, k = 2
# Output: 3
# Explanation: Here are the steps of the game:
# 1) Start at friend 1.
# 2) Count 2 friends clockwise, which are friends 1 and 2.
# 3) Friend 2 leaves the circle. Next start is friend 3.
# 4) Count 2 friends clockwise, which are friends 3 and 4.
# 5) Friend 4 leaves the circle. Next start is friend 5.
# 6) Count 2 friends clockwise, which are friends 5 and 1.
# 7) Friend 1 leaves the circle. Next start is friend 3.
# 8) Count 2 friends clockwise, which are friends 3 and 5.
# 9) Friend 5 leaves the circle. Only friend 3 is left, so they are the winner.
# Example 2:
# Input: n = 6, k = 5
# Output: 1
# Explanation: The friends leave in this order: 5, 4, 6, 2, 3. The winner is friend 1.

# Constraints:
# 1 <= k <= n <= 500

# 思路：1. 用一个从1开始的list记录还剩的玩家，每个位置的值代表玩家的初始序号
#      2. 思路一好理解，计算每次应该剔除的位置，从下个位置重新组装list
#      3. 思路二难理解，k是每次要走的步数，index是本次计算得到的应该剔除的位置，同时也相当于下次开始时已经走的步数，因此下轮一共要走
#         index+k步，走完后对应的位置是(index+k-1)%len(l).
#         注意：因为list的index从0开始，所以从0位置开始走完k步对应的位置是k-1。而该位置要pop，所以留下了前面k-1个数，正好相当于
#         index(也就是k-1)就是下次开始前已经走的步数。

class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        ls = list(range(1, n + 1))
        while ls:
            i = (k - 1) % len(ls)
            res = ls.pop(i)
            ls = ls[i:] + ls[:i]  # 注意切片时，即使只有一个数或者是空集，ls[1:]或者ls[100:]也不会报错，只是返回空集
            # 但如果是指定位置ls[1],就会报错
        return res


class Solution1:
    def findTheWinner(self, n: int, k: int) -> int:
        remain, index = [i for i in range(1, n+1)], 0
        while remain:
            index = (k - 1 + index) % len(remain) # index -1 +k是本轮一共要走的步数
            result = remain.pop(index)
        return result
