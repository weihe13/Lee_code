# Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. (i.e., from left to
# right, then right to left for the next level and alternate between).
# Example 1:
# Input: root = [3,9,20,null,null,15,7]
# Output: [[3],[20,9],[15,7]]
# Example 2:
# Input: root = [1]
# Output: [[1]]
# Example 3:
# Input: root = []
# Output: []

# Constraints:
# The number of nodes in the tree is in the range [0, 2000].
# -100 <= Node.val <= 100

# 思路：1. 有两种方法实现BFS，一是两层循环，外层循环判断层数，内层循环判断每层node数。One way would be that we run a two-level
# nested loop, with the outer loop iterating each level on the tree, and with the inner loop iterating each node
# within a single level.
#      2. 另一种是implement BFS with a single loop though. The trick is that we append the nodes to be visited into
#      a queue and we separate nodes of different levels with a sort of delimiter (e.g. an empty node). The delimiter
#      marks the end of a level, as well as the beginning of a new level. 注意：
#         1）用is_order_left记录order，每次遇到delimiter，就换相反order。
#         2）往存数的deque（node_queue）里放数时，一直是先放每层左边的node，从node_queue里取数时也是先取list左边的，唯一区别是往
#            结果中level_list放数时，如果是偶数行则用appendleft。效果是因为取数也是从list左边取，就保证了把下一层的node往node_queue
#            里放时，也是按从左往右的顺序往里放。
#         3）用delimiter（None）隔断每一层，遇到None就换方向并清空level_list。

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
from collections import deque

class Solution:
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        ret = []
        level_list = deque()
        if root is None:
            return []
        # start with the level 0 with a delimiter
        node_queue = deque([root, None])
        is_order_left = True

        while len(node_queue) > 0:
            curr_node = node_queue.popleft()

            if curr_node:
                if is_order_left:
                    level_list.append(curr_node.val) # 奇数行
                else:
                    level_list.appendleft(curr_node.val) # 偶数行

                if curr_node.left:
                    node_queue.append(curr_node.left)
                if curr_node.right:
                    node_queue.append(curr_node.right)
            else:
                # we finish one level
                ret.append(level_list)
                # add a delimiter to mark the level
                if len(node_queue) > 0:   # 这步判断很细节，如果len(node)等于0说明没有下一层了，所以不用在append(None)否则
                                          # len([None])==1,会一直循环下去。
                    node_queue.append(None)

                # prepare for the next level
                level_list = deque()
                is_order_left = not is_order_left

        return ret
