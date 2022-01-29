# Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST. According to
# the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest
# node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

# Example 1:
# Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
# Output: 6
# Explanation: The LCA of nodes 2 and 8 is 6.
# Example 2:
# Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
# Output: 2
# Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA
# definition.
# Example 3:
# Input: root = [2,1], p = 2, q = 1
# Output: 2

# Constraints:
# The number of nodes in the tree is in the range [2, 105].
# -109 <= Node.val <= 109
# All Node.val are unique.
# p != q
# p and q will exist in the BST.

# 思路： 1. 关键是利用BST的性质，如果p.val q.val都大于node.val，说明LCA一定在node的右边，所以再检查node.right, 直到出现第一个p和q在
#          它两侧的点，这个点就是LCA。

class Solution1:
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        parent_val = root.val
        p_val = p.val
        q_val = q.val
        if p_val > parent_val and q_val > parent_val:
            return self.lowestCommonAncestor(root.right, p, q)
        elif p_val < parent_val and q_val < parent_val:
            return self.lowestCommonAncestor(root.left, p, q)
        # We have found the split point, i.e. the LCA node.
        else:
            return root
# Time Complexity: O(N), where NN is the number of nodes in the BST. In the worst case we might be visiting all the
# nodes of the BST.
# Space Complexity: O(N). This is because the maximum amount of space utilized by the recursion stack would be NN
# since the height of a skewed BST could be NN.

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        p_value = p.val
        q_value = q.val
        stack = [root]

        while stack:
            node = stack.pop()
            value = node.val
            if p_value > value and q_value > value:
                stack.append(node.right)
            elif p_value < value and q_value < value:
                stack.append(node.left)
            else:
                return node
# 因为stack中实际永远只有一个node，所以不需要stack，直接改node就行：
class Solution2:
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        p_val = p.val
        q_val = q.val
        node = root

        while node:
            parent_val = node.val
            if p_val > parent_val and q_val > parent_val:
                node = node.right
            elif p_val < parent_val and q_val < parent_val:
                node = node.left
            else:
                return node


