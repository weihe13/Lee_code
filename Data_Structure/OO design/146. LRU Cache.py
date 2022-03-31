# Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.
# Implement the LRUCache class:

# LRUCache(int capacity) Initialize the LRU cache with positive size capacity. int get(int key) Return the value of
# the key if the key exists, otherwise return -1. void put(int key, int value) Update the value of the key if the key
# exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this
# operation, evict the least recently used key. The functions get and put must each run in O(1) average time
# complexity.

# Example 1:
# Input
# ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
# [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
# Output
# [null, null, null, 1, null, -1, null, -1, 3, 4]
# Explanation
# LRUCache lRUCache = new LRUCache(2);
# lRUCache.put(1, 1); // cache is {1=1}
# lRUCache.put(2, 2); // cache is {1=1, 2=2}
# lRUCache.get(1);    // return 1
# lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
# lRUCache.get(2);    // returns -1 (not found)
# lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
# lRUCache.get(1);    // return -1 (not found)
# lRUCache.get(3);    // return 3
# lRUCache.get(4);    // return 4

# Constraints:
# 1 <= capacity <= 3000
# 0 <= key <= 104
# 0 <= value <= 105
# At most 2 * 105 calls will be made to get and put.

# 思路： 1. 可以用hashmap去记录每个key对应的前一个node，方便添加和删除，用listnode记录顺序，实现O(1)操作

class ListNode:
    def __init__(self, key=None, val=None):
        self.key = key
        self.val = val
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dummy = ListNode()
        self.tail = self.dummy
        self.key_to_pre = {}

    def get(self, key: int) -> int:
        if key in self.key_to_pre:
            self.kick(key)
            return self.tail.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.key_to_pre:
            self.kick(key)
            self.tail.val = value
        else:
            curr = ListNode(key, value)
            self.push_end(curr)
        if len(self.key_to_pre) > self.capacity:
            self.pop_front()

    def pop_front(self):
        curr = self.dummy.next
        self.dummy.next = curr.next
        del self.key_to_pre[curr.key]
        self.key_to_pre[curr.next.key] = self.dummy

    def kick(self, key):
        pre = self.key_to_pre[key]
        curr = pre.next
        if self.tail == curr:
            return
        pre.next = curr.next
        self.key_to_pre[curr.next.key] = pre
        curr.next = None
        self.push_end(curr)

    def push_end(self, node):
        self.tail.next = node
        self.key_to_pre[node.key] = self.tail
        self.tail = self.tail.next

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)