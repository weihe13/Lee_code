# Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val ==
# val, and return the new head.

# Example 1:
# Input: head = [1,2,6,3,4,5,6], val = 6
# Output: [1,2,3,4,5]
# Example 2:
# Input: head = [], val = 1
# Output: []
# Example 3:
# Input: head = [7,7,7,7], val = 7
# Output: []

# Constraints:
# The number of nodes in the list is in the range [0, 104].
# 1 <= Node.val <= 50
# 0 <= val <= 50

# 思路： 1. 按顺序排查，发现是val就连下一个node
#       2. 注意需要另设curr.next= head， 然后开始循环，这样才能排查到第一个node
#       3. 发现curr.next.val == val，并curr.next = curr.next.next后，仍然要判断curr.next.val是否是val，所以想到while循环


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        curr = res = ListNode(1)
        curr.next = head  # res.next这里也指向了head
        while curr:  # 判断当前node，不是None才可以curr.next，是None就说明遍历完了
            while curr.next and curr.next.val == val:  # 判断curr.next，不是None，才可以curr.next.val。且若是None则说明已经循环
                # 到最后一个node，且该node已经判断过不是val(否则会继续curr.next)。所以
                # 不再内层循环，执行curr = curr.next(None),跳出外层循环，return res.next
                curr.next = curr.next.next
            curr = curr.next
        return res.next
