# -*- coding:utf-8 -*-
class Solution:
    def FindGreatestSumOfSubArray(self, array):
        # write code here
        def dp(sum_array, array):
            for i in range(len(array)):
                if i == 0:
                    sum_array[i] = array[i]
                else:
                    if sum_array[i-1] < 0:
                        sum_array[i] = array[i]
                    else:
                        sum_array[i] = sum_array[i-1] + array[i]
            return max(sum_array)
        sum_array = [0] * len(array)
        return dp(sum_array, array)