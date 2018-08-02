"""
给定一个无重复元素的数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。

candidates 中的数字可以无限制重复被选取。

说明：

所有数字（包括 target）都是正整数。
解集不能包含重复的组合。
示例 1:

输入: candidates = [2,3,6,7], target = 7,
所求解集为:
[
  [7],
  [2,2,3]
]
示例 2:

输入: candidates = [2,3,5], target = 8,
所求解集为:
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]
"""


class Solution:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def dfs(start, res, result_list, target):
            if target < 0:
                return
            elif target == 0:
                result_list.append(res)
            else:
                for i in range(start, len(candidates)):
                    dfs(i, res+[candidates[i]], result_list, target-candidates[i])


        res = []
        result_list = []
        dfs(0, res, result_list, target)
        return result_list


if __name__ == "__main__":
    solution = Solution()
    print(solution.combinationSum([2,3,6,7], 7))


