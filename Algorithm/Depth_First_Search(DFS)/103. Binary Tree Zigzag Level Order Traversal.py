# Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. (i.e., from left to
# right, then right to left for the next level and alternate between).
# Example 1:
# Input: root = [3,9,20,null,null,15,7]
# Output: [[3],[20,9],[15,7]]
# Example 2:
# Input: root = [1]
# Output: [[1]]
# Example 3:
# Input: root = []
# Output: []

# Constraints:
# The number of nodes in the tree is in the range [0, 2000].
# -100 <= Node.val <= 100

# 思路：如果用DFS，对每一层而言，一定是左边的node先进入，所以只需要用deque改变单数层的加数方向就行。

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        from collections import deque
        levels = []

        if not root:
            return levels

        def build(node, level):
            if len(levels) == level:
                levels.append(deque())
            if level % 2 == 0:
                levels[level].append(node.val)
            if level % 2 == 1:
                levels[level].appendleft(node.val)

            if node.left is not None:
                build(node.left, level + 1)
            if node.right is not None:
                build(node.right, level + 1)

        build(root, 0)
        return levels
