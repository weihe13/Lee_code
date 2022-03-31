# Given a reference of a node in a connected undirected graph.
# Return a deep copy (clone) of the graph.
# Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.
#
# class Node {
#     public int val;
#     public List<Node> neighbors;
# }

# Test case format: For simplicity, each node's value is the same as the node's index (1-indexed). For example,
# the first node with val == 1, the second node with val == 2, and so on. The graph is represented in the test case
# using an adjacency list. An adjacency list is a collection of unordered lists used to represent a finite graph.
# Each list describes the set of neighbors of a node in the graph. The given node will always be the first node with
# val = 1. You must return the copy of the given node as a reference to the cloned graph.

# Example 1:
# Input: adjList = [[2,4],[1,3],[2,4],[1,3]]
# Output: [[2,4],[1,3],[2,4],[1,3]]
# Explanation: There are 4 nodes in the graph.
# 1st node (val = 1)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
# 2nd node (val = 2)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).
# 3rd node (val = 3)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
# 4th node (val = 4)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).
# Example 2:
# Input: adjList = [[]]
# Output: [[]]
# Explanation: Note that the input contains one empty list. The graph consists of only one node with val = 1 and it
# does not have any neighbors.
# Example 3:
# Input: adjList = []
# Output: []
# Explanation: This an empty graph, it does not have any nodes.

# Constraints:
# The number of nodes in the graph is in the range [0, 100].
# 1 <= Node.val <= 100
# Node.val is unique for each node.
# There are no repeated edges and no self-loops in the graph.
# The Graph is connected and all nodes can be visited starting from the given node.

# 思路：1. 要理解清楚输入的node是个什么？input list只是代表这个图里各个node的关系，真正输入给function的是一个Node。最后return的则是输入
#         node的copy。
#      2. 三步走，第一步，先找到需要copy的所有点，
#                第二步，把所有点copy下来，这里的copy是指生成一个新的Node，node.val和original的点一样
#                第三步，利用第二步形成的original node和copy node的mapping，把原图中的关系copy下来。

class Solution:
    def __init__(self):
        pass

    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None

        nodes = self.find_node_bydfs(node)
        mapping = self.copy_node(nodes)
        self.copy_edges(nodes, mapping)
        return mapping[node]

    def find_node_bydfs(self, node):
        queue = collections.deque([node])
        visited = set([node])   # 注意初始visited不能是空的，要包含初始node
        while queue:
            currnode = queue.popleft()
            for neighbor in currnode.neighbors:
                if neighbor in visited:
                    continue
                queue.append(neighbor)  # 一旦进入queue，就要进入visited
                visited.add(neighbor)
        return list(visited)

    def copy_node(self, nodes):
        mapping = {}
        for node in nodes:
            mapping[node] = Node(node.val)    # 每个node对应一个copy
        return mapping

    def copy_edges(self, nodes, mapping):
        for node in nodes:
            new_node = mapping[node]     # 找到copy的node，改变其neighbor
            for neighbor in node.neighbors:
                new_node.neighbors.append(mapping[neighbor])  # 这里注意添加的是new neighbor
