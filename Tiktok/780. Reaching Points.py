# Given four integers sx, sy, tx, and ty, return true if it is possible to convert the point (sx, sy) to the point (
# tx, ty) through some operations, or false otherwise. The allowed operation on some point (x, y) is to convert it to
# either (x, x + y) or (x + y, y).

# Example 1:
# Input: sx = 1, sy = 1, tx = 3, ty = 5
# Output: true
# Explanation:
# One series of moves that transforms the starting point to the target is:
# (1, 1) -> (1, 2)
# (1, 2) -> (3, 2)
# (3, 2) -> (3, 5)
# Example 2:
# Input: sx = 1, sy = 1, tx = 2, ty = 2
# Output: false
# Example 3:
#
# Input: sx = 1, sy = 1, tx = 1, ty = 1
# Output: true

# Constraints:
# 1 <= sx, sy, tx, ty <= 109

# 思路：1. 利用recursion进行exhaustive search：
class Solution1(object):
    def reachingPoints(self, sx, sy, tx, ty):
        if sx > tx or sy > ty: return False
        if sx == tx and sy == ty: return True
        return self.reachingPoints(sx + sy, sy, tx, ty) or \
               self.reachingPoints(sx, sx + sy, tx, ty)


#      2. 利用recursion+DP
class Solution2(object):
    def reachingPoints(self, sx, sy, tx, ty):
        seen = set()

        def search(x, y):
            if (x, y) in seen: return
            if x > tx or y > ty: return
            seen.add((x, y))
            search(x + y, y)
            search(x, x + y)

        search(sx, sy)
        return (tx, ty) in seen


# 3. Work Backwards:
# 1)Every parent point (x, y) has two children, (x, x+y) and (x+y, y). However, every point (x,
# y) only has one parent candidate (x-y, y) if x >= y, else (x, y-x). This is because we never have points with
# negative coordinates.
# 2) Say tx > ty. We know that the next parent operations will be to subtract ty from tx,
# until such time that tx = tx % ty. When both tx > ty and ty > sy, we can perform all these parent operations in one
# step, replacing while tx > ty: tx -= ty with tx %= ty.
# 3) Otherwise, if say tx > ty and ty <= sy, then we know ty will not be changing (it can only decrease). Thus,
# only tx will change, and it can only change by subtracting by ty. Hence, (tx - sx) % ty == 0 is a necessary and
# sufficient condition for the problem's answer to be True.

class Solution3(object):
    def reachingPoints(self, sx, sy, tx, ty):
        while tx >= sx and ty >= sy:
            if tx == ty: # 等于的情况没法放在大于或小于中一起讨论，所以单独拿出来
                break
            elif tx > ty:
                if ty > sy:
                    tx %= ty
                else:  # 因为循环时已经判断了ty >= sy，所以else这里已经确定ty == sy.
                    return (tx - sx) % ty == 0
            else:
                if tx > sx:
                    ty %= tx
                else:
                    return (ty - sy) % tx == 0

        return tx == sx and ty == sy
