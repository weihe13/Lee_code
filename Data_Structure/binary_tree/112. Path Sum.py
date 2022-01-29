# Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that
# adding up all the values along the path equals targetSum. A leaf is a node with no children.

# Example 1:
# Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
# Output: true
# Explanation: The root-to-leaf path with the target sum is shown.
# Example 2:
# Input: root = [1,2,3], targetSum = 5
# Output: false
# Explanation: There two root-to-leaf paths in the tree:
# (1 --> 2): The sum is 3.
# (1 --> 3): The sum is 4.
# There is no root-to-leaf path with sum = 5.
# Example 3:
# Input: root = [], targetSum = 0
# Output: false
# Explanation: Since the tree is empty, there are no root-to-leaf paths.

# Constraints:
# The number of nodes in the tree is in the range [0, 5000].
# -1000 <= Node.val <= 1000
# -1000 <= targetSum <= 1000

# 思路： 1. 思考清楚base case是什么：当not node的时候，说明已经判断过leaf node了，仍然没有满足条件，所以return False
#       2. 每次调用自己时，把减掉本层val后的target sum作为参数
#       3. 注意，不能:
#                   if targetSum < 0: return False
#          因为targetSum和node.val都可以是负数。比如 -2 + -3 + -3 = -8
#       4. 如果当前node不满足条件，不能return True，但还要继续看node.left 或者node.right，又一个符合条件就可以。

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        targetSum -= root.val
        if targetSum == 0 and not root.left and not root.right:
            return True
        return self.hasPathSum(root.left, targetSum) or self.hasPathSum(root.right, targetSum)
# Time complexity : we visit each node exactly once, thus the time complexity is O(N), where NN is the
# number of nodes. Space complexity : in the worst case, the tree is completely unbalanced, e.g. each node has only
# one child node, the recursion call would occur NN times (the height of the tree), therefore the storage to keep the
# call stack would be O(N). But in the best case (the tree is completely balanced), the height of the
# tree would be log(N). Therefore, the space complexity in this case would be O(log(N)).

class Solution2:
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False

        de = [(root, sum - root.val), ]
        while de:
            node, curr_sum = de.pop()
            if not node.left and not node.right and curr_sum == 0:
                return True
            # 因为这里不用BFS，是直接pop(),不在意顺序，但是也先append right，这样pop时先pop的是左边的node
            if node.right:
                de.append((node.right, curr_sum - node.right.val)) # 判断哪个node就减那个node的value
            if node.left:
                de.append((node.left, curr_sum - node.left.val))
        return False