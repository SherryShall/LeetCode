"""
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
"""


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res = []
        N = len(nums)-1
        if N < 2:
            return res
        div_pos = -1
        for i, num in enumerate(nums):
            if num >= 0:
                div_pos = i
                break
        # print(nums)
        # print(div_pos)
        if div_pos == -1:
            return res
        if sum([int(n == 0) for n in nums]) >= 3:
            res.append([0, 0, 0])
        for l_index in range(div_pos):
            target = -nums[l_index]
            start = div_pos
            end = N
            while start < end:
                i, j = self.edgeSearch(target, nums, start, end)
                if i > -1 and j > -1:
                        res.append([nums[l_index], nums[i], nums[j]])
                        start = i+1
                        end = j-1
                else:
                    break
        for r_index in range(div_pos, N+1):
            target = -nums[r_index]
            start = 0
            end = div_pos-1
            while start < end:
                i, j = self.edgeSearch(target, nums, start, end)
                if i > -1 and j > -1:
                    res.append([nums[i], nums[j], nums[r_index]])
                    start = i+1
                    end = j-1
                else:
                    break
        res.sort()
        # print(res)
        tmp_pos = 0
        while tmp_pos < len(res)-1:
            if res[tmp_pos+1] == res[tmp_pos]:
                del res[tmp_pos+1]
            else:
                tmp_pos += 1
        return res

    def edgeSearch(self, target, nums, i, j):
        while i < j:
            if nums[i] + nums[j] == target:
                return i, j
            elif nums[i] + nums[j] > target:
                j -= 1
            else:
                i += 1
        return -1, -1

if __name__ == "__main__":
    solution = Solution()
    # print(solution.threeSum([-1,0,1,2,-1,-4]))
    print(solution.threeSum([0, 0, 0]))