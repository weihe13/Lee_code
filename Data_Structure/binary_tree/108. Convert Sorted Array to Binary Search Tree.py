# Given an integer array nums where the elements are sorted in ascending order, convert it to a height-balanced
# binary search tree. A height-balanced binary tree is a binary tree in which the depth of the two subtrees of every
# node never differs by more than one.

# Example 1:
# Input: nums = [-10,-3,0,5,9]
# Output: [0,-3,9,-10,null,5]
# Explanation: [0,-10,5,null,-3,null,9] is also accepted:
# Example 2:
# Input: nums = [1,3]
# Output: [3,1]
# Explanation: [1,3] and [3,1] are both a height-balanced BSTs.

# Constraints:
# 1 <= nums.length <= 104
# -104 <= nums[i] <= 104
# nums is sorted in a strictly increasing order.

# 思路：1. 要理解，inorder traversal of BST就是一个sorted array in ascending order。
#      2. 单独的inorder traversal没法identify一个BST，inorder + preorder或者inorder+postorder可以。
#      3. 因为要height-balanced,因此每次取mid 作为root
#      4. 答案里另外两种方法还需要再理解下

# 时间复杂度：因为每个node visit 1次，O(n)
# 空间复杂度：因为是height-balanced，The recursion stack requires O(logN) space because the tree
# is height-balanced. Note that the O(N) space used to store the output does not count as auxiliary space,
# so it is not included in the space complexity.

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        def helper(left, right):
            if left > right:
                return None

            # always choose left middle node as a root
            p = left + (right - left) // 2

            # preorder traversal: node -> left -> right
            root = TreeNode(nums[p])
            root.left = helper(left, p - 1)
            root.right = helper(p + 1, right)
            return root

        return helper(0, len(nums) - 1)


class Solution2:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        def helper(left, right):
            if left > right:
                return None

            # always choose right middle node as a root
            p = (left + right) // 2
            if (left + right) % 2:
                p += 1

                # preorder traversal: node -> left -> right
            root = TreeNode(nums[p])
            root.left = helper(left, p - 1)
            root.right = helper(p + 1, right)
            return root

        return helper(0, len(nums) - 1)


from random import randint


class Solution3:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        def helper(left, right):
            if left > right:
                return None

            # choose random middle node as a root
            p = (left + right) // 2
            if (left + right) % 2:
                p += randint(0, 1)

                # preorder traversal: node -> left -> right
            root = TreeNode(nums[p])
            root.left = helper(left, p - 1)
            root.right = helper(p + 1, right)
            return root

        return helper(0, len(nums) - 1)

