"""
把只包含质因子2、3和5的数称作丑数（Ugly Number）。
例如6、8都是丑数，但14不是，因为它包含质因子7。
习惯上我们把1当做是第一个丑数。求按从小到大的顺序的第N个丑数
"""
# -*- coding:utf-8 -*-
class Solution:
    def GetUglyNumber_Solution(self, index):
        # write code here
        if index == 0:
            return 0
        res = [1]
        while len(res) < index:
            for num in res:
                num2 = num * 2
                if num2 > res[-1]:
                    break
            for num in res:
                num3 = num * 3
                if num3 > res[-1]:
                    break
            for num in res:
                num5 = num * 5
                if num5 > res[-1]:
                    break
            next_num = min(num2, num3, num5)
            res.append(next_num)
        return res[-1]