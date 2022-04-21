# Given the root of a binary tree and an integer targetSum, return all root-to-leaf paths where the sum of the node
# values in the path equals targetSum. Each path should be returned as a list of the node values, not node references.
# A root-to-leaf path is a path starting from the root and ending at any leaf node. A leaf is a node with no children.

# Example 1:
# Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
# Output: [[5,4,11,2],[5,8,4,5]]
# Explanation: There are two paths whose sum equals targetSum:
# 5 + 4 + 11 + 2 = 22
# 5 + 8 + 4 + 5 = 22
# Example 2:
# Input: root = [1,2,3], targetSum = 5
# Output: []
# Example 3:
# Input: root = [1,2], targetSum = 0
# Output: []

# Constraints:
#
# The number of nodes in the tree is in the range [0, 5000].
# -1000 <= Node.val <= 1000
# -1000 <= targetSum <= 1000

# 思路：1. dfs, think of what returns for each recursion call: The curr including input node or the curr not including
#         the input node. If include the input node, should also minus the input node.val from target sum.
#      2. time complexity: Consider the tree like so:
#
#           A
#          / \
#         B   C
#            / \
#           D   E
#              / \
#         and so on...
# Let the number of nodes = n
# Therefore depth of tree is approx n/2 and number of leaves are also approx n/2
# Now, potential correct paths are of length: 2, 3, ... n/2
# Copying these n/2 paths n/2 times to the answer arr gives us the complexity O(n*2)
#
# I'll definitely consider this tree in future tree / recursion / DFS problems
#      3. space complexity: The only additional space that we use is the pathNodes list to keep track of nodes along
#      a branch.


class Solution1:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []
        if not root:
            return res
        self.dfs(root, [], res, targetSum)
        return res

    def dfs(self, node, curr, res, targetSum):
        if not node.left and not node.right:
            if targetSum == node.val:
                res.append(curr + [node.val])
            return

        if node.left:
            self.dfs(node.left, curr + [node.val], res, targetSum - node.val)

        if node.right:
            self.dfs(node.right, curr + [node.val], res, targetSum - node.val)


class Solution2:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []
        if not root:
            return res
        self.dfs(root, [root.val], res, targetSum - root.val)
        return res

    def dfs(self, node, curr, res, targetSum):
        if not node.left and not node.right:
            if targetSum == 0:
                res.append(curr)
            return

        if node.left:
            self.dfs(node.left, curr + [node.left.val], res, targetSum - node.left.val)

        if node.right:
            self.dfs(node.right, curr + [node.right.val], res, targetSum - node.right.val)
