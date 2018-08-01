"""
输入一个字符串,按字典序打印出该字符串中字符的所有排列。
例如输入字符串abc,则打印出由字符a,b,c所能排列出来的所有字符串abc,acb,bac,bca,cab和cba。
"""

# -*- coding:utf-8 -*-
class Solution:
    def Permutation(self, ss):
        # write code here
        res = []
        if not ss:
            return res
        if len(ss) == 1:
            res.append(ss)
            return res
        res += [ss[0] + later_str for later_str in self.Permutation(ss[1:])]
        for j in range(1, len(ss)):
            if ss[0] != ss[j]:
                swap_str = self.Swap(ss, j)
                res += [swap_str[0] + later_str for later_str in self.Permutation(swap_str[1:])]
        res.sort()
        return res

    def Swap(self, ss, j):
        ss = list(ss)
        ss[0], ss[j] = ss[j], ss[0]
        return ''.join(ss)