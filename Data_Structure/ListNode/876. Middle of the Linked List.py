# Given the head of a singly linked list, return the middle node of the linked list.
# If there are two middle nodes, return the second middle node.

# Example 1:
# Input: head = [1,2,3,4,5]
# Output: [3,4,5]
# Explanation: The middle node of the list is node 3.
# Example 2:
# Input: head = [1,2,3,4,5,6]
# Output: [4,5,6]
# Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.

# Constraints:
# The number of nodes in the list is in the range [1, 100].
# 1 <= Node.val <= 100

# 思路： 1. 自己想法：先把head从头到尾走一遍，得到长度，知道哪个位置是中间后再走一遍。
#       2. 两个指针，一个的速度是另一个的两倍，当快的走到后满的正好在中间位置，要注意通过判断fast和fast.next看fast是否还能继续走。
#       3. 用一个list把node按顺序存下来，空间复杂度高，但是写法可以学习下(通过array[-1]把list和listnode联系起来了)。

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 自己的方法，O(n)时间复杂度
        length = 1
        listnode = head
        while listnode.next is not None:
            listnode = listnode.next
            length += 1

        for i in range(length // 2):
            head = head.next
        return head

        # two pointers
        slow = fast = head
        while fast and fast.next: # 注意除了要判断fast是不是None，还要判断fast.next,只要fast.next是None，就不能继续了
                                  # 偶数node时fast会成为None，奇数node时，fast.next会成为None。
            slow = slow.next
            fast = fast.next.next
        return slow

        # 用一个list把node存下来
        arr = [head]
        while arr[-1].next:
            arr.append(arr[-1].next)
        return arr[len(arr) // 2]