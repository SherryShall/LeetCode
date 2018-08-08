"""
判断5张扑克牌是否为顺子，大小王为0，可以代替任意数字
"""

# -*- coding:utf-8 -*-
import Sort_QuickSort

class Solution:
    def IsContinuous(self, numbers):
        # write code here
        if not numbers:
            return False
        Sort_QuickSort.quick_sort(numbers)
        zero_count = 0
        diff_count = 0
        for i in range(len(numbers)):
            if numbers[i] == 0:
                zero_count += 1
            elif i == len(numbers)-1:
                break
            else:
                if numbers[i+1] == numbers[i]:
                    return False
                diff_count += (numbers[i+1] - numbers[i] - 1)
        if diff_count <= zero_count:
            return True
        return False
