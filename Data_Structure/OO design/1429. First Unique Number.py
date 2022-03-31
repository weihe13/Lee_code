# You have a queue of integers, you need to retrieve the first unique integer in the queue.
# Implement the FirstUnique class:

# FirstUnique(int[] nums) Initializes the object with the numbers in the queue. int showFirstUnique() returns the
# value of the first unique integer of the queue, and returns -1 if there is no such integer. void add(int value)
# insert value to the queue.

# Example 1:
# Input:
# ["FirstUnique","showFirstUnique","add","showFirstUnique","add","showFirstUnique","add","showFirstUnique"]
# [[[2,3,5]],[],[5],[],[2],[],[3],[]]
# Output:
# [null,2,null,2,null,3,null,-1]
# Explanation:
# FirstUnique firstUnique = new FirstUnique([2,3,5]);
# firstUnique.showFirstUnique(); // return 2
# firstUnique.add(5);            // the queue is now [2,3,5,5]
# firstUnique.showFirstUnique(); // return 2
# firstUnique.add(2);            // the queue is now [2,3,5,5,2]
# firstUnique.showFirstUnique(); // return 3
# firstUnique.add(3);            // the queue is now [2,3,5,5,2,3]
# firstUnique.showFirstUnique(); // return -1
# Example 2:
# Input:
# ["FirstUnique","showFirstUnique","add","add","add","add","add","showFirstUnique"]
# [[[7,7,7,7,7,7]],[],[7],[3],[3],[7],[17],[]]
# Output:
# [null,-1,null,null,null,null,null,17]
# Explanation:
# FirstUnique firstUnique = new FirstUnique([7,7,7,7,7,7]);
# firstUnique.showFirstUnique(); // return -1
# firstUnique.add(7);            // the queue is now [7,7,7,7,7,7,7]
# firstUnique.add(3);            // the queue is now [7,7,7,7,7,7,7,3]
# firstUnique.add(3);            // the queue is now [7,7,7,7,7,7,7,3,3]
# firstUnique.add(7);            // the queue is now [7,7,7,7,7,7,7,3,3,7]
# firstUnique.add(17);           // the queue is now [7,7,7,7,7,7,7,3,3,7,17]
# firstUnique.showFirstUnique(); // return 17
# Example 3:
# Input:
# ["FirstUnique","showFirstUnique","add","showFirstUnique"]
# [[[809]],[],[809],[]]
# Output:
# [null,809,null,-1]
# Explanation:
# FirstUnique firstUnique = new FirstUnique([809]);
# firstUnique.showFirstUnique(); // return 809
# firstUnique.add(809);          // the queue is now [809,809]
# firstUnique.showFirstUnique(); // return -1

# Constraints:
# 1 <= nums.length <= 10^5
# 1 <= nums[i] <= 10^8
# 1 <= value <= 10^8
# At most 50000 calls will be made to showFirstUnique and add.

# 思路： 1. hashmap的查询是O(1),但没有index，考虑用hashmap和array或者hashmap和listNode结合。
#       2. 用hashmap定位后，ListNode删除某个节点就不用再搜索了，所以可以O(1)实现删除和插入
#       3. 即使用hashmap定位，arraylist删除中间节点的时间复杂度也是O(n)。需要结合这道题分析，因为这个class只需要返回第一个unique value，
#          因此重复的值就没用了。所以只需要用hashmap记录每个value是否unique，如果不唯一就直接popleft(删掉)，这样array中的第一个value永
#          远是unique的，不用再重复搜索，showFirstUnique()的时间复杂度就是O(1)(amortized).
#       4. 用ListNode时需要一个dict记录每个点之前的node，方便删除，还需要一个set记录重复的点，空间复杂度虽然还是O(n)，但实际会比用array
#          list高。

class ListNode():
    def __init__(self, num):
        self.val = num
        self.next = None


class FirstUnique1:

    def __init__(self, nums: List[int]):
        self.dummy = ListNode(0)
        self.tail = self.dummy
        self.nums_to_pre = {}
        self.duplicate = set()
        for num in nums:
            self.add(num)

    def showFirstUnique(self) -> int:
        if self.dummy.next:
            return self.dummy.next.val
        return -1

    def add(self, value: int) -> None:
        if value in self.duplicate:  # value已经出现过2次
            return

        if value not in self.nums_to_pre:  # value一次没有出现过
            self.tail.next = ListNode(value)
            self.nums_to_pre[value] = self.tail  # value对应的node指向tail的位置
            self.tail = self.tail.next  # tail重新赋值为tail.next, nums_to_pre[value]不会跟着变
            #  如果是self.tail.val = 10, nums_to_pre[value].val也会变成10
            return

        self.remove(value)  # value已经出现过1次，这是第二次
        self.duplicate.add(value)

    def remove(self, value):
        pre = self.nums_to_pre[value]  # 利用mapping定位到前一个点
        pre.next = pre.next.next  # 删除该节点
        del self.nums_to_pre[value]  # 没有这步也没问题
        if pre.next:  # 如果不是最后一个点，要把删除节点的后一个点的前一个点更新（原本的前一个点是当前节点，已被删除）
            self.nums_to_pre[pre.next.val] = pre
        else:  # 如果是最后一个点，要更新self.tail。
            self.tail = pre


class FirstUnique2:
    # 这里mapping也可以只记录True or False而不是实际出现次数
    def __init__(self, nums: List[int]):
        self.nums = collections.deque(nums)
        self.l = len(self.nums)
        self.mapping = {}
        for i in range(len(nums)):
            if nums[i] not in self.mapping:
                self.mapping[nums[i]] = 1
            else:
                self.mapping[nums[i]] += 1

    def showFirstUnique(self) -> int:
        while self.nums and self.mapping[self.nums[0]] != 1:
            self.nums.popleft()
        if self.nums:
            return self.nums[0]
        return -1

    def add(self, value: int) -> None:
        self.nums.append(value)
        if value in self.mapping:
            self.mapping[value] += 1
        else:
            self.mapping[value] = 1

# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)
