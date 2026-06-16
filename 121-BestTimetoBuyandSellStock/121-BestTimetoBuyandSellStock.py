# Last updated: 6/16/2026, 5:09:24 PM
1class Solution:
2    def twoSum(self, nums, target):
3        for i in range(len(nums)):
4            for j in range(i + 1, len(nums)):
5                if nums[i] + nums[j] == target:
6                    return [i, j]
7        return []