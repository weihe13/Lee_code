# Given the head of a linked list, remove the nth node from the end of the list and return its head.

# Example 1:
# Input: head = [1,2,3,4,5], n = 2
# Output: [1,2,3,5]
# Example 2:
# Input: head = [1], n = 1
# Output: []
# Example 3:
# Input: head = [1,2], n = 1
# Output: [1]

# Constraints:
# The number of nodes in the list is sz.
# 1 <= sz <= 30
# 0 <= Node.val <= 100
# 1 <= n <= sz

# 思路：1. 考虑先过一遍listNode得到长度，那么倒数第n个元素就是length-n+1个元素，就简单了。通过length-n次move可以到达第length-n+1个
#         元素，所以先通过length-n-1次move，到达第length-n个元素，然后.next = .next.next，删掉目标元素。
#      2. 要注意的是当链条长度等于n时，意味着去掉的是第一个元素，所以没有第length-n个元素，不会触发循环，删不掉第一个元素，另外当只有
#         一个元素时，.next = .next.next会报错，因为None没有.next，所以考虑设置dummy,dummy.next = head。
#      3. 不用dummy也可以，但需要多讨论一种情况，当要删除的就是第一个元素时，直接return head.next。
#      4. The above algorithm could be optimized to one pass. Instead of one pointer, we could use two pointers.
#      The first pointer advances the list by n+1 steps from the beginning, while the second pointer starts from
#      the beginning of the list. Now, both pointers are exactly separated by n nodes apart. We maintain this constant
#      gap by advancing both pointers together until the first pointer arrives past the last node. The second pointer
#      will be pointing at the nth node counting from the last. We relink the next pointer of the node referenced by
#      the second pointer to point to the node's next next node.
#      5. 想改变ListNode从而进行自我迭代时，一定要注意两个指针要等于需要改变的ListNode,否则比如：
#         dummy = ListNode()
#         dummy.next = head
#         first = ListNode()
#         first.next = head
#         second = ListNode()
#         second.next = head
#         这时如果n!=listNode的长度，会修改head位置的链条，，而dummy.next=head指向同一位置，dummy也会变。
#         但如果n==ListNode的长度，不会跑第二次循环而是直接second.next = second.next.next，这时second正确地去掉了第一个元素，
#         但因为改的时second.next,没有改变head位置的链条，所以dummy不会改变。因此正确写法是：
#         dummy = ListNode()
#         dummy.next = head
#         first = dummy
#         second =dummy

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        copy = dummy
        length = 1
        while copy.next is not None:
            copy = copy.next
            length += 1

        before_remove = dummy
        for i in range(length - n - 1):  # 第length-n+1个数，移动length-n次正好到要去掉的位置，
            # length -n -1到他之前
            before_remove = before_remove.next
        before_remove.next = before_remove.next.next
        return dummy.next  # 注意，


class Solution_1: #不用dummy
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        copy = head
        length = 1
        while copy.next is not None:
            copy = copy.next
            length += 1

        if length == n:      # 判断一下要删除的是否是第一个元素
            return head.next

        before_remove = head
        for i in range(length - n - 1):  # 第length-n+1个数，移动length-n次正好到要去掉的位置，
            # length -n -1到他之前
            before_remove = before_remove.next
        before_remove.next = before_remove.next.next
        return head

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        first = dummy
        second =dummy
        for i in range(n):
            first = first.next
        while first.next is not None:
            first = first.next
            second = second.next
        second.next = second.next.next
        return dummy.next