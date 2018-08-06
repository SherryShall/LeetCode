# -*- coding:utf-8 -*-
class Solution:
    def LeftRotateString(self, s, n):
        # write code here
        def reverse(s):
            new_s = ""
            for i in range(len(s)-1, -1, -1):
                new_s += s[i]
            return new_s

        s1 = reverse(s[:n])
        s2 = reverse(s[n:])
        s = s1 + s2
        s = reverse(s)
        return s
