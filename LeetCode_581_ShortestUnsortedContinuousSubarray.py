"""
Given an integer array, you need to find one continuous subarray that if you only sort this subarray in ascending order, then the whole array will be sorted in ascending order, too.

You need to find the shortest such subarray and output its length.

Example 1:
Input: [2, 6, 4, 8, 10, 9, 15]
Output: 5
Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole array sorted in ascending order.
Note:
Then length of the input array is in range [1, 10,000].
The input array may contain duplicates, so ascending order here means <=.
"""


class Solution:
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return 0

        for i in range(len(nums)-1):
            if nums[i+1] >= nums[i]:
                i += 1
            else:
                break
        for _ in range(i+1, len(nums)):
            while nums[_] < nums[i]:
                i -= 1
                if i < 0:
                    break
            if i < 0:
                break

        for j in range(len(nums)-1, 0, -1):
            if nums[j-1] <= nums[j]:
                j -= 1
            else:
                break
        for _ in range(j-1, -1, -1):
            while nums[_] > nums[j]:
                j += 1
                if j >= len(nums):
                    break
            if j >= len(nums):
                break

        if j <= i:
            return 0
        else:
            return j-i-1





