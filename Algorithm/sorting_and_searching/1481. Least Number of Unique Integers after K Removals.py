# Given an array of integers arr and an integer k. Find the least number of unique integers after removing exactly k
# elements.
# Example 1: Input: arr = [5,5,4], k = 1 Output: 1 Explanation: Remove the single 4, only 5 is left.
# Example 2: Input: arr = [4,3,1,1,3,3,2], k = 3 Output: 2 Explanation: Remove 4, 2 and either one of the two 1s or
# three 3s. 1 and 3 will be left.

# Constraints:
# 1 <= arr.length <= 10^5
# 1 <= arr[i] <= 10^9
# 0 <= k <= arr.length

# 思路： 1. 第一时间想到Counter后排序，然后就是细节问题
#       2. 最后循环判断时，考虑到如果input是[1], 1，需要提前判断return的结果，所以用removed+i和k去比，而不是removed和k比
#       3. 这里按value对diction排序时，可以只保留value，不需要key，更方便。
#          如果保留key一起排序，写法是:sorted_counts = sorted(counts.items(), key=lambda item: item[1])

class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        from collections import Counter
        dict = Counter(arr)
        length = len(dict)
        valdict = sorted(dict.values())
        removed = 0

        for val in valdict:
            if (removed+val) > k: # 已经去掉的element数量加上下一个数字的frequency会大于k，所以下一个数字不能全部剔除
                return length
            elif (removed+val) == k: # 下一个element正好能全部剔除
                return length-1
            else:
                removed += val  # 如果用removed去和k比，对于input为[1], 1的情况，'1'循环完就结束了，会return None
                length -= 1

        # 快很多的循环写法：
        for count in dict:
            if k >= count:
                k = k - count
                length -= 1
            else:
                return length

            if k == 0:
                return length
