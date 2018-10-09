"""
Given a Binary Search Tree (BST), convert it to a Greater Tree such that every key of the original BST is changed to the original key plus sum of all keys greater than the original key in BST.

Example:

Input: The root of a Binary Search Tree like this:
              5
            /   \
           2     13

Output: The root of a Greater Tree like this:
             18
            /   \
          20     13
"""
import sys
sys.setrecursionlimit(1000000)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        li = []
        self.midOrderSearch(root, li)
        for i in range(len(li)-2, -1, -1):
            li[i][1] += li[i+1][1]
        for item in li:
            item[0].val = item[1]
        #count = 0
        #self.setTree(root, li, count)
        return root

    def midOrderSearch(self, root, li):
        if root:
            self.midOrderSearch(root.left, li)
            li.append([root, root.val])
            self.midOrderSearch(root.right, li)
        else:
            return

    def setTree(self, root, li, count):
        if root:
            self.setTree(root, li, count)
            root.val = li[count]
            count += 1
            self.setTree(root, li, count)
        else:
            return
