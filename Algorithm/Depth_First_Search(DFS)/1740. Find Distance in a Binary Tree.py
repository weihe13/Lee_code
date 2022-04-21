# Given the root of a binary tree and two integers p and q, return the distance between the nodes of value p and
# value q in the tree.
# The distance between two nodes is the number of edges on the path from one to the other.

# Example 1:
# Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 0
# Output: 3
# Explanation: There are 3 edges between 5 and 0: 5-3-1-0.
# Example 2:
# Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 7
# Output: 2
# Explanation: There are 2 edges between 5 and 7: 5-2-7.
# Example 3:
# Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 5
# Output: 0
# Explanation: The distance between a node and itself is 0.

# Constraints:
#
# The number of nodes in the tree is in the range [1, 104].
# 0 <= Node.val <= 109
# All Node.val are unique.
# p and q are values in the tree.

# logic: 1. find the lca of p and q.
#        2. find the distance between the p,q and lca

class Solution:
    def findDistance(self, root: Optional[TreeNode], p: int, q: int) -> int:
        def lca(root, p, q):
            if not root or root.val == p or root.val == q:
                return root

            left_lca = lca(root.left, p, q)
            right_lca = lca(root.right, p, q)

            if left_lca and right_lca:
                return root
            return left_lca or right_lca

        def distance(root, target):
            if not root:
                return float('inf')
            if root.val == target:
                return 0
            return 1 + min(distance(root.left, target), distance(root.right, target))

        node = lca(root, p, q)
        return distance(node, p) + distance(node, q)