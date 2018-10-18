"""
Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
"""
from math import ceil

class Solution(object):
	def searchRange(self, nums, target):
		"""
		:type nums: List[int]
		:type target: int
		:rtype: List[int]
		"""
		res = [-1, -1]
		if len(nums) <= 1:
			if len(nums) == 0 or nums[0] != target:
				return res
			else:
				return [0, 0]
		i = 0
		j = len(nums)-1
			
		left = i
		right = j
		# 求左边界
		while left < right:
			mid = (left+right) // 2
			if nums[mid] < target:
				left = mid + 1
			else:
				right = mid
		if nums[left] == target:
			res[0] = left

		right = j
		# 求右边界
		while left < right:
			mid = (left+right)//2 + 1
			if nums[mid] > target:
				right = mid - 1
			else:
				left = mid
		if nums[right] == target:
			res[1] = right
			
		return res

if __name__ == "__main__":
	solution = Solution()
	print(solution.searchRange(nums=[5,7,7,8,8,10], target=8))
	print(solution.searchRange(nums = [5,7,7,8,8,10], target = 6))