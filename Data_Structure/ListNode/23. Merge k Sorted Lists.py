# You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
# Merge all the linked-lists into one sorted linked-list and return it.

# Example 1:
# Input: lists = [[1,4,5],[1,3,4],[2,6]]
# Output: [1,1,2,3,4,4,5,6]
# Explanation: The linked-lists are:
# [
#   1->4->5,
#   1->3->4,
#   2->6
# ]
# merging them into one sorted list:
# 1->1->2->3->4->4->5->6
# Example 2:
# Input: lists = []
# Output: []
# Example 3:
#
# Input: lists = [[]]
# Output: []
# Constraints:
#
# k == lists.length
# 0 <= k <= 104
# 0 <= lists[i].length <= 500
# -104 <= lists[i][j] <= 104
# lists[i] is sorted in ascending order.
# The sum of lists[i].length will not exceed 104.

# 思路： 1. brute force:
#          (1)Traverse all the linked lists and collect the values of the nodes into an array.
#          (2)Sort and iterate over this array to get the proper value of nodes.
#          (3)Create a new sorted linked list and extend it with the new nodes.
#          time complexity: O(Nlog(N)):where N is the total number of nodes.
#          1) Collecting all the values costs O(N) time.
#          2) A stable sorting algorithm costs O(NlogN) time.
#          3) Iterating for creating the linked list costs O(N) time.
#          space complexity: O(N)
#       2. Use priority queue(heapq):
#          time complexity: O(Nlog(k)):where k is the number of linked list.
#               The comparison cost will be reduced to O(logk) for every pop and insertion to priority queue.
#               But finding the node with the smallest value just costs O(1) time.
#               There are N nodes in the final linked list.
#          space complexity: O(k)
class Solution2:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        class Wrapper():
            def __init__(self, node):
                self.node = node

            def __lt__(self, other):   # 注意ListNode没有__lt__，不能比大小
                return self.node.val < other.node.val

        heap = []
        for l in lists:
            if l:
                heapq.heappush(heap, Wrapper(l))
                l = l.next
        head = pointer = ListNode(0)

        while heap:
            node = heapq.heappop(heap).node
            pointer.next = node
            pointer = pointer.next
            node = node.next
            if node:
                heapq.heappush(heap, Wrapper(node))
        return head.next


class Solution1:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        nodes = []
        for List in lists:
            while List:
                nodes.append(List.val)
                List = List.next
        head = pointer = ListNode(0)

        for node in sorted(nodes):
            pointer.next = ListNode(node)
            pointer = pointer.next

        return head.next
