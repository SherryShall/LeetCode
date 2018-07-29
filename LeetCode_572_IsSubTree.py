"""
给定两个非空二叉树 s 和 t，检验 s 中是否包含和 t 具有相同结构和节点值的子树。
s 的一个子树包括 s 的一个节点和这个节点的所有子孙。s 也可以看做它自身的一棵子树。

示例 1:
给定的树 s:

     3
    / \
   4   5
  / \
 1   2
给定的树 t：

   4
  / \
 1   2
返回 true，因为 t 与 s 的一个子树拥有相同的结构和节点值。

示例 2:
给定的树 s：

     3
    / \
   4   5
  / \
 1   2
    /
   0
给定的树 t：

   4
  / \
 1   2
返回 false。
"""
#coding=utf-8

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left_child = None
        self.right_child = None

class Solution:
    # 368ms 50%
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        if s is None:
            if t is None:
                return True
            else:
                return False
        if s.val == t.val:
            result = self.getResult(s, t)
            if result:
                return result
        return self.isSubtree(s.left_child, t) or self.isSubtree(s.right_child, t)

    def getResult(self, s, t):
        if s is None and t is None:
            return True
        elif not (s and t):
            return False
        else:
            if s.val == t.val:
                return self.getResult(s.left_child, t.left_child) and self.getResult(s.right_child, t.right_child)
            else:
                return False

if __name__ == "__main__":
    solution = Solution()

    s = TreeNode(3)
    s.left_child = TreeNode(4)
    s.right_child = TreeNode(5)
    s.left_child.left_child = TreeNode(1)
    s.left_child.right_child = TreeNode(2)

    t = TreeNode(4)
    t.left_child = TreeNode(1)
    t.right_child = TreeNode(2)

    print(solution.isSubtree(s, t))