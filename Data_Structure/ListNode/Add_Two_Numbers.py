# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse
# order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.
# 2 -> 4 -> 3
# 5 -> 6 -> 4
# answer: 7 -> 0 -> 8
# explanation: 342+465 = 807
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        # 直接在当前Node改，所以每次先add listnode(0)再改，因此add新node前要判断sums 是否为0
        # 这种题要记住，虽然输入l1 l2的是一串链条，但真正输入的只是起始的node！只有一个val和next
        # 为什么必须要tmp = ans？
        # 1. 必须要自我迭代才能把一个链条变长(通过tmp = tmp.next),否则一直tmp = ans.next始终改的是初始node的next
        # 2. 但是自我迭代的时候，如果直接用ans，那么ans一直在被赋值为ans.next，没有记录之前的改变

        #         ans = ListNode(0)
        #         tmp = ans
        #         sums = 0

        #         while True:
        #             if l1:
        #                 sums += l1.val
        #                 l1 = l1.next
        #             if l2:
        #                 sums += l2.val
        #                 l2 = l2.next
        #             tmp.val = sums % 10
        #             sums //= 10

        #             if not l1 and not l2 and not sums:
        #                 break
        #             tmp.next = ListNode(0)
        #             tmp = tmp.next
        #         return ans

        # add的是listnode(out),不用加listnode(0)再然后改val，可以和l1 l2一起判断是否为0/None
        # l1 = l1.next前要先判断是否为None，因为None没有next method
        result = ListNode(0)
        result_tail = result
        carry = 0

        while l1 or l2 or carry:
            val1 = (l1.val if l1 else 0)
            val2 = (l2.val if l2 else 0)
            carry, out = divmod(val1 + val2 + carry, 10)

            result_tail.next = ListNode(out)
            result_tail = result_tail.next

            l1 = (l1.next if l1 else None)
            l2 = (l2.next if l2 else None)

        return result.next