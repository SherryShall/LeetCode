"""
题目描述
输入一颗二叉树的跟节点和一个整数，打印出二叉树中结点值的和为输入整数的所有路径。
路径定义为从树的根结点开始往下一直到叶结点所经过的结点形成一条路径。(注意: 在返回值的list中，数组长度大的数组靠前)
"""
# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, expectNumber):
        # write code here
        tree_path = self.dfs(root)
        res = []
        for path in tree_path:
            path_array = map(int, path.split("->"))
            if sum(path_array) == expectNumber:
                res.append(path_array)
        res.sort(key=len, reverse=True)
        return res

    def dfs(self, root):
        if not root:
            return []
        elif not root.left and not root.right:
            return [str(root.val)]
        else:
            cur_path = [str(root.val) + "->" + last_path for last_path in self.dfs(root.left)]
            cur_path += [str(root.val) + "->" + last_path for last_path in self.dfs(root.right)]
        return cur_path
