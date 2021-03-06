# Given the root of a binary tree, return the length of the diameter of the tree. The diameter of a binary tree is
# the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.
# The length of a path between two nodes is represented by the number of edges between them.

# Example 1:
# Input: root = [1,2,3,4,5]
# Output: 3
# Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].
# Example 2:
# Input: root = [1,2]
# Output: 1

# Constraints:
# The number of nodes in the tree is in the range [1, 104].
# -100 <= Node.val <= 100

# 思路：1. The longest path has to be between two leaf nodes. 2. We know that in a tree, nodes are only
# connected with their parent node and 2 children. Therefore we know that the longest path in the tree would consist
# of a node, its longest left branch, and its longest right branch. So, our algorithm to solve this problem will find
# the node where the sum of its longest left and right branches is maximized. This would hint at us to apply
# Depth-first search (DFS) to count each node's branch lengths, because it would allow us to dive deep into the
# leaves first, and then start counting the edges upwards.
# 体会： 1. DFS 的实现：if left: recursion_function(left)
#                     if right: recursion_function(right)
#          这样在每个node，都是先看左边的情况再看右边，一直到最左边的leafnode，才开始return上一级，看上一级的右边是否存在。
#       2. 在最后return时加1，使得return回的已经是对于上一级node而言最长的path
#       3. 对于嵌套函数，想用内层函数改变外层函数的变量时(除了set list dictionary变量)，要用nonlocal（python3）
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        max_depth = 0

        def helper(root):
            nonlocal max_depth
            if not root:  # 注意不是node时直接return 0，不+1
                return 0
            left_path = helper(root.left)  # 只能在return时+1，不能在这里+1，这里+1会使得leaf node的left depth变成1，应该是0
            right_path = helper(root.right)
            curr_path = left_path + right_path
            max_depth = max(max_depth, curr_path)
            return 1 + max(left_path, right_path)  # 所有node在return时+1，表示返回上一层后的depth

        helper(root)
        return max_depth
