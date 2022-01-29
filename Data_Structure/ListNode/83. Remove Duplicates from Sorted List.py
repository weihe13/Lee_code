# Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the
# linked list sorted as well.

# Example 1:
# Input: head = [1,1,2]
# Output: [1,2]
# Example 2:
# Input: head = [1,1,2,3,3]
# Output: [1,2,3]

# Constraints:
# The number of nodes in the list is in the range [0, 300].
# -100 <= Node.val <= 100
# The list is guaranteed to be sorted in ascending order.

# 思路：1. 因为已经说是sorted的list了，可以直接比较curr和curr.next的value，如果相等就留curr，删curr.next
#      2. 如果没说sort，可以用hashmap

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        hashmap = {}
        curr = res = ListNode(1000)
        curr.next = head
        while curr:
            while curr.next and curr.next.val in hashmap:
                curr.next = curr.next.next
                if not curr.next: # 如果已经到了最后一个node
                    return res.next
                # 判断过curr.next.val不在hashmap里了，加进去
                hashmap[curr.next.val] = hashmap.get(curr.next.val, 0) + 1
                curr = curr.next
        return res.next

class Solution2:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = res = ListNode(1000)
        curr.next = head
        while curr and curr.next:
            if curr.next.val == curr.val:
                curr.next = curr.next.next
            else:
                curr = curr.next
        # 当curr或者curr.next是None时，说明已经判断过最后一个node
        return res.next