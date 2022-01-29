# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
# Implement the MinStack class:
# MinStack() initializes the stack object.
# void push(int val) pushes the element val onto the stack.
# void pop() removes the element on the top of the stack.
# int top() gets the top element of the stack.
# int getMin() retrieves the minimum element in the stack.

# Example 1:
# Input
# ["MinStack","push","push","push","getMin","pop","top","getMin"]
# [[],[-2],[0],[-3],[],[],[],[]]
# Output
# [null,null,null,null,-3,null,0,-2]
# Explanation
# MinStack minStack = new MinStack();
# minStack.push(-2);
# minStack.push(0);
# minStack.push(-3);
# minStack.getMin(); // return -3
# minStack.pop();
# minStack.top();    // return 0
# minStack.getMin(); // return -2

# Constraints:
# -231 <= val <= 231 - 1
# Methods pop, top and getMin operations will always be called on non-empty stacks.
# At most 3 * 104 calls will be made to push, pop, top, and getMin.

# 思路：1. 核心想法后进来的元素会放到最上面，不管最上面的元素怎么变，只要拿它和min比就行，比min大就不会影响min。getmin()只需要return min

class MinStack:
    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append((val, val))
            return  # 跳过下面 这里return很重要，否则还会继续执行code

        current_min = self.stack[-1][1]
        self.stack.append((val, min(val, current_min)))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]

# Time Complexity : O(1) for all operations.
# push(...): Checking the top of a Stack, comparing numbers, and pushing
# to the top of a Stack (or adding to the end of an Array or List) are all O(1) operations. Therefore,
# this overall is an O(1) operation.
#
# pop(...): Popping from a Stack (or removing from the end of an Array, or List) is an O(1)O(1) operation.
#
# top(...): Looking at the top of a Stack is an O(1) operation.
#
# getMin(...): Same as above. This operation is O(1) because we do not need to compare values to find it. If we
# had not kept track of it on the Stack, and instead had to search for it each time, the overall time complexity
# would have been O(n).
#
# Space Complexity : O(n).
# Worst case is that all the operations are push. In this case, there will be O(2 \cdot n) = O(n)O(2⋅n)=O(n) space used.
