"""
给定一个整数数组 nums ，找出一个序列中乘积最大的连续子序列（该序列至少包含一个数）。

示例 1:

输入: [2,3,-2,4]
输出: 6
解释: 子数组 [2,3] 有最大乘积 6。
示例 2:

输入: [-2,0,-1]
输出: 0
解释: 结果不能为 2, 因为 [-2,-1] 不是子数组。
"""

class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """
        解题思路：
        乘法与加法最大差别在于，当前元素的符号具有全局性的作用。
        如果当前元素为负，那么连乘到上个元素的最大乘积，再乘以当前元素，就变成负数，甚至可能成为最小乘积。
        同样，连乘到上个元素的最小乘积如为负，再乘以当前元素，就变成正数，甚至可能成为最大乘积。
 
        因此使用动态规划的方法：
        记maxLast/minLast为连乘到上个元素的最大/小乘积
        记maxCur/minCur为连乘到当前元素的最大/小乘积
        记maxAll为全局最大乘积
        """
        if not nums:
            return 0
        maxLast = minLast = maxAll = nums[0]
        for num in nums[1:]:
            maxCur = max(maxLast*num, minLast*num, num)
            minCur = min(maxLast*num, minLast*num, num)
            maxAll = max(maxCur, maxAll)
            maxLast = maxCur
            minLast = minCur
        return maxAll