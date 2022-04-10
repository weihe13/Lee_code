# Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree. According to the
# definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node
# in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

# Example 1
# Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
# Output: 3
# Explanation: The LCA of nodes 5 and 1 is 3.
# Example 2:
# Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
# Output: 5
# Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA
# definition.
# Example 3:
# Input: root = [1,2], p = 1, q = 2
# Output: 1

# Constraints:
# The number of nodes in the tree is in the range [2, 105].
# -109 <= Node.val <= 109
# All Node.val are unique.
# p != q
# p and q will exist in the tree.

# 思路：1. 要理解p和q是reference，不是value
#      2. 核心问题是怎么return，如果return的是LCA，那比如p在leaf节点，因为在该节点只找到p没有q，所以没找到LCA，就会return None，那么
#         找到p或者q和一个没找到就没有区别了。因此想到的思路是有啥return啥。找到p就return p，找到LCA就找到LCA，什么都没找到就return
#         None. 因为这题保证一定存在p和q且因为是reference所以都只有一个。当左子树找到LCA时，右子树一定是None。

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        pass

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # 对根结点的处理
        if not root:
            return None
        if root == p:  # 这里比的是reference，是位置，不是value
            return root
        if root == q:
            return root

        # 一般情况处理
        left_lca = self.lowestCommonAncestor(root.left, p, q)
        right_lca = self.lowestCommonAncestor(root.right, p, q)
        if left_lca and right_lca:
            return root
        elif left_lca:
            return left_lca
        elif right_lca:
            return right_lca
        return None
