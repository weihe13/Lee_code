# You are given the heads of two sorted linked lists list1 and list2. Merge the two lists in a one sorted list. The
# list should be made by splicing together the nodes of the first two lists. Return the head of the merged linked list.

# Example 1:
# Input: list1 = [1,2,4], list2 = [1,3,4]
# Output: [1,1,2,3,4,4]
# Example 2:
# Input: list1 = [], list2 = []
# Output: []
# Example 3:
# Input: list1 = [], list2 = [0]
# Output: [0]

# Constraints:
# The number of nodes in both lists is in the range [0, 50].
# -100 <= Node.val <= 100
# Both list1 and list2 are sorted in non-decreasing order.
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # recursion
        # 一直寻找更小的header
        # 第一个merge决定的是第一个header是l1.val，第二个merge决定的是第二个header，以此类推，最后一级一级return回来，

        # if l1 is None:
        #     return l2
        # elif l2 is None:
        #     return l1
        # elif l1.val < l2.val:
        #     l1.next = self.mergeTwoLists(l1.next, l2)
        #     return l1
        # else:
        #     l2.next = self.mergeTwoLists(l1, l2.next)
        #     return l2

        # 答案二思路，比自己思路简单非常多：
        # 1. 先考虑list1 和list2一样长时的情况，再考虑不一样长的情况，分开写
        # 2. 直接用prev.next = list1 或者list2, 不用再改prev.val
        prehead = ListNode(-1)

        prev = prehead
        while l1 and l2:
            if l1.val <= l2.val:
                prev.next = l1
                l1 = l1.next
            else:
                prev.next = l2
                l2 = l2.next
            prev = prev.next

        # At least one of l1 and l2 can still have nodes at this point, so connect
        # the non-null list to the end of the merged list.
        prev.next = l1 if l1 is not None else l2

        return prehead.next

        # 自己思路，速度还行，但要考虑的情况太多了，类似把所有情况同时考虑：
        # 1. 注意不能用if not l2，得用if l2 is not None（why？https://towardsdatascience.com/python-the-boolean-confusion-f7fc5288f0ce）
        # 2. 因为不是直接赋值list1,而是赋值l1(list1.val)或者l2,不仅在考虑list1是不是None，还在考虑l1是不是None，麻烦很多
        # 3. 需要先prev.next = ListNode()再prev = prev.next，否则新的prev不是ListNode Class，而是None，没有val
#         ans = ListNode()
#         tmp = ans

#         while True:
#             if list1:
#                 l1 = list1.val
#             else:
#                 l1 = None
#             if list2:
#                 l2 = list2.val
#             else:
#                 l2 = None

#             if l1 is not None and l2 is not None:
#                 if l1 < l2:
#                     tmp.val = l1
#                     list1 = list1.next
#                 else:
#                     tmp.val = l2
#                     list2 = list2.next
#             else:
#                 if l1 is None and l2 is None:
#                     return None
#                 elif l1 is None:
#                     tmp.val = l2
#                     list2 = list2.next
#                 elif l2 is None:
#                     tmp.val = l1
#                     list1 = list1.next
#             if not list1 and not list2:
#                 break
#             tmp.next = ListNode()
#             tmp = tmp.next
#         return ans