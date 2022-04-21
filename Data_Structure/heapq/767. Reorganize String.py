# Given a string s, rearrange the characters of s so that any two adjacent characters are not the same.
# Return any possible rearrangement of s or return "" if not possible.

# Example 1:
# Input: s = "aab"
# Output: "aba"
# Example 2:
# Input: s = "aaab"
# Output: ""

# Constraints:
#
# 1 <= s.length <= 500
# s consists of lowercase English letters.

#  Logic: 1. The idea is to build a max heap with freq. count
# a) At each step, we choose the element with highest freq (a, b) where b is the element, to append to result.
# b) Now that b is chosen. We cant choose b for the next loop. So we don't add b with decremented value count
# immediately into the heap. Rather we store it in prev_a, prev_b variables.
# c) Before we update our prev_a, prev_b variables as mentioned in step 2, we know that whatever prev_a,
# prev_b contains, has become eligible for next loop selection. so we add that back in the heap.
# In essence,
# at each step, we make the currently added one ineligible for next step, by not adding it to the heap
# at each step, we make the previously added one eligible for next step, by adding it back to the heap

# The key is each step, we need to add the character with highest count.

import collections
import heapq


class Solution:
    def __init__(self):
        pass

    def reorganizeString(self, s: str) -> str:
        res, counts = [], collections.Counter(s)
        pre_count, pre_char = 0, ''
        heap = [(-value, key) for key, value in counts.items()]
        heapify(heap)

        while heap:
            curr = heapq.heappop(heap)
            res += curr[1]
            if pre_count < 0:  # if pre_count >= 0, we also can update pre_count in this case
                heapq.heappush(heap, (pre_count, pre_char))
            pre_count, pre_char = curr[0], curr[1]
            pre_count += 1
        return "".join(res) if len(res) == len(s) else ""
