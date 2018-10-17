"""
Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

Example 1:

Input: "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()"
Example 2:

Input: ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()"

"""


class Solution(object):
	def longestValidParentheses(self, s):
		"""
		:type s: str
		:rtype: int
		"""
		stack = []
		n = len(s)
		for i in range(n):
			if s[i] == "(":
				stack.append(i)
			else:
				if stack and s[stack[-1]] == "(":
					stack.pop()
				else:
					stack.append(i)

		if not stack:
			return n
		else:
			l = stack.pop()
			r = n
			max_len = r-l-1
			while stack:
				r = l
				l = stack.pop()
				max_len = max(max_len, r-l-1)
			max_len = max(max_len, l)
			return max_len

if __name__ == "__main__":
	solution = Solution()
	print(solution.longestValidParentheses("()))((())"))
