"""
输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的双向链表。
要求不能创建任何新的结点，只能调整树中结点指针的指向。
"""
# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 思路：非递归的中序遍历
class Solution:
    def Convert(self, pRootOfTree):
        # write code here
        CurNode = pRootOfTree
        PreNode = None
        StartNode = None
        stack = []
        while stack or CurNode:
            if not CurNode:
                CurNode = stack.pop()
                # print(CurNode)
                if PreNode:
                    PreNode.right = CurNode
                    CurNode.left = PreNode
                else:
                    StartNode = CurNode
                PreNode = CurNode
                CurNode = CurNode.right
            else:
                stack.append(CurNode)
                CurNode = CurNode.left
        return StartNode
