# Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes
# you can see ordered from top to bottom.

# Example 1:
# Input: root = [1,2,3,null,5,null,4]
# Output: [1,3,4]
# Example 2:
# Input: root = [1,null,3]
# Output: [1,3]
# Example 3:
# Input: root = []
# Output: []

# Constraints:
# The number of nodes in the tree is in the range [0, 100].
# -100 <= Node.val <= 100

# 思路：1. DFS, 把每层的node都加到list of list里，每个sub list代表一层，然后再把每个子list最后一个元素加到res里
#      2. BFS, 每层遍历完，把最后一个元素加到res里

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return
        res = []
        level_list = []
        node_list = deque([root, None])

        while node_list:
            curr_node = node_list.popleft()
            if curr_node:
                level_list.append(curr_node.val)
                if curr_node.left:
                    node_list.append(curr_node.left)
                if curr_node.right:
                    node_list.append(curr_node.right)
            else:
                res.append(level_list[-1])
                if len(node_list) > 0:
                    node_list.append(None)
                level_list = []
        return res


class Solution2:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        res = []

        def dfs(node, level):
            if not node:
                return
            if level == len(res):
                res.append(deque([node.val]))
            else:
                res[level].append(node.val)
            dfs(node.left, level + 1)
            dfs(node.right, level + 1)

        dfs(root, 0)
        ans = []
        for i in res:
            ans.append(i[-1])
        return ans