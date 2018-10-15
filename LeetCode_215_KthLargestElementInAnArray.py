"""
Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.

Example 1:

Input: [3,2,1,5,6,4] and k = 2
Output: 5
Example 2:

Input: [3,2,3,1,2,4,5,5,6] and k = 4
Output: 4
Note:
You may assume k is always valid, 1 ≤ k ≤ array's length.
"""


class Solution(object):
	def findKthLargest(self, nums, k):
		"""
		:type nums: List[int]
		:type k: int
		:rtype: int
		"""
		store = []
		for num in nums:
			if len(store) < k:
				store.append(num)
			else:
				store_min = min(store)
				if num > store_min:
					store[store.index(store_min)] = num
		return min(store)

		# 基于快排partition  TLE??
	# 	k = len(nums) - k
	# 	start = 0
	# 	end = len(nums)-1
	# 	parti_pos = self.partition(start, end, nums)
	# 	while parti_pos != k:
	# 		if parti_pos > k:
	# 			end = parti_pos
	# 		elif parti_pos < k:
	# 			start = parti_pos
	# 		parti_pos = self.partition(start, end, nums)
	# 	return nums[parti_pos]
	# def partition(self, start, end, arr):
	# 	parti_num = arr[end]
	# 	larger_pos = start
	# 	for _ in range(end-start):
	# 		if arr[start+_] < parti_num:
	# 			arr[start+_], arr[larger_pos] = arr[larger_pos], arr[start+_]
	# 			larger_pos += 1
	# 	arr[larger_pos], arr[end] = arr[end], arr[larger_pos]
	# 	return larger_pos



