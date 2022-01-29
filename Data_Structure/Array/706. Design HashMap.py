# Design a HashMap without using any built-in hash table libraries. Implement the MyHashMap class: MyHashMap()
# initializes the object with an empty map. void put(int key, int value) inserts a (key, value) pair into the
# HashMap. If the key already exists in the map, update the corresponding value. int get(int key) returns the value
# to which the specified key is mapped, or -1 if this map contains no mapping for the key. void remove(key) removes
# the key and its corresponding value if the map contains the mapping for the key.

# Example 1:
# Input
# ["MyHashMap", "put", "put", "get", "get", "put", "get", "remove", "get"]
# [[], [1, 1], [2, 2], [1], [3], [2, 1], [2], [2], [2]]
# Output
# [null, null, null, 1, -1, null, 1, null, -1]
# Explanation
# MyHashMap myHashMap = new MyHashMap();
# myHashMap.put(1, 1); // The map is now [[1,1]]
# myHashMap.put(2, 2); // The map is now [[1,1], [2,2]]
# myHashMap.get(1);    // return 1, The map is now [[1,1], [2,2]]
# myHashMap.get(3);    // return -1 (i.e., not found), The map is now [[1,1], [2,2]]
# myHashMap.put(2, 1); // The map is now [[1,1], [2,1]] (i.e., update the existing value)
# myHashMap.get(2);    // return 1, The map is now [[1,1], [2,1]]
# myHashMap.remove(2); // remove the mapping for 2, The map is now [[1,1]]
# myHashMap.get(2);    // return -1 (i.e., not found), The map is now [[1,1]]

# Constraints:
# 0 <= key, value <= 106
# At most 104 calls will be made to put, get, and remove.

# 思路：1. 首先一定要看清题目要求，不能用built-in hash table function。
#      2. 因为输入都是int，想到用%（mod）来对数据进行hash，形成一个list of lists。
class Bucket:
    def __init__(self):
        self.bucket = []

    def get(self, key):
        for (k, v) in self.bucket:   # 注意，每一步改变bucket时都要有self.
            if k == key:
                return v
        return -1

    def update(self, key, value):
        found = False
        for i, kv in enumerate(self.bucket):  # 注意enumerate的用法，如果直接用k, v，if k==key 改v，不会改变list中的v
            if kv[0] == key:
                self.bucket[i] = (key, value)
                found = True
                break
        if not found:
            self.bucket.append((key, value))

    def remove(self, key):
        for i, kv in enumerate(self.bucket):
            if kv[0] == key:
                del self.bucket[i]      # 删除list中的元素，del


class MyHashMap:

    def __init__(self):
        self.space = 2200
        self.buckets = [Bucket() for i in range(2200)]

    def put(self, key: int, value: int) -> None:
        hash_key = key % self.space     # 调用时记得加self.
        return self.buckets[hash_key].update(key, value)  # 注意hash_key只是用来定位第几个bucket，添加的时候还是加原key

    def get(self, key: int) -> int:
        hash_key = key % self.space
        return self.buckets[hash_key].get(key)

    def remove(self, key: int) -> None:
        hash_key = key % self.space
        return self.buckets[hash_key].remove(key)

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)