# Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect. If
# the two linked lists have no intersection at all, return null. For example, the following two linked lists begin to
# intersect at node c1: The test cases are generated such that there are no cycles anywhere in the entire linked
# structure. Note that the linked lists must retain their original structure after the function returns.

# Example 1: Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,6,1,8,4,5], skipA = 2, skipB = 3 Output:
# Intersected at '8' Explanation: The intersected node's value is 8 (note that this must not be 0 if the two lists
# intersect). From the head of A, it reads as [4,1,8,4,5]. From the head of B, it reads as [5,6,1,8,4,5]. There are 2
# nodes before the intersected node in A; There are 3 nodes before the intersected node in B.
# Example 2: Input: intersectVal = 2, listA = [1,9,1,2,4], listB = [3,2,4], skipA = 3, skipB = 1 Output: Intersected
# at '2' Explanation: The intersected node's value is 2 (note that this must not be 0 if the two lists intersect).
# From the head of A, it reads as [1,9,1,2,4]. From the head of B, it reads as [3,2,4]. There are 3 nodes before the
# intersected node in A; There are 1 node before the intersected node in B.
# Example 3: Input: intersectVal = 0, listA = [2,6,4], listB = [1,5], skipA = 3, skipB = 2 Output: No intersection
# Explanation: From the head of A, it reads as [2,6,4]. From the head of B, it reads as [1,5]. Since the two lists do
# not intersect, intersectVal must be 0, while skipA and skipB can be arbitrary values. Explanation: The two lists do
# not intersect, so return null.

# Constraints:
# The number of nodes of listA is in the m.
# The number of nodes of listB is in the n.
# 1 <= m, n <= 3 * 104
# 1 <= Node.val <= 105
# 0 <= skipA < m
# 0 <= skipB < n
# intersectVal is 0 if listA and listB do not intersect.
# intersectVal == listA[skipA] == listB[skipB] if listA and listB intersect.

# Follow up: Could you write a solution that runs in O(m + n) time and use only O(1) memory?

# 思路：1. 首先想清楚什么样的node是相同的node？可以用node1 == node2直接判断，val 和 next都相等。意味着next只向相同的位置，之后的node
#         val和数量完全一样。
#      2. 因为可以用node1 == node2直接判断是否相等，想到hash table，遍历N，把每个node存到一个set里，再遍历另一个list，看是否有node存
#         在set中。因此时间复杂度O(N+M),空间复杂度O(N).
#      3. 因为肯定需要遍历两个list的每一个node，所以时间复杂度一定是O(n+m)不可能减小了，考虑优化空间复杂度。
#         分析：注意这道题的intersection，一定是从一个node一直到结尾完全一样（中间一段相等不属于本体的intersection）。因此可以先把两个
#         list都遍历一遍，找到长度，然后把长的那个定位到和短的一样长的位置，同时移动两个pointer，每次移动前比较是否相等。
#      4. 进一步优化，通过一次遍历完成搜索。分析：M+N == N+M,且如果存在intersection，无论从list1到list2还是从list2到list1，最后一定
#         会同时指向intersection的node head。用两个指针，分别指向headA和headB，分别遍历两个list，None就指向另一个list的head，直到
#         相等（注意，如果没有intersection，最后两个指针也会同时指向None，仍然会相等，终止循环）。
#         这样时间复杂度O(n+m),空间复杂度O(1)。

class Solution1:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        nodes_in_B = set()

        while headB is not None:
            nodes_in_B.add(headB)
            headB = headB.next

        while headA is not None:
            # if we find the node pointed to by headA,
            # in our set containing nodes of B, then return the node
            if headA in nodes_in_B:
                return headA
            headA = headA.next

        return None


class Solution2:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        pA = headA
        pB = headB

        while pA != pB:
            pA = headB if pA is None else pA.next
            pB = headA if pB is None else pB.next

        return pA  # 最后pA pB一定相等，return哪个都一样

        # Note: In the case lists do not intersect, the pointers for A and B
        # will still line up in the 2nd iteration, just that here won't be
        # a common node down the list and both will reach their respective ends
        # at the same time. So pA will be NULL in that case.
