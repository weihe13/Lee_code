# Design a max stack data structure that supports the stack operations and supports finding the stack's maximum
# element. Implement the MaxStack class: MaxStack() Initializes the stack object. void push(int x) Pushes element x
# onto the stack. int pop() Removes the element on top of the stack and returns it. int top() Gets the element on the
# top of the stack without removing it. int peekMax() Retrieves the maximum element in the stack without removing it.
# int popMax() Retrieves the maximum element in the stack and removes it. If there is more than one maximum element,
# only remove the top-most one.

# Example 1:
# Input
# ["MaxStack", "push", "push", "push", "top", "popMax", "top", "peekMax", "pop", "top"]
# [[], [5], [1], [5], [], [], [], [], [], []]
# Output
# [null, null, null, null, 5, 5, 1, 5, 1, 5]
# Explanation
# MaxStack stk = new MaxStack();
# stk.push(5);   // [5] the top of the stack and the maximum number is 5.
# stk.push(1);   // [5, 1] the top of the stack is 1, but the maximum is 5.
# stk.push(5);   // [5, 1, 5] the top of the stack is 5, which is also the maximum, because it is the top most one.
# stk.top();     // return 5, [5, 1, 5] the stack did not change.
# stk.popMax();  // return 5, [5, 1] the stack is changed now, and the top is different from the max.
# stk.top();     // return 1, [5, 1] the stack did not change.
# stk.peekMax(); // return 5, [5, 1] the stack did not change.
# stk.pop();     // return 1, [5] the top of the stack and the max element is now 5.
# stk.top();     // return 5, [5] the stack did not change.

class MaxStack():

    def __init__(self):
        self.stack = []

    """
    @param: number: An integer
    @return: nothing
    """

    def push(self, x):
        self.stack.append(x)

    """
    @return: An integer
    """

    def pop(self):
        return self.stack.pop()

    """
    @return: An integer
    """

    def top(self):
        return self.stack[-1]

    """
    @return: An integer
    """

    def peekMax(self):
        return max(self.stack)

    """
    @return: An integer
    """

    def popMax(self):  #
        maxnum = max(self.stack)
        for i in range(len(self.stack) - 1, -1, -1):
            if self.stack[i] == maxnum:
                self.stack.pop(i)
                break
        return maxnum

# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()
