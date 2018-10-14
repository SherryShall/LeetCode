from __future__ import division

"""
There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

You may assume nums1 and nums2 cannot be both empty.

Example 1:

nums1 = [1, 3]
nums2 = [2]

The median is 2.0
Example 2:

nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5
"""


class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        M = len(nums1)
        N = len(nums2)
        if (M+N) & 1 == 0:
            return self.findMedianOfOdd(nums1, nums2, M, N)
        else:
            return self.findMedianOfEven(nums1, nums2, M, N)

    def findMedianOfEven(self, nums1, nums2, M, N):
        target_pos = (M+N)//2
        if M == 0:
            return float(nums2[target_pos])
        elif N == 0:
            return float(nums1[target_pos])
        i = j = 0
        # target = 0
        for _ in range(target_pos+1):
            if i == M:
                return float(nums2[j+target_pos-_])
            elif j == N:
                return float(nums1[i+target_pos-_])
            if nums1[i] < nums2[j]:
                if _ == target_pos:
                    return float(nums1[i])
                i += 1
            else:
                if _ == target_pos:
                    return float(nums2[j])
                j += 1

    def findMedianOfOdd(self, nums1, nums2, M, N):
        target_pos_1 = (M+N)//2 - 1
        # target_pos_2 = target_pos_1 + 1
        if M == 0:
            return (nums2[target_pos_1] + nums2[target_pos_1+1])/2
        elif N == 0:
            return (nums1[target_pos_1] + nums1[target_pos_1+1])/2
        i = j = 0
        for _ in range(target_pos_1+1):
            if i == M:
                return (nums2[j+target_pos_1-_]+nums2[j+target_pos_1-_+1])/2
            elif j == N:
                return (nums1[i+target_pos_1-_]+nums1[i+target_pos_1-_+1])/2
            if nums1[i] < nums2[j]:
                if _ == target_pos_1:
                    if i == M-1 or nums2[j] < nums1[i+1]:
                        return (nums1[i] + nums2[j])/2
                    else:
                        return (nums1[i] + nums1[i+1])/2
                i += 1
            else:
                if _ == target_pos_1:
                    if j == N - 1 or nums1[i] < nums2[j+1]:
                        return (nums2[j] + nums1[i]) / 2
                    else:
                        return (nums2[j] + nums2[j + 1]) / 2
                j += 1

if __name__ == "__main__":
    nums1 = [3]
    nums2 = [1, 2, 4]
    solution = Solution()
    print(solution.findMedianSortedArrays(nums1, nums2))