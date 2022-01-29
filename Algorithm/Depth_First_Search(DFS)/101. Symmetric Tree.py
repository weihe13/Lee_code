# Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).
# Example 1:
# Input: root = [1,2,2,3,4,4,3]
# Output: true
# Example 2:
# Input: root = [1,2,2,null,3,null,3]
# Output: false

# Constraints:
# The number of nodes in the tree is in the range [1, 1000].
# -100 <= Node.val <= 100

# 思路： 1. 就像照镜子，规律是镜子里外的root不管在第几层，永远是root1.left == root2.right.


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.mirror(root.left, root.right)  # 注意调用solution class的function时要用self.

    # mirror 返回的是本层的两个node是否是镜像
    def mirror(self, node1, node2):  # 注意定义solution下的function时，第一个输入参数是self
        if not node1 and not node2:
            return True

        if not node1 or not node2:
            return False
        # 注意调用solution class的function时，自己调用自己也要self.
        return node1.val == node2.val and self.mirror(node1.left, node2.right) and self.mirror(node1.right, node2.left)

# Time complexity : O(n). Because we traverse the entire input tree once, the total run time is O(n)O(n),
# where nn is the total number of nodes in the tree.
#
# Space complexity : The number of recursive calls is bound by the height of the tree. In the worst case, the tree is
# linear and the height is in O(n). Therefore, space complexity due to recursive calls on the stack is O(n)
# in the worst case.
