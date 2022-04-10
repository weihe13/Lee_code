# Given a binary tree, find the subtree with minimum sum. Return the root of the subtree.
# The range of input and output data is in int.
# LintCode will print the subtree which root is your return node.
# It's guaranteed that there is only one subtree with minimum sum and the given binary tree is not an empty tree.

# Example
# Example 1:
# Input:
# {1,-5,2,1,2,-4,-5}
# Output:1
# Explanation:
# The tree is look like this:
#      1
#    /   \
#  -5     2
#  / \   /  \
# 1   2 -4  -5
# The sum of whole tree is minimum, so return the root.
# Example 2:
#
# Input:
# {1}
# Output:1
# Explanation:
# The tree is look like this:
#    1
# There is one and only one subtree in the tree. So we return 1.

# 思路： 1. DFS + divide and conquer

class Solution:
    """
    @param root: the root of binary tree
    @return: the root of the minimum subtree
    """

    def __init__(self):
        pass

    def find_subtree(self, root: TreeNode) -> TreeNode:
        # write your code here
        self.min_value = float('inf')
        self.min_node = None
        self.find_min(root)
        return self.min_node

    def find_min(self, node):
        if not node:
            return 0

        left_sum = self.find_min(node.left)
        right_sum = self.find_min(node.right)
        curr_sum = left_sum + right_sum + node.val
        if curr_sum < self.min_value:
            self.min_value = curr_sum
            self.min_node = node
        return curr_sum