# In an infinite chess board with coordinates from -infinity to +infinity, you have a knight at square [0,
# 0]. A knight has 8 possible moves it can make, as illustrated below. Each move is two squares in a cardinal
# direction, then one square in an orthogonal direction. Return the minimum number of steps needed to move the knight
# to the square [x, y]. It is guaranteed the answer exists.

# Example 1:
# Input: x = 2, y = 1
# Output: 1
# Explanation: [0, 0] → [2, 1]
# Example 2:
# Input: x = 5, y = 5
# Output: 4
# Explanation: [0, 0] → [2, 1] → [4, 2] → [3, 4] → [5, 5]

# Constraints:
# -300 <= x, y <= 300
# 0 <= |x| + |y| <= 300

# 思路： 1. 如果有加障碍的限制，就是在判断nextstep是否valid时多加一个限制条件，即grid[next_x][next_y]是否为1（障碍）

class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        # directions 略作调整
        directions = [[1,2],[2,1],[2,-1],[1,-2],[-1,-2],[-2,-1],[-2,1],[-1,2]]
        queue = collections.deque([(0, 0)])
        visited = {(0,0):0}
        while queue:
            curr = queue.popleft()
            if curr[0] == x and curr[1] == y:
                return visited[curr]
            for delta_x, delta_y in directions:
                next_x = curr[0] + delta_x
                next_y = curr[1] + delta_y
                if (next_x, next_y) in visited:
                    continue
                queue.append((next_x, next_y))
                visited[(next_x, next_y)] = visited[curr] + 1