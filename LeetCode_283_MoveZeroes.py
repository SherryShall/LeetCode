"""
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
Note:

You must do this in-place without making a copy of the array.
Minimize the total number of operations.
"""

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        zero_count = nums.count(0)
        nums[:] = [n for n in nums if n != 0]
        nums += [0]*zero_count

if __name__ == "__main__":
    solution = Solution()
    solution.moveZeroes([0, 0, 1, 2, 4])