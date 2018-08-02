"""
一个整型数组里除了两个数字之外，其他的数字都出现了偶数次。
请写程序找出这两个只出现一次的数字。
"""


# -*- coding:utf-8 -*-
class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        res = 0
        for num in array:
            res ^= num
        first_one_in_res = 0
        while res & 1 == 0:
            res >>= 1
            first_one_in_res += 1
        group_set_num = 2 ** first_one_in_res
        group1 = []
        group2 = []
        for num in array:
            if num & group_set_num == 0:
                group1.append(num)
            else:
                group2.append(num)
        num1 = num2 = 0
        for num in group1:
            num1 ^= num
        for num in group2:
            num2 ^= num
        result = [num1, num2]
        result.sort()
        return result

if __name__ == "__main__":
    solution = Solution()
    print(solution.FindNumsAppearOnce([2, 4, 3, 6, 3, 2, 5, 5]))
