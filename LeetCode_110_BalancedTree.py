"""
给定一个二叉树，判断它是否是高度平衡的二叉树。

本题中，一棵高度平衡二叉树定义为：

一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过1。

示例 1:

给定二叉树 [3,9,20,null,null,15,7]

    3
   / \
  9  20
    /  \
   15   7
返回 true 。

示例 2:

给定二叉树 [1,2,2,3,3,null,null,4,4]

       1
      / \
     2   2
    / \
   3   3
  / \
 4   4
返回 false 。
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def get_status_and_depth(root):
            if not root:
                return True, 0
            l_status, l_depth = get_status_and_depth(root.left)
            r_status, r_depth = get_status_and_depth(root.right)
            if l_status and r_status and abs(l_depth-r_depth) <= 1:
                return True, max(l_depth, r_depth)+1
            return False, max(l_depth, r_depth)+1
        status, depth = get_status_and_depth(root)
        return status
