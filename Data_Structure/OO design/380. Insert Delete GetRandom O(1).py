# Implement the RandomizedSet class: RandomizedSet() Initializes the RandomizedSet object. bool insert(int val)
# Inserts an item val into the set if not present. Returns true if the item was not present, false otherwise. bool
# remove(int val) Removes an item val from the set if present. Returns true if the item was present, false otherwise.
# int getRandom() Returns a random element from the current set of elements (it's guaranteed that at least one
# element exists when this method is called). Each element must have the same probability of being returned. You must
# implement the functions of the class such that each function works in average O(1) time complexity.

# Example 1:
# Input
# ["RandomizedSet", "insert", "remove", "insert", "getRandom", "remove", "insert", "getRandom"]
# [[], [1], [2], [2], [], [1], [2], []]
# Output
# [null, true, false, true, 2, true, false, 2]
# Explanation
# RandomizedSet randomizedSet = new RandomizedSet();
# randomizedSet.insert(1); // Inserts 1 to the set. Returns true as 1 was inserted successfully.
# randomizedSet.remove(2); // Returns false as 2 does not exist in the set.
# randomizedSet.insert(2); // Inserts 2 to the set, returns true. Set now contains [1,2].
# randomizedSet.getRandom(); // getRandom() should return either 1 or 2 randomly.
# randomizedSet.remove(1); // Removes 1 from the set, returns true. Set now contains [2].
# randomizedSet.insert(2); // 2 was already in the set, so return false.
# randomizedSet.getRandom(); // Since 2 is the only number in the set, getRandom() will always return 2.

# Constraints:
# -231 <= val <= 231 - 1
# At most 2 * 105 calls will be made to insert, remove, and getRandom.
# There will be at least one element in the data structure when getRandom is called.

# 思路： 1. insert 和 remove操作需要判断val是否在randomset中，很容易想到hashmap或者hashset。想要O(1)随机获取元素，可以用random随机
#          获取index，但是hashmap和hashset没有index，想到把arraylist和hashmap结合。
#       2. remove操作时，hash只需要O(1),但是list删除中间元素需要O(n)。这里有个算法技巧，对list中指定位置重新赋值为最后一个元素的value，
#          再把最后一个元素删除，就能实现O(1)删除指定位置的元素了。（因为在这道题里顺序不重要）
class RandomizedSet:

    def __init__(self):
        self.map = {}
        self.list = []

    def insert(self, val: int) -> bool:
        if val in self.map:
            return False
        self.map[val] = len(self.list)
        self.list.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.map:
            return False
        last = self.list[-1]
        index = self.map[val]
        self.list[index] = last
        self.map[last] = index
        self.list.pop()
        del self.map[val]
        return True

    def getRandom(self) -> int:
        index = random.randint(0, len(self.list)-1)
        return self.list[index]

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
