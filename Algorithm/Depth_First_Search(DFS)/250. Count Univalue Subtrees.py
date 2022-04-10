# Given the root of a binary tree, return the number of uni-value subtrees.
# A uni-value subtree means all nodes of the subtree have the same value.

# Example 1:
# Input: root = [5,1,5,5,5,null,5]
# Output: 4
# Example 2:
# Input: root = []
# Output: 0
# Example 3:
#
# Input: root = [5,5,5,5,5,null,5]
# Output: 6

# Constraints:
# The number of the node in the tree will be in the range [0, 1000].
# -1000 <= Node.val <= 1000

# 思路：1. 想到DFS，所有leaf node都是满足条件的，然后从leaf node往回check，左右子node
#      2. 自己的写法还是没有想到最清楚，所以会漏掉一些corner case，test不过再补

class Solution:
    def __init__(self):
        pass

    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:
        count = 0
        if not root:
            return count

        def helper(node):
            nonlocal count
            if not node.left and not node.right:
                count += 1
                return True, node.val
            elif not node.right:
                left, left_val = helper(node.left)
                right, right_val = True, node.val
            elif not node.left:
                right, right_val = helper(node.right)
                left, left_val = True, node.val
            else:
                left, left_val = helper(node.left)
                right, right_val = helper(node.right)
            if left and right and node.val == left_val == right_val:
                count += 1
                return True, node.val

            return False, node.val

        helper(root)
        return count


class Solution2:
    def __init__(self):
        pass

    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:
        self.count = 0
        if root is None:
            return 0
        self.check(root, root.val)
        return self.count

    def check(self, node, val):
        if node is None: return True
        left = self.check(node.left, node.val)
        right = self.check(node.right, node.val)
        if not (left and right):
            return False
        self.count += 1
        return node.val == val
