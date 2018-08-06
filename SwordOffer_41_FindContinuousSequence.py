"""
找出所有和为S的连续正数序列
"""
# -*- coding:utf-8 -*-
class Solution:
    def FindContinuousSequence(self, tsum):
        # write code here
        res = []
        small_num = 1
        large_num = 2
        while small_num < (tsum+1)/2:
            seq_sum = sum(i for i in range(small_num, large_num+1))
            if seq_sum == tsum:
                res.append([i for i in range(small_num, large_num+1)])
                small_num += 1
            elif seq_sum < tsum:
                large_num += 1
            else:
                small_num += 1
        return res

if __name__ == "__main__":
    solution = Solution()
    print(solution.FindContinuousSequence(15))

