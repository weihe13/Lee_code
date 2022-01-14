# You are given two binary trees root1 and root2.Imagine that when you put one of them to cover the other,
# some nodes of the two trees are overlapped while the others are not. You need to merge the two trees into a new
# binary tree. The merge rule is that if two nodes overlap, then sum node values up as the new value of the merged
# node. Otherwise, the NOT null node will be used as the node of the new tree. Return the merged tree.Note: The
# merging process must start from the root nodes of both trees.

# Example 1:
# Input: root1 = [1,3,2,5], root2 = [2,1,3,null,4,null,7]
# Output: [3,4,5,5,4,null,7]
# Example 2:
# Input: root1 = [1], root2 = [1,2]
# Output: [2,2]

# Constraints:
# The number of nodes in both trees is in the range [0, 2000].
# -104 <= Node.val <= 104

# 思路：1. 难点在于recursion的时候，如果遇到None，None.left会报错，所以在每次recursion的最开始需要判断是不是None，是None就
#         停止recursion（通过return).
#      2. 注意当node1是None时，直接return node2就行，因为node2下面的节点node1一定没有对应位置了。

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def mergeTrees(self, t1: Optional[TreeNode], t2: Optional[TreeNode]) -> Optional[TreeNode]:
        if t1 == None and t2 == None:
            return None  # 也可以不用判断都是None的情况，直接if node1 == None,return node2.
                         # 因为如果node2是None也可以直接return node2。
        elif t1 == None:
            return t2
        elif t2 == None:
            return t1
        new_root = TreeNode(t1.val + t2.val)
        new_root.left = self.mergeTrees(t1.left, t2.left)
        new_root.right = self.mergeTrees(t1.right, t2.right)
        return new_root

    # 一个意思，利用or的性质简化code，感觉意义不大，反而不好理解
    def mergeTrees(self, t1, t2):
        if t1 and t2:
            node = TreeNode(t1.val + t2.val)
            node.left = self.mergeTrees(t1.left, t2.left)
            node.right = self.mergeTrees(t1.right, t2.right)
            return node
        return t1 or t2
