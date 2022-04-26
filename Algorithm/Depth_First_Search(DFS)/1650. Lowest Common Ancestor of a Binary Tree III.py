# Given two nodes of a binary tree p and q, return their lowest common ancestor (LCA).
#
# Each node will have a reference to its parent node. The definition for Node is below:
#
# class Node { public int val; public Node left; public Node right; public Node parent; } According to the definition
# of LCA on Wikipedia: "The lowest common ancestor of two nodes p and q in a tree T is the lowest node that has both
# p and q as descendants (where we allow a node to be a descendant of itself)."

# Example 1:
# Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
# Output: 3
# Explanation: The LCA of nodes 5 and 1 is 3.
# Example 2:
# Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
# Output: 5
# Explanation: The LCA of nodes 5 and 4 is 5 since a node can be a descendant of itself according to the LCA definition.
# Example 3:
# Input: root = [1,2], p = 1, q = 2
# Output: 1

# Constraints:
# The number of nodes in the tree is in the range [2, 105].
# -109 <= Node.val <= 109
# All Node.val are unique.
# p != q
# p and q exist in the tree.

# 思路：1. Use a set to store the parent node of p. Then check q's parent, if it is in the set, return it.
#      2. Firstly find the level of q and p respectively, then move them to the same level. At last, find the common
#         parent for them.


class Solution1:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        seen = set()

        def find_parent(node):
            if not node or node in seen:
                return node
            seen.add(node)
            return find_parent(node.parent)

        return find_parent(p) or find_parent(q)
    

class Solution2:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        def find_level(node, h):
            while node:
                node = node.parent
                h += 1
            return h

        p_level = find_level(p, 1)
        q_level = find_level(q, 1)

        for i in range(p_level - q_level):
            p = p.parent

        for j in range(q_level - p_level):
            q = q.parent

        while p != q:
            p = p.parent
            q = q.parent
        return p