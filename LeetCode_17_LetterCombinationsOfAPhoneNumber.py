"""
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.



Example:

Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
Note:

Although the above answer is in lexicographical order, your answer could be in any order you want.
"""

class Solution(object):
	def letterCombinations(self, digits):
		"""
		:type digits: str
		:rtype: List[str]
		"""
		if not digits:
			return []
		res = [""]
		for num in list(map(int, digits)):
			if num == 7:
				res = [a+chr(asc) for a in res for asc in range(91+3*num, 95+3*num)]
				# option = [chr(asc) for asc in range(91+3*num, 95+3*num)]
			elif num == 8:
				res = [a+chr(asc) for a in res for asc in range(92+3*num, 95+3*num)]
			elif num == 9:
				res = [a+chr(asc) for a in res for asc in range(92+3*num, 96+3*num)]
			else:
				res = [a+chr(asc) for a in res for asc in range(91+3*num, 94+3*num)]
				# option = [chr(asc) for asc in range(91+3*num, 95+3*num)]
			# options.append(option)
		# for op in options
		return res
