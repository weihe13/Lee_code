# Given the root of a binary tree, invert the tree, and return its root.

# Example 1:
# Input: root = [4,2,7,1,3,6,9]
# Output: [4,7,2,9,6,3,1]
# Example 2：
# Input: root = [2,1,3]
# Output: [2,3,1]
# Example 3:
# Input: root = []
# Output: []

# Constraints:
# The number of nodes in the tree is in the range [0, 100].
# -100 <= Node.val <= 100

# 思路：1. recursion, 每次都将node.left 和node.right互换位置,DFS和BFS其实不影响
#      2. iteration

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return

        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root


# Since each node in the tree is visited only once, the time complexity is O(n)O(n), where nn is the number of nodes
# in the tree. We cannot do better than that, since at the very least we have to visit each node to invert it.
#
# Because of recursion, O(h)O(h) function calls will be placed on the stack in the worst case, where hh is the height
# of the tree. Because h\in O(n)h∈O(n), the space complexity is O(n)O(n).

from collections import deque

# iteration & BFS
# 因为是先按层往queue里加node，再从左侧按顺序取出来，所以是BFS
class Solution2:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root == None:
            return None
        queue = deque([root])
        while queue:
            cur = queue.popleft()
            temp = cur.right
            cur.right = cur.left
            cur.left = temp
            if cur.left:
                queue.append(cur.left)
            if cur.right:
                queue.append(cur.right)
        return root
# Since each node in the tree is visited / added to the queue only once, the time complexity is O(n)O(n), where nn is
# the number of nodes in the tree.
#
# Space complexity is O(n)O(n), since in the worst case, the queue will contain all nodes in one level of the binary
# tree. For a full binary tree, the leaf level has [n 2] = O(n) leaves.
