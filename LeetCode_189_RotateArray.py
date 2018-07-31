"""
给定一个数组，将数组中的元素向右移动 k 个位置，其中 k 是非负数。

示例 1:

输入: [1,2,3,4,5,6,7] 和 k = 3
输出: [5,6,7,1,2,3,4]
解释:
向右旋转 1 步: [7,1,2,3,4,5,6]
向右旋转 2 步: [6,7,1,2,3,4,5]
向右旋转 3 步: [5,6,7,1,2,3,4]
示例 2:

输入: [-1,-100,3,99] 和 k = 2
输出: [3,99,-1,-100]
解释:
向右旋转 1 步: [99,-1,-100,3]
向右旋转 2 步: [3,99,-1,-100]
说明:

尽可能想出更多的解决方案，至少有三种不同的方法可以解决这个问题。
要求使用空间复杂度为 O(1) 的原地算法。
"""

#coding=utf-8

class Solution:
    # 方法1：
    # 翻转原数组
    # 翻转nums[:k]
    # 翻转nums[k:]
    # 72ms 71.5%
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        self.reverse_array(nums, 0, len(nums)-1)
        self.reverse_array(nums, 0, k-1)
        self.reverse_array(nums, k, len(nums)-1)
        return nums

    def reverse_array(self, array, i, j):
        while j > i:
            array[i], array[j] = array[j], array[i]
            i += 1
            j -= 1
        return array

    # 方法2：
    # 每次移1步
    # 若k > len(nums)/2，则左移len(nums)-k步
    # TLE??
    # def rotate(self, nums, k):
    #     """
    #     :type nums: List[int]
    #     :type k: int
    #     :rtype: void Do not return anything, modify nums in-place instead.
    #     """
    #     n = len(nums)
    #     if n <= 1:
    #         return nums
    #     k = k % n
    #     if k > n/2:
    #         for _ in range(n-k):
    #             self.left_rotate_by_one(nums)
    #     else:
    #         for _ in range(k):
    #             self.right_rotate_by_one(nums)
    #     return nums
    #
    # def left_rotate_by_one(self, nums):
    #     i = 0
    #     tmp = nums[i]
    #     while i < len(nums)-1:
    #         nums[i] = nums[i+1]
    #         i += 1
    #     nums[i] = tmp
    #
    # def right_rotate_by_one(self, nums):
    #     i = len(nums)-1
    #     tmp = nums[i]
    #     while i > 0:
    #         nums[i] = nums[i-1]
    #         i -= 1
    #     nums[i] = tmp

if __name__ == "__main__":
    solution = Solution()
    print(solution.rotate(nums=[1, 2, 3, 4, 5, 6, 7], k=3))
    print(solution.rotate(nums=[-1, -100, 3, 99], k=2))
