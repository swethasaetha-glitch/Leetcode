# Last updated: 6/22/2026, 2:24:39 PM
1class Solution:
2    def findMaxAverage(self, nums: List[int], k: int) -> float:
3        window = sum(nums[:k])
4        ans = window
5
6        for i in range(k, len(nums)):
7            window += nums[i] - nums[i-k]
8            ans = max(ans, window)
9
10        return ans / k