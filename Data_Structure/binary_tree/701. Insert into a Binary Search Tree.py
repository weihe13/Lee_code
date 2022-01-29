# You are given the root node of a binary search tree (BST) and a value to insert into the tree. Return the root node
# of the BST after the insertion. It is guaranteed that the new value does not exist in the original BST. Notice that
# there may exist multiple valid ways for the insertion, as long as the tree remains a BST after insertion. You can
# return any of them.

# Example 1:
# Input: root = [4,2,7,1,3], val = 5
# Output: [4,2,7,1,3,5]
# Explanation: Another accepted tree is:
# Example 2:
# Input: root = [40,20,60,10,30,50,70], val = 25
# Output: [40,20,60,10,30,50,70,null,null,25]
# Example 3:
# Input: root = [4,2,7,1,3,null,null,null,null,null,null], val = 5
# Output: [4,2,7,1,3,5]

# Constraints:
# The number of nodes in the tree will be in the range [0, 104].
# -108 <= Node.val <= 108
# All the values Node.val are unique.
# -108 <= val <= 108
# It's guaranteed that val does not exist in the original BST.

# 思路： 1. 题目里说了保证val不在tree里，所以只要小了就找右边，大了就找左边，最后一定会找到可以插入的leaf node
#       2. 找到合适的leaf node后怎么操作？recursion的过程中直接root.left =,这样最后leaf node直接加上了val，前序node不会变。每一层
#          return的都是当前node。

class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)

        if root.val > val:
            root.left = self.insertIntoBST(root.left, val)

        else:
            root.right = self.insertIntoBST(root.right, val)

        return root

# 其实iteration 就是从root到leaf，不断更新node
class Solution2:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)

        node = root
        while node:
            if node.val > val:
                if not node.left:
                    node.left = TreeNode(val)
                    return root
                else:
                    node = node.left
            else:
                if not node.right:
                    node.right = TreeNode(val)
                    return root
                else:
                    node = node.right
        return root

