"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((())0)",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
"""


class Solution(object):
	def generateParenthesis(self, n):
		"""
		:type n: int
		:rtype: List[str]
		"""
		# 暴力去重
		# unique_step = ["("*i + ")"*i for i in range(1, n+1)]
		# res = [""] * n
		# for i in range(1, n+1):
		# 	res[i-1] = [unique_step[i-1]]
		# 	for j in range(1, i):
		# 		res[i-1] += [unique_step[j-1] + s for s in res[i-j-1]]
		# 		res[i-1] += [s1+s2 for s1 in res[j-1] for s2 in res[i-j-1]]
		# 		for s in res[i-j-1]:
		# 			res[i-1] += [unique_step[j-1][:j] + s + unique_step[j-1][j:]]
		# 		#res[i-1] += [s.join("") for s in res[i-j-1]]
		# output = list(set(res[n-1]))
		# output.sort()
		# return output
		res = []
		self.backTrack("", 0, 0, n, res)
		return res
	# 回溯法
	def backTrack(self, str, op, clo, mx, res):
		if len(str) == 2*mx:
			res.append(str)
			return
		if op < mx:
			self.backTrack(str+"(", op+1, clo, mx, res)
		if clo < op:
			self.backTrack(str+")", op, clo+1, mx, res)



