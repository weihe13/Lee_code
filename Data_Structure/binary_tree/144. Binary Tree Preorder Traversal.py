# Given the root of a binary tree, return the preorder traversal of its nodes' values.
# Example 1:
# Input: root = [1,null,2,3]
# Output: [1,2,3]
# Example 2:
# Input: root = []
# Output: []
# Example 3:
# Input: root = [1]
# Output: [1]

# Constraints:
# The number of nodes in the tree is in the range [0, 100].
# -100 <= Node.val <= 100
# Follow up: Recursive solution is trivial, could you do it iteratively?

# 思路：1. preorder的顺序就是DFS的顺序，先穷尽左边的node再看右边的node
#      2. recursion的套路可以记住，先写判断终止recurtion的条件，如果是preorder就是先val，再left，最后right；
#         如果是inorder，就是先left，再val，最后right。preorder或者inorder指的是val的位置。

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def traveral(root):
            # stop condition
            if not root:
                return

            # preorder -> root / left / right
            output.append(root.val)
            traveral(root.left)
            traveral(root.right)
            return

        output = []
        traveral(root)
        return output


class Solution2(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []

        stack, output = [root, ], []

        while stack:
            root = stack.pop()
            if root is not None:
                output.append(root.val)
                if root.right is not None:
                    stack.append(root.right)
                if root.left is not None:
                    stack.append(root.left)

        return output