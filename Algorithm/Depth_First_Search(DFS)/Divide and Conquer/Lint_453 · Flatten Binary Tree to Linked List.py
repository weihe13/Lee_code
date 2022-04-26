# Flatten a binary tree to a fake "linked list" in pre-order traversal.
# Here we use the right pointer in TreeNode as the next pointer in ListNode.
# Don't forget to mark the left child of each node to null. Or you will get Time Limit Exceeded or Memory Limit
# Exceeded.
# Example
# Example 1:
# Input:{1,2,5,3,4,#,6}
# Output：{1,#,2,#,3,#,4,#,5,#,6}
# Explanation：
#      1
#     / \
#    2   5
#   / \   \
#  3   4   6
#
# 1
# \
#  2
#   \
#    3
#     \
#      4
#       \
#        5
#         \
#          6
# Example 2:
#
# Input:{1}
# Output:{1}
# Explanation：
#          1
#          1
# Challenge
# Do it in-place without any extra memory.

# Logic: 1. Think of merge sort. For each subtree, get the last node of its left child and right child, then transform
#           and return the right_last_node or left_last_node(it became the right_last_node after transform) or root.

class Solution:
    """
    @param root: a TreeNode, the root of the binary tree
    @return: nothing
    """

    def flatten(self, root: TreeNode):
        # write your code here
        self.flatten_and_return_last(root)

    def flatten_and_return_last(self, node):
        if not node:
            return

        left_last = self.flatten_and_return_last(node.left)
        right_last = self.flatten_and_return_last(node.right)

        if left_last:
            left_last.right = node.right
            node.right = node.left
            node.left = None

        return right_last or left_last or node