"""
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n).

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
"""

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return -1
        if nums[-1] < nums[0]:
            rot_pos = self.findRotatedPos(nums)
        else:
            rot_pos = 0
        return self.searchInRotatedArray(nums, target, rot_pos)

    def searchInRotatedArray(self, nums, target, rot_pos):
        l = 0
        r = len(nums)-1
        while r >= l:
            mid = (l+r) // 2
            real_mid = (mid + rot_pos) % len(nums)
            if nums[real_mid] < target:
                l = mid + 1
            elif nums[real_mid] > target:
                r = mid - 1
            else:
                return real_mid
        return -1

    def findRotatedPos(self, nums):
        l = 0
        r = len(nums)-1
        while r - l > 1:
            mid = (r+l) // 2
            if nums[mid] > nums[r]:
                l = mid
            else:
                r = mid
        return l if nums[l] < nums[r] else r