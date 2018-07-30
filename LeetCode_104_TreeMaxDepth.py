"""
给定一个二叉树，找出其最大深度。

二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。

说明: 叶子节点是指没有子节点的节点。

示例：
给定二叉树 [3,9,20,null,null,15,7]，

    3
   / \
  9  20
    /  \
   15   7
返回它的最大深度 3 。
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # 递归 60 ms  92.95%
        # if root is None:
        #     return 0
        # l_depth = self.maxDepth(root.left)
        # r_depth = self.maxDepth(root.right)
        # return max(l_depth, r_depth) + 1

        # 非递归 基于广度优先遍历bfs 64 ms  83.69%
        if root is None:
            return 0
        queue = [root]
        level_count = 0
        while len(queue) > 0:
            level_node_num = len(queue)
            for node_count in range(level_node_num):
                node = queue[0]
                del queue[0]
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            level_count += 1
        return level_count