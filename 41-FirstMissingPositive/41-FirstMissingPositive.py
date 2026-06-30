# Last updated: 6/30/2026, 3:53:06 PM
1class Solution:
2    def firstMissingPositive(self, nums: List[int]) -> int:
3        nums.sort()
4
5        ans = 1
6
7        for num in nums:
8            if num == ans:
9                ans += 1
10
11        return ans