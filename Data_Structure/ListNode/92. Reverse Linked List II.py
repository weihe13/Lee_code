# Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of
# the list from position left to position right, and return the reversed list.

# Example 1:
# Input: head = [1,2,3,4,5], left = 2, right = 4
# Output: [1,4,3,2,5]
# Example 2:
# Input: head = [5], left = 1, right = 1
# Output: [5]

# Constraints:
# The number of nodes in the list is n.
# 1 <= n <= 500
# -500 <= Node.val <= 500
# 1 <= left <= right <= n
# Follow up: Could you do it in one pass?

# 思路： 1. 以reverse linked list为基础，这里要把m位置变成最后一个位置，所以从m位置的next开始反转，先把该位置的next单独指出，
#          然后m位置的next位置掉头指向m位置，把m位置的next位置重新指出，依次循环。
#       2. 每一个变量都是代表指向一个存储空间，一个位置，这个理解很重要。所以先用frozen变量把m位置存下来，掉头完成后，m位置的next
#          仍然指向原始链条中m位置的next，这时把m.next重新指向n.next的位置，m到n才转换完成。

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # write your code here
        dummy = ListNode(0)
        dummy.next = head
        p1 = dummy
        p2 = head
        for i in range(left - 1):
            p1 = p1.next
            p2 = p2.next

        p1_frozen = p1  # p1_frozen指向m之前的位置，最后拼接上n位置
        p2_frozen = p2  # p2_frozen指向m的位置，最后拼接上n.next的位置
        p1 = p1.next
        p2 = p2.next

        for i in range(right - left):
            p3 = p2.next
            p2.next = p1
            p1 = p2
            p2 = p3

        p1_frozen.next = p1
        p2_frozen.next = p2

        return dummy.next
