# You are given a perfect binary tree where all leaves are on the same level, and every parent has two children. The
# binary tree has the following definition:
# struct Node {
#   int val;
#   Node *left;
#   Node *right;
#   Node *next;
# }

# Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should
# be set to NULL.
# Initially, all next pointers are set to NULL.

# Example 1:
# Input: root = [1,2,3,4,5,6,7]
# Output: [1,#,2,3,#,4,5,6,7,#]
# Explanation: Given the above perfect binary tree (Figure A), your function should populate each next pointer to
# point to its next right node, just like in Figure B. The serialized output is in level order as connected by the
# next pointers, with '#' signifying the end of each level.
# Example 2:
# Input: root = []
# Output: []

# Constraints:
# The number of nodes in the tree is in the range [0, 212 - 1].
# -1000 <= Node.val <= 1000

# Follow-up:
# You may only use constant extra space.
# The recursive approach is fine. You may assume implicit stack space does not count as extra space for this problem.

# 思路：1. Level Order Traversal, using deque
#      2. Using previously established next pointers

class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


import collections


class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return root

        Q = collections.deque([root])
        while Q:
            size = len(Q)  # 关键是这一步，先固定住循环次数(当前层node数)，到次数后自动开始下一层的循环
            for i in range(size):
                node = Q.popleft()
                if i < size - 1:
                    node.next = Q[0]

                if node.left:
                    Q.append(node.left)
                if node.right:
                    Q.append(node.right)
        return root

class Solution:
        if not root:
            return root

        leftmost = root
        while leftmost.left: # 判断是否还有下一行
            head = leftmost
            while head:      # 判断本行是否还有右侧的点
                head.left.next = head.right
                if head.next:
                    head.right.next = head.next.left
                head = head.next
            leftmost = leftmost.left
        return root
