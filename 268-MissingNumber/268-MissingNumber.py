# Last updated: 6/15/2026, 11:36:08 AM
1class Solution:
2    def missingNumber(self, nums: List[int]) -> int:
3        n=len(nums)
4        a=n*(n+1)//2
5        b=sum(nums)
6        return a-b