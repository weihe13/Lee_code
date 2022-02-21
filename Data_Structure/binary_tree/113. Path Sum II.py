# Given the root of a binary tree and an integer targetSum, return all root-to-leaf paths where the sum of the node
# values in the path equals targetSum. Each path should be returned as a list of the node values,
# not node references. A root-to-leaf path is a path starting from the root and ending at any leaf node. A leaf is a
# node with no children.

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
# The number of nodes in the tree is in the range [0, 5000].
# -1000 <= Node.val <= 1000
# -1000 <= targetSum <= 1000

# 思路： 1. 想到要recursion + backstrack
#       2. 每次recursion输入的node和remainsum代表本次检查的node和当前的剩余目标sum，相等且没有子node时append


# 自己写法：
class Solution1:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []
        # 这里复杂了，因为想着用target==0来做basecase的判断条件，使得输入的target需要是减完当前node.val后的值，
        # 其实把target==0换种写法就行，比如target == node.val
        targetSum -= root.val
        res = []
        path = []

        def get_sum(node, target):

            path.append(node.val)  # 每次都先append再判断

            if not node.left and not node.right and target == 0:
                res.append(list(path))  # 这里很关键，必须要把当前path的值复制下来，否则append的是path位置，一直在变，最后path就是
                # [root.val]，并不是每次recursion时满足要求的path。

            if node.left:
                get_sum(node.left, target - node.left.val)
                path.pop()  # 因为自己写法是先判断不是None（没有把if none作为base case），再继续recursion，所以每次recursion都会
                # append val，因此发现不满足条件后先要把刚才加的pop掉，再继续试另一边。
            if node.right:
                get_sum(node.right, target - node.right.val)
                path.pop()

        get_sum(root, targetSum)
        return res


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

    def recurseTree(self, node, remainingSum, pathNodes, pathsList):

        if not node:
            return

            # Add the current node to the path's list
        pathNodes.append(node.val)

        # Check if the current node is a leaf and also, if it
        # equals our remaining sum. If it does, we add the path to
        # our list of paths
        if remainingSum == node.val and not node.left and not node.right:
            pathsList.append(list(pathNodes))
        else:
            # Else, we will recurse on the left and the right children
            self.recurseTree(node.left, remainingSum - node.val, pathNodes, pathsList)
            self.recurseTree(node.right, remainingSum - node.val, pathNodes, pathsList)

        # We need to pop the node once we are done processing ALL of it's
        # subtrees.
        pathNodes.pop()  # 因为base case 是None，所以对于每一个leaf node，最后两次recursion一定啥也没干，所以可以两边都recursion
        # 完再pop当前node

    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        pathsList = []
        self.recurseTree(root, sum, [], pathsList)
        return pathsList
