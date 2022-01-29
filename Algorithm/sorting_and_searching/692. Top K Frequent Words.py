# Given an array of strings words and an integer k, return the k most frequent strings. Return the answer sorted by
# the frequency from highest to lowest. Sort the words with the same frequency by their lexicographical order.

# Example 1: Input: words = ["i","love","leetcode","i","love","coding"], k = 2 Output: ["i","love"] Explanation: "i"
# and "love" are the two most frequent words. Note that "i" comes before "love" due to a lower alphabetical order.
# Example 2: Input: words = ["the","day","is","sunny","the","the","the","sunny","is","is"], k = 4 Output: ["the",
# "is","sunny","day"] Explanation: "the", "is", "sunny" and "day" are the four most frequent words, with the number
# of occurrence being 4, 3, 2 and 1 respectively.

# Constraints:
# 1 <= words.length <= 500
# 1 <= words[i] <= 10
# words[i] consists of lowercase English letters.
# k is in the range [1, The number of unique words[i]]
# Follow-up: Could you solve it in O(n log(k)) time and O(n) extra space?

# 思路： 1. 第一时间想到Counter，问题是如何按照要求排序：通过list.sort
#       2. heap默认先第一个数从小到大，后按第二个输入（这里是字符串）排序

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]：
        # 方法一
        freq = collections.Counter(words)
        # De-duplicated words
        ddwords = list(freq.keys())
        # sort first with decreasing frequency then the second key is the word itself
        ddwords.sort(key=lambda x: (-freq[x], x))
        # return the first k words
        return ddwords[:k]

        # 方法二
        counts = collections.Counter(words)
        # get a array which will have a tuple of word and count
        heap = [(-count, word) for word, count in counts.items()]
        # as default heap structure in python min heap and we want max heap
        # to get top frequent word, we will do a make the counter negative
        # so that the topmost element will come up (i.e -8 < -2 so in min heap -8 will come up wich is actually 8)

        heapq.heapify(heap)  # creating heap in place
        # by deualt it will sort by fre then word

        return [heapq.heappop(heap)[1] for _ in range(k)]
