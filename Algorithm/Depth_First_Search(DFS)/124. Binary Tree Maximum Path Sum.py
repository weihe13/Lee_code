# A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge
# connecting them. A node can only appear in the sequence at most once. Note that the path does not need to pass
# through the root. The path sum of a path is the sum of the node's values in the path. Given the root of a binary
# tree, return the maximum path sum of any non-empty path.

# Example 1:
# Input: root = [1,2,3]
# Output: 6
# Explanation: The optimal path is 2 -> 1 -> 3 with a path sum of 2 + 1 + 3 = 6.
# Example 2:
# Input: root = [-10,9,20,null,null,15,7]
# Output: 42
# Explanation: The optimal path is 15 -> 20 -> 7 with a path sum of 15 + 20 + 7 = 42.

# Constraints:
# The number of nodes in the tree is in the range [1, 3 * 104].
# -1000 <= Node.val <= 1000

# 思路：1. 和543很像，想到用DFS，关键同样是用一个nonlocal的变量记录到目前为止的最大sum。dfs内部计算的是以当前node为root的最大sum，每次
#         把以当前node为root的最大sum和maxsum比较，看是否要更新maxsum。
#      2. 这种题在function 内定义内部function通过nonlocal计算比较简单。定义一个同级别function会比较麻烦，因为还要不停返回maxsum。

class Solution:
    def __init__(self):
        pass

    def maxPathSum(self, root):
        def max_gain(node):
            nonlocal max_sum
            if not node:
                return 0  # 要先想清楚底层return的是什么，然后逐级返回

            # max sum on the left and right sub-trees of node
            left_gain = max(max_gain(node.left), 0)  # 左边能获得的最大sum
            right_gain = max(max_gain(node.right), 0)  # 右边能获得的最大sum

            # the price to start a new path where `node` is a highest node
            price_newpath = node.val + left_gain + right_gain  # 以当前node为root的最大sum

            # update max_sum if it's better to start a new path
            max_sum = max(max_sum, price_newpath)

            # for recursion :
            # return the max gain if continue the same path
            return node.val + max(left_gain, right_gain)  # 往上层return时左右只能选一个，选更大的那个。（如果为负上层会drop）

        max_sum = float('-inf')
        max_gain(root)
        return max_sum


# 思路一样，写法不同，两个平级function
class Solution2:
    def __init__(self):
        pass

    def maxPathSum(self, root):
        _, max_sum = self.get_max(root)
        return max_sum

    def get_max(self, root):
        if not root:
            return 0, -float("inf")
        get_left, left_max = self.get_max(root.left)
        get_right, right_max = self.get_max(root.right)
        get_left_max = max(get_left, 0)
        get_right_max = max(get_right, 0)
        curr_max = root.val + get_left_max + get_right_max
        max_sum = max(curr_max, right_max, left_max)
        return root.val + max(get_left_max, get_right_max), max_sum
