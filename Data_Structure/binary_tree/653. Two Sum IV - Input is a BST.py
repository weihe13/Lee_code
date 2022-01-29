# Given the root of a Binary Search Tree and a target number k, return true if there exist two elements in the BST such that their sum is equal to the given target.

# Example 1:
# Input: root = [5,3,6,2,4,null,7], k = 9
# Output: true
# Example 2:
# Input: root = [5,3,6,2,4,null,7], k = 28
# Output: false

# Constraints:
# The number of nodes in the tree is in the range [1, 104].
# -104 <= Node.val <= 104
# root is guaranteed to be a valid binary search tree.
# -105 <= k <= 105

# 思路： 1. 一次搜索到底如果没有发现符合要求的组合，并不代表组合不存在。因为满足要求的组合可能在任意两个路径上，可能是两个leaf node，所以
#          如果要利用binary search tree的order的性质去搜索也很难。比如exaple中的root是5，假定5是两个数中的一个，利用大小关系搜索一次
#          后如果没有发现满足条件的组合，只能说明5不满足条件，还得继续往下试，所以利用大小关系并没有加快速度。
#       2. 考虑类似hash map，把见过的node的目标另一半存下来，这样遍历一遍就可以。
#       3. 写BFS的时候注意，因为是return True或False，如果用下面这种写法：
#          if root.left:
#              return helper(root.left, k)
#          if root.right:
#              return helper(root.right, k)
#          有两个错误：一是run 完left后并不会run right，因为已经return了，所以如果找左边没找到会直接return False。
#          二是不需要判断root.left和root.right,recursion function 的 base case就是if not root。
#          这种写法一般用在赋值value的时候，即if root.left: leftlength = helper(root.left, k)
#
#        4. 下面这种写法也不行：
#           helper(root.left, k)
#           helper(root.right, k)
#           这样即使左边线路找到了满足要求的组合，return了True，也只是内层的helper函数return了一个True，并没有把True在上层helper函数
#           输出，所以只是达到base line后停止了左侧的recursion，开始右边，全部run完并没有任何输出，return的就是None。
#        5. 为了让左右都能run达到DFS的效果，同时又return 回True or False的结果，可以用return helper(left) or helper(right).

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        targets = []  # target要在helper外定义
        def helper(root, k):
            if not root:
                return
            if root.val in targets:
                return True
            else:
                another = k - root.val
                targets.append(another)
            return helper(root.left, k) or helper(root.right, k)
        return helper(root, k)
# BFS + hashmap
class Solution2(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        queue = collections.deque([root])
        seen = set()
        while queue:
            u = queue.popleft()
            if k - u.val in seen:
                return True
            else:
                seen.add(u.val)
            if u.left:
                queue.append(u.left)
            if u.right:
                queue.append(u.right)
        return False