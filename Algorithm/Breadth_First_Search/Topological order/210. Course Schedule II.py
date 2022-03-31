# There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array
# prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take
# course ai. For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1. Return
# the ordering of courses you should take to finish all courses. If there are many valid answers, return any of them.
# If it is impossible to finish all courses, return an empty array.

# Example 1:
# Input: numCourses = 2, prerequisites = [[1,0]]
# Output: [0,1]
# Explanation: There are a total of 2 courses to take. To take course 1 you should have finished course 0. So the
# correct course order is [0,1].
# Example 2:
# Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
# Output: [0,2,1,3]
# Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both courses 1 and
# 2. Both courses 1 and 2 should be taken after you finished course 0.
# So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3].
# Example 3:
# Input: numCourses = 1, prerequisites = []
# Output: [0]

# Constraints:
# 1 <= numCourses <= 2000
# 0 <= prerequisites.length <= numCourses * (numCourses - 1)
# prerequisites[i].length == 2
# 0 <= ai, bi < numCourses
# ai != bi
# All the pairs [ai, bi] are distinct.

# 思路： 1. 可以构建一个有向图，想到拓扑排序。拓扑排序的步骤：
#          1）算每个点的入度（in_degree）,即有多少prerequest
#          2）把入度为0的点放进queue，因为他们没有prerequest，
#          3）每把一个点从queue中取出放到res中，就把以他为入度的点入度减一
#          4）把新的入度为0的点放到queue中
#       2. 一个注意点是要用nums记录放了几个点，最后nums == numCourse才说明所有点都放到了res中，形成了一个有效拓扑，否则while循环完不代表
#       所有点都在res中，有的点可能是一个环（三个点互为prerequest），就无法放到res中，但while循环也会停止。

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(numCourses)]
        in_degree = [0 for _ in range(numCourses)]

        for course_in, course_out in prerequisites:
            graph[course_out].append(course_in)
            in_degree[course_in] += 1

        queue = collections.deque([])
        visited = set()
        res = []
        nums = 0
        for i in range(len(in_degree)):
            if in_degree[i] == 0:
                queue.append(i)
                visited.add(i)

        while queue:
            curr = queue.pop()
            res.append(curr)
            nums += 1
            for course in graph[curr]:
                if course in visited:
                    continue
                in_degree[course] -= 1
                if in_degree[course] == 0:
                    queue.append(course)
                    visited.add(course)
        return res if nums == numCourses else []