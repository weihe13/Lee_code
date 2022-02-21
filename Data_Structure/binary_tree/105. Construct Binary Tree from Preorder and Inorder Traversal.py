# Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.

# Example 1:
# Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
# Output: [3,9,20,null,null,15,7]
# Example 2:
# Input: preorder = [-1], inorder = [-1]
# Output: [-1]

# Constraints:
# 1 <= preorder.length <= 3000
# inorder.length == preorder.length
# -3000 <= preorder[i], inorder[i] <= 3000
# preorder and inorder consist of unique values.
# Each value of inorder also appears in preorder.
# preorder is guaranteed to be the preorder traversal of the tree.
# inorder is guaranteed to be the inorder traversal of the tree.

# 思路： 1. 注意限制条件，preorder and inorder consist of unique values，满足这个条件才能用inorder_map
#       2. 可以回看solution的解释，关键是理解，对于inorder list，root左边和右边的sublist就是sub tree，而对于preorder list，root
#          一定是preorder[0],且接着一定先遍历左边，然后才是右边，preorder[1]就是left sub tree的root。
#       3. inorder[0:root.index-1]遍历完时，意味着preorder list的左边也遍历完了，下一个index的数就是right sub list 的root（因为
#          是preorder，先加root.val），再下一个index的数就是sublist的left sublist的root.val,以此类推，recursion下去。
#       4. 对于tree，除了leef node，所有的node都是sub tree的root node。inorder list能告诉我们root左边和root右边分别有哪些node，但
#          具体顺序不知道（有点类似quick sort），preorder list能告诉我们node的顺序，但不知道在左边还是右边，所以结合起来。
#       5. preorder能告诉我们下一个应该加的node，但是不知道是left node还是right node。这时通过inorder list告诉我们应该加到左边还是右
#          边：如果root左边没有sub tree了（left>right），则preorder的下一个数要加到right node，如果root右边也没有sub tree了
#          （left2 > right2）,则意味着本层root遍历完了没有leef node（他自己就是leef node），return本层root，加到上层root的left
#          node，继续检查上层root的right node，若上层root的right node左边有sub tree（left3 < right3），则添加。
#       6. 规律：inorder traversal of BST is an array sorted in the ascending order。
#               inorder traversal is not a unique identifier of BST，but inorder+preorder or inorder+postorder are both
#               unique identifier of BST。
# 时间复杂度： 先遍历inorder list形成hashmap，是O(n)。build tree时，一次recursion是O(1), 一个node就对应一次recursion，也是O(n).
# 空间复杂度： recursion的空间需求取决于树的高度，因此最多O(n),平均O(logn),hashmap是O(n),综合考虑就是O(n)。

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:

        def array_to_tree(left, right):
            nonlocal preorder_index
            # if there are no elements to construct the tree
            if left > right: return None

            # select the preorder_index element as the root and increment it
            root_value = preorder[preorder_index]
            root = TreeNode(root_value)

            preorder_index += 1  # 下一个应该加的数的index
            # build left and right subtree
            # excluding inorder_index_map[root_value] element because it's the root
            root.left = array_to_tree(left, inorder_index_map[root_value] - 1)     # 变成了两个子问题
            root.right = array_to_tree(inorder_index_map[root_value] + 1, right)

            return root

        preorder_index = 0
        # build a hashmap to store value -> its index relations
        inorder_index_map = {}
        for index, value in enumerate(inorder):
            inorder_index_map[value] = index

        return array_to_tree(0, len(preorder) - 1)
