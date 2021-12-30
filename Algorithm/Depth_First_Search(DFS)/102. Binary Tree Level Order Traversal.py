# Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right,
# level by level).

# Example 1:
# Input: root = [3,9,20,null,null,15,7]
# Output: [[3],[9,20],[15,7]]
# Example 2:
# Input: root = [1]
# Output: [[1]]
# Example 3:
# Input: root = []
# Output: []

# Constraints:
# The number of nodes in the tree is in the range [0, 2000].
# -1000 <= Node.val <= 1000

# 思路：   1. 注意build里recursion时没有return
#         2. 这里if left，if right的结构和parr教的tree一样，先穷尽left，再找right，一层一层回归
#         3. 巧妙利用level变量去定位应该在第几层对应的list加value

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        levels = []

        if not root:
            return levels

        def build(node, level):
            if len(levels) == level:
                levels.append([])

            levels[level].append(node.val)

            if node.left is not None:
                build(node.left, level + 1)
            if node.right is not None:
                build(node.right, level + 1)

        build(root, 0)
        return levels