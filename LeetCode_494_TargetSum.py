#coding=UTF-8

import collections

class Solution(object):
	# TLE的做法：dfs递归
	# def findTargetSumWays(self, nums, S):
	# 	"""
	# 	:type nums: List[int]
	# 	:type S: int
	# 	:rtype: int
	# 	"""
	# 	if len(nums) == 0 or (len(nums) == 1 and (nums[0] != S and -nums[0] != S)):
	# 		return 0
	# 	elif len(nums) == 1 and (nums[0] == S or -nums[0] == S):
	# 		return 1
	# 	else:
	# 		return self.findTargetDp(nums, 0, len(nums)-1, S)
	#
	# def findTargetDp(self, nums, i, j, S):
	# 	if i == j:
	# 		if nums[i] == S or -nums[i] == S:
	# 			if nums[i] == -nums[i]:
	# 				return 2
	# 			else:
	# 				return 1
	# 		else:
	# 			return 0
	# 	else:
	# 		return self.findTargetDp(nums, i+1, j, S-nums[i]) + self.findTargetDp(nums, i+1, j, S+nums[i])

# """
# 其实一般能用dfs解决的题目，如果题目只要求满足条件的数字而不是所有的结果，那么dfs会超时。
# 解决方法其实基本只有一条路：动态规划。
#
# 设了一个数组，数组中保存的是字典，字典保存的是该index下的能求得的和为某个数的个数。
#
# 所以从左到右进行遍历，在每个位置都把前一个位置的字典拿出来，看前一个位置的所有能求得的和。和当前的数值分别进行加减操作，就能得出新一个位置能求得的和了。
# """
	def findTargetSumWays(self, nums, S):
		"""
		:type nums: List[int]
		:type S: int
		:rtype: int
		"""
		# 要注意一点是，dp初始不能采用下面方式：
		# dp = [collections.defaultdict(int)] * (_len + 1)
		# 这种初始化方式会使每个位置的元素其实是同一个字典
		if len(nums) == 0:
			return 0
		dp = [{} for _ in range(len(nums))]
		dp[0] = {nums[0]: 1, -nums[0]: 1} if nums[0] != 0 else {0: 2}	#第一位是0的case
		for i in range(1, len(nums)):
			for item in dp[i-1]:
				dp[i][item+nums[i]] = dp[i].get(item+nums[i], 0) + dp[i-1][item]
				dp[i][item-nums[i]] = dp[i].get(item-nums[i], 0) + dp[i-1][item]
		return dp[len(nums)-1].get(S, 0)

if __name__ == "__main__":
	solution = Solution()
	print(solution.findTargetSumWays([1, 1, 1, 1, 1], 3))