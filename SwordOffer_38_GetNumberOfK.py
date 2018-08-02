"""
统计一个数字在排序数组中出现的次数。
"""

# -*- coding:utf-8 -*-
class Solution:
    def GetNumberOfK(self, data, k):
        # write code here
        def get_first_K(data, start, end, k):
            if end - start < 0:
                return -1
            mid_pos = (start+end)//2
            if k < data[mid_pos]:
                return get_first_K(data, start, mid_pos-1, k)
            elif k > data[mid_pos]:
                return get_first_K(data, mid_pos+1, end, k)
            else:
                if mid_pos == 0 or data[mid_pos-1] != k:
                    return mid_pos
                else:
                    return get_first_K(data, start, mid_pos-1, k)

        def get_last_K(data, start, end, k):
            if end - start < 0:
                return -1
            mid_pos = (start+end)//2
            if k < data[mid_pos]:
                return get_last_K(data, start, mid_pos-1, k)
            elif k > data[mid_pos]:
                return get_last_K(data, mid_pos+1, end, k)
            else:
                if mid_pos == len(data)-1 or data[mid_pos+1] != k:
                    return mid_pos
                else:
                    return get_last_K(data, mid_pos+1, end, k)

        first_k = get_first_K(data, 0, len(data)-1, k)
        last_k = get_last_K(data, 0, len(data)-1, k)
        if first_k == -1 or last_k == -1:
            return 0
        else:
            return last_k-first_k+1
