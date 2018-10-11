"""
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"
"""


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = "#" + "#".join(s) + "#"
        len_rec = [1] * len(s)
        # print(s)
        for i, ch in enumerate(s):
            count = 1
            l = r = i
            while l-1 >= 0 and r+1 <= len(s)-1:
                if s[l-1] == s[r+1]:
                    count += 2
                    l -= 1
                    r += 1
                    # print(i, ch)
                else:
                    break
            len_rec[i] = count

        # print(len_rec)
        max_len = max(len_rec)
        pos = len_rec.index(max_len)
        res = s[pos-max_len/2:pos+max_len/2+1].replace("#", "")
        return res

