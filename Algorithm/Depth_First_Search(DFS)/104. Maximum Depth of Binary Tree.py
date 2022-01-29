# Given the root of a binary tree, return its maximum depth. A binary tree's maximum depth is the number of nodes
# along the longest path from the root node down to the farthest leaf node.

# Example 1:
# Input: root = [3,9,20,null,null,15,7]
# Output: 3
# Example 2:
# Input: root = [1,null,2]
# Output: 2

# Constraints:
# The number of nodes in the tree is in the range [0, 104].
# -100 <= Node.val <= 100

# 思路：1. 第一时间想到DFS

class Solution:
    def maxDepth(self, root):  # 得到本层的深度
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        # 注意这里要用else，不能再用if node.left, if node.right去判断了，因为：
        # 1. 如果root is None，直接return 0，已经判断过了
        # 2. 如果用if node.left再次判断，当node.left是None时不会给left_height赋值，return时就会报错，used before assigned
        else:
            left_height = self.maxDepth(root.left)
            right_height = self.maxDepth(root.right)
            return max(left_height, right_height) + 1


class Solution2:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        stack = []
        if root:
            stack.append((1, root))

        depth = 0
        while stack:
            current_depth, root = stack.pop()
            if root:
                depth = max(depth, current_depth)
                stack.append((current_depth + 1, root.left))
                stack.append((current_depth + 1, root.right))
        return depth
# Time complexity : O(N).
# Space complexity : in the worst case, the tree is completely unbalanced, e.g. each node has only left child node,
# the recursion call would occur NN times (the height of the tree), therefore the storage to keep the call stack
# would be \mathcal{O}(N)O(N). But in the average case (the tree is balanced), the height of the tree would be \log(
# N)log(N). Therefore, the space complexity in this case would be O(log(N)).
