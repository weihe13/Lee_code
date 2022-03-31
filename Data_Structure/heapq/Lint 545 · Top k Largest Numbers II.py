# Description
# Implement a data structure, provide two interfaces:
# add(number). Add a new number in the data structure.
# topk(). Return the top k largest numbers in this data structure. k is given when we create the data structure.

# Example1
# Input:
# s = new Solution(3);
# s.add(3)
# s.add(10)
# s.topk()
# s.add(1000)
# s.add(-99)
# s.topk()
# s.add(4)
# s.topk()
# s.add(100)
# s.topk()
# Output:
# [10, 3]
# [1000, 10, 3]
# [1000, 10, 4]
# [1000, 100, 10]
# Explanation:
# s = new Solution(3);
# >> create a new data structure, and k = 3.
# s.add(3)
# s.add(10)
# s.topk()
# >> return [10, 3]
# s.add(1000)
# s.add(-99)
# s.topk()
# >> return [1000, 10, 3]
# s.add(4)
# s.topk()
# >> return [1000, 10, 4]
# s.add(100)
# s.topk()
# >> return [1000, 100, 10]

# 思路：对空数组和只有一个元素的数组，是不需要heapify的。
#      维持一个大小恒定为k的堆，是不需要一直push/pop的，可以先看新来的数字是不是足够大可以进堆，push和pop也可结合起来。
#      一个升序排列的数组也就是一个最完美的堆。一个绝大部分已排好序的数组，再用Python的Timsort排一遍，排的会更快。
import heapq


class Solution1:
    """
    @param: k: An integer
    """

    def __init__(self, k):
        # do intialization if necessary
        self.size = k
        self.heap = []

    """
    @param: num: Number to be added
    @return: nothing
    """

    def add(self, num):
        # write your code here
        heapq.heappush(self.heap, num)
        if len(self.heap) > self.size:
            heapq.heappop(self.heap)

    """
    @return: Top k element
    """

    def topk(self):
        # write your code here
        return sorted(self.heap, reverse=True)  # 注意不能return heap.sort(reverse=True),因为会改变原始heap，导致下次pop的是
        # 剩下的k个数中最大的。（heap其实还是一个arraylist，只是每次heapq.heappush和heapq.heappop都在维持index 0 位置是最小的数。）


from heapq import heappush, heappushpop


class Solution:

    def __init__(self, k):

        self.h = []
        self.k = k

    def add(self, num):

        h, k = self.h, self.k
        # 先判断下能不能进堆，理论上时间会更快
        if len(h) < k:
            heappush(h, num)
        elif num > h[0]:
            heappushpop(h, num)

    def topk(self):
        self.h.sort()
        return self.h[::-1]
