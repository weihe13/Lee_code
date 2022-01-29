# You are given the root of a binary search tree (BST) and an integer val. Find the node in the BST that the node's
# value equals val and return the subtree rooted with that node. If such a node does not exist, return null.

# Example 1:
# Input: root = [4,2,7,1,3], val = 2
# Output: [2,1,3]
# Example 2:
# Input: root = [4,2,7,1,3], val = 5
# Output: []

# Constraints:
# The number of nodes in the tree is in the range [1, 5000].
# 1 <= Node.val <= 107
# root is a binary search tree.
# 1 <= val <= 107

# 思路：1. 思路很简单，如果等于就return当前node。因为是binary tree，所以一次没找到，就意味着没有，不用遍历整个tree，因此调用自己的写法
#         是if : return f(node.left),else: return f(node.right)，而不用并列写。

class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return
        if root.val == val:
            return root
        if root.val > val:
            return self.searchBST(root.left, val)
        return self.searchBST(root.right, val)
# Time complexity : O(H), where H is a tree height. That results in O(logN) in the average case, and O(N) in the
# worst case.
# Space complexity : O(H) to keep the recursion stack, i.e. O(logN) in the average case, and O(N) in the worst case.

# iteration
class Solution2:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        while root is not None and root.val != val:
            root = root.left if val < root.val else root.right
        return root
# Time complexity : O(H), where H is a tree height. That results in O(logN) in the average case, and O(N) in the
# worst case.
# Space complexity : O(1) since it's a constant space solution.
