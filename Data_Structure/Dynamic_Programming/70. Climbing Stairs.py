# You are climbing a staircase. It takes n steps to reach the top.
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

# Example 1:
# Input: n = 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps
# Example 2:
# Input: n = 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step

# Constraints:
# 1 <= n <= 45

# 思路： 1. https://www.youtube.com/watch?v=Y0lT9Fck7qI
#       2. 对第i个位置而言，到该位置有两种方式：从i-1走1步，或者从i-2走两步。所以到i位置的方法总共有N(i-1)+N(i-2),即到达前两个位置的
#          方法数之和。对于第一层而言，i-1是地面，到i-1就是初始状态，算1种方法，不存在i-2,所以N(i-2)=0,到达第1个位置共有1+0=1种方法。
#          对于第二层而言，i-2是地面，i-1是第一层，N(i-1)+N(i-2)=1+1=2种方法。
#          对与第三层而言，i-2是第一层，i-2是第二层，N(i-1)+N(i-2) = 2+1 =3种方法。
#          以此类推，到第几层就要加几次，初始的one和two是1和0。
#       3. 也可以倒过来想，不论n是多少层，站在n上算1种，最后从n-1到n只有1种方法，从n-2开始循环，从n-2到n一定有1+1=2种方法，从n-3到n一定
#          有2+1=3种方法，以此类推。初始one和two是1和1，循环n-1次。
#       4. DFS: 每一步都有两种选择，1或者2，把每次步数相加可以得到目前层数，最后i==n或者>n时是base case。recursion的时候注意，比如n=5，
#          从地面到3有3种方法，但是从3到5的方法是固定的，所以第一次走到3后，可以把结果存下来，后面每次走到3就直接调用之前的结果就行，这样
#          时间复杂度就从O(2^n)(每一步都有两种可能，总共n步)降低到了O(n)(第一次走到底后把每一步的值存下来，后面走到相同层直接调用)。

# DP
class Solution:
    def climbStairs(self, n: int) -> int:
        one, two = 1, 0
        for _ in range(n):
            one, two = one + two, one
            # 等价写法：
            # temp = one
            # one = one + two
            # two = temp
        return one

# recursion
class Solution:
    cache = {}
    # 调用solution下的变量和function，都要用self.
    def climbStairs(self, n: int) -> int:

        if n in self.cache:
            return self.cache[n]  # 记得用self.cache而不是cache
        # base case
        if n == 1 or n == 0:
            return 1
        else:
            count_sum = self.climbStairs(n - 1) + self.climbStairs(n - 2)
            self.cache[n] = count_sum
            return count_sum
