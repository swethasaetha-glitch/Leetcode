# Last updated: 6/22/2026, 11:17:23 AM
1class Solution:
2    def zeroFilledSubarray(self, nums: List[int]) -> int:
3        count = 0
4        ans = 0
5
6        for num in nums:
7            if num == 0:
8                count += 1
9                ans += count
10            else:
11                count = 0
12
13        return ans